from django.urls import path
from links import views
from links.views import update_prices,LinkDeleteView

urlpatterns = [
    path('',views.index,name='index'),
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),  
	path('logout', views.UserLogout, name='logout'),
    path('home',views.home,name='home'),
    path('update/', update_prices, name='update-prices'),
    path('delete/<pk>/', LinkDeleteView.as_view(), name="delete"),
]