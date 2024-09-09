
from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register('api', BookViewSet, basename='api')
#urlpatterns = router.urls
urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
    
    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('books/',views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/',views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/',views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/',views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/',views.BookDeleteView.as_view(), name='book-delete'),
]











