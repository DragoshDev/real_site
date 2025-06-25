from django.urls import path
from . import views 
from .api_views import api_transfers , api_rumors
from .views import register_view
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("inregistrare/", register_view, name="register"),
    path("" , views.startapp, name='startpage' ),
   # path("posts/", views.post , name='postpage'),
    path("posts/<slug:slug>", views.post_detail, name='post-detail-page'), #posts/my-firstpost
    path('posts/', views.all_posts, name='all_post'),
    path("transferuri/", views.transferuri, name="transferuri"),
    path("zvonuri/", views.zvonuri, name="zvonuri"),
    path("legende/", views.legende, name="legende"),

    path("echipa/", views.echipa, name="echipa"),  # ✅ adaugă aceasta
    path("postari/<slug:slug>/", views.post_detail, name="post_detail"),
    path("index/" , views.index, name='index'),
    path('api/transfers/', api_transfers, name='api_transfers'),
    path('api/rumors/', api_rumors, name='api_rumors'),



    path("login/", LoginView.as_view(template_name="realblog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", register_view, name="register"),

]

