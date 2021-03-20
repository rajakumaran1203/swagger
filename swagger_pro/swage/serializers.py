from rest_framework import serializers
from .models import stu
from uuid import uuid4
class Empserial(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=255,required=False)
    email = serializers.EmailField(max_length=255, required=False,allow_null=False)
    job = serializers.JSONField()
    class Meta:
        model=stu
        fields=('name','email','job')