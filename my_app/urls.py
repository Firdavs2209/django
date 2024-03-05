# myapp/urls.py
from django.urls import path
from .views import page_view, create_page

urlpatterns = [
    path('page/<int:page_number>/', page_view, name='page_view'),
    path('page/1/', create_page, {'page_number': 1, 'next_page': 2}, name='first_page'),
    path('page/2/', create_page, {'page_number': 2, 'prev_page': 1, 'next_page': 3}, name='second_page'),
    path('page/3/', create_page, {'page_number': 3, 'prev_page': 2, 'next_page': 4}, name='third_page'),
    path('page/4/', create_page, {'page_number': 4, 'prev_page': 3, 'next_page': 5}, name='fourth_page'),
    path('page/5/', create_page, {'page_number': 5, 'prev_page': 4}, name='fifth_page'),
]
