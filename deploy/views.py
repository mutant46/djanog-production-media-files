from django.shortcuts import render
from .forms import MediaFileForm
from django.http import HttpResponse
from django.views.generic import ListView
from .models import MediaFile
# Create your views here.


def index(request):
    if request.method == "POST":
        form = MediaFileForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('file has been added')
    else:
        form = MediaFileForm()
    return render(request, 'addfile.html', {'form': form})


class MyList(ListView):
    model = MediaFile
