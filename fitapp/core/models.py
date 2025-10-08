from django.db import models
from fitapp.core.utils.slug import generate_unique_slug


# 🔹 BaseModel padrão do projeto
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 🔹 SlugBaseModel global e reutilizável
class SlugBaseModel(models.Model):
    """
    Classe base para models que precisam de slugs únicos globais.
    Basta herdar e o campo será criado automaticamente.
    """

    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True  # não cria tabela no banco

    def save(self, *args, **kwargs):
        if not self.slug:
            # Usa o melhor campo textual disponível para gerar slug
            base_value = (
                getattr(self, "nome", None)
                or getattr(self, "titulo", None)
                or getattr(self, "username", None)
                or str(self.pk or "")
            )
            self.slug = generate_unique_slug(self, base_value)
        super().save(*args, **kwargs)
