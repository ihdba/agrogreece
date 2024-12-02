from django.urls import path


from . import views

app_name = 'products'


urlpatterns = [
    path('', views.index, name='index'),
    path('producers', views.producers, name='producers'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_producer/', views.add_producer, name='add_producer'),
    path('producers/<int:id>/', views.producer_detail, name='producer_detail'),
    path('<int:id>/', views.product_detail, name='product_detail'),
]
