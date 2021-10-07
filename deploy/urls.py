from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='firstfile'),
    path('list/', views.MyList.as_view(), name='showfile')
]
