import Math;
from Math import fact;
from Name import Name;

print "The factorial of 10 is %d" % fact(10);

print "The Fib of 10 is %d" % Math.fib(10);

print __name__;

def sum(a,b):
     """ This is a sum Function.
         Inputs: Two integers
         Output: Summed value
     """
     return a+b

print Math.fact.__doc__;

name = Name("rahul","kumar");
name.display();
