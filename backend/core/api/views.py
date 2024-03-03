from datetime import tzinfo
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView, Response
from django.contrib.auth.models import User
from django.utils import timezone
from api.models import Post
from .serializers import PostSerializer
import pytz

class UserRegisterView(APIView) :
    permission_classes = [AllowAny]
    def post(self , request) :
        username = request.data.get("username")
        print(username)
        email = request.data.get("email")
        print(email)
        password = request.data.get("password")
        user = User.objects._create_user(username = username , email = email , password = password)
        user.save()
        return Response({
            "status" : "success now login"
        })

class ListAllPosts(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self , request) :
        posts = Post.objects.filter(status = "published")

        serializer = PostSerializer(data = posts,many = True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)

class CreatePost(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self , request) :
        import datetime
        post_at = datetime.datetime.strptime(request.data.get("post_at"), '%Y-%m-%dT%H:%M')
        post_at = pytz.timezone("Asia/Kolkata").localize(post_at)
        title = request.data.get("title")
        content = request.data.get("content")
        current_ist_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

        if post_at <= current_ist_time :
            status = "Published"
        else :
            status = "Scheduled"

        p = Post.objects.create(
            title = title ,
            content = content ,
            user = User.objects.get(id = request.user.id),
            post_at = post_at ,
            status = status
        )
        p.save()
        return Response({
            "post":"saved"
        })
