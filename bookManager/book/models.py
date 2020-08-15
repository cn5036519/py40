from django.db import models

# Create your models here.
class BookInfo(models.Model):
    # 必须设置max_length参数。
    name = models.CharField(max_length=10, verbose_name="书名")   # 设置verbose_name参数，不需要生成迁移文件和执行迁移文件就可生效。
    # 出版日期。 对应数据库中的date,且该字段可以为空。
    pub_date = models.DateField(null=True, verbose_name="出版日期")
    # 阅读量。对应数据库中的int(11),在数据库中default值没有设置成功。
    readcount = models.IntegerField(default=0, verbose_name="阅读量")  # 设置default参数，不需要生成迁移文件和执行迁移文件就可生效。
    # 评论量
    commentcount = models.IntegerField(default=0, verbose_name="评论量")
    # 是否删除。对应数据库中的tinyint(1),在数据库中default值没有设置成功。
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "bookinfo"
        verbose_name = "书籍信息"
        verbose_name_plural = "书籍信息"


class PeopleInfo(models.Model):
    # id字段(0~4294967295)，不手动创建也可以，django会默认创建。对应数据库中的主键
    # primary_key为必填参数，否则会报错“一个模型不能有多个AutoField”。
    id = models.AutoField(primary_key=True, verbose_name="ID")
    # 对应数据库中的varchar(10)
    name = models.CharField(max_length=10, verbose_name="人物")
    # 对应数据库中的smallint(6),0~65535。从小到大的顺序：tinyint > smallint > mediumint > int > bigint
    gender = models.SmallIntegerField(choices=((0, "男"),(1, "女")), default=1, verbose_name="性别")
    description = models.CharField(max_length=200, null=True, verbose_name="人物描述")
    # 对应数据库中的tinyint(1),0~255，在数据库中default值没有设置成功。
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    # 级联删除（删除主表数据的同时，自动删除从表的数据。）
    book = models.ForeignKey("BookInfo", on_delete=models.CASCADE, verbose_name="关联书籍")

    def __str__(self):
        return self.name + '(' + str(self.book) + ')'

    class Meta:
        # 修改表名（默认为“应用名_类名”）
        db_table = "peopleinfo"
        # 在admin管理后台，汉化显示的名字
        verbose_name = "人物信息"
        verbose_name_plural = "人物信息"