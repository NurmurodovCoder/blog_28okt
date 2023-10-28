from django.shortcuts import render, redirect
from .models import Post, Person, Tag, Category, Comments, Contact
from .forms import ContactForm, CommentsForm

def index(request):
    posts = Post.objects.order_by('-id')[3:6]
    banner = Post.objects.order_by('-id')[:3]
    # a = posts.reate_time()

    context = {
        'posts':posts,
        'banner':banner,
        # 'a':a
    }
    return render(request, 'index.html', context)


def blog(request):
    posts = Post.objects.all().order_by('-id')

    return render(request, 'blog.html', {'posts':posts})


def detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment.all()
    form = CommentsForm()
    if request.method=='POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            parent_obj = None
            try:
                parent_id = request.POST.get('parentId')
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comments.objects.get(pk=parent_id)
            if parent_obj:
                comment = form.save(commit=False)
                comment.parent = parent_obj 
                comment.post_id = post.id
                comment.save()
                return redirect('detail', pk)
            
            else:
                comment = form.save(commit=False)
                comment.post_id = post.id
                comment.save()
                return redirect('detail', pk)
    
    return render(request, 'single.html', {
        'post':post,
        'comments':comments,
        'form':form
        })


def about(request):
    about = Person.objects.first
    return render(request, 'about.html', {'about': about})


def contact(request):
    person = Person.objects.first()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('index')
    
    return render(request, 'contact.html', {'person':person, 'form':form})

