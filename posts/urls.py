from django.conf.urls import url,include
from .views import PostListView, PostDetailView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns =[
    url('^$',views.index,name = "index"),
    url('^profile/',views.profile,name = "profile"),
    url('^new-post/',views.new_post,name = "new_post"),
    url('^show-post/',PostListView.as_view(),name = "show_post"),
    path('post/<int:pk>/',PostDetailView.as_view(),name = "post-detail"),
    url('^like-post/',views.like_post,name = "like_post"),
    url(r'^search/', views.search_results, name='search_results')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)