from django.urls import path
from bookapp import views


urlpatterns = [
   path('home',views.homepage),
   path('addbook',views.addbook),
   path('delete/<bookid>',views.deletebook),
   path('update/<bookid>',views.updatebook)
]