from ast import pattern
from django.urls import path
from . import views


app_name='myapp'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('<int:id>/',views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:id>/', views.update_product, name='update_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('mylistings', views.my_listings, name='mylistings'),
]