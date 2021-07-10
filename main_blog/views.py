from django.shortcuts import render, get_object_or_404 
from .models import Post

#homepage
def starting_page(request): 
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "main_blog/index.html", {
      "posts": latest_posts  
    }) 

#post index
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "main_blog/all-posts.html", {
       "all_posts": all_posts
    })

#post show page
def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "main_blog/post-details.html", {
      "post": identified_post,
      "post_tags": identified_post.tags.all()
    })
