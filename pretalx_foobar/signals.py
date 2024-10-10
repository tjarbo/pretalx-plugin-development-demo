
from django.dispatch import receiver
from django.urls import reverse
from pretalx.orga.signals import nav_event_settings


@receiver(nav_event_settings)
def pretalx_foobar_settings(sender, request, **kwargs):
    if not request.user.has_perm("orga.change_settings", request.event):
        return []
    return [
        {
            "label": "pretalx FooBar plugin",
            "url": reverse(
                "plugins:pretalx_foobar:settings",
                kwargs={"event": request.event.slug},
            ),
            "active": request.resolver_match.url_name
            == "plugins:pretalx_foobar:settings",
        }
    ]

