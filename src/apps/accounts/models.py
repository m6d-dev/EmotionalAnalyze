from django.db import models

from src.apps.accounts.manager import UserManager
from src.utils.models import CustomAbstractUser


class User(CustomAbstractUser):
    email_confirmed = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def clean_username(self):
        return self.username.split("@")[0]

    class Meta(CustomAbstractUser.Meta):
        app_label = "accounts"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class UserUsageTracker(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usage_trackers"
    )
    api_call_count = models.PositiveIntegerField(default=0)
    last_called_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User API Usage Tracker"
        verbose_name_plural = "User API Usage Trackers"
        unique_together = ('user',)

    def increment(self):
        self.api_call_count += 1
        self.save(update_fields=['api_call_count', 'last_called_at'])

    def __str__(self):
        return f"{self.user.username} - {self.api_call_count} calls"
