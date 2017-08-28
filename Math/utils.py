"""This is Math Module"""
def fact(val):
    """Gives Factorial of a number"""
    if(val==0 or val==1):
         return 1;
    return val*fact(val-1);

def fib(val):
    if(val==0 or val==1):
         return 1;
    return fib(val-1) + fib(val-2);
