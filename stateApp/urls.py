from django.urls import path
from . import views

urlpatterns = [
    path('state/create/',views.StateCreateView.as_view(),name='state_create'),
    path('state/<int:pk>/',views.StateDetailView.as_view(),name='state_detail'),
    path('state/<int:pk>/delete', views.StateDeleteView.as_view(),name='state_delete'),
    path('',views.StateListView.as_view(), name='state_list'),
    path('state/<int:pk>/update/', views.StateUpdateView.as_view(), name='state_update'),
]