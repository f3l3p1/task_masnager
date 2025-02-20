from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login),  # Redirect to the login page by default
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
]
