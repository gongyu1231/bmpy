from django.db import models

# Create your models here.
class adduser(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField('姓名', max_length = 20)  # 博客标题
    ename = models.CharField('英文姓名', max_length = 20)  # 博客标题
    gender_list = (
        (1,'男'),
        (2,'女'),
        (3,'其他'),
    )
    gender = models.IntegerField(choices=gender_list, default=1, verbose_name='性别')  # 博客标题
    nation = models.CharField('国籍', max_length = 20)  # 博客标题
    birthday = models.DateField('生日')  # 博客标题
    passport = models.CharField('护照号码', max_length = 20)  # 博客标题
    idcard = models.CharField('身份证号', max_length = 20)  # 博客标题
    mobile = models.CharField('手机号码', max_length = 20)  # 博客标题
    wechat = models.CharField('微信', max_length = 20)  # 博客标题
    email = models.EmailField('电子邮箱', max_length = 20)  # 博客标题
    add = models.CharField('邮寄地址', max_length = 20)  # 博客标题
    money = models.BigIntegerField('会费')
    company = models.CharField('公司', max_length = 20)  # 博客标题
    industry = models.CharField('公司行业', max_length = 20)  # 博客标题
    firmsize = models.CharField('公司规模', max_length = 20)  # 博客标题
    financingsituation = models.CharField('资产规模', max_length = 20)  # 博客标题
    department = models.CharField('部门', max_length = 20)  # 博客标题
    title = models.CharField('职位', max_length = 20)  # 博客标题
    comadd = models.CharField('公司地址', max_length = 20)  # 博客标题
    hobby = models.CharField('爱好', max_length = 20)  # 博客标题
    recom1 = models.CharField('推荐人1', max_length = 20)  # 博客标题
    reason1 = models.CharField('推荐理由', max_length = 20)  # 博客标题
    recom2 = models.CharField('推荐人2', max_length = 20)  # 博客标题
    reason2 = models.CharField('推荐理由2', max_length = 20)  # 博客标题
    timestamp = models.DateTimeField('创建时间', auto_now=True)          # 创建时间

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['name']  # 按照哪个栏目排序

class points(models.Model):
#    userid = models.ForeignKey('adduser', related_name= 'uid', verbose_name='用户ID', on_delete=models.CASCADE)
    name = models.ForeignKey('adduser', verbose_name='用户姓名', on_delete=models.CASCADE)
    money = models.DecimalField(max_digits=10, decimal_places=2, )  # 充值金额
    cardinality = models.DecimalField(default=1,max_digits=2, decimal_places=0,)  #金额变积分的基数
    total = models.DecimalField(max_digits=10, decimal_places=2, )  # 余额
    pointstimes = models.DateField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True, )  # 充值时间


    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name = '积分充值'
        verbose_name_plural = '积分充值'
        ordering = ['name']  # 按照哪个栏目排序

class consume(models.Model):
    consumename = models.CharField('消费名称', max_length= 40)
    add = models.CharField('消费地点', max_length=20)
    #user = models.ForeignKey(adduser,verbose_name='消费用户', )
    name = models.ManyToManyField(adduser, verbose_name='消费用户')
    amount = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='消费金额')
    quantity = models.DecimalField(max_digits=3,decimal_places=0,verbose_name='消费人数')
    consumetimes = models.DateTimeField('消费时间',)  # 创建时间
    timestamp = models.DateTimeField('创建时间', auto_now=True)          # 创建时间

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '积分消费'
        verbose_name_plural = '消费名称'
        ordering = ['consumename']  # 按照哪个栏目排序
