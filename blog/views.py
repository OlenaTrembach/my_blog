from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
from .form import CommentsForm
from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
class PostView(View):
    """ Вывод статей """

    def get(self, request):
        posts = Post.objects.order_by('-id')
        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/articals.html', {'page_obj': page_obj})


def get_art_filter(request):
    topic_type = request.GET.get('type', None)
    if topic_type:
        queryset = Post.objects.filter(type=topic_type).order_by('-id')
    else:
        queryset = Post.objects.order_by('-id')

    paginator = Paginator(queryset, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'blog/articals.html', context)


class PostSingle(View):
    """  Одна статья отдельно и подробно """

    def get(self, request, art_id):
        post = Post.objects.get(id=art_id)
        return render(request, 'blog/single.html', {'post': post})


class AddComments(View):
    """ Добавление комментариев """

    def post(self, request, art_id):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = art_id
            form.save()
        return redirect(f'/{art_id}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, art_id):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, post_id=art_id)
            return redirect(f'/{art_id}')
        except:
            post = Post.objects.get(id=art_id)
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = post
            new_like.save()
            return redirect(f'/{art_id}')


class DelLike(View):
    def get(self, request, art_id):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client, post_id=art_id)
            like.delete()
            return redirect(f'/{art_id}')
        except:
            return redirect(f'/{art_id}')
