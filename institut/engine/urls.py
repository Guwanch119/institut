from django.urls import path
from . import views
from .views import tazelikView,ArticleDetailView,addView,UpdatePostView,DeletePostView,addcategoryView
app_name = 'engine'

urlpatterns = [
    path("",views.dashboardView,name='index'),
    path("navbar",views.navbarView,name="navbarURL"),
    path("sidebar",views.sideView,name="sidebar"),
    path("about",views.aboutView,name='about'),
    path("yaglar",views.yaglarView,name="yaglar"),
    path("aspirant",views.aspiranturaView,name="aspirantura"),
    path("tazelikler",tazelikView.as_view(),name="tazelik"),
    path("tazelik/<int:pk>",ArticleDetailView.as_view(),name="article-detail"),
    path("tazelik_gos/",addView.as_view(),name="add_post"),
    path("tazelik_kategoriya/",addcategoryView.as_view(),name="add_category"),
    path("tazelik/uytget/<int:pk>",UpdatePostView.as_view(),name="update_post"),
    path("tazelik/<int:pk>/poz",DeletePostView.as_view(),name="delete_post"),
    path("hunarmen",views.hunarmenView,name="hunarmen"),
    path("bakalawr",views.bakalawr,name="bakalawr"),
    path("maslahatlar",views.maslahatlar,name="maslahat"),
    path("reyting",views.reyting,name="reyting"),
    path("category/<str:cats>/",views.CategoryView,name="category"),
    path("habarlasmak",views.HabarlasmakView,name="habarlasmak"),
    path("faculty/<int:ID>",views.faculty_details,name="faculties"),
    path("search-blogs/",views.BlogSearchView.as_view(),name="search_blogs")
]