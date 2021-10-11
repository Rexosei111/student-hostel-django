from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


def normalize_index_number(index: str) -> str:
    try:
        index_number = index.lower()
    except Exception:
        raise ValueError(_('Invalid Index Number'))
    if (index_number.startswith("bs") and len(index_number) == 11):
        return index_number
    else:
        raise ValueError(_('Invalid Index Number'))


class UserManager(BaseUserManager):

    def normalize_index_number(self, index: str) -> str:
        try:
            index_number = index.lower()
        except Exception:
            raise ValueError(_('Invalid Index Number'))
        if (index_number.startswith("bs") and len(index_number) == 11):
            return index_number
        else:
            raise ValueError(_('Invalid Index Number'))

    def create_user(self, index_number, email, password, **extra_fields):
        if not index_number:
            raise ValueError(_('Index Number must be set'))
        index_number = self.normalize_index_number(index_number)
        email = self.normalize_email(email)
        user = self.model(index_number=index_number,
                          email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, index_number, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Staffuser must have is_staff=True.'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Staffuser must have is_active=True.'))
        return self.create_user(index_number, email, password, **extra_fields)

    def create_superuser(self, index_number, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given index number, email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(index_number, email, password, **extra_fields)
