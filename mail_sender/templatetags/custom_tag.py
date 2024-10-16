from django import template

register = template.Library()


@register.filter
def make_image_link(data):
    """Тег добавляет к адресу папку медиа"""
    if data:
        return f"/media/{data}"
    return "#"


@register.filter
def cut_100_chars(description):
    """Тег обрезает 100 первых символов"""
    return description[:100]
