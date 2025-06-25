from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transfer , Rumor
from .serializers import TransferSerializer , RumorSerializer

@api_view(['GET'])
def api_transfers(request):
    transfers = Transfer.objects.all()
    serializer = TransferSerializer(transfers, many=True, context={'request': request})
    return Response(serializer.data)



@api_view(['GET'])
def api_rumors(request):
    rumors = Rumor.objects.all().order_by('-date')
    serializer = RumorSerializer(rumors, many=True, context={'request': request})
    return Response(serializer.data)
