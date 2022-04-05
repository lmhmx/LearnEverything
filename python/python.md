# str

## format

* `"{:^ns}"`居中对齐，`"{:<ns}"`左对齐，`"{:>ns}"`右对齐
* `"{:ns}".format(str)`对字符串进行格式化操作

# 返回值

## 返回值有多个

``` python
from typing import Tuple

def aa()->Tuple[str, str]:
    return "as","asf"
a,b=aa()
```
