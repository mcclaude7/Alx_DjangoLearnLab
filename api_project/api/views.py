

#from rest_framework import viewsets
#from .models import Book
#from .serializers import BookSerializer
#from rest_framework.response import Response

#class BookViewSet(viewsets.ModelViewSet):
    #def list(self, request):            
        #queryset = Book.objects.all()
       # serializer_class = BookSerializer(queryset, many=True)
        #return Response(serializer_class.data)
    
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Book
from .seriealizers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class BookViewSet(viewsets.ModelViewSet):
    #def list(self,request):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
        #return Response(serializer_class.data)
    def retrieve(self,request,pk=None):
        books = Book.objects.filter(pk=pk).first()
        if not books:
            message: {'detail' f"api with id {pk} not found"}
            return Response(message, status=404)
        serializer_class = BookSerializer(books) 
        return Response(serializer_class.data)
    def  create(self,request):
        queryset = Book.objects.create(**request.data)
        serializer_class = BookSerializer(queryset)
        return Response(serializer_class.data)

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def createViews(self, serializer):
        serializer.save()

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def updateViews(self, serializer):
        serializer.save()

class DeleteView(generics.DeleteAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    

    #return Response(serializer_class.data)

    