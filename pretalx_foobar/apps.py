from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "pretalx_foobar"
    verbose_name = "pretalx FooBar plugin"

    class PretalxPluginMeta:
        name = gettext_lazy("pretalx FooBar plugin")
        author = "Your name"
        description = gettext_lazy("pretalx plugin for pretalx FooBar plugin")
        visible = True
        version = __version__
        category = "FEATURE"

    def ready(self):
        from . import signals  # NOQA
