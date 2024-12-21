import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user():
    """Create and return a user instance for test cases."""
    return User.objects.create_user(username="testuser", password="testpassword")
