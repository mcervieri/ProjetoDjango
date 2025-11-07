from django import template

register = template.Library()


@register.filter
def get_field_label(form, field_name):
    """Retorna o label de um campo do formulário."""
    try:
        return form[field_name].label
    except Exception:
        return field_name
