x_points=[0,1,2]
y_points=[1,3,7]
n=len(x_points)
P=0

V=[]
for x in x_points:
    row=[]
    for power in range(n):
       row.append(x** power)

    V.append(row)
  
print(V)
