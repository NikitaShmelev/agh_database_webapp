from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from users.forms import CustomUserCreationForm


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)