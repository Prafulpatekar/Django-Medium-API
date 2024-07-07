# TODO: Change the DEFAULT_FROM_EMAIL to production
from django_medium_api.settings.local import DEFAULT_FROM_EMAIL
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

from .exceptions import CantFollowYourself
from .models import ProfileModel
from .pagination import ProfilePagination
from .renderers import ProfileJSONRenderer, ProfilesJSONRenderer
from .serializers import ProfileSerializer, FollowingSerializer, UpdateProfileSerializer

User = get_user_model()

class ProfileListAPIView(generics.ListAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = ProfilePagination
    renderer_classes = [ProfilesJSONRenderer]


class ProfileDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    renderer_classes = [ProfileJSONRenderer]

    def get_queryset(self):
        queryset = ProfileModel.objects.select_related("user")
        return queryset

    def get_object(self):
        user = self.request.user
        profile = self.get_queryset().get(user=user)
        return profile

class UpdateProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    renderer_classes = [ProfileJSONRenderer]

    def get_object(self):
        profile = self.request.user.profile
        return profile

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FollowingListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            profile = ProfileModel.objects.get(user__id=request.user.id)
            follower_profiles = profile.followers.all()
            serializer = FollowingSerializer(follower_profiles, many=True)
            formatted_response = {
                "status_code": status.HTTP_200_OK,
                "followings_count": follower_profiles.count(),
                "followings": serializer.data,
            }
            return Response(formatted_response, status=status.HTTP_200_OK)
        except ProfileModel.DoesNotExist:
            return Response(status=404)
        
    
class FollowerListView(APIView):
    def get(self, request, format=None):
        try:
            profile = ProfileModel.objects.get(user__id=request.user.id)
            following_profiles = profile.following.all()
            serializer = FollowingSerializer(following_profiles, many=True)
            formatted_response = {
                "status_code": status.HTTP_200_OK,
                "followers_count": following_profiles.count(),
                "followers": serializer.data,
            }
            return Response(formatted_response, status=status.HTTP_200_OK)
        except ProfileModel.DoesNotExist:
            return Response(status=404)
        
class FollowAPIView(APIView):
    def post(self, request, user_id, format=None):
        try:
            follower = ProfileModel.objects.get(user=self.request.user)
            user_profile = request.user.profile
            profile = ProfileModel.objects.get(user__id=user_id)

            if profile == follower:
                raise CantFollowYourself()

            if user_profile.check_following(profile):
                formatted_response = {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": f"You are already following {profile.user.first_name} {profile.user.last_name}",
                }
                return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

            user_profile.follow(profile)
            subject = "A new user follows you"
            message = f"Hi there, {profile.user.first_name}!!, the user {user_profile.user.first_name} {user_profile.user.last_name} now follows you"
            from_email = DEFAULT_FROM_EMAIL
            recipient_list = [profile.user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            return Response(
                {
                    "status_code": status.HTTP_200_OK,
                    "message": f"You are now following {profile.user.first_name} {profile.user.last_name}",
                },
            )
        except ProfileModel.DoesNotExist:
            raise NotFound("You can't follow a profile that does not exist.")

class UnfollowAPIView(APIView):
    def post(self, request, user_id, *args, **kwargs):
        user_profile = request.user.profile
        profile = ProfileModel.objects.get(user__id=user_id)

        if not user_profile.check_following(profile):
            formatted_response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": f"You can't unfollow {profile.user.first_name} {profile.user.last_name}, since you were not following them in the first place ",
            }
            return Response(
                formatted_response,
                status.HTTP_400_BAD_REQUEST,
            )

        user_profile.unfollow(profile)
        formatted_response = {
            "status_code": status.HTTP_200_OK,
            "message": f"You have unfollowed {profile.user.first_name} {profile.user.last_name}",
        }
        return Response(formatted_response, status.HTTP_200_OK)