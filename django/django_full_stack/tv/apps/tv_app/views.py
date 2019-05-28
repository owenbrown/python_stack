from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, render
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
        form = ShowForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse(viewname="index"))
    show = Show.objects.get(pk=pk)
    form = ShowForm(instance=show)
    return render(request, "tv_app/update.html", {"form": form, "show": show})


def new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShowForm(request.POST)
        # check whether it's valid:
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
