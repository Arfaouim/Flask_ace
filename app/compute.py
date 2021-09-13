from sympy.abc import*
from sympy import Sum, factorial, oo, IndexedBase, Function, latex, simplify,symbols
from string import ascii_uppercase

upper = ','.join(ascii_uppercase) 

A,B,C,D,E,F,G,H,I,J,K,L,M,O,P,Q,R,S,T,U,V,W,X,Y,Z = symbols("A B C D E F G H I J K L M O P Q R S T U V W X Y Z")

def expr(fun,var,start,end):
    return latex(Sum(fun, (var, start, end)))

def calc_(fun,var,start,end):
    return Sum(fun, (var, start, end)).doit()

def simplified(exp):
    return latex(simplify(exp)) 

# if __name__ == '__main__':
#     serie(a,1,n)    