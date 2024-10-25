from rest_framework import viewsets, filters, generics
from fintech.models import Transacao, Categoria
from fintech.serializers import TransacaoSerializer, CategoriaSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['data_transacao', 'valor']
    

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao']
   
class TransacaoListPorUsuario(generics.ListAPIView):
    serializer_class = TransacaoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['data_transacao', 'valor']

    
    def get_queryset(self):
        usuario_id = self.kwargs['id_usuario']
        return Transacao.objects.filter(usuario_id=usuario_id)
    

class TransacaoListPorCategoria(generics.ListAPIView):
    serializer_class = TransacaoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['data_transacao', 'valor']

    def get_queryset(self):
        categoria_id = self.kwargs['id_categoria']
        return Transacao.objects.filter(categoria_id=categoria_id)

