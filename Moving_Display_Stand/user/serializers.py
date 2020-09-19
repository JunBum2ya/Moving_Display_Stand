from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User # 모델 설정 
        fields = ('user_id','user_name','user_email') # 필드 설정