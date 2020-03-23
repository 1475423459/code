from django.conf.urls import url
from django.contrib import admin
from hello import views
from . import view, testdb
urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url('^home/', views.home),
    url('^demo/$', views.demo),
    url('^juan$', views.juan),
    url('^page1/$', views.page1),
    url('^sonpage/$', views.sonpage),
    url(r'^testdb$', testdb.testdb),
    url(r'^register$', testdb.add_user),
    url(r'^update$', testdb.update_psw),
    url(r'^delect$', testdb.delect_user),
    url(r'^name$', testdb.select_name),
    url(r'^all$', testdb.select_all),
    url(r'^filter$', testdb.select_filter),
    url(r'^value$', testdb.select_values),
    url(r'^exculd$', testdb.select_exclude),
    url(r'^json$', testdb.get_json),
    url(r'^dict$', testdb.to_dict),
    url(r'^tovalue$', testdb.to_value),
]

