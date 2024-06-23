from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model to represent user details including profile information.

    Attributes:
        gender: A CharField representing the user's gender from the associated profile.
        phone_number: A PhoneNumberField representing the user's phone number from the associated profile.
        profile_photo: A read-only URL field representing the URL of the user's profile photo.
        country: A CountryField representing the user's country from the associated profile.
        city: A CharField representing the user's city from the associated profile.

    Methods:
        to_representation(instance):
            Custom representation method to add 'admin' field for superuser instances.
    """
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ReadOnlyField(source="profile.profile_photo.url")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "gender",
            "phone_number",
            "profile_photo",
            "country",
            "city",
        ]

    def to_representation(self, instance):
        """
        Custom method to represent User instance.

        Adds 'admin' field to the representation if the user is a superuser.

        Args:
            instance: User instance for which representation is being generated.

        Returns:
            dict: Serialized representation of the User instance.
        """
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CustomRegisterSerializer(RegisterSerializer):
    """
    Custom serializer for user registration, extending RegisterSerializer.

    Attributes:
        first_name: Required CharField for the user's first name.
        last_name: Required CharField for the user's last name.
        email: Required EmailField for the user's email address.
        password1: Write-only CharField for the user's password.
        password2: Write-only CharField for password confirmation.

    Methods:
        get_cleaned_data():
            Retrieves and returns cleaned input data for user registration.
        
        save(request):
            Saves the user registration data and creates a new user instance.
    """
    username = None
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        """
        Retrieve and return cleaned input data for user registration.

        Returns:
            dict: Cleaned data including 'email', 'first_name', 'last_name', 'password1'.
        """
        super().get_cleaned_data()
        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
        }

    def save(self, request):
        """
        Save user registration data and create a new user instance.

        Args:
            request: Request object containing registration data.

        Returns:
            User: Newly created user instance.
        """
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self)
        user.save()

        setup_user_email(request, user, [])
        user.email = self.cleaned_data.get("email")
        user.password = self.cleaned_data.get("password1")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")

        return user
    

