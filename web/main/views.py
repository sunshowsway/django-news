from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import Post
from django.views.generic.list import ListView
from django.template import Template, RequestContext


class PostList(ListView):
    model = Post
    paginate_by = 20
    context_object_name = 'posts'

    def get_queryset(self):
        category = self.request.GET.get('category')
        keyword = self.request.GET.get('keyword')
        if category:
            return Post.objects.filter(category=category)
        elif keyword:
            return Post.objects.filter(title__contains=keyword)
        else:
            return Post.objects.all()


# class PostDetail(DetailView):
#     model = Post
#     context_object_name = 'post'
post_template = [None]
def post(request, pk):
    post = Post.objects.get(id=pk)
    if post_template[0] is None:
        return render(request, 'main/post_detail.html',
                      {'post': post})
    else:
        template = Template(post_template[0])
        context = RequestContext(request, {'post': post})
        return HttpResponse(template.render(context))


def recover(request):
    messages.warning(request, '已经恢复默认模板!')
    post_template[0] = None
    return redirect(request.META.get('HTTP_REFERER'))

