from enum import Enum
from django.db import models
from common.models import BaseModel
from users.models import User

class InterviewStyle(Enum):
  VIDEO = 'video'
  VOICE = 'voice'
  TEXT = 'text'
  
class PositionType(Enum):
  FRONTEND = 'frontend'
  BACKEND = 'backend'
  FULLSTACK = 'fullstack'
  
class Interview(BaseModel):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  resume = models.IntegerField()
  title = models.CharField(max_length=255)
  style = models.CharField(choices=[(tag, tag.value) for tag in InterviewStyle])
  position = models.CharField(choices=[(tag, tag.value) for tag in PositionType])
  
class Interview_Type(models.Model):
  type_name = models.CharField(max_length=20)
  
class Type_Choice(models.Model):
  interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
  interview_type = models.ForeignKey(Interview_Type, on_delete=models.CASCADE)
  

class Question(BaseModel):
  interview = models.ForeignKey(Interview)
  content = models.CharField(max_length=255)
  
class Answer(BaseModel):
  question = models.OneToOneField(Question, on_delete=models.CASCADE)
  content = models.CharField(max_length=255)
  record_url = models.CharField(max_length=500)
  