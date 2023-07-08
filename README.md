# hello-python

Learn to use Python

## 基础

- Python允许在数字中间以`_`分隔，如：`10_000_000`、`0xa1b2_c3d4`
- 字符串不转义：`r'\\\t\\'`
- 精确除法：`/`，地板除：`//`
- 整数和浮点数都是没有大小限制的，浮点数超出一定范围直接表示为`inf`
- `ord()`获取字符的整数表示，`chr()`把编码转换为对应的字符
- bytes类型：`b'ABC'`，bytes要变为str，可以用`decode()`，如果有一小部分无效字节，可以传入errors='ignore'来忽略字节：`b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')`
- f-string格式化字符串

  ```python
  >>> r = 2.5
  >>> s = 3.14 * r ** 2
  >>> print(f'The area of a circle with radius {r} is {s:.2f}')
  The area of a circle with radius 2.5 is 19.62
  >>>
  ```

- 只有一个元素的tuple：`(1,)`
- 函数的命名关键字参数(如果没有可变参数就必须加一个`*`作为特殊分隔符)：`def person(name, age, *, city, job)`
