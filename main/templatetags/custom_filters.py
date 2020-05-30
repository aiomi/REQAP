""" Custom defined template filters """

from django import template

register = template.Library()


@register.filter
def add_class(modelform_input, css_class):
    """ Adds a class to a field in a form

    :param modelform_input: form field to add class to
    :css_class: the class to be added to the field
    """
    return modelform_input.as_widget(attrs={'class': css_class})


@register.filter
def add_id(modelform_input, script_id):
    """ Adds a class to a field in a form

    :param modelform_input: form field to add class to
    :css_class: the class to be added to the field
    """
    return modelform_input.as_widget(attrs={'id': script_id})


@register.filter(name='subtract')
def subtract(value, arg):
    """ returns value of template value substraction """

    return value - arg
