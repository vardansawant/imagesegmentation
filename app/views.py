from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm
from .processor import worker
import shutil

# Create your views here.
def index(request):
    if request.method=='GET':
        context = {
            'form': InputForm()
        }
    if request.method=='POST':
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            output = worker('media/input/'+request.FILES['image_file'].name)
            dir = 'media/input'
            shutil.rmtree(dir)
            context = {'output_image': '/media/output/converted.png'}
            # output.save("media/output/converted.png", format="png")
            return render(request, 'app/test.html', context)

    return render(request, 'app/test.html', context)