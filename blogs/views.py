from django.shortcuts import render,HttpResponse,redirect
from .models import Blogs, Category, Comment
from django.shortcuts import get_object_or_404 # Assuming Blogs model is imported
from django.db.models import Q
from django.http import HttpResponseRedirect



# Create your views here.

def posts_by_category(request, category_id):
    # fetch the posts that belong to the category with the given id
    posts = Blogs.objects.filter(status='published', category__id=category_id)  
    # use try/except when u perform some action when category not avaviable
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')

    #when u want to show 404 error 
    #category = get_object_or_404(Category, pk=category_id)    
    context = {
        'posts': posts,
        'category': category
    }

    return render(request, 'posts_by_category.html', context)  # Correct indentation here

#blogs

def blogs(request,slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published')

    #comment
    if request.method=="POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info) 
    comments = Comment.objects.filter(blog = single_post)
    comment_count = comments.count()
    context = {
        'single_post':single_post,
        'comments':comments,
        'comment_count':comment_count
     }
    return render(request, 'blogs.html',context)

# search functionality
def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword), status='published')
    content = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html',content)