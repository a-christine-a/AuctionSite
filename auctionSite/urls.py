from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('hii', views.product_list, name="product_list"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('join us/',views.JoinTeam.as_view(), name="join"),
    path('application success/',views.app_success, name="teamsuccess"),
    path('<slug:category_slug>/', views.product_list, name="product_list_by_category"),
    path('<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),
]