from django.urls import path
from .views import index, register, LoginView, profile
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path("",index, name= "index"),
    path("register", register, name= "register"),
    path("login", LoginView.as_view(next_page = "profile"), name='login'),
    path("profile", profile, name="profile"),
    path("logout", LogoutView.as_view(next_page =  "/"), name='logout'),

] 