from django.contrib.auth.models import AbstractUser
from django.db import models
from fitapp.core.models import BaseModel

class User(AbstractUser, BaseModel):
    class Roles(models.TextChoices):
        ALUNO = "aluno", "Aluno"
        PERSONAL = "personal", "Personal"
        NUTRICIONISTA = "nutricionista", "Nutricionista"
        ADMIN = "admin", "Administrador"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.ALUNO,
    )

    def is_admin(self):
        return self.role == self.Roles.ADMIN