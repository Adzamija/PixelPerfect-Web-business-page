from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("pricing/", views.pricing, name="pricing"),
    path("FAQ/", views.faq, name="faq"),
    path("blogPost/<int:blog_id>", views.blog_post, name="blog_post"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("portfolioItem/<int:work_id>", views.portfolio_item, name="portfolio_item"),
    path("privacyandterms", views.privacy, name="privacy"),
    
]