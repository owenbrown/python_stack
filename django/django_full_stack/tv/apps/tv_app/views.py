from django.contrib import messages
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.views import generic

from .forms import ShowForm
from .models import Show


class IndexView(generic.ListView):
    template_name = 'tv_app/index.html'

    # use default context object name, "show_list"
    # context_object_name = 'all_shows'

    def get_queryset(self):
        """Return view of all tv, sorted by title."""
        return Show.objects.order_by('title')


class DetailView(generic.DetailView):
    model = Show
    template_name = 'tv_app/detail.html'


def update(request, pk):
    if request.method == 'POST':
        errors = Show.objects.extra_validation(request.POST)
        form = ShowForm(request.POST)
        # show = Show.objects.get(id=pk)
        if errors:
            for k, v in errors.items():
                messages.error(request, v)
                print("returned errors. Are they rendering?")
                show = Show.objects.get(pk=pk)
                return render(request, "tv_app/update.html", {"form": form, "show": show})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("detail", args=[pk]))
        else:
            messages.error("form was not valid!")
            for e in form.errors:
                messages.error(e)
            return render(request, 'tv_app/update.html', context={'form': form})

    show = Show.objects.get(pk=pk)
    form = ShowForm(instance=show)
    return render(request, "tv_app/update.html", {"form": form, "show": show})


def new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShowForm(request.POST)
        # check whether it's valid:
        errors = Show.objects.extra_validation(request.POST)
        if errors:
            for k, v in errors.items():
                messages.error(request, v)
                return render(request, 'tv_app/new.html', context={'form': form})

        if form.is_valid() and form.cleaned_data["description"] != 'invalid':
            # process the data in form.cleaned_data as required
            Show.objects.create(
                title=form.cleaned_data["title"],
                network=form.cleaned_data["network"],
                description=form.cleaned_data["description"],
                release_date=form.cleaned_data["release_date"]
            ).save()
            print("Success creating Show!")
            # redirect to a new URL:
            messages.success(request, "new show added")
            return HttpResponseRedirect(reverse(viewname="index"))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ShowForm()

    return render(request, 'tv_app/new.html', context={'form': form})


def destroy(request, pk):
    try:
        show = Show.objects.get(id=pk)
    except Show.DoesNotExist:
        raise Http404("requested resource not found")
    show.delete()
    return HttpResponseRedirect(reverse(viewname="index"))


def url_redirect(request):
    return HttpResponseRedirect("/shows/")
