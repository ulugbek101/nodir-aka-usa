from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="index"),       # http://localhost:8000/
    path("classes/", views.classes, name="classes"),  # http://localhost:8000/classes/
    path("profile/", views.profile, name="profile"),  # http://localhost:8000/profile/
    path("update-profile/", views.update_profile, name="update_profile"),
    path("classes/<int:class_id>/", views.class_detail, name="class_detail"),
    path("lesson-edit/<int:lesson_id>/", views.lesson_edit, name="lesson_edit"),
    path("lesson-delete/<int:lesson_id>/", views.lesson_delete, name="lesson_delete"),
    path("lesson-detail/<int:lesson_id>/", views.lesson_detail, name="lesson_detail"),
]
