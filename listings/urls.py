from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'listings'),
    path('<int:listing_id>', views.listing, name = 'listing'),
    path('search', views.search, name = 'search'),
    path('new_listing_form', views.new_listing_form, name = 'new_listing_form'),
    path('simple_checkout', views.simple_checkout, name = 'simple_checkout'),
]