from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

import core.views

router = routers.DefaultRouter()
router.register('', core.views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', core.views.MyObtainTokenPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
