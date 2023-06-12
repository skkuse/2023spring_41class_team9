from django.db import models


class Problems(models.Model):
    problem_id = models.IntegerField(primary_key=True)
    problem_title = models.CharField(max_length=255, blank=True)
    problem = models.TextField(blank=True)
    problem_input = models.TextField(blank=True)
    problem_output = models.TextField(blank=True)

    test_1 = models.TextField(max_length=255, blank=True)
    test_2 = models.TextField(max_length=255, blank=True)
    test_3 = models.TextField(max_length=255, blank=True)
    test_ans_1 = models.TextField(max_length=255, blank=True)
    test_ans_2 = models.TextField(max_length=255, blank=True)
    test_ans_3 = models.TextField(max_length=255, blank=True)

    class Meta:
        db_table = 'problems'
# Create your models here.


