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

# 查询图书，要求图书人物为"郭靖"
print(models.BookInfo.objects.filter(peopleinfo__name="郭靖"))
# 查询图书，要求图书中人物的描述包含"八"
print(models.BookInfo.objects.filter(peopleinfo__description__contains="八"))
# 查询人物ID=20的图书信息
people = models.PeopleInfo.objects.get(id=20)
print(models.BookInfo.objects.get(peopleinfo=people))


# 查询书名为“天龙八部”的所有人物
print(models.PeopleInfo.objects.filter(book__name="天龙八部"))
# 查询图书阅读量大于30的所有人物
print(models.PeopleInfo.objects.filter(book__readcount__gt=30))
# 查询book_id=4的所有人物
book = models.BookInfo.objects.get(id=4)
print(models.PeopleInfo.objects.filter(book=book))

# exists()的使用：
print(models.PeopleInfo.objects.exists())
print(models.PeopleInfo.objects.filter(book_id=4).exists())
print(models.PeopleInfo.objects.all().exists())



"""
QuerySet的两个特性:
    1、它是惰性机制，即创建结果集不会去访问数据库，只有调用数据时，才会去访问数据库执行。
        # 创建结果集
        books = models.BookInfo.objects.all()
        # 数据调用：for循环遍历、序列化、与if语句一起使用，都是数据调用。
        print([book for book in books])
    2、缓存
        概念：这里的缓存，是指将硬盘中的数据存放到内存。再次使用数据时，从内存中读取，不必要重新从硬盘获取，这样速度会很慢。（减少了数据库的查询次数）
        如何缓存呢？  
            # 通过创建结果集来进行缓存
            books = models.BookInfo.objects.all()
            # 数据调用：只有第一次会与数据库进行交互执行，之后的都会从缓存中直接读取。
            [book for book in books]
        什么是对结果集没有进行缓存呢？
            # 没有创建结果集就不会缓存
            [book for book in models.BookInfo.objects.all()]    
            
"""
# 创建结果集
books = models.BookInfo.objects.all()
# 数据调用
print([book for book in books])


# 限制查询集(即切片操作)
peoples = models.PeopleInfo.objects.all()
# 执行了查询
p1 = peoples[0]
# 没有执行查询    (peoples[0] 等价于 peoples[0:1].get())
peoples2 = peoples[0:1]
# 执行了查询
print(peoples2.get())    # QuerySet还有get()方法呢,要调用get方法,必须保证有且只有1条数据,否则报错.
# 不写过滤条件,则查找所有数据
print(peoples.filter())


# 分页
peoples = models.PeopleInfo.objects.all()
from django.core.paginator import Paginator
# per_page:每页显示条数
p = Paginator(peoples, 2)
# 返回数据总条数
print(p.count)
# 返回总页数 = (p.count / p.per_page) if (p.count % p.per_page) == 0 else (p.count // p.per_page)+1
print(p.num_pages)
# 返回从1开始的页面范围
print(p.page_range) # range(1, 10)


# 返回一个基于页码1的Page对象
print(p.page(1))    # <Page 1 of 9>
print(type(p.page(1)))    # <class 'django.core.paginator.Page'>
# 返回一个QuerySet
print(p.page(1).object_list)


page_obj = p.page(2)
# 判断是否还有下一页
print(page_obj.has_next())
# 判断是否还有上一页
print(page_obj.has_previous())
# 判断是否还有其他页码
print(page_obj.has_other_pages())
# 下一页码
print(page_obj.next_page_number())
# 上一页码
print(page_obj.previous_page_number())
# 返回此页上第一个数据的索引和最后一个数据的索引
print(page_obj.start_index())
print(page_obj.end_index())
