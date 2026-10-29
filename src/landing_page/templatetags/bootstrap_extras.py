from django import template

from landing_page.models import Project

register = template.Library()


@register.filter
def add_class(field, css_class):
    """Render a form field with a Bootstrap class, e.g. {{ field|add_class:"form-control" }}."""
    return field.as_widget(attrs={'class': css_class})


@register.simple_tag
def nav_projects():
    """Approved projects for the navbar menu: current projects first, then previous ones."""
    return Project.objects.filter(is_approved=True).order_by('-status', 'title')
