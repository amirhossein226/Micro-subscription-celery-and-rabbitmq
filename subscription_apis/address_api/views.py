from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

from .models import Address
from .serializers import AddressSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def address_list(request):
    if request.method == 'GET':
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        print(request.data)
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def address_detail(request, pk):

    try:
        address = Address.objects.get(id=pk)
    except Address.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddressSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH' or request.method == 'PUT':
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class AddressList(ListCreateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer


# class AddressDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer

# class AddressList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class AddressDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         self.destroy(request, *args, **kwargs)


# class AddressList(APIView):
#     def get(self, request, format=None):
#         addresses = Address.objects.all()
#         serializer = AddressSerializer(addresses, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         address = request.data
#         serializer = AddressSerializer(data=address)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AddressDetail(APIView):
#     def get(self, request, pk):
#         address = self.get_object(pk)
#         serializer = AddressSerializer(address)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         address = get_object(pk)
#         serializer = AddressSerializer(address, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP)

#     def delete(self, request, pk):
#         address = Address.objects.get(id=pk)
#         address.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def get_object(self, pk):
#         try:
#             address = Address.objects.get(id=int(pk))
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         return address
