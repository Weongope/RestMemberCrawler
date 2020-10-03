from rest_framework import serializers
from .models import Member

class memberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'name', 'email', 'political_force', 'birth_date', 'birth_place', 'languages', 'profession')
