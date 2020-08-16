from django.apps import AppConfig

# 当创建应用时，django会默认向该配置文件中写入一个该应用的配置类
class BookConfig(AppConfig):
    name = 'book'
    """
    verbose_name:在admin管理后台显示的应用名称。它的默认值是app_name.rpartition(".")[2].title()
    str.rpartition(".") # 返回一个3元组，从字符串的右边开始查找分隔符。
    str.title() # 返回字符串的标题版本
    """
    verbose_name = "图书"

