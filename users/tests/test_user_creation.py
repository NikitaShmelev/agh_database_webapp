import pytest
from django.contrib.auth import get_user_model
from professors.models import ProfessorProfile
from students.models import StudentProfile


@pytest.mark.django_db
def test_create_user_without_profiles():
    user = get_user_model().objects.create_user(
        username="testuser", email="testuser@example.com", password="testpassword123"
    )

    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert not user.is_student
    assert not user.is_professor
    assert not StudentProfile.objects.all()
    assert not ProfessorProfile.objects.all()


@pytest.mark.django_db
def test_create_user_with_student_profile():
    user = get_user_model().objects.create_user(
        username="studentuser",
        email="studentuser@example.com",
        password="testpassword123",
        is_student=True,
    )

    assert user.is_student
    assert not user.is_professor

    assert StudentProfile.objects.get(user=user)
    assert not ProfessorProfile.objects.all()


@pytest.mark.django_db
def test_create_user_with_professor_profile():
    user = get_user_model().objects.create_user(
        username="professoruser",
        email="professoruser@example.com",
        password="testpassword123",
        is_professor=True,
    )

    # Test user has the professor profile
    assert not user.is_student
    assert user.is_professor
    assert ProfessorProfile.objects.get(user=user)
    assert not StudentProfile.objects.all()


@pytest.mark.django_db
def test_create_user_with_both_profiles():
    user = get_user_model().objects.create_user(
        username="bothuser",
        email="bothuser@example.com",
        password="testpassword123",
        is_professor=True,
        is_student=True,
    )

    # Test user has both profiles
    assert user.is_student
    assert user.is_professor
    assert ProfessorProfile.objects.get(user=user)
    assert StudentProfile.objects.get(user=user)
