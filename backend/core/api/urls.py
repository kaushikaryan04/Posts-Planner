from django.urls import path

from api.views import CreatePost, ListAllPosts, UserRegisterView

urlpatterns = [
    path("register" , UserRegisterView.as_view()),
    path("allposts" , ListAllPosts.as_view()),
    path("createpost" , CreatePost.as_view())
]
