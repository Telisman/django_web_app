from django.shortcuts import render,get_object_or_404
from chores.forms import AddChoresForm
from django.http import HttpResponseRedirect
from chores.models import ChoresPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView




# Add new offer
def AddOfferPage(request):
    submitted = False
    if request.method == "POST":
        form = AddChoresForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        pass

    form = AddChoresForm
    return render(request, "form_add_offer.html", {'form': form})




#show all offers
def OfferView(request):
    offers = ChoresPost.objects.all()
    context = {
        'offers': offers,
    }
    return render(request,"offers.html", context)


# show offer detail full description

class ShowOffer(DetailView):
    model = ChoresPost
    template_name = "offer_detail_view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowOffer, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(ChoresPost, pk=self.kwargs['pk'])
        return context


