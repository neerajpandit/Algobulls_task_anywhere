from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TodoItemListView, TodoItemDetailView, ATodoItemListView

router=DefaultRouter()
router.register('api',ATodoItemListView)

urlpatterns = [
    path('', include(router.urls)),
    path('todo/', TodoItemListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoItemDetailView.as_view(), name='todo-detail'),
    # path('token/', TokenObtainView.as_view(), name='token-obtain'),
]
