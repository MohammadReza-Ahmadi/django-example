from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('v1/', views.view_1, name="view-1"),
    path('profile/<user_id>', views.get_profile, name='get-profile'),
]
