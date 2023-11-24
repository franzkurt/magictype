
# Test the function with a script
script = """def foo(bar:str, baz, qux=4):
    x = bar + baz
    return [4.3,2]
foo(3.2, "2.0", "3.4")
"""
print(annotate_types(script))

script2 = """a:int=1
b=1.3
c='1.3'
b=False
f=[1,2,3]
f={1,2,3}
f=(1,2,3)
"""
print(annotate_types(script2))

script3 = """
class oi:
    def __init__(self, oi3333, ber, sho=4.4):
        x = bar + baz
        return 4

    def foo(bar:str, baz, qux=4):
        x = bar + baz
        return 4.3

i=oi(1,2,3)
i.foo(3.2, "2.0", "3.4")

class bbb:
    def __init__(self, abc, defss, ghd):
        x = bar + baz
        return '4.3'

    def foo(bar:int, baz, qux=4):
        x = bar + baz
        return '4'

def lucas(a):
    return 5
lucas(9)

def jonas(a):
    return 5
jonas([9.3,'p'])

ib=bbb(["dsiod",2,2.3], 3, 3.4)
ib.foo(3.2, "2.0", "3.4")
"""
print(annotate_types(script3))
