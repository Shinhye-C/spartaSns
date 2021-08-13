from django.contrib import admin
from .models import UserModel
# .models means we are going to call models.py file in the same directory


# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
