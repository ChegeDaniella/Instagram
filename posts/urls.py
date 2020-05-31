from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url('^$',views.index,name = "index"),
    url('^profile/$',views.profile,name = "profile"),
    url('^new-post/$',views.new_post,name = "new_post"),
    url('^show-post/$',views.show_post,name = "show_post"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)