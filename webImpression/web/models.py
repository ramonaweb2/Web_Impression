from django.core.validators import EmailValidator
from django.db import models

EMAIL_MAX_LENGTH = 50


class UserSubscriber(models.Model):

    email = models.CharField(
        unique=True,
        max_length=EMAIL_MAX_LENGTH,
        validators=[EmailValidator],
    )
