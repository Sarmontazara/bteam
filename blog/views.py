from django.shortcuts import render, get_object_or_404,HttpResponseRedirect,render_to_response
from django.utils import timezone
from blog.forms import OrderForm
from .models import Post,Order,Status
from django.core.mail import send_mail
from django.core.paginator import Paginator


def index(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        try:
            if form.is_valid():
                order = form.save(commit=False)
                order.page = request.META.get('HTTP_REFERER', '')
                order.price = 0
                order.zstatus_id = 1
                if 'sale' not in request.POST:
                    order.sale = False
                order.save()

                send_mail(
                    'Письмо с сайта bazulurteam.ru',
                    request.POST.get('text'),
                    'goth_of_rose@bk.ru',
                    ['goth_of_rose@bk.ru'],
                    fail_silently=True,
                )

        except Exception as e:
            print(e)

        return HttpResponseRedirect("/thanks.html")


    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})
def blog(request):
    last_pages = Post.objects.order_by("-pk")[0:5]  # Вывод последних 5 статей справа
    articles_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')  # Пагинация
    paginator = Paginator(articles_list, 5)  # Show 5 contacts per page
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'blog/blog.html', {'last_pages': last_pages, 'articles': articles})
def post_detail(request, pk):
    last_pages = Post.objects.order_by("-pk")[0:5]  # Вывод последних 5 статей справа
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'last_pages': last_pages, 'post': post})
def thanks(request):
    return render(request, 'blog/thanks.html')
def yandexver(request):
    return render(request, 'blog/yandex_2ce42828c2811ce8.html')
def seosan(request):
    return render(request, 'blog/seosan-verification-f45fecc59a2f45da.html')
def links(request):
    return render(request, 'blog/links1059627.html')
def policy(request):
    return render(request, 'blog/policy.html')
