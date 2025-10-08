import uuid
import re
from django.utils.text import slugify
from django.apps import apps


def generate_unique_slug(instance, value=None):
    """
    Gera um slug global único para o projeto inteiro.
    - `value`: texto base para gerar o slug (ex: nome, título, username, etc.)
    - Garante que o slug não exista em NENHUMA model do projeto.
    """
    base_slug = slugify(value or str(uuid.uuid4()))
    slug = base_slug
    counter = 1

    all_models = apps.get_models()

    while True:
        slug_exists = False
        for model in all_models:
            if hasattr(model, "slug"):
                if model.objects.filter(slug=slug).exists():
                    slug_exists = True
                    break

        if not slug_exists:
            return slug

        slug = f"{base_slug}-{counter}"
        counter += 1
