from rest_framework import generics
from .serializers import SnackSerializer
from .models import Snack
from .permissions import IsOwnerOrReadOnly 



class SnackList(generics.ListCreateAPIView):

    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    # Serializer_class
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


# The ThingDetail needs the same things
class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsOwnerOrReadOnly,) 