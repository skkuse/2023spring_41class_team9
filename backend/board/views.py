from django.shortcuts import render
from .models import Problems
import random
import builtins
import io
import types
import subprocess
import os

def practice(request):
    return render(request, 'practice.html')

def real(request):
    return render(request, 'real.html', {'random_number':random.randint(11,15)})

def practice_start(request, id):
    problem = Problems.objects.get(problem_id=id)

    if request.method == 'POST':
        
        user_answer = request.POST.get('user_answer', '')  # 폼 요소의 name 속성 값을 사용하여 데이터 불러오기
        with open('a.py', 'w') as file:
            file.write(user_answer)
        file.close()
        path = os.path.abspath('./a.py')
        if problem.test_1 != '' :
            test_1= (problem.test_1).replace("입력 예시 1)\r\n", '').replace("\r", "")
            test_ans_1= (problem.test_ans_1).replace("출력 예시 1)\r\n", '').replace("\r", "")
            correct1 = subprocess.run(['python', path], input=test_1, capture_output=True, text=True)
            correct1 = correct1.stdout[:-1]
            if(str(correct1) == test_ans_1):
                if problem.test_2 != '' :
                    test_2= (problem.test_2).replace("입력 예시 2)\r\n", '').replace("\r", "")
                    test_ans_2= (problem.test_ans_2).replace("출력 예시 2)\r\n", '').replace("\r", "")
                    correct2 = subprocess.run(['python', path], input=test_2, capture_output=True, text=True)
                    correct2 = correct2.stdout[:-1]
                    if(str(correct2) == str(test_ans_2)):
                        if problem.test_3 != '' :
                            test_3= (problem.test_3).replace("입력 예시 3)\r\n", '').replace("\r", "")
                            test_ans_3= (problem.test_ans_3).replace("출력 예시 3)\r\n", '').replace("\r", "")
                            correct3 = subprocess.run(['python', path], input=test_3, capture_output=True, text=True)
                            correct3 = correct3.stdout[:-1]
                            if(str(correct3) == test_ans_3):
                                print("Correct!!!!")
                            else :
                                print("Wrong!!!!")
                        else:
                            print("Correct!!!!")
                    else:
                        print("Wrong!!!!")
                else :
                    print("Correct!!!!")
            else:
                print("Wrong!!!!")


        
        
    return render(request, 'practice_mode_start.html',{'problem_title':problem.problem_title, 'problem_content':problem.problem, 'problem_input':problem.problem_input, 'problem_output':problem.problem_output, 'io_example1':problem.test_1, 'io_ex_answer1':problem.test_ans_1, 'io_example2':problem.test_2, 'io_ex_answer2':problem.test_ans_2, 'io_example3':problem.test_3, 'io_ex_answer3':problem.test_ans_3})

def real_start(request, id):
    problem = Problems.objects.get(problem_id=id)

    if request.method == 'POST':
        
        user_answer = request.POST.get('user_answer', '')  # 폼 요소의 name 속성 값을 사용하여 데이터 불러오기
        with open('a.py', 'w') as file:
            file.write(user_answer)
        file.close()
        path = os.path.abspath('./a.py')
        if problem.test_1 != '' :
            test_1= (problem.test_1).replace("입력 예시 1)\r\n", '').replace("\r", "")
            test_ans_1= (problem.test_ans_1).replace("출력 예시 1)\r\n", '').replace("\r", "")
            correct1 = subprocess.run(['python', path], input=test_1, capture_output=True, text=True)
            correct1 = correct1.stdout[:-1]
            if(str(correct1) == test_ans_1):
                if problem.test_2 != '' :
                    test_2= (problem.test_2).replace("입력 예시 2)\r\n", '').replace("\r", "")
                    test_ans_2= (problem.test_ans_2).replace("출력 예시 2)\r\n", '').replace("\r", "")
                    correct2 = subprocess.run(['python', path], input=test_2, capture_output=True, text=True)
                    correct2 = correct2.stdout[:-1]
                    if(str(correct2) == str(test_ans_2)):
                        if problem.test_3 != '' :
                            test_3= (problem.test_3).replace("입력 예시 3)\r\n", '').replace("\r", "")
                            test_ans_3= (problem.test_ans_3).replace("출력 예시 3)\r\n", '').replace("\r", "")
                            correct3 = subprocess.run(['python', path], input=test_3, capture_output=True, text=True)
                            correct3 = correct3.stdout[:-1]
                            if(str(correct3) == test_ans_3):
                                print("Correct!!!!")
                            else :
                                print("Wrong!!!!")
                        else:
                            print("Correct!!!!")
                    else:
                        print("Wrong!!!!")
                else :
                    print("Correct!!!!")
            else:
                print("Wrong!!!!")

    return render(request, 'real_mode_start.html',{'problem_title':problem.problem_title, 'problem_content':problem.problem, 'problem_input':problem.problem_input, 'problem_output':problem.problem_output, 'io_example1':problem.test_1, 'io_ex_answer1':problem.test_ans_1, 'io_example2':problem.test_2, 'io_ex_answer2':problem.test_ans_2, 'io_example3':problem.test_3, 'io_ex_answer3':problem.test_ans_3})

def review(request):
    return render(request, 'review.html')


