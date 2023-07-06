from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('shoes/', views.ShoeList.as_view(), name="shoe_list"),
    path('shoes/new/', views.ShoeCreate.as_view(), name="shoe_create"),
    path('shoes/<int:pk>/', views.ShoeDetail.as_view(), name="shoe_detail"),
    path('shoes/<int:pk>/update', views.ShoeUpdate.as_view(), name="shoe_update"),
    path('shoes/<int:pk>/delete',views.ShoeDelete.as_view(), name="shoe_delete"),
    path('shoes/<int:pk>/songs/new/', views.StoreCreate.as_view(), name="store_create"),
    path('shoppingcart/<int:pk>/stores/<int:store_pk>/', views.ShoppingCartStoreAssoc.as_view(), name="shoppingcart_store_assoc"),
]
