from django.shortcuts import render, redirect
from .models import Signup
import feedparser

def one(request):
    return render(request, 'one.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = Signup.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            request.session['username'] = user.username
            return redirect('one')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Signup.objects.filter(username=username).exists():
            return render(request, 'signup.html', {
                'error': 'Username already exists'
            })

        Signup.objects.create(
            username=username,
            email=email,
            password=password
        )

        return render(request, 'signup.html', {
            'success': 'Signup Successfully'
        })

    return render(request, 'signup.html')


def todaysnews(request):
    feed = feedparser.parse(
        "https://www.thehindu.com/feeder/default.rss"
    )

    news_list = []

    for item in feed.entries[:10]:
        news_list.append({
            'title': item.title,
            'link': item.link,
            'summary': item.summary
        })

    return render(request, 'todaysnews.html', {
        'news_list': news_list
    })
def check_news(request):
    return render(request, 'check_news.html')