from django.shortcuts import render

# Create your views here.

#index
def starting_page(request):
    return render(request, "main_blog/index.html") 

def posts(request):
    return render(request, "main_blog/all-posts.html")

def post_detail(request):
    pass 
