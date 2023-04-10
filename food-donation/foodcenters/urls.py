from django.urls import path
from .import views

urlpatterns = [
    path('centerlist/',views.center_list,name='list'),
    path('centerlist/book/<int:id>',views.book,name='book'),
]