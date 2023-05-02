from rest_framework import serializers
from .models import *

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('problem_id', 'title',)

