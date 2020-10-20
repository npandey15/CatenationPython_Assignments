# defining a decorator 
def hello_decorator(func): 
    
    def inner(): 
        print("Hello, How are you? ") 
   
        func() 
  
        print("Sounds Great! ")         
    return inner 
  
# defining a function, to be called inside wrapper 
def function_to_be_used(): 
    print("I am doing good !!") 

function_to_be_used = hello_decorator(function_to_be_used) 

# calling the function 
function_to_be_used()