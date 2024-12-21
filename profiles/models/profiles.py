from django.db import models
from users.models import CustomUser


class Profile(models.Model):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("professor", "Professor"),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    additional_data = models.JSONField(
        null=True, blank=True
    )  # Optional: Store dynamic fields

    def __str__(self):
        return f"{self.user.username} - {self.role}"
