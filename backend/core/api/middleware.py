from .models import Post
from django.utils import timezone

class CheckPostScheduleMiddleware :
    def __init__(self , get_response) :
        self.get_response = get_response

    def __call__(self,request):
        scheduled_post = Post.objects.filter(status = "Scheduled")
        for p in scheduled_post :
            if p.is_to_be_posted() :
                p.status = "published"
                p.save()
        response = self.get_response(request)
        return response
