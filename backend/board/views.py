from django.shortcuts import render
from django.http import HttpResponse
from .models import Problems
from user.models import User
import random
import subprocess
import os
import requests


def practice(request):
    context = {}
    user = None
    if 'user' in request.session:
        user_id = request.session['user']
        user = User.objects.get(id=user_id)
    problems = Problems.objects.all()[:10]
    context = {'user':user, 'problems':problems}
    return render(request, 'practice.html', context)

def real(request):

    user = None
    if 'user' in request.session:
        user_id = request.session['user']
        user = User.objects.get(id=user_id)

    return render(request, 'real.html', {'user':user,'random_number':random.randint(11,15)})

def practice_start(request, id, hint_id=1):
    problem = Problems.objects.get(problem_id=id)
    context = {}
    user = None
    if 'user' in request.session:
        user_id = request.session['user']
        user = User.objects.get(id=user_id)


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


        user_code = user_answer
        print(user_code)
        problem_content = problem.problem
        problem_input = problem.problem_input
        problem_output = problem.problem_output
        prompt = f"문제는 다음과 같다.\n{problem_content}\n문제의 입력에 관한 설명은 다음과 같다.\n{problem_input}\n문제의 출력에 관한 설명은 다음과 같다.\n{problem_output}"
        prompt_hint_1 = "해당 문제를 해결하기 위한 20자 이내의 간단한 힌트를 줘."
        prompt_hint_2 = f"현재까지 작성한 code는 다음과 같다.\n{user_code}\n이 문제를 해결하기 위한 다음단계에 관한 20자 이내의 간단한 힌트를 줘."
        prompt_hint_3 = f"현재까지 작성한 code는 다음과 같다.\n{user_code}\n이 코드를 보고 틀린 부분에 대한 20자 이내의 간단한 힌트를 줘."
        #prompt_hint_4 = "해당 문제를 보고 python을 사용해 정말 간단한 skeleton code를 짜줘."
        contents=[]
        contents.append(prompt + prompt_hint_1)
        contents.append(prompt + prompt_hint_2)
        contents.append(prompt + prompt_hint_3)
        #contents.append(prompt + prompt_hint_4)

        url = 'https://api.openai.com/v1/chat/completions'
        payload=[0, 0, 0]
        for i in range(3):
            payload[i] = {
                'messages': [
                {'role': 'user', 'content': contents[i]}
                ],
                'model': 'gpt-3.5-turbo',
                'max_tokens': 1000
            }
                
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'codecraft'
        }

        hint = []
        cnt = 0
        for i in range(3):
            response = requests.post(url, json=payload[i], headers=headers)
            print(response.status_code)
            if (response.status_code == 200):
                hint.append(response.json()['choices'][0]['message']['content'])
                print(hint[i])
                cnt = cnt + 1
                if cnt == 3:
                    return render(request, 'practice_mode_start.html',{'problem_title':problem.problem_title, 'problem_content':problem.problem, 'problem_input':problem.problem_input, 'problem_output':problem.problem_output, 'io_example1':problem.test_1, 'io_ex_answer1':problem.test_ans_1, 'io_example2':problem.test_2, 'io_ex_answer2':problem.test_ans_2, 'io_example3':problem.test_3, 'io_ex_answer3':problem.test_ans_3, 'hint1': hint[0],'hint2': hint[1], 'hint3': hint[2]})
            else:
                return HttpResponse('An error occurred')
        
    return render(request, 'practice_mode_start.html',{'user':user,'problem_title':problem.problem_title, 'problem_content':problem.problem, 'problem_input':problem.problem_input, 'problem_output':problem.problem_output, 'io_example1':problem.test_1, 'io_ex_answer1':problem.test_ans_1, 'io_example2':problem.test_2, 'io_ex_answer2':problem.test_ans_2, 'io_example3':problem.test_3, 'io_ex_answer3':problem.test_ans_3})


def real_start(request, id):
    problem = Problems.objects.get(problem_id=id)
    user = None
    if 'user' in request.session:
        user_id = request.session['user']
        user = User.objects.get(id=user_id)


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

    return render(request, 'real_mode_start.html',{'user':user,'problem_title':problem.problem_title, 'problem_content':problem.problem, 'problem_input':problem.problem_input, 'problem_output':problem.problem_output, 'io_example1':problem.test_1, 'io_ex_answer1':problem.test_ans_1, 'io_example2':problem.test_2, 'io_ex_answer2':problem.test_ans_2, 'io_example3':problem.test_3, 'io_ex_answer3':problem.test_ans_3})


def review(request):
    user=None
    if 'user' in request.session:
        user_id = request.session['user']
        user = User.objects.get(id=user_id)
    return render(request, 'review.html',{"user":user})


