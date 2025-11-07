from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from fitapp.profile.models.choices import RolesChoices
from fitapp.core.models import BaseModel, SlugBaseModel


class Profile(BaseModel, SlugBaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="profile")

    role = models.CharField(
        max_length=20,
        choices=RolesChoices.choices,
        default=RolesChoices.ALUNO,
    )

    personal = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="alunos_personal",
        limit_choices_to={"role__iexact": RolesChoices.PERSONAL},
        verbose_name="Personal Trainer",
    )

    nutricionista = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="alunos_nutricionista",
        limit_choices_to={"role__iexact": RolesChoices.NUTRICIONISTA},
        verbose_name="Nutricionista",
    )

    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="profiles/%Y/%m/%d", null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    goal = models.TextField(null=True, blank=True)

    cref = models.CharField(max_length=50, null=True, blank=True)
    crn = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    specialty = models.TextField(null=True, blank=True)

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    def is_admin(self):
        return self.role.strip().lower() == RolesChoices.ADMIN.strip().lower()

    def needs_completion(self):
        return not self.is_completed

    def save(self, *args, **kwargs):
        if not self.slug:
            from fitapp.core.utils.slug import generate_unique_slug

            base_value = self.user.username
            self.slug = generate_unique_slug(self, base_value)
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
