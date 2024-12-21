from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.is_student:
            from students.models import StudentProfile
            StudentProfile.objects.get_or_create(user=self)

        if self.is_professor:
            from professors.models import ProfessorProfile
            ProfessorProfile.objects.get_or_create(user=self)