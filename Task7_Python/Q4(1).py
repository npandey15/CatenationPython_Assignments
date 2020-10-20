class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

# Traceback (most recent call last):
AttributeError: Derived_Test instance has no attribute 'x'
# Output is error as class B inherits Class A but variable x is not inherited.