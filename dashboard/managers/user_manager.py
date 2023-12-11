from django.contrib.auth.base_user import BaseUserManager
from django.db import DatabaseError, transaction


class UserManager(BaseUserManager):
    def validate_email(self, email):
        if not email:
            raise ValueError("The given email must be set")
        if self.filter(email=email).exists():
            raise ValueError("The given email is already in use")
        return email

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except DatabaseError:
            raise

    def create_user(self, email, password=None, **extra_fields):
        # email validation
        self.validate_email(email)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password=password, **extra_fields)
