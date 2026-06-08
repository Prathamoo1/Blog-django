from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogs.models import Blog ,Category

# Create your views here.
def posts_by_category(request,category_id):
    posts=Blog.objects.filter(status='Published',category=category_id)
    try:
        category=Category.objects.get(pk=category_id)
    except:
        # redirect user to home page
        return redirect("home")
    # use get_object_or_404 when to show 404 error page if category is not found
    # catgory=get_object_or_404(category,pk=category_id)
    context={
        'posts': posts,
        'category':category ,
    }
    return render(request,'posts_by_category.html',context)