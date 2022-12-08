from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import User, Post, Likes
from .forms import PostForm, RegisterForm


def index(request):
    form = PostForm()
    posts = Post.objects.order_by('-post_date')

    context= {
        'form': form,
        'posts': posts,
    }
    return render(request, "network/index.html", context=context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.pk
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, "network/register.html", {
                "message": "Fill out all the requested fields."
            })
        else:
            user_image = request.FILES['registerImageFile']
            first_name = request.POST['registerFirstName']
            last_name = request.POST['registerLastName']
            username = request.POST["registerUsername"]
            email = request.POST["registerEmail"]

            # Ensure password matches confirmation
            password = request.POST["registerPassword"]
            confirmation = request.POST["registerConfPassword"]

            if password != confirmation:
                context = {
                    'form': form,
                    'message':'Passwords must match.',
                }
                return render(request, "network/register.html", context)

            # Attempt to create new user
            try:
                user = User.objects.create_user(username=username,
                                                first_name=first_name, 
                                                last_name=last_name, 
                                                email=email, 
                                                password=password,
                                                user_image=user_image)
                user.save()
                request.session['user_id'] = user.id
            except IntegrityError:
                context = {
                    'form': form,
                    'message': 'Username already taken.',
                }
                return render(request, "network/register.html", context)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

    context = {
        "form": form,
    }
    return render(request, "network/register.html", context=context)

def posts(request):
    form = PostForm()
    posts = Post.objects.order_by('-post_date')
    likes = Likes.objects.all()
    context= {
        'form': form,
        'posts': posts,
        'likes': likes,
    }
    return render(request, "network/index.html", context=context)

@login_required
def save_post(request):
    form = PostForm()
    user = get_object_or_404(User.objects.filter(pk=request.session['user_id']))

    if request.method == "POST":
        form = PostForm(request.POST)

        # Attempt to create new listing
        try:
            post = Post()
            post.user = user
            post.post_id = post.pk
            post.post_content = request.POST['postContent']
            post.post_date = timezone.now()
            post.save()
        except IntegrityError:
            context = {
                'form': form,
                'message': 'Error while saving post.',
            }
            return render(request, "network/index.html", context=context)
        return HttpResponseRedirect(reverse("index"))
    else:
        posts = Post.objects.order_by('-post_date')

    context= {
        'form': form,
        'userName': user.first_name + ' ' + user.last_name,
        'userImage': user.user_image,
    }
    return render(request, "network/index.html", context=context)


@login_required
def like_post(request):
    return HttpResponseRedirect(reverse("index"))

@login_required
def following(request):
    return HttpResponseRedirect(reverse("index"))
