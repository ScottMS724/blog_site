from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.views.generic import ListView 
from django.views import View 
from .models import Post
from .forms import CommentForm 

#homepage with 3 most recent posts
class StartingPageView(ListView):
  template_name = "main_blog/index.html"
  model = Post 
  ordering = ["-date"]
  context_object_name = "posts"

  def get_queryset(self):
    queryset = super().get_queryset()
    data = queryset[:3]
    return data 

#post index- all posts 
class AllPostsView(ListView):
  template_name = "main_blog/all-posts.html"
  model = Post 
  ordering = ["-date"]
  context_object_name = "all_posts" 

#single post show page
class SinglePostView(View):
 
  def get(self, request, slug): 
    post = Post.objects.get(slug=slug)
    context = {
      "post": post,
      "post_tags": post.tags.all(),
      "comment_form": CommentForm()
    }
    return render(request, "main_blog/post-details.html", context)


  def post(self, request, slug):
    comment_form = CommentForm(request.POST)
    post = Post.objects.get(slug=slug)

    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post 
      comment.save()

      return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

    context = {
      "post": post,
      "post_tags": post.tags.all(), 
      "comment_form": comment_form
    }
    return render(request, "main_blog/post-details.html", context)
    