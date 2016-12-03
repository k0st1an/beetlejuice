# coding: utf-8

from rest_framework.routers import SimpleRouter

from apps.mailer.views import SenderViewSet

router = SimpleRouter()
router.register(r'send', SenderViewSet, base_name='send')

urlpatterns = router.urls
