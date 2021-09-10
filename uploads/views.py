from uploads.models import Upload
from django.shortcuts import render

# Create your views here.

def home(request):
  photo = Upload.objects.all()
    # adding context 
  ctx = {'photo':photo}

  return render(request, 'index.html', ctx)
