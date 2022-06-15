from email.contentmanager import raw_data_manager
from unittest import expectedFailure
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

# Create your views here


# If the user is authenticated, then render the index.html page with info about the user's profile.           
def index(request):
    news = News.objects.all().order_by('-id')
    # Take the latest news and show it on the breaking news bar:
    breakNews = News.objects.order_by("id").reverse()[:1]
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'news/index.html', {
        'profile': profile,
        'news': news,
        'breakNews': breakNews
    })
    else:
        return render(request, 'news/index.html', {
        'news': news
    })



@csrf_exempt
@login_required
def post_comment(request):
    if request.method == 'POST':
        news_id = request.POST.get('id')
        singleNews = News.objects.get(id=news_id)
        user = User.objects.get(username=request.POST.get('user'))
        comment_body = request.POST.get('comment')
        profile = Profile.objects.get(user=user)
        try:
            comment = Comment.objects.create(comment=comment_body, user=user, profile=profile)
            comment.user = user
            comment.save()
            comment.profile = profile
            comment.save()
            singleNews.comments.add(comment)
            singleNews.save()
            return JsonResponse({'status':200, 'comment_id': comment.id, 'time': comment.time})
        except Exception as e:
            print(e)
            return JsonResponse({'status':500})




def single_news(request, news_id):
    allNews = News.objects.all().order_by('?')[:2]
    singleNews = News.objects.get(id=news_id)
    allProfiles = Profile.objects.all()
    allComments = Comment.objects.filter(news_comments=news_id).order_by('-id')
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        commentForm = CommentForm(request.POST)
        return render(request, "news/news.html", {
            'singleNews': singleNews,
            'profile': profile, 
            'commentForm': commentForm,
            'allProfiles': allProfiles,
            'allComments': allComments,
            'allNews': allNews,
        })
    else:
        return render(request, 'news/news.html', {
        'singleNews': singleNews,
        'allProfiles': allProfiles,
        'allComments': allComments,
        'allNews': allNews,
    })



# Show index version for users or continue at login.html till a correct auth:
def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "news/login.html", {
                "login_message": "Invalid username and/or password."
            })
    else:
        return render(request, "news/login.html")



# Go out the logged user version and show the normal index page:
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



# If passwords match, try to save the new user if his/her email is not taken.
# Render the login page, because register and login are in the same place: 
def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "news/login.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(email, email, password)
            user.username = username
            user.last_name = last_name
            user.first_name = first_name
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "news/login.html", {
                "register_message": "Email address already taken."
            })
        login(request, user)
        # Redirect user to avatar.html
        return HttpResponseRedirect(reverse("avatar"))
    else:
        return render(request, "news/login.html")



# Take the AvatarForm from forms.py and save the value:
@login_required
def avatar(request):
    user = request.user
    avatarForm = AvatarForm(request.POST)
    if request.method == 'POST':
        if avatarForm.is_valid():
            profile = avatarForm.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, "news/avatar.html", {
        "avatarForm": avatarForm,
    })



@login_required
def write_news(request):
    newsForm = NewsForm(request.POST)
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile_id = Profile.objects.get(user=request.user)
        if newsForm.is_valid():
            newsForm = newsForm.save(commit=False)
            newsForm.user = request.user
            newsForm.save()
            newsForm.profile = profile_id
            newsForm.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'news/write.html', {
                'newsForm': newsForm, 
                'profile': profile
            })        



@csrf_exempt
@login_required
# Get the call via JS to add or remove Likes from the likelist:
def add_to_readlist(request):
    if request.method == "POST":
        news_id = request.POST.get('id')
        try:
            # If logged user didn't click Like before, add her/him:
            news = News.objects.get(id=news_id)
            if request.user in news.readlist.all():
                news.readlist.remove(request.user)
                news.save()
                count = news.readlist.count()
                return JsonResponse({
                    'count': count,
                    "status":201
                })
            # If logged user clicked Like already, remove her/him:
            else:
                news.readlist.add(request.user)
                news.save()
                count = news.readlist.count()
                return JsonResponse({'count': count, "status":201})
        except:
            return JsonResponse({}, status=404)
    return JsonResponse({}, status=404)



@login_required
def del_from_readlist(request, news_id):
    news = News.objects.get(id=news_id)
    user = User.objects.get(username=request.user)
    news.readlist.remove(user)
    news.save
    return HttpResponseRedirect(reverse("index"))



@login_required
def load_readlist(request):
    profile = Profile.objects.get(user=request.user)
    user = User.objects.get(username=request.user)
    readlist = News.objects.filter(readlist=user).order_by('-time') 
    return render(request, "news/readlist.html",{
                "profile": profile,
                "user": user,
                "readlist": readlist,
            })


@login_required
@csrf_exempt
def delete(request):
    if request.method == "POST":
        try: 
            comment_id = request.POST.get('id')
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({}, status=201)
        except:
            return JsonResponse({}, status=404)
    return JsonResponse({}, status= 400)



@csrf_exempt
@login_required
def edit_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('id')
        comment_body = request.POST.get('comment')
        print(comment_body)
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.comment = comment_body
            comment.save()
            return JsonResponse({}, status=201)
        except:
            return JsonResponse({}, status=404)
    return JsonResponse({}, status=400)