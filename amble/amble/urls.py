"""amble URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import account.views as account
import community.views as community
import blog.views as blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', account.login_view, name="login"),
    path('signup', account.signup_view, name="signup"),
    path('', account.home, name="home"),
    path('community', community.community, name="community"),
    path('community/detail/<int:community_id>', community.detail, name="detail"),
    path('communtiy/new', community.new, name="new"),
    path('community/create', community.create, name="create"),
    path('community/edit/<int:community_id>', community.edit, name="edit"),
    path('community/update/<int:community_id>', community.update, name="update"),
    path('community/delete/<int:community_id>', community.delete, name="delete"),
    path('community/reply/<int:community_id>', community.reply, name="reply"),
    path('community/reply/delete/<int:community_id>/<int:reply_id>', community.reply_delete, name="reply_delete"),
    path('blog', blog.blog, name="blog"),
    path('blog/detail/<int:blog_id>', blog.detail, name="blog_detail"),
    path('blog/new', blog.new, name="blog_new"),
    path('blog/create', blog.create, name="blog_create"),
    path('blog/edit/<int:blog_id>', blog.edit, name="blog_edit"),
    path('blog/update/<int:blog_id>', blog.update, name="blog_update"),
    path('blog/delete/<int:blog_id>', blog.delete, name="blog_delete"),
    path('blog/reply/<int:blog_id>', blog.reply, name="blog_reply"),
    path('blog/reply/delete/<int:blog_id>/<int:reply_id>', blog.reply_delete, name="blog_reply_delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
