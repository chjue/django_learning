from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index,name='index'), # http://127.0.0.1:8000/ 这样的url中什么都没有 则匹配views中的index函数
    url(r'^(\d+)/(\d+)/$', views.detail), # 任意数字匹配views中的detail函数,例子：http://127.0.0.1:8000/2/3/ 页面显示detail-2-3
    url(r'^grades/$', views.grades),
    url(r'^grades2/$', views.grades2),
    url(r'^students/$', views.students),
    url(r'^grades/(\d+)$', views.gradesStudents),#(\d+)是任意数字，可以当做参数传递给views的gradesStudents方法
    url(r'^grades/(\d+)/$', views.gradesStudents),  # (\d+)是任意数字，可以当做参数传递给views的gradesStudents方法
    url(r'^grades/(\d+)/(\d+)$', views.detailStudent),
    url(r'^students/(\d+)$', views.detailStudent2),
    url(r'^addstudent/$', views.addstudent),
    url(r'^deleteStudent/$', views.deletestudent),
    url(r'^modifyStudent/$', views.modifystudent),
    url(r'^modifyStudent/modifyStudentInfo$', views.modifyStudentInfo),
    url(r'^modifyStudent/toModifyStudent/$', views.toModifyStudent),
    url(r'^deleteStudent/deleteStudentInfo$', views.deletestudentInfo),
    url(r'^addstudent2/$', views.addstudent2),
    url(r'^students2/$', views.students2),
    url(r'^students3/$', views.students3),
    url(r'^stu/(\d+)/$', views.stupage),
    url(r'^stu/(\d+)/(\d+)/$', views.detailStudent),
    url(r'^attribute/$', views.attribute),
    url(r'^get1/$', views.get1), #获取get传递的参数,网址访问：http://127.0.0.1:8000/get1?a=1&b=2&c=3
    url(r'^get2/$', views.get2), #一个键带多个值，网址访问：http://127.0.0.1:8000/get2?a=1&a=2&c=3
    url(r'^showregist$', views.showregist,name="showregist"),#显示注册界面
    url(r'^showregistforgrade$', views.showregistforgrade, name="showregistforgrade"),  # 显示注册界面
    url(r'^showregist/regist/$', views.regist),  # 注册界面
    url(r'^regist/$', views.regist),  # 注册界面
    url(r'^registgrade/$', views.registgrade),  # 注册界面
    url(r'^showresponse/$', views.showresponse),  # 注册界面
    url(r'^cookieset/$', views.cookieset),  # 注册界面
    url(r'^rediret1/$', views.rediret1),  # 注册界面
    url(r'^rediret2/$', views.rediret2),
    url(r'^main/$', views.main),
    url(r'^main/login/$', views.login),
    url(r'^showmain/$', views.showmain),
    url(r'^main/quit/$', views.quit),
    url(r'^good(\d+)/$', views.good,name="good"),
    url(r'^mainbase/$', views.mainbase),
    url(r'^upfile', views.upfile),
    url(r'^savefile$', views.savefile),
    url(r'^studentpage/(\d+)$', views.studentpage),#学生分页

]


# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path(r'',views.index), # http://127.0.0.1:8000/ 这样的url中什么都没有 则匹配views中的index函数
#     path(r'^(\d+)/$',views.detail)
# ]






















