from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from django.shortcuts import render
from .serializer import *
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.models import User

# from .models import CustomUser as User
import json
import math
import random
from django.db import transaction


from .models import *

# import requests
from rest_framework import status
# from json.decoder import JSONDecodeError
# from django.shortcuts import render, redirect
# # import jwt
# from dotenv import load_dotenv
# import os
# from pathlib import Path
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views import View

from .models import *
from .serializer import *

class ProblemAPI(APIView):
    # 사용자조회
    def get(self, request):
        try:
            problems = Problem.objects.all()
            serializer = ProblemSerializer(problems,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"err_code":111, "message":"없는 사용자입니다."}, status=status.HTTP_400_BAD_REQUEST)