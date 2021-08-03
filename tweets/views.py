from django.http.response import Http404, JsonResponse
from django.shortcuts import render, HttpResponse

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, './pages/home.html')

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": query.id, "content": query.content} for query in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_datail_view(request,tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,   
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content 
    except:
        data["message"] = "Not found"
        status = 404

    return JsonResponse(data, status=status)
