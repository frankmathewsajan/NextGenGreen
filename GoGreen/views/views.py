from django.shortcuts import render

def index(request):
        return render(request, 'GoGreen/index.html') if request.user.is_authenticated else render(request, 'GoGreen/home.html')

def home(request):
        return render(request, 'GoGreen/home.html')
    
def profile(request):
    return render(request, 'GoGreen/profile.html')

def blogs(request):
    return render(request, 'GoGreen/blogs.html')


def blog_post(request):
      return render(request, 'GoGreen/blog-post.html')