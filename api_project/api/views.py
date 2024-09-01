

#from rest_framework import viewsets
#from .models import Book
#from .serializers import BookSerializer
#from rest_framework.response import Response

#class BookViewSet(viewsets.ModelViewSet):
    #def list(self, request):            
        #queryset = Book.objects.all()
       # serializer_class = BookSerializer(queryset, many=True)
        #return Response(serializer_class.data)
    
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    #def list(self,request):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
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


    

    #return Response(serializer_class.data)

    