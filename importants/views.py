from django.shortcuts import render
from django.http import HttpResponse
from importants.models import important

# Create your views here.

def importants_home(request):
    return render(request, 'importants/index.html')

def read_important(request,pk):
    importants = important.objects.get(category=pk)
    context = {'importants':importants}

    return render(request, 'importants/read.html', context)    