from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    """
    默认值是app_name.rpartition(".")[2].title()
    str.rpartition(".") # 返回一个3元组，从字符串的右边开始查找分隔符。
    str.title() # 返回字符串的标题版本
    """
    verbose_name = "图书"

