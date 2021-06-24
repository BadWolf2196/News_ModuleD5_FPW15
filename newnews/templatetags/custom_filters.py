from django import template

register = template.Library()
@register.filter(name='censor')
def multiply(value, arg):
    return str(value) * arg