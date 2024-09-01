
from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('api', BookViewSet, basename='api')
#urlpatterns = router.urls
urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
    
    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]











