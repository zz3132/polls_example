from django.contrib import admin
from polls.models import Question, Choice
#polls 안에있는 모델.py에서 question, choice 함수 불러온거

class ChoiceInline(admin.TabularInline):
    model = Choice #초이스 모델을 사용
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Statement', {'fields' : ['question_text']}),
              ('Date Information', {'fields' : ['pub_date'], 'classes':['collapse']})]
    inlines = [ChoiceInline] #적용된 초이스모델을 question admin 클래스 안에 넣어줘서 같은 화면에 표시되게 함
                            #실제로 값이 변경된것이 아니라 같은 구성에서 출력만 바꿔놓음
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)