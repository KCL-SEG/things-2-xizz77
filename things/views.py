from django.shortcuts import render
from .forms import ThingForm
def home(request):
    form = ThingForm()
    if request.method == "Post":
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'home.html', {'form': form})
