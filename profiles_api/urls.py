from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') # (url, class, basename)
router.register('profile', views.UserProfileViewSet) # base_name is not required as we configured the queryset.. DRF will figureout the name using the queryset, base_name is only required when we dont have a queryset or when we want to override the name of the queryset


urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path("", include(router.urls)), # router.urls will generate list of urls for our viewsets based on the methods defined
]
