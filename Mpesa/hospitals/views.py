from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import HospitalSerializer
from .models import Hospital


# Create your views here.
class HospitalsList(APIView):
    """
    List all Hospitals, or create a new Hospital.
    """
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        users = Hospital.objects.all()
        serializer = HospitalSerializer(users, many=True)
        return Response(serializer.data)

class HospitalDetail(APIView):
    """
    Retrieve, update or delete a Hospital instance.
    """
    permission_classes = (permissions.AllowAny,)
    def get_object(self, pk):
        try:
            return Hospital.objects.get(pk=pk)
        except Hospital.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = HospitalSerializer(user)
        return Response(serializer.data)
    
    def patch(self, request, pk, format=None):
        user = self.get_object(pk)

        serializer = HospitalSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = HospitalSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)