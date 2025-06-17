from datetime import datetime

from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from app_main.models import Class, Lesson


def home_page(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        # Not authenticated
        return redirect("login")


def classes(request):
    teacher = request.user
    classes = teacher.classes.all()

    context = {
        "classes": classes,  # [ ..., ... ]
        "active_route": "classes",
    }
    return render(request=request, template_name="classes.html", context=context)


def profile(request):
    return render(request=request, template_name="profile.html")


def update_profile(request):
    user = request.user

    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    middle_name = request.POST.get("middle_name")
    email = request.POST.get("email")
    phone_number = request.POST.get("phone_number")
    address = request.POST.get("address")

    user.first_name = first_name
    user.last_name = last_name
    user.middle_name = middle_name
    user.email = email
    user.phone_number = phone_number
    user.address = address
    user.save()

    return redirect("/profile/")


def class_detail(request, class_id):
    teacher_class = Class.objects.get(id=class_id)

    context = {
        "class": teacher_class,
        "today": timezone.now(),
        "active_route": "classes",
    }
    return render(request, "class_detail.html", context)


def lesson_edit(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == "POST":
        theme = request.POST.get("theme")
        lesson_date_str = request.POST.get("lesson_date")

        try:
            lesson_datetime = datetime.strptime(lesson_date_str, "%Y-%m-%dT%H:%M")
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect(f"/lesson-edit/{lesson.id}")

        if lesson_datetime.date() <= timezone.now().date():
            messages.error(request, "Lesson date cannot be today or in the past.")
            return redirect(f"/lesson-edit/{lesson.id}")

        lesson.theme = theme
        lesson.lesson_date = lesson_datetime
        lesson.save()
        
        return redirect(f"/classes/{lesson.class_name.id}")

    context = {
        "lesson": lesson,
    }
    return render(request, "lesson_form.html", context)


def lesson_delete(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    class_id = lesson.class_name.id

    if request.method == "POST":
        if lesson.class_name.teacher != request.user:
            messages.error(request, "You cannot delete other teacher's lesson")
            return redirect("/classes/")

        lesson.delete()
        return redirect(f"/classes/{class_id}")

    context = {
        "lesson": lesson,
    }
    return render(request, "delete.html", context)


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if lesson.class_name.teacher != request.user:
        messages.error(request, "You cannot view other teacher's lesson")
        return redirect("/classes/")

    context = {
        "lesson": lesson,
    }
    return render(request, "lesson_datail.html", context)
