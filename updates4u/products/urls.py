from django.urls import path
from products import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', views.home, name="home" ),
    path('search', views.search, name="search" ),
    path('product/<str:id>', views.singleproduct, name="search" ),
    path('product', views.product, name="product" ),
    path('about', views.about, name="about" ),
    path('update/<str:id>', views.updateProduct, name="search" ),


    
    ]

urlpatterns += staticfiles_urlpatterns()