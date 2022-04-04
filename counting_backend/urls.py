from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello),
    path('insert_a_consume/',views.insert_a_consume),
    path('show_latest_month_consume/',views.show_latest_month_consume),
    path('show_category_consume/',views.show_category_consume),
]