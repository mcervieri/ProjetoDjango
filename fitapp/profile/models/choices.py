from django.db import models


class RolesChoices(models.TextChoices):
    ALUNO = "aluno", "Aluno"
    NUTRICIONISTA = "nutricionista", "Nutricionista"
    PERSONAL = "personal", "Personal Trainer"
    ADMIN = "admin", "Administrador"
