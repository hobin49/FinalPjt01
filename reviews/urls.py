from django.urls import path
from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name="delete"),
    path('<int:pk>/like/', views.like, name='like'),
    # comment
    path('<int:pk>/comment/create', views.comment_create, name="comment_create"),
    path('<int:pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('taste/', views.taste, name="taste"),
]
