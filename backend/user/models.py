from django.db import models
from board.models import Problems

class User(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    score = models.IntegerField(default=0)
    stage = models.IntegerField(default=1)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'practice_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

class UserProblem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    # Add any additional fields for the relationship here
    hint = models.IntegerField(default=0)
    solved = models.IntegerField(default=0)
    started = models.IntegerField(default=0)
    class Meta:
        db_table = 'user_problems'