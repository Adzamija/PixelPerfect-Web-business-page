from django.db import IntegrityError, OperationalError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def index(request):
    blogs = Blog.objects.filter()
    return render(request, "main/index.html",{
        "blogs": blogs
    })


def about(request):
    return render(request, "main/about.html")


def contact(request):
    if request.method == "POST":
        subject = request.POST["subject"]
        from_email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        if subject and from_email and phone and message:
            try:
                send_mail(subject, message, from_email, ["adzamija@icloud.com"])
            except BadHeaderError:
                return render(request, "main/contact.html", {
                    "message": "Invalid header found."
                })
            return render(request, "main/contact.html", {
                "message": "Success! Thank you for your message."
            })

    else:
        return render(request, "main/contact.html")


def pricing(request):
    return render(request, "main/pricing.html")


def faq(request):
    return render(request, "main/faq.html")

def blog_home(request):
    return render(request, "main/blog-home.html")


def blog_post(request, blog_id):
    if request.method == "POST":
        new_comment = Comments(blog=Blog.objects.get(pk=blog_id), comment=request.POST['comment'])
        new_comment.save()
        comments = Comments.objects.filter(blog=blog_id)
        blog = Blog.objects.get(pk=blog_id)
        return render(request, "main/blog-post.html", {
            "blog": blog,
            "comments":comments
        })
    else:
        comments = Comments.objects.filter(blog=blog_id)
        blog = Blog.objects.get(pk=blog_id)
        return render(request, "main/blog-post.html", {
            "blog": blog,
            "comments":comments
        })


def portfolio(request):
    portfiolios = Portfolio.objects.filter()
    return render(request, "main/portfolio.html", {
        "portfolio": portfiolios,
    })


def portfolio_item(request, work_id):
    work = Portfolio.objects.get(pk=work_id)
    return render(request, "main/portfolio-item.html", {
        "work": work,
    })


def privacy(request):
    return render(request, "main/privacyandterms.html")


