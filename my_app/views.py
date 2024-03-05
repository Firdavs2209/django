# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def page_view(request, page_number):
    return HttpResponse(f'This is page {page_number}')

def create_page(request, page_number, prev_page=None, next_page=None):
    return render(request, 'page.html', {'page_number': page_number, 'prev_page': prev_page, 'next_page': next_page})
