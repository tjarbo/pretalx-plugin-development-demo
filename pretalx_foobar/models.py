from django.db import models




class FoobarSettings(models.Model):
    event = models.OneToOneField(
        to="event.Event",
        on_delete=models.CASCADE,
        related_name="pretalx_foobar_settings",
    )
    some_setting = models.CharField(max_length=10, default="A")
