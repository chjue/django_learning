from django.db import models

# Create your models here.

# 对应数据库中的 grades 表
class Grades(models.Model):
    gname = models.CharField(max_length=20) # 对应表里字段
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default = False)
    def __str__(self):
        return "%s-%d-%d"%(self.gname,self.ggirlnum,self.gboynum)
    class Meta:
        db_table="grades"
        ordering=['id']

    #定义一个类方法创建对象,相当于构造方法
    # cls相当于self指的是Grades类
    @classmethod
    def createGrade(cls,gname,gdate,ggirlnum,gboynum,isDelete=False):
        gra=cls(gname=gname,gdate=gdate,ggirlnum=ggirlnum,gboynum=gboynum,isDelete=isDelete)
        return gra




# 自定义模型管理器Manager类
class StudentsManager(models.Manager):
    def get_queryset(self):#返回过滤后的查询结果集
        return super(StudentsManager,self).get_queryset().filter(isDelete=False)

    def get_queryset2(self,id):#返回过滤后的查询结果集
        return super(StudentsManager,self).get_queryset().filter(id=id)

    def createStudent(self,name,age,gender,contend,grade,lastT,createT,isD=False):#此方法在view中addstudent2使用
        stu=self.model()
        stu.sname=name
        stu.sage=age
        stu.sgender=gender
        stu.lastTime=lastT
        stu.createTime=createT
        stu.sgrade=grade
        return stu





# 对应数据库中的 students 表
class Students(models.Model):
    stuObj = models.Manager() # 自定义模型管理器，如果写了自定义模型管理器则objects就不能用了
    stuObj2 = StudentsManager() # 使用自定义模型管理器Manager类
    sname = models.CharField(max_length=20) # 对应表里字段
    sgender = models.BooleanField(default = True) # 性别，默认 男
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE) # 关联Grades对象表外键
    isDelete = models.BooleanField(default = False)
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.sname
    class Meta:
        db_table="students" # 表名
        ordering=['id']  # 升序
        # ordering = ['-id'] #降序

    #定义一个类方法创建对象,相当于构造方法
    # cls相当于self指的是Students类
    @classmethod
    def createStudent(cls,name,age,gender,contend,grade,lastT,createT,isD=False):
        stu=cls(sname=name,sage=age,sgender=gender,scontend=contend,sgrade=grade,lastTime=lastT,createTime=createT,isDelete=isD)
        return stu









