from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    # Add other URL patterns specific to the 'search_app' app
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('full/<int:product_id>/', views.full_remove, name='full_remove'),
]
