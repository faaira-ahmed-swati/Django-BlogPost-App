from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import BlogPost


# def blog_post_detail_page_by_id(request, id):
#     # Getting data from db
#     # obj = BlogPost.objects.get(id=id)
#     obj = get_object_or_404(BlogPost, id=id)
#     template_name = 'blog/detail.html'
#     context = {"title": "Blog Post Example", "object": obj}
#     return render(request, template_name, context)


# def blog_post_detail_page_by_slug(request, slug):
#     # Getting data from db
#     obj = get_object_or_404(BlogPost, slug=slug)
#     template_name = 'blog/detail.html'
#     context = {"title": "Blog Post Example", "object": obj}
#     return render(request, template_name, context)


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {'title': 'Blog Posts List', 'object_list': qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    template_name = 'blog/create.html'
    context = {'title': 'Blog Posts Create', 'form': None}
    return render(request, template_name, context)

# Retrieves only one document


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'title': 'Blog Posts Detail', "object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {'title': 'Blog Posts Update', "object": obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {'title': 'Blog Posts Delete', "object": obj}
    return render(request, template_name, context)
