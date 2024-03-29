from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)

    date_birth = models.DateField(verbose_name="Birth date", null=True, blank=True)

    email = models.EmailField(verbose_name="email", unique=True, max_length=60)

    image = models.ImageField(blank=True, null=True, upload_to='images/', default='images/ProfilePicture.png')

    friends = models.ManyToManyField("self", blank=True, null=True)

    balance = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=5, default=00.00)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'  # поле яке застосовується при заході в аккаунт
    REQUIRED_FIELDS = ['email']

    objects = CustomAccountManager()

    def get_id(self):
        return self.id

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @classmethod
    def get_user_by_id(cls, user_id=1):
        return cls.objects.get(id=user_id)
