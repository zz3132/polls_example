from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data=models.DateField('data published')

    def __str__(self):
        return self.question_text #결과창에 쓴 내용이 그대로 나오게 하는 역할


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #vote의 기본값을 0 으로 인터넷에 들어갔을때 기본값이 0으로 되어있음

    def __str__(self):
        return self.choice_text
    #str은 데이터베이스의 구조를 변경하는 것이 아니라 표현되는 내용(함수)만 표현했기에
    #서버가 켜져있어도 데이터베이스의 변화가 없기에 즉각 반영됨.