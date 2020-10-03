from .models import Member
from . serializers import memberSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser	
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db import OperationalError

try:   
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
except OperationalError: 
    pass

class listViewSet(viewsets.ModelViewSet):
        '''
        If used without any paramethers, this endpoint returns a list of all the **Members** of the parliament.
        Example: 
        http://127.0.0.1:8000/list/

        Add one or more of the following parameters to filter the list based on the column of the respective database column:
                'name',
                'email',
                'political_force',
                'birth_date',
                'birth_place',
                'languages',
                'profession'

        In the current version of the application, the value of the parameter needs to be an exact match
        to the value of the database field. A future version might include the capability to filter by partial matches.

        Examples:     
        http://127.0.0.1:8000/list?political_force=ПП%20ГЕРБ
        

        http://127.0.0.1:8000/list?political_force=БСП%20за%20БЪЛГАРИЯ&languages=Руски


        http://127.0.0.1:8000/list/?profession=Инженер
        '''
        queryset = Member.objects.all()
        serializer_class = memberSerializer
        http_method_names = ['get']
        filter_backends = [DjangoFilterBackend]       
        filterset_fields = ['name', 'email', 'political_force', 'birth_date', 'birth_place', 'languages', 'profession']
       # authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated, IsAdminUser) 

class searchViewSet(viewsets.ModelViewSet):  
        '''
        If used without any paramethers, this endpoint returns a list of all the **Members** of the parliament.
        Example: 
        http://127.0.0.1:8000/search/

        Add the 'search' parameter and set it equal to a string
        to have the endpoint return a list of all the members whose names conatain the provided string.

        Example:     
        http://127.0.0.1:8000/search/?search=Цвета
        '''     
        queryset = Member.objects.all()
        serializer_class = memberSerializer
        http_method_names = ['get']
        filter_backends = [filters.SearchFilter]
        search_fields = ['name']
        #authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)

class mpViewSet(viewsets.ModelViewSet):
        '''
        If used without any paramethers, this endpoint returns a list of all the **Members** of the parliament.
        Example: 
        http://127.0.0.1:8000/mp/

        Add the 'id' parameter with the exact number value
        to get the endpoint to return all the information for this exact member.

        Examples:     
        http://127.0.0.1:8000/mp/?id=3
        '''    
        queryset = Member.objects.all()
        serializer_class = memberSerializer
        http_method_names = ['get']
        filter_backends = [DjangoFilterBackend]       
        filterset_fields = ['id']
       # authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)