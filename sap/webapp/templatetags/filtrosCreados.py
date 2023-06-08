import re
from django import template
from personas.models import Persona


register = template.Library()

@register.filter()
def total(total):
    if total:
        total.delete()



register.filter(total)