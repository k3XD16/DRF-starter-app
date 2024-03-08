from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import MobileSerializer
from drfapp.models import Mobile

class TestView(APIView):
    
    permission_classes = (IsAuthenticated, )
    def get(self,request,*args,**kwargs):
        qs = Mobile.objects.all()
        # mobile1 = qs.first()
        serializer = MobileSerializer(qs,many=True)
        # serializer = MobileSerializer(mobile1 )
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer = MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    