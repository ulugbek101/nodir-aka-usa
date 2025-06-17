from django.utils import timezone
from django.shortcuts import render, redirect

from app_main.models import Class


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
