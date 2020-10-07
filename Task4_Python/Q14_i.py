def foo():
   try:
      return 1
   finally:
      return 2
k = foo()
print(k)

# The output of above program will be 2