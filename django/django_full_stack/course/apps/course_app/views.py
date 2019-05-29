from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CourseForm
from .models import Course


def index(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        errors = Course.objects.extra_validation(request.POST)
        if errors:
            for _, v in errors.items():
                messages.error(request, v)
                return render(request, 'course_app/index.html', dict(form=form))
        if form.is_valid():
            print("form is valid")
            Course.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"]).save()
        else:
            return render(request, 'course_app/index.html', context={'form': form})

    course_list = Course.objects.all()
    form = CourseForm()
    return render(request,
                  'course_app/index.html',
                  dict(course_list=course_list, form=form))


def destroy(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        raise Http404("course does not exist")

    return render(request, "course_app/destroy.html", dict(course=course))


def destroy_confirm(request, pk):
    try:
        course = Course.objects.get(id=pk)
        course.delete()
    except Course.DoesNotExist:
        messages.error('id does not exist')

    return redirect(to=reverse("index"))
