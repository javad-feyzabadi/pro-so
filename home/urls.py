from django.urls import path

from . views import HomeView,PostDetailView,PostDeleteView

app_name = 'home'

urlpatterns = [
    path('',HomeView.as_view(),name ='home'),
    path('post/<int:post_id>/<slug:post_slug>/',PostDetailView.as_view(),name='post_detail'),
    path('post/delete/<int:post_id>//',PostDeleteView.as_view(),name='post_delete'),

]