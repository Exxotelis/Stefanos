from django.shortcuts import render

# Create your views here.


def nifika(request):
    return render(request, 'nifika.html')
