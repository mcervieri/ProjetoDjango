from django.db import models
from django.contrib.auth.models import User
from fitapp.profile.models.choices import RolesChoices
from fitapp.core.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="profile")

    role = models.CharField(
        max_length=20,
        choices=RolesChoices.choices,
        default=RolesChoices.ALUNO,
    )

    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    goal = models.TextField(null=True, blank=True)

    cref = models.CharField(max_length=50, null=True, blank=True)
    crn = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    specialty = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    def is_admin(self):
        return self.role == RolesChoices.ADMIN
