from django.shortcuts import render, redirect, Http404
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm

def article_detail_view(request, article_id):
    articles = {
        1: {'title': 'Economy Ski Set', 'template': 'argument1.html', 'price': 20, 'content': 'Content for Economy Ski Set'},
        2: {'title': 'Premium Ski Set', 'template': 'argument2.html', 'price': 30, 'content': 'Content for Premium Ski Set'},
        3: {'title': 'Superior Ski Set', 'template': 'argument3.html', 'price': 40, 'content': 'Content for Superior Ski Set'},
        4: {'title': 'Economy Snowboard Set', 'template': 'argument4.html', 'price': 25, 'content': 'Content for Economy Snowboard Set'},
        5: {'title': 'Premium Snowboard Set', 'template': 'argument5.html', 'price': 35, 'content': 'Content for Premium Snowboard Set'},
        6: {'title': 'Superior Snowboard Set', 'template': 'argument6.html', 'price': 45, 'content': 'Content for Superior Snowboard Set'},
    }
    article = articles.get(article_id)
    if not article:
        raise Http404("Article does not exist")
    return render(request, f'articles/{article["template"]}', {'article': article})

def like_article(request, id):
    return JsonResponse({'status': 'success'})

def dislike_article(request, id):
    return JsonResponse({'status': 'success'})

def home(request):
    return render(request, 'homepage.html')

def add_to_cart(request, id):
    article = next((article for article in articles_list if article['id'] == id), None)
    if article:
        quantity = int(request.POST.get('quantity', 1))
        days = int(request.POST.get('days', 1))
        cart_item = {
            'id': article['id'],
            'title': article['title'],
            'price': article['price'],
            'quantity': quantity,
            'days': days,
            'total_price': article['price'] * quantity * days
        }
        cart = request.session.get('cart', [])
        cart.append(cart_item)
        request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['total_price'] for item in cart)
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, id):
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['id'] != id]
    request.session['cart'] = cart
    return redirect('cart')

# Lista artykułów
articles_list = [
    {'id': 1, 'title': 'ECONOMY SKI SET', 'content': 'Economy Ski Set description', 'price': 20},
    {'id': 2, 'title': 'PREMIUM SKI SET', 'content': 'Premium Ski Set description', 'price': 30},
    {'id': 3, 'title': 'SUPERIOR SKI SET', 'content': 'Superior Ski Set description', 'price': 40},
    {'id': 4, 'title': 'ECONOMY SNOWBOARD SET', 'content': 'Economy Snowboard Set description', 'price': 25},
    {'id': 5, 'title': 'PREMIUM SNOWBOARD SET', 'content': 'Premium Snowboard Set description', 'price': 35},
    {'id': 6, 'title': 'SUPERIOR SNOWBOARD SET', 'content': 'Superior Snowboard Set description', 'price': 45},
]

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')

def homepage(request):
    return render(request, 'homepage.html')

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about_us.html')

articles_files = {
    1: 'articles/argument1.html',
    2: 'articles/argument2.html',
    3: 'articles/argument3.html',
    4: 'articles/argument4.html',
    5: 'articles/argument5.html',
    6: 'articles/argument6.html',
}

def articles_view(request):
    articles = [
        {'id': 1, 'title': 'Economy Ski Set', 'template': 'argument1.html'},
        {'id': 2, 'title': 'Premium Ski Set', 'template': 'argument2.html'},
        {'id': 3, 'title': 'Superior Ski Set', 'template': 'argument3.html'},
        {'id': 4, 'title': 'Economy Snowboard Set', 'template': 'argument4.html'},
        {'id': 5, 'title': 'Premium Snowboard Set', 'template': 'argument5.html'},
        {'id': 6, 'title': 'Superior Snowboard Set', 'template': 'argument6.html'},
    ]
    return render(request, 'articles.html', {'articles': articles})

def contact_view(request):
    return render(request, 'contact_info.html')

def search_results(request):
    query = request.GET.get('query')
    filtered_articles = [article for article in articles_list if query.lower() in article['title'].lower()]
    return render(request, 'search_results.html', {'articles': filtered_articles, 'query': query})

def article_detail(request, id):
    article = next((article for article in articles_list if article['id'] == id), None)
    template_name = articles_files.get(id, 'articles_details.html')
    return render(request, template_name, {'article': article})

def argument_view(request, article_id):
    article = next((article for article in articles_list if article['id'] == article_id), None)
    if not article:
        raise Http404("Article does not exist")
    template_name = articles_files.get(article_id, 'articles_details.html')
    return render(request, template_name, {'article': article})