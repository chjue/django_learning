import os
import time

from django.conf import settings
from django.contrib.auth import logout
from django.core import paginator
from django.core.exceptions import MultipleObjectsReturned
from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from myApp.models import Grades, Students


def index(request):
    return render(request,'myApp/index.html')


def detail(request,num,num2): #num,num2 是url中的 例子：http://127.0.0.1:8000/1/2
    return HttpResponse("detail-%s-%s"%(num,num2))


def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    # 将 gradesList 传递给grades.html中的变量grades
    return render(request,'myApp/grades.html',{"grades": gradesList}) #grades是grades.html中的变量

def grades2(request):
    # 去模板里取数据
    g = Grades.objects.filter(students__scontend__contains="我叫")
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    # 将 gradesList 传递给grades.html中的变量grades
    return HttpResponse(g)



def students(request):
    # 去模板里取数据
    studentsList = Students.stuObj2.all()
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    # 将 gradesList 传递给students.html中的变量students
    return render(request,'myApp/students.html',{"students": studentsList,
                                                 "hahayou":"我是传过去的值",
                                                 "list":["hello","nihaoma"],
                                                 "num":10,
                                                 "code":"<h1>我是测试html转义</h1>"
                                                 }
                  ) #students是students.html中的变量

def students2(request):
    # 去模板里取数据
    try:
        studentsList = Students.stuObj2.get(sgender=True)
        # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
        # 将 gradesList 传递给students.html中的变量students
        return render(request,'myApp/students.html',{"students": studentsList}) #grades是grades.html中的变量
    except MultipleObjectsReturned:
        return HttpResponse("有多条符合条件数据")

# 显示前2个
def students3(request):
    # 去模板里取数据
    studentsList = Students.stuObj2.all()[0:2]
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    # 将 gradesList 传递给students.html中的变量students
    return render(request,'myApp/students.html',{"students": studentsList}) #grades是grades.html中的变量


# 分页显示学生
def stupage(request,page):
    # 一页显示2个,http://127.0.0.1:8000/stu/3/ 这样去访问即可
    page=int(page)
    studentsList = Students.stuObj2.all()[(page-1)*2:page*2]
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    # 将 gradesList 传递给students.html中的变量students
    return render(request, 'myApp/students.html', {"students": studentsList})  # grades是grades.html中的变量


def gradesStudents(request,num): # 点击班级现实班级中的所有学生
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    studentsListNew=[]
    for student in studentsList:
        if student.isDelete==False:
            studentsListNew.append(student)
    return render(request, 'myApp/students.html', {"students": studentsListNew})  # grades是grades.html中的变量

def detailStudent(request,num,num2): # 点击班级现实班级中的所有学生
    student = Students.stuObj2.get(pk=num2)
    studentsList = []
    studentsList.append(student)
    return render(request, 'myApp/studentDetail.html', {"students": studentsList})  # grades是grades.html中的变量


def detailStudent2(request,num): # 点击班级现实班级中的所有学生
    student = Students.stuObj2.get(pk=num)
    studentsList = []
    studentsList.append(student)
    return render(request, 'myApp/studentDetail.html', {"students": studentsList})  # grades是grades.html中的变量



def addstudent(request): # 点击班级现实班级中的所有学生
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("刘德华",34,True,"wojia",grade,"2017-8-10","2017-8-11")
    stu.save()
    return HttpResponse("successful")


def deletestudent(request): # 删除学生

    return render(request, 'myApp/deletestudent.html')

def deletestudentInfo(request): # 删除学生
    id=request.POST.get("id")
    student = Students.stuObj2.get(pk=id)
    student.isDelete=True
    student.save()
    return HttpResponse("successful")


def modifystudent(request): # 修改学生信息

    return render(request, 'myApp/modifystudent.html')

def modifyStudentInfo(request): # 修改学生信息
    id=request.POST.get("id")
    stu = Students.stuObj2.get(pk=id)
    # stuList=Students.stuObj2.get_queryset()
    # for stu in stuList:
    #     if stu.
    return render(request, 'myApp/modifystudentInfo.html',{"student": stu})


def toModifyStudent(request): # 修改学生信息
    id=request.POST.get("id")
    # name=request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    gradeid = request.POST.get('grade')
    hobby = request.POST.getlist('hobby')
    stu = Students.stuObj2.get(pk=id)
    # stu.sname=name
    stu.sgender=gender
    stu.sage=age
    stu.scontend=hobby
    stu.sgrade=gradeid
    stu.save()
    return HttpResponse("successful")


def addstudent2(request): # 点击班级现实班级中的所有学生
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj2.createStudent("刘华",34,True,"wojia",grade,"2017-8-10","2017-8-11")
    stu.save()
    return HttpResponse("successful")


def attribute(request): #
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.post)
    # e=request.get
    return HttpResponse("attribute")

def get1(request): #
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    # e=request.get
    return HttpResponse(a+" "+b+" "+c)

def get2(request): #
    a = request.GET.getlist('a')
    a1=a[0]
    a2=a[1]
    c = request.GET.get('c')
    # e=request.get
    return HttpResponse(a1+" "+a2+" "+c)


#POST
def showregist(request): #
    return render(request, 'myApp/regist.html')

#POST
def showregistforgrade(request): #
    return render(request, 'myApp/registgrade.html')




def regist(request): #
    #表单元素中的name属性的值就是键值
    name=request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    gradeid = request.POST.get('grade')
    hobby = request.POST.getlist('hobby')

    grade = Grades.objects.get(pk=gradeid)
    stu = Students.createStudent(name,age,gender,"I like "+hobby[0],grade,"2017-8-10","2017-8-11")
    stu.save()

    return HttpResponse(name+gender+age+hobby[0])

def registgrade(request): #
    #表单元素中的name属性的值就是键值
    name=request.POST.get('name')
    mannumber = request.POST.get('mannumber')
    girlnumber = request.POST.get('girlnumber')
    date=request.POST.get('date')

    gra = Grades.createGrade(name,date,mannumber,girlnumber)
    gra.save()
    return HttpResponse(name+mannumber+girlnumber)



#Response
def showresponse(request):
    #浏览器访问http://127.0.0.1:8000/showresponse/
    res=HttpResponse()
    res.content=b'good like this'  #这是要显示网页的内容
    print(res.content)
    print(res.charset)
    print(res.status_code)
    # print(res.conten)
    return res

#cookie
def cookieset(request):
    res = HttpResponse()
    # cookies=res.set_cookie("sunck","good")
    cookis=request.COOKIES
    res.write("<h1>"+cookis["sunck"]+"</h1>")
    return res




# 重定向
def rediret1(request):
    # return HttpResponseRedirect('/rediret2')
    return redirect('/rediret2') #这个是上面的简便写法



def rediret2(request):
    return HttpResponse("我是重定向后的视图")


#
def main(request):
    #取session
    username=request.session.get("name","游客") # 如果没取到，默认是游客

    return render(request,"myApp/main.html",{'username':username})


def login(request):
    return render(request,"myApp/login.html")


def showmain(request):
    username=request.POST.get('username')
    print(username)
    # 存储session
    request.session['name']=username
    request.session.set_expiry(10)  # 设置过期时间，单位是秒，10秒
    return redirect("/main")



def quit(request):
    #清除session
    logout(request)#推荐用这个
    #或者用这个
    # request.session.clear()
    return redirect("/main")



#反向解析
def good(request,num):
    #清除session
    logout(request)#推荐用这个
    #或者用这个
    # request.session.clear()
    return render(request,"myApp/good.html",{"num":num})

#模板继承
def mainbase(request):
    return render(request,"myApp/mainBase.html")

#上传文件
def upfile(request):
    return render(request,"myApp/upfile.html")

#保存文件
def savefile(request):
    if request.method=="POST":
        f=request.FILES["file"]
        #文件在服务器端的路径
        filePath=os.path.join(settings.MEDIA_ROOT, f.name)
        #把文件打开写到upfile中
        with open(filePath,'wb') as fp:
            #f.chunks()用于把文件流分段
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功")
        # return redirect("/showregist",{"upfileresut":"sucess"} )
    else:
        return HttpResponse("请求方法不对，上传失败")




# 实现学生分页
def studentpage(request,pageid):
    # 所有学生的列表
    allList=Students.stuObj2.all()
    paginator=Paginator(allList,3)#每页3个
    page=paginator.page(pageid)
    return render(request,"myApp/studentpage.html",{"students":page})

# ajax学习
def ajaxStudent(request):
    return render(request,"myApp/ajaxStudents.html")


# ajax学习
from django.http import JsonResponse
def studentsinfo(request):
    stus=Students.stuObj2.all()
    list=[]
    for stu in stus:
        list.append([stu.sname,stu.sage])

    return JsonResponse({"data":list})







# 实现富文本
def edit(request):

    return render(request,"myApp/edit.html")

# 实现celery
def celery(request):
    # 把下面的耗时操作挪到task里面去
    # print("sucnk is a good man")
    # time.sleep(10) #模拟耗时操作，十秒钟后才能返回页面
    return render(request,"myApp/celery.html")





























