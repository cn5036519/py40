import logging

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotAllowed
from django.utils.decorators import classonlymethod


class View(object):
    http_method_names = ['get', 'post', 'put', 'delete', 'patch', 'trace', 'head', 'options']

    # 关键字传参
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            # 给View实例对象设置属性值
            setattr(self, key, value)

    # 返回View实例对象允许的所有请求方法列表
    def _allowed_method(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def http_method_not_allowed(self, request, *args, **kwargs):
        """
        HttpResponseNotAllowed 继承 HttpResponse ,它返回的状态码是405
        """
        logging.warning('Method Not Allowed (%s): %s', request.method, request.path, extra={'status_code': 405, 'request': request})
        return HttpResponseNotAllowed(self._allowed_method())

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            # 获取View实例对象的属性,如果属性不存在,则返回默认值.
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            print(type(handler))
        else:
            # 成员方法:http_method_not_allowed
            handler = self.http_method_not_allowed
        # 执行http请求方法
        return handler(request, *args, **kwargs)

    def setup(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs

    @classonlymethod
    def as_view(cls, **initkwargs):
        for key in initkwargs:
            # 如果key是get\post\put...
            if key in cls.http_method_names:
                raise TypeError("You tried to pass in the %s method name as a keyword argument to %s(). Don't do that." % (key, cls.__name__))
            # 如果View类没有属性key
            if not hasattr(cls, key):
                raise TypeError("%s() received an invalid keyword %r. as_view "
                                "only accepts arguments that are already "
                                "attributes of the class." % (cls.__name__, key))

        # 闭包
        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            # 如果有get请求,但是没有head请求,那么head请求就是get请求
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            self.setup(request, *args, **kwargs)
            if not hasattr(self, 'request'):
                raise AttributeError("%s instance has no 'request' attribute. Did you override "
                    "setup() and forget to call super()?" % cls.__name__)
            # 再次调用dispatch()方法
            return self.dispatch(request, *args, **kwargs)
        view.view_class = cls
        view.view_initkwargs = initkwargs

        return view


class LoginRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return "xxxxx"
        return super().dispatch(request, *args, **kwargs)


if __name__ == '__main__':
    # from django.contrib.auth.mixins import LoginRequiredMixin 报错
    print(LoginRequiredMixin.__mro__)
