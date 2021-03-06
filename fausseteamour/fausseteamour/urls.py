"""fausseteamour URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views import generic
from rest_framework import routers
from blogpost import views as blogpostViews
from release import views as releaseViews
from social_icons import views as socialIconsViews

router = routers.DefaultRouter()
router.register(r'blogpost', blogpostViews.BlogpostViewSet)
router.register(r'release', releaseViews.ReleaseViewSet)
router.register(r'social_icon', socialIconsViews.SocialIconsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', generic.TemplateView.as_view(template_name='main.html')),
    url(r'^', include(router.urls)),
]
