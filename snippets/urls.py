
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetViewSet,UserViewSet
from rest_framework import renderers

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

snippet_list = SnippetViewSet.as_view({
    'get':'list',
    'post':'create'
})
snippet_detail=SnippetViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy',
})
snippet_highlight= SnippetViewSet.as_view({
    'get':'highlight',
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list=UserViewSet.as_view({
    'get':'list'
})
user_detail=UserViewSet.as_view({
    'get':'retrieve'
})

router=DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)

urlpatterns= [
    path('', include(router.urls)),
    path('snippets/', snippet_list,name='snippet-list'),
    path('snippets/<int:pk>',snippet_detail,name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',snippet_highlight ,name='snippet-highlight'),
    path('users/', user_list,name='user-list'),
    path('users/<int:pk>',user_detail,name='user-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

