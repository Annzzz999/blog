from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Kategori,Bluda1

def post_list(request):
    Kategoriis = Kategori.objects.filter()
    return render(request, 'blog/post_list.html', {'posts': Kategoriis})

def post_single(request,pk):
    Bluda = Bluda1.objects.filter(kategori=pk)

    return render(request, 'blog/post_single.html', {'posts': Bluda})