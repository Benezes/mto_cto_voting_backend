from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.UserCreate.as_view(), name="user-create"),
    path("posts/", views.PostList.as_view(), name="post-list"),
    path("posts/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path("posts/<int:pk>/vote/", views.VoteCreate.as_view(), name="post-vote"),
]
