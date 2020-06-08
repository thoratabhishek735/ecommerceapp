from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name="Shophome"),
    path("about/", views.about , name="About us"),
    path("mens/", views.mens , name="mens"),
    path("womens/", views.womens , name="womens"),
    path("contact/", views.contact , name="Contact us"),
    path("search/", views.search , name="search"),
    path("tracker/", views.tracker , name="Order tracker"),
    path("productview/<int:myid>", views.productview , name="view product"),
    path("productviewm/<int:myidm>", views.productviewm , name="view productm"),
    path("checkout/", views.checkout , name="checkout"),
    
    

]