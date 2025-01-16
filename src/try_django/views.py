# views are simple python func that render something
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm


def home_page(request):
    # Render context in templates
    return render(request, 'hello_world.html', {"title": "Hello World"})


def about_page(request):
    return render(request, 'about.html', {"title": "About Us"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, 'form.html', context)


def test_page(request):
    return HttpResponse('<h1>Testing</h1>')

# Send template as HttpResponse


def example_page(request):
    context = {"title": "Example Page"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))
