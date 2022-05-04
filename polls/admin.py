from django.contrib import admin
from polls.models import Question, Choice
#polls 안에있는 모델.py에서 question, choice 함수 불러온거

admin.site.register(Question)
admin.site.register(Choice)