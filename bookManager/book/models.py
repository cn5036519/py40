from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    # id字段，不手动创建也可以，django会默认创建。对应数据库中的主键
    # primary_key为必填字段，否则会报错“一个模型不能有多个AutoField”。
    id = models.AutoField(primary_key=True)
    # 对应数据库中的varchar(10)
    name = models.CharField(max_length=10)
    # 对应数据库中的
    gender = models.BooleanField(default=True)
    # 级联删除（删除主表数据的同时，自动删除从表的数据。）
    book = models.ForeignKey("BookInfo", on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '(' + str(self.book) + ')'
