from django import template

register = template.Library()

CENSOR = ['типо', 'какбы', 'чё', 'шо']


@register.filter(name='censor')
def censor(value):
    text = value.split()
    for x in text:
        if x.lower() in CENSOR:
            value = value.replace(x, '*' * len(x))
    return value