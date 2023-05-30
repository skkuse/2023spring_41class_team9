from django.shortcuts import render
from .models import Problems
import random

def practice(request):
    return render(request, 'practice.html')

def real(request):
    return render(request, 'real.html', {'random_number':random.randint(11,15)})

def practice_start(request, id):
    problem = Problems.objects.get(problem_id=id)
    return render(request, 'practice_mode_start.html',{'problem_title':problem.problem_title, 'problem_content':problem.problem, 'problem_input':problem.problem_input, 'problem_output':problem.problem_output, 'io_example1':problem.test_1, 'io_ex_answer1':problem.test_ans_1, 'io_example2':problem.test_2, 'io_ex_answer2':problem.test_ans_2, 'io_example3':problem.test_3, 'io_ex_answer3':problem.test_ans_3})

def real_start(request, id):
    problem = Problems.objects.get(problem_id=id)
    return render(request, 'real_mode_start.html',{'problem_title':problem.problem_title, 'problem_content':problem.problem, 'problem_input':problem.problem_input, 'problem_output':problem.problem_output, 'io_example1':problem.test_1, 'io_ex_answer1':problem.test_ans_1, 'io_example2':problem.test_2, 'io_ex_answer2':problem.test_ans_2, 'io_example3':problem.test_3, 'io_ex_answer3':problem.test_ans_3})

def review(request):
    return render(request, 'review.html')