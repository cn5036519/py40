from django.db.models import F, Q, Sum, Count, Avg
from django.test import TestCase
from book import models

# 新增数据（方式1）
book = models.BookInfo(name="射雕英雄传")
book.save()
print(book)

# 新增数据（方式2）
manager_obj = models.BookInfo.objects   # <django.db.models.manager.Manager object at 0x7f8cb5fc2470>
book = manager_obj.create(name="天龙八部", pub_date='1986-7-24', commentcount=35, readcount=40, is_delete=0)
print(book)

# 修改数据（方式1）
book = models.BookInfo.objects.get(id=3)
book.commentcount = 12
book.readcount = 34
book.pub_date = "1980-5-1"
book.save()

# 修改数据（方式2）
query_set = models.BookInfo.objects.filter(id__exact=2)  # <QuerySet [<BookInfo: 红楼梦>]>
result = query_set.update(pub_date = "1986-4-1")
print(result)   # 返回成功更新的数据条数

# 删除数据（方式1）
result = models.BookInfo.objects.get(id=1).delete()
# 返回一个元组：第1个元素为删除的数据条数，第2个元素为1个字典。即(3, {'book.PeopleInfo': 2, 'book.BookInfo': 1}) ——> people表删除了2条，book表删除了1条。
print(result)
# 删除数据（方式2）
models.BookInfo.objects.filter(id=1).delete()

# 查询功能（1）
# get(查询条件):只能查询单条数据。如果没有查询到数据也会报错。返回一个实例对象。
book = models.BookInfo.objects.get(id=2)
# filter(查询条件)：查询多条数据，返回一个QuerySet实例对象。
query_set = models.BookInfo.objects.filter(name="红楼梦")
# all()：没有参数，返回一个QuerySet实例对象，获取所有数据。
models.BookInfo.objects.all()
# 获取所有数据条数
print(models.BookInfo.objects.count())
# 获取符合条件的数据条数
print(models.BookInfo.objects.filter(name="红楼梦").count())

# 查询功能（2）
# 查询编号为2的图书
print(models.BookInfo.objects.filter(id__exact=2))
# 查询编号不等于3的图书
models.BookInfo.objects.exclude(id=3)
# 查询书名包含'湖'的图书
print(models.BookInfo.objects.filter(name__contains="湖"))
# 查询书名以'部'结尾的图书
print(models.BookInfo.objects.filter(name__endswith="部"))
print(models.BookInfo.objects.filter(name__startswith="笑"))
# 查询书名为空的图书
print(models.BookInfo.objects.filter(name__isnull=True))
# 查询编号为1或3或5的图书
print(models.BookInfo.objects.filter(id__in=(1, 3, 5)))
print(models.BookInfo.objects.filter(pk__in=[1, 3, 5]))
# 查询编号大于3的图书
print(models.BookInfo.objects.filter(id__gt=3))
# 查询1980年发表的图书
print(models.BookInfo.objects.filter(pub_date__year=1980))
print(models.BookInfo.objects.filter(pub_date__contains="1980"))
# 查询1990年1月1日后发表的图书
models.BookInfo.objects.filter(pub_date__gt="1990-1-1")


# 查询功能（3）：F和Q对象
# 查询阅读量大于等于评论量的图书
print(models.BookInfo.objects.filter(readcount__gte=F('commentcount')))    # F里面的参数需要加引号
# 查询阅读量大于2倍评论量的图书
models.BookInfo.objects.filter(readcount__gt=2*F("commentcount"))
# 查询阅读量大于20，并且编号小于6的图书
print(models.BookInfo.objects.filter(readcount__gt=20, id__lt=6))
print(models.BookInfo.objects.filter(Q(readcount__gt=20) & Q(id__lt=6)))
# 查询阅读量大于20的图书
print(models.BookInfo.objects.filter(Q(readcount__gt=20)))
# 查询阅读量大于20，或编号小于6的图书
print(models.BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=6)))
# 查询编号不等于3的图书
print(models.BookInfo.objects.filter(~Q(id=3)))


# 聚合函数和排序函数
# 查询图书的总阅读量
print(models.BookInfo.objects.aggregate(Sum("readcount")))  # {'readcount__sum': 155}
# 查询图书总数
print(models.BookInfo.objects.aggregate(Count("id"), Sum("readcount"), Avg("commentcount")))
# 排序
print(models.BookInfo.objects.order_by("-id"))
print(models.BookInfo.objects.all().order_by("-id"))
models.BookInfo.objects.filter().order_by("-id")


# 查询功能（4）
# 查询书籍为4的所有人物信息
print(models.PeopleInfo.objects.filter(book_id=4))
# bookinfo模型对象里有一个peopleinfo_set属性，访问这个属性，返回的是一个RelatedManager实例对象.
print(models.BookInfo.objects.get(id=4).peopleinfo_set.all())

# 查询人物为20的书籍信息
print(models.BookInfo.objects.filter(peopleinfo__id=20))
print(models.BookInfo.objects.get(peopleinfo__id=20))
# PeopleInfo模型对象里有一个book属性，访问这个属性，返回的是一个Bookinfo实例对象。
print(models.PeopleInfo.objects.get(id=20).book)
# 查询书籍为4的书籍信息
print(models.BookInfo.objects.filter(peopleinfo__book_id=4))
