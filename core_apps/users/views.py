from .serializers import UserSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserDetailView(RetrieveUpdateAPIView):
    """
    API view for retrieving and updating details of the authenticated user.

    Attributes:
        serializer_class: UserSerializer class used for serializing user details.
        permission_classes: Tuple of permission classes, requires IsAuthenticated for access.

    Methods:
        get_object():
            Retrieves and returns the authenticated user object.
        
        get_queryset():
            Returns an empty queryset, as user details are retrieved directly using get_object().
    """
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """
        Retrieve the authenticated user object.

        Returns:
            User: Authenticated user object.
        """
        return self.request.user
    
    def get_queryset(self):
        """
        Return an empty queryset.

        Since user details are fetched using get_object(), this method returns an empty
        queryset to prevent accidental querying of user objects.

        Returns:
            QuerySet: Empty queryset.
        """
        return User.objects.none()
    

