from django.urls import include, path
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("sign_up/", views.SignUpView.as_view(), name="sign_up"),
]