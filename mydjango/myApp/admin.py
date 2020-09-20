from django.contrib import admin

# Register your models here.
"""
站点管理
"""
from .models import Grades,Students

#注册

# 关联对象：
class StudentsInfo(admin.TabularInline): #在创建一个班级时，可以直接添加几个学生
    model = Students
    extra = 2 #创建两个学生

@admin.register(Grades) #使用装饰器注册，将数据库表Grades注册给函数
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo] # 添加关联对象
    # 列表页属性
    list_display = ["pk","gname","gdate","ggirlnum","gboynum","isDelete"] # 显示字段
    list_filter = ["gname","isDelete"]  # 过滤字段
    search_fields = ["gname"]  # 搜索框，按名字搜索
    list_per_page = 5  # 分页，每5条是一页
    # 添加，修改页属性
    # fields = ["ggirlnum","gboynum","gname","gdate","isDelete"]  # 规定属性的先后顺序
    fieldsets = [("num",{"fields":["ggirlnum","gboynum"]}), #给属性分组
                 ("base",{"fields":["gname","gdate","isDelete"]})]
    # fields，fieldsets不能同时使用

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self): # 让boolean显示男或女
        if self.sgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"
    # 列表页属性
    list_display = ["pk","sname","sage",gender,"scontend","sgrade","isDelete"] # 显示字段
    list_filter = []  # 过滤字段
    search_fields = []  # 搜索框，按名字搜索
    list_per_page = 5  # 分页，每5条是一页
    # 添加，修改页属性
    fields = ["sname","sage","sgender","scontend","sgrade","isDelete"]  # 规定属性的先后顺序
    # fieldsets = [("num",{"fields":["sname","sage","sgender","scontend"]}), #给属性分组
    #              ("base",{"fields":["sgrade","isDelete"]})]
    actions_on_bottom = True # 执行动作(go)的位置
    actions_on_top = False

# admin.site.register(Grades,GradesAdmin)#admin注册方式
#
# admin.site.register(Students,StudentsAdmin)




















