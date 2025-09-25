from rest_framework_nested import routers

from post.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = router.urls