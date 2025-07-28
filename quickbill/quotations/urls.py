from django.urls import path
from . import views


urlpatterns = [
    path('quotation/', views.quotation_list, name='quotation_list'),
    path('quotation/create', views.create_quotation, name='create_quotation'),
    path('quotation/<int:pk>/', views.quotation_detail, name='quotation_detail'),
    path('quotation/<int:pk>/edit', views.update_quotation, name='update_quotation'),
    path('quotation/<int:pk>/delete', views.delete_quotation, name='delete_quotation'),
]

