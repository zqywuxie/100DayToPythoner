"""
@Project ：PythonLearnProject 
@File    ：coverter.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/5 16:19 
@Description TODO 文件描述
"""
import typing as t

from werkzeug.routing import BaseConverter, Map


class RegexConverter(BaseConverter):
    def __init__(self, map: Map, *args: t.Any, **kwargs: t.Any) -> None:
        super(RegexConverter, self).__init__(map)
        # 传入的第一个参数就作为正则匹配
        self.regex = args[0]
        # print(args)

    def to_python(self, value: str) -> t.Any:
        return int(value) + 1

    def to_url(self, value: t.Any) -> str:
        val = super(RegexConverter, self).to_url(value)
        return val
