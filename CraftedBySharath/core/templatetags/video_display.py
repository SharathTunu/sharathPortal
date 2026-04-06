from pathlib import Path

from django import template

register = template.Library()


@register.filter
def video_display_name(filename):
    if not filename:
        return ""
    s = str(filename).strip()
    stem = Path(s).stem if "." in s else s
    return stem.replace("_", " ").title()
