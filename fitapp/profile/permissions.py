from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_superuser or getattr(user, "role", "") == "admin"


admin_required = user_passes_test(is_admin)
