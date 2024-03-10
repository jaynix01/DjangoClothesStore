from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProducsListView.as_view(), name='index'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/',
         views.basket_remove, name='basket_remove'),
    path('category/<int:category_id>/', views.ProducsListView.as_view(), name='category'),
    path('page/<int:page>/', views.ProducsListView.as_view(), name='paginator'),

]
