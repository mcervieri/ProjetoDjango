class TailwindFormMixin:
    INPUT_CLASS = "block w-full rounded-lg border border-gray-300 bg-white text-gray-900 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary"
    SELECT_CLASS = INPUT_CLASS
    TEXTAREA_CLASS = INPUT_CLASS + " min-h-[120px]"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            widget = field.widget
            cls_now = widget.attrs.get("class", "")
            base = self.INPUT_CLASS
            if widget.__class__.__name__.lower().find("select") >= 0:
                base = self.SELECT_CLASS
            if widget.__class__.__name__.lower().find("textarea") >= 0:
                base = self.TEXTAREA_CLASS
            widget.attrs["class"] = f"{base} {cls_now}".strip()
            widget.attrs.setdefault("placeholder", field.label or name.capitalize())
