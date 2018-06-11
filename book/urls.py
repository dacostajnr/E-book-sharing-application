from django.conf.urls import url,include
from . import views


urlpatterns = [    
    #electricalhub.com
    url(r"^$",views.home,name="home"),
    #electricalhub.com/year/1/semester/2/
    url(r"^year/(?P<year_id>[0-9]+)/semester/(?P<semester_id>[0-9]+)/$",views.semester_detail,name="semester_detail"),
    url(r"^search/$",views.search,name="search"),
    url(r"^upload/$",views.upload,name="upload"),
    url(r"^about/$",views.about,name="about"),
    url(r"^others/$",views.others,name="others"),
    url(r"^upload_other/$",views.upload_other,name="upload_other"),
 ]


