from django.shortcuts import render
from .forms import RestaurantForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            return render(request, 'index.html', {'form': form})
    context = {'form': RestaurantForm()}
    return render(request, 'index.html', context)