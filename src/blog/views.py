from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .models import BlogPost
from .forms import BlogpostModelForm


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


@staff_member_required
# @login_required
def blog_post_create_view(request):
    form = BlogpostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        # can do above instead of doing .create
        # obj = BlogPost.objects.create(**form.cleaned_data)
        form = BlogpostModelForm()
    template_name = 'form.html'
    context = {'title': 'Blog Posts Create', 'form': form}
    return render(request, template_name, context)

# Retrieves only one document


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'title': 'Blog Posts Detail', "object": obj}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogpostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'title': f'Update {obj.title}', 'form': form}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    context = {'title': 'Blog Posts Delete', "object": obj}
    return render(request, template_name, context)
