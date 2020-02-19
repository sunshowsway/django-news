from .models import Post


def categories(request):
    query = Post.objects.values('category').distinct()
    categories = [item['category'] for item in query]
    return {
        'categories': categories
    }
