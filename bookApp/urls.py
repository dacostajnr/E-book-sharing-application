from django.conf.urls import url,include
from django.contrib import admin
from book import views
from django.conf.urls.static import  static 
from django.conf import settings 
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', admin.site.urls),    
   	url(r"^",include("book.urls",app_name="book",namespace="book")),
   	url(r"^static/(?P<path>.*)$",serve,{"document_root":settings.STATIC_ROOT,}),
   	url(r"^media/(?P<path>.*)$",serve,{"document_root":settings.MEDIA_ROOT,}),
]


# if (settings.DEBUG):
#     urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


