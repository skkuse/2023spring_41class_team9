from django import template

register = template.Library()

from user.models import User, UserProblem
from board.models import Problems
from django.utils.safestring import mark_safe
from django.urls import reverse


@register.simple_tag
def bg_top(user, p_id):
    problem = Problems.objects.get(problem_id=p_id)
    userprob = UserProblem.objects.get(user=user, problem=problem)

    start_id = UserProblem.objects.filter(user=user, started=0).order_by("problem_id")[0].problem_id

    # start인지 아닌지
    if p_id == start_id:
        return "bg-start"
    # solved인지 아닌지
    elif userprob.solved:
        return "bg-opened"

    else:
        return "bg-locked"

@register.simple_tag
def bg_bottom(user, p_id):
    problem = Problems.objects.get(problem_id=p_id)
    userprob = UserProblem.objects.get(user=user, problem=problem)

    start_id = UserProblem.objects.filter(user=user, started=0).order_by("problem_id")[0].problem_id

    # start인지 아닌지
    if p_id == start_id:
        return "bg-none"
    elif not userprob.started:
        return "bg-none"
    # solved인지 아닌지
    elif userprob.solved:
        cnt = 0
        hint = userprob.hint
        hint1_cnt = hint % 1000
        hint -= hint1_cnt
        hint /= 1000
        hint2_cnt = hint % 1000
        hint -= hint2_cnt
        hint /=1000
        hint3_cnt = hint
        li = [hint1_cnt, hint2_cnt, hint3_cnt]
        print(".................")
        print(li)
        if li.count(0) == 3:
            return "bg-crown-3"
        elif li.count(0) == 2:
            return "bg-crown-2"
        elif li.count(0) == 1:
            return "bg-crown-1"
        else:
            return "bg-crown-0"

    else:
        return "bg-crown-0"


@register.simple_tag
def btn_alert(user, p_id):
    problem = Problems.objects.get(problem_id=p_id)
    userprob = UserProblem.objects.get(user=user, problem=problem)

    start_id = UserProblem.objects.filter(user=user, started=0).order_by("problem_id")[0].problem_id

    if not userprob.started and not start_id==p_id:
        return mark_safe("alert('이전문제를 먼저 시작해주세요.')")
    else:
        strurl = reverse('problem-view', args=[p_id])

        return mark_safe("location.href='%s'"%strurl)


@register.simple_tag
def hint(user, p_id, p1, p2, hint_num):

    problem = Problems.objects.get(problem_id=p_id)
    userprob = UserProblem.objects.get(user=user, problem=problem)
    print("!!!!!!!!!!!!!!!!!!")
    print(hint_num)
    if hint_num == 1:
        userprob.hint += 1
    elif hint_num == 2:
        userprob.hint += 1000
    else:
        userprob.hint += 1000000

    userprob.save()
    return mark_safe("showHint('%s',"%p1+"'"+p2+"'" +")")
