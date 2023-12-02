from django.urls import path
from .views import home_page, models_3d, DetailModel


urlpatterns = [
    path('', home_page, name='home_page'),
    path('modellar/', models_3d, name='models'),
    path('modellar/<int:pk>/', DetailModel.as_view(), name='detail')
]