from django.shortcuts import render
from first_app.models import CreatePost
from django.shortcuts import render, get_object_or_404
from .models import CreatePost
# here just get the last one of the post and show the index _page 
def home_view(request):
    data = CreatePost.objects.all().order_by('-created_at')[:1]
   
    context = {
        "data":data
    }

    return render(request,'index.html',context)



# sort by the data created and show them at all 
def show_oldest(request):
    data = CreatePost.objects.all().order_by('-created_at')
    context = {
        "data":data
    }

    return render(request,'oldest.html',context)






def post_detail(request, pk):
    post = get_object_or_404(CreatePost, pk=pk)
    share_url = request.build_absolute_uri()
    context = {
        'post': post,
        'share_url': share_url,
    }
    return render(request, 'post_detail.html', context)


