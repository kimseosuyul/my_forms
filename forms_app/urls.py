from .views import ApiViewset, MasterViewset, PaymentConfirmation
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'add_data', ApiViewset, basename='add_data')
router.register(r'master_page', MasterViewset, basename='master_page')
router.register(r'confirmation', PaymentConfirmation, basename='confirmation')

urlpatterns = router.urls