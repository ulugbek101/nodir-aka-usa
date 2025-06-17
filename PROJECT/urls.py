from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, 
                                      PasswordResetConfirmView, PasswordResetCompleteView)

from users import views


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", include("app_main.urls")),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path("password-reset/", PasswordResetView.as_view(template_name="password-reset.html"), name="password_reset"),
    path("password-reset-done/", PasswordResetDoneView.as_view(template_name="password-reset-done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="password-reset-confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", PasswordResetCompleteView.as_view(template_name="password-reset-complete.html"), name="password_reset_complete"),
]


# urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)
