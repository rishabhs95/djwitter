"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from twitter_app.views import index, login_view, logout_view, signup, public, submit, users, follow

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^login$', login_view, name='login_view'),
    url(r'^logout$', logout_view, name='logout_view'),
    url(r'^signup$', signup, name='signup'),
    url(r'^tweets$', public, name='public'),
    url(r'^submit$', submit, name='submit'),
    url(r'^users/$', users, name='users'),
    url(r'^users/(?P<username>\w{0,30})/$', users, name='users'),
    url(r'^follow$', follow, name='follow'),
]
