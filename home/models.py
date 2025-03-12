
# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# # User Manager to handle user creation
# class UserManager(BaseUserManager):
#     def create_user(self, email, name,tc, password=None):
#         if not email:
#             raise ValueError("Email is required")

#         user = self.model(
#             email=self.normalize_email(email),
#             tc=tc,
#             name=name   
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, name,tc, password=None):
#         user = self.create_user(email, name,tc, password)
#         user.is_admin = True,
#         # user.is_staff = True,
#         user.is_superuser = True,
#         user.save(using=self._db)
#         return user


# # Custom User Model
# class User(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=100)
#     tc= models.BooleanField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = UserManager()
#     is_superuser = models.BooleanField(default=False)



#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["name","tc"]

#     def __str__(self):
#         return self.email

#     @property
#     def is_staff(self):
#         return self.is_admin
    


#     def has_perm(self, perm, obj=None):
#         """Grant all permissions to superusers"""
#         return self.is_superuser

#     def has_module_perms(self, app_label):
#         """Allow user to view the admin panel if superuser"""
#         return self.is_superuser




from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, tc, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          tc=tc,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, tc, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          tc=tc,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200)
  tc = models.BooleanField()
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'tc']

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin



