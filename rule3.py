from http.client import TOO_MANY_REQUESTS
from os import close
import time
with open('config.txt', 'r') as myFile:  # This closes the file for you when you are done
    contents = myFile.read()
array = []
for i in contents.split():
    array.append(int(i))
N = array[0]  # no of coloumns
M = array[1]  # no of rows
no_blacks = array[2]  # total number of blacks each correspond to coordinate
co_ordinate_array = [[0]*(2)for i in range(no_blacks)]
a = 0
for i in range(no_blacks):
    for j in range(2):
        co_ordinate_array[i][j] = array[3+a]
        a = a+1
        # for i in range(no_blacks):
        #     for j in range(2):
        #         print(co_ordinate_array[i][j])
t_array = [[0]*(N)for i in range(M)]
for i in range(no_blacks):
        t_array[M-co_ordinate_array[i][1]][co_ordinate_array[i][0]-1] = 1
sum=0
print("Initial state of the grid\n")
print(t_array)
def rule(i,j):
        a=(t_array[i] [(j-1)])  
        b= (t_array[i][(j+1)]) 
        c=(t_array[(i-1)][j]) 
        d=(t_array[(i+1)][j] ) 
        e=( t_array[(i-1)][(j-1)]) 
        f= (t_array[(i-1)][(j+1)]) 
        g= ( t_array[(i+1)][(j-1)])
        h= (t_array[(i+1)][(j+1)])
        return a+b+c+d+e+f+g+h
while(1):
    iterations = int(input("Enter Number of Iterations\n"))
    if iterations == -1:
     quit()
    print("State of the grid after iteration\n")
    sum=sum+iterations
    for me in range(sum):
            with open('output.txt', 'w') as o:
                for i in range(M):
                    for j in range(N):
                        if t_array[i][j]==1:
                            t_array[i][j]=0
                        else:
                            t_array[i][j]=1
                        if(t_array[i][j]==1):
                          o.write("X")
                        else:
                          o.write("O")
                    o.write("\n")
            o.close();
            time.sleep(0.5)
    print(t_array)

