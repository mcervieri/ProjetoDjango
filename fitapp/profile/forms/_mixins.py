class AdminLTEFormMixin:
    """Aplicação de classes padrão no estilo AdminLTE/Bootstrap."""

    INPUT_CLASS = "form-control"
    SELECT_CLASS = "form-control"
    TEXTAREA_CLASS = "form-control"
    FILE_CLASS = "form-control-file"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            widget = field.widget
            widget_name = widget.__class__.__name__.lower()
            existing = widget.attrs.get("class", "")

            if "file" in widget_name:
                base_class = self.FILE_CLASS
            elif "textarea" in widget_name:
                base_class = self.TEXTAREA_CLASS
            elif "select" in widget_name:
                base_class = self.SELECT_CLASS
            elif widget.input_type == "checkbox":
                base_class = "form-check-input"
            else:
                base_class = self.INPUT_CLASS

            widget.attrs["class"] = " ".join(
                cls for cls in [base_class, existing] if cls
            )
            widget.attrs.setdefault("placeholder", field.label or name.capitalize())

            if self.is_bound and self.errors.get(name):
                # Adiciona o destaque de erro do Bootstrap quando necessário.
                widget.attrs["class"] += " is-invalid"


TailwindFormMixin = AdminLTEFormMixin
