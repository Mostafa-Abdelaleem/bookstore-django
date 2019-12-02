from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'template.html')

def store(request):
    count = Book.objects.all().count
    context_vars= {'count': count }
    return render(request, 'template2.html', context_vars)
