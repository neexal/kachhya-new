
from rest_framework import generics
  
from curriculum.models import Standard
from curriculum.serializers import StandardSerializer
  
class StandardList(generics.ListCreateAPIView):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer
  
class StandardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer