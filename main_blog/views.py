from django.shortcuts import render, get_object_or_404 
from django.views.generic import ListView, DetailView 
from .models import Post

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
class SinglePostView(DetailView):
  template_name = "main_blog/post-details.html"
  model = Post 

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["post_tags"] = self.object.tags.all() 
    return context