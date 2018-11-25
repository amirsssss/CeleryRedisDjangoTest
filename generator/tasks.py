from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from .models import GeneratorModel

@task(name="random generator")
def randomgenerator():
    num=random.randint(1,300)
    GeneratorModel.objects.create(firstp=num)
    return num

# @task(name="multiply_two_numbers")
# def mul(x, y):
#     total = x * (y * random.randint(3, 100))
#     return total

# @task(name="sum_list_numbers")
# def xsum(numbers):
#     return sum(numbers)