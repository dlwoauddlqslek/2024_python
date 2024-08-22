import mod1
# [1] import 모듈이름:
    # 모듈이름.함수명()
mod1.add(3,4)

# [2] from 모듈이름 import 함수명, 함수명
from mod1 import add
add(3,4) # 함수명()

# [3] from 모듈이름 import *
from mod1 import *
sub(3,4)

# [4]
import mod2
print(mod2.PI) # 3.141592

a=mod2.Math()
print(a)    #<mod2.Math object at 0x000001D0BACD1EB0>
print(a.solv(2))    #12.566368

print(mod2.add(3,4)) #7

from mod2 import Math,PI
print(PI)   #3.141592
b=Math()
print(b)    #<mod2.Math object at 0x000001D0BACD1F10>

# [5]
from src.day06.Task6 import Info
s=Info('이',30)
