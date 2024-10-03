from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import LatestNews, BangladeshNews, PoliticsNews,WorldNews,SportsNews,TradeNews,TechnologyNews,EntertainmentNews
from . forms import LatestNewsForm, BangladeshNewsForm,PoliticsNewsForm,WorldNewsForm,SportsNewsForm,TradeNewsForm,TechnologyNewsForm,EntertainmentNewsForm,SignUpForms,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout

def home(request):
    latest_news_items = LatestNews.objects.all()
    bd_news_items = BangladeshNews.objects.all() 
    politics_news_items = PoliticsNews.objects.all() 
    world_news_items = WorldNews.objects.all() 
    sports_news_items = SportsNews.objects.all() 
    trade_news_items = TradeNews.objects.all() 
    technology_news_items = TechnologyNews.objects.all() 
    entertainment_news_items = EntertainmentNews.objects.all() 
    return render(request, 'news/home.html', {
        'l_news': latest_news_items, 
        'bnews': bd_news_items,
        'pl_news':politics_news_items,
        'w_news':world_news_items,
        'sp_news':sports_news_items,
        'trd_news':trade_news_items,
        'tech_news':technology_news_items,
        'en_news':entertainment_news_items,
        })


# <------------------ Base News View ---------------------->
def handle_news_form(request, form_class, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = form_class()

    return render(request, template_name, {'form': form})

# <------------------ Latest News ---------------------->
def latest_news(request):
    return handle_news_form(request, LatestNewsForm, 'news/latest_form.html')

# <--------------------- Bangladesh News ---------------->
def bangladesh_news(request):
    return handle_news_form(request, BangladeshNewsForm, 'news/bdform.html')

# <--------------------- Politics News ------------------->
def politics_news(request):
    return handle_news_form(request, PoliticsNewsForm, 'news/politics_form.html')

# <--------------------- world News ------------------->
def World_news(request):
    return handle_news_form(request, WorldNewsForm, 'news/politics_form.html')

# <--------------------- Sports News ------------------->
def sports_news(request):
    return handle_news_form(request, SportsNewsForm, 'news/politics_form.html')

# <--------------------- Trade News ------------------->
def trade_news(request):
    return handle_news_form(request, TradeNewsForm, 'news/politics_form.html')

# <--------------------- technology News ------------------->
def technology_news(request):
    return handle_news_form(request, TechnologyNewsForm, 'news/politics_form.html')

# <--------------------- entertainment News ------------------->
def entertainment_news(request):
    return handle_news_form(request, EntertainmentNewsForm, 'news/politics_form.html')


def dashboard(request):
    return render(request,'news/dashboard.html')

def sign_up(request):
    if request.method == "POST":
        form = SignUpForms(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations! You have become reporters')
            form.save()
            return redirect('login')
    else:
        form = SignUpForms()
    return render(request,'news/signup.html',{'form':form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if already logged in

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                auth_login(request, user)  # Log the user in
                messages.success(request, 'Logged in successfully!')
                return redirect('dashboard')  # Redirect to dashboard
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()  # Create a new form instance if not POST

    return render(request, 'news/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def details_news(request):
    return render(request,'news/detail_news.html')