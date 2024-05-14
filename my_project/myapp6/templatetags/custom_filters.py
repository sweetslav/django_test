from django import template

register = template.Library()


@register.filter
def sum_quantity(products):
    return sum(product.quantity for product in products)
