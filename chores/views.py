from django.shortcuts import render, get_object_or_404
from chores.forms import AddChoresForm
from django.http import HttpResponseRedirect
from chores.models import ChoresPost
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from chores.filters import ChoresPostFilters


# Add new offer
def AddOfferPage(request):
    submitted = False
    if request.method == "POST":
        form = AddChoresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html')
    else:
        pass

    form = AddChoresForm
    return render(request, "add_offer.html", {'form': form})


# search condition
def is_valid_queryparam(param):
    return param != '' and param is not None


# show all offers
def OfferView(request):
    offers = ChoresPost.objects.all()
    listing_filter = ChoresPostFilters(request.GET, queryset=offers)
    context = {
        'listing_filter': listing_filter,
    }

    return render(request, "project.html", context)


# show offer detail full description

class ShowOffer(DetailView):
    model = ChoresPost
    template_name = "offer_detail_view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowOffer, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(ChoresPost, pk=self.kwargs['pk'])
        return context
