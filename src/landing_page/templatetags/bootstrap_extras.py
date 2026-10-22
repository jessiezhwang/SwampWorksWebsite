from django import template

register = template.Library()


@register.filter
def add_class(field, css_class):
    """Render a form field with a Bootstrap class, e.g. {{ field|add_class:"form-control" }}."""
    return field.as_widget(attrs={'class': css_class})
