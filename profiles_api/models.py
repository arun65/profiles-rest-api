from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""
    
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email) # converts second half of email address to lower case
        user = self.model(email=email, name=name) # creates a new model that this manager is representing(here UserProfile model)
        
        user.set_password(password) # set_password() is method in AbstractBaseUser class which hashes(encrypt) the password
        user.save(using=self._db) # stand procedure for saving objects in django

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with given details"""
        
        user = self.create_user(email, name, password) # create a user object
        user.is_superuser = True # is_superuser is created by PermissionsMixin by default
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' # use email instead of name
    REQUIRED_FIELDS = ['name'] # name field is required... ie here email is required

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email