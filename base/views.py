from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .form import ImageForm
from .models import Image

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)   # Redirect to a success page after saving the image
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
