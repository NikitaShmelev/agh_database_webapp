import pytest
from django.contrib.auth.models import User
from users.models import CustomUser


@pytest.fixture
def get_user():
    """Create and return a user instance for test cases."""
    return User.objects.create_user(username="testuser", password="testpassword")
