from django.db import models

# Create your models here.
class BookInfo(models.Model):
    # 必须设置max_length参数。unique：表示name不允许重复，在mysql中添加了唯一键约束。blank：用于表单验证，默认值为False，表示输入不允许为空。
    name = models.CharField(max_length=10, verbose_name="书名", unique=True, blank=False)   # 设置verbose_name参数，不需要生成迁移文件和执行迁移文件就可生效。
    # 出版日期。 对应数据库中的date,且该字段可以为空。db_column：表示在mysql数据库中显示的字段名。
    pub_date = models.DateField(null=True, verbose_name="出版日期", db_column="publish_date", blank=False)
    # 阅读量。对应数据库中的int(11),在数据库中default值没有设置成功。
    readcount = models.IntegerField(default=0, verbose_name="阅读量", blank=True)  # 设置default参数，不需要生成迁移文件和执行迁移文件就可生效。
    # 评论量。mysql中int(11)，数字11表示mysql客户端展示该字段的数据宽度为11位，数据超过11位，也是能存储的。如果不足11位，想要显示11位，可以使用0来补充，但必须修改该字段的约束为unsigned zerofill
    commentcount = models.IntegerField(default=0, verbose_name="评论量", blank=True)
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
    # 对应数据库中的varchar(10)。db_index：若值为True, 则在表中会为此字段创建索引。
    name = models.CharField(max_length=10, verbose_name="人物", db_index=True, blank=False)
    # 对应数据库中的smallint(6),0~65535。从小到大的顺序：tinyint > smallint > mediumint > int > bigint
    gender = models.SmallIntegerField(choices=((0, "男"),(1, "女")), default=1, verbose_name="性别", blank=False)
    description = models.CharField(max_length=200, null=True, verbose_name="人物描述", blank=True)
    # 对应数据库中的tinyint(1),0~255，在数据库中default值没有设置成功。
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    # 级联删除（删除主表数据的同时，自动删除从表的数据。）
    book = models.ForeignKey("BookInfo", on_delete=models.CASCADE, verbose_name="关联书籍")
    """
    models.CASCADE  ：级联删除
    models.PROTECT  ：如果从表已经引用了主表中的数据，则不允许删除该主表数据，会报错ProtectedError。
    models.SET_NULL ：如果从表已经引用了主表中的数据，则删除主表数据时，从表的字段会被设置为null，前提是：该从表字段允许为空。
    models.SET_DEFAULT  ：如果从表已经引用了主表中的数据，则删除主表数据时，从表的字段会被设置为默认值，前提是：该从表字段设置了default默认值。
    models.SET()        ：设置为特定值或调用特定方法
    models.DO_NOTHING   ：不做任何操作。？？
    """

    def __str__(self):
        return self.name + '(' + str(self.book) + ')'

    class Meta:
        # 修改表名（默认为“应用名_类名”）
        db_table = "peopleinfo"
        # 在admin管理后台，汉化显示的名字
        verbose_name = "人物信息"
        verbose_name_plural = "人物信息"