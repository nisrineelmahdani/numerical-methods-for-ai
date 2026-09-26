import sympy as sp 
x=sp.symbols('x')
x_points=[1,10,8]
y_points=[3,7,5]


P=0

for k in range(len(x_points)):
    L=1
    for j in range(len(y_points)):
        if j!=k:
            L*= ( x-x_points[j] )/( x_points[k]-x_points[j] )
   
    P+= y_points[k]*L

P=sp.expand(P)
print("lagrange polynomial is: ",P)