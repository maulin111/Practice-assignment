from typing import Union

class Money:

    def __init__(self, value:Union[int,float], denomination:str="INR"):
        self.value = value
        self.denomination = denomination

    def __repr__(self):
        return f"<Money:{self.denomination} {self.value}>"

    def convert2dollar(self):
        return Money(self.value/80,"DLR")

v1 = Money(10, "INR")
v2 = Money(10.2)
# print(v2)
c1 = v1.convert2dollar()
print(c1)

def money_value(obj):
    return obj.value

List1 = [Money(10), Money(12), Money(8)]
# print(List1.sort(key=lambda x:x.value))
print(List1.sort(key=money_value))
print(List1)

