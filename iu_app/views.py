from rest_framework.generics import ListAPIView

from .models import Kiosk
from .serializers import KioskSerializer


class KioskListView(ListAPIView):
    serializer_class = KioskSerializer
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Kiosk.objects.all()
        else:
            return Kiosk.objects.filter(name__startswith='A')
        

