from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/',views.card_add,name='cart_add'),
    path('minus/<int:product_id>/',views.card_minus,name='cart_minus'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('all_remove/',views.all_remove,name='all_remove')
]
