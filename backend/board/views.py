from django.shortcuts import render
from .models import Problems
import random

# Create your views here.

def practice(request):
    return render(request, 'practice.html')

def real(request):
    return render(request, 'real.html', {'random_number':random.randint(11,15)})

def practice_start(request, id):
    problem = Problems.objects.get(problem_id=id)
    return render(request, 'practice_mode_start.html',{'problem_content':problem.problem, 'problem_title':problem.problem_title, 'io_example1':problem.test_1, 'io_ex_answer1':problem.test_ans_1})  

def real_start(request, id):
    problem = Problems.objects.get(problem_id=id)
    return render(request, 'real_mode_start.html',{'problem_content':problem.problem, 'problem_title':problem.problem_title, 'io_example1':problem.test_1, 'io_ex_answer1':problem.test_ans_1})  
