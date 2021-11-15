from django.urls import path, include
from rest_framework import routers
import todo.views

router = routers.DefaultRouter()
router.register(r'task/category', todo.views.CategoryViewSet)
router.register(r'task/todo', todo.views.TodoViewSet)
router.register(r'tag', todo.views.TagViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
