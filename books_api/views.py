from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response

# BookViewSet is for CRUD_Broweable view for the Book model

class BookViewSet(viewsets.ViewSet):
    def list(self,request):
        book = Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            book = Book.objects.get(pk=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)

    def create(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serialzer.error,status = status.HTTP_BAD_REQUEST)

    def update(self,request,pk=None):
        id = pk
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.error,status= status.HTTP_BAD_REQUEST)

    def partial_update(self,request,pk=None):
        id = pk
        book = Book.objects.get(pk=id)
        serializer= BookSerializer(book,data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'})
        return Response(serializer.error,status= status.HTTP_BAD_REQUEST)

    def destroy(self,request,pk):
        id=pk
        book = Book.objects.get(pk=id)
        book.delete()
        return Response({'msg': 'delete data'})
