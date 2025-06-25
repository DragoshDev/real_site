from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Transfer, Player, Rumor, Match , Legend

from .forms import CommentForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


def startapp(request):
    latest_posts = Post.objects.all().order_by('-date')[:6]
    return render(request, 'realblog/index.html', {
        "posts": latest_posts,
    })



@login_required
def index(request):
    posts = Post.objects.all()
    matches = Match.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'realblog/index.html', {
        "posts": posts,
        "matches": matches
    })


@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True).order_by('-created_at')

    similar_posts = Post.objects.filter(tag__in=post.tag.all()).exclude(id=post.id).distinct()[:3]


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        form = CommentForm()

    return render(request, 'realblog/post-detail.html', {
    'post': post,
    'comments': comments,
    'form': form,
    'similar_posts': similar_posts,
})

@login_required
def all_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'realblog/all-posts.html', {
        'posts': posts
    })

@login_required
def transferuri(request):
    transfer = Transfer.objects.all()
    return render(request, "realblog/transferuri.html", {"transfers": transfer})

@login_required
def zvonuri(request):
    rumors = Rumor.objects.all()
    return render(request, 'realblog/zvonuri.html', {'rumors': rumors})


@login_required
def legende(request):
    legends = Legend.objects.all()[:10]
    return render(request, "realblog/legends.html", {"legends": legends})

@login_required
def echipa(request):
    all_players = Player.objects.all().order_by('number')
    starting_players = Player.objects.filter(is_starting=True).order_by('number')
    context = {
        'players': all_players,
        'starting_players': starting_players,
    }
    return render(request, 'realblog/echipa.html', context)


@login_required
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "realblog/register.html", {"form": form})







