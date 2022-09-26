import time
with open('config.txt', 'r') as myFile:  # This closes the file for you when you are done
        contents = myFile.read()

array = []
for i in contents.split():
        array.append(int(i));


N = array[0]
M = array[1]
t = [['O']*(N)for i in range(M)]
A = array[3]-1
B = array[4]
i=A
j=B
t[M-B][A] = 'X'
sum=0
flag=0
print("Initial state of the grid\n")
print(t)
def rule(i,j):
        a=(t[i] [(j-1)])  
        b= (t[i][(j+1)]) 
        c=(t[(i-1)][j]) 
        d=(t[(i+1)][j] ) 
        e=( t[(i-1)][(j-1)]) 
        f= (t[(i-1)][(j+1)]) 
        g= ( t[(i+1)][(j-1)])
        h= (t[(i+1)][(j+1)])
        return a+b+c+d+e+f+g+h
while 1:
        
        iterations = int(input("Enter number of iterations:"))
        sum=sum+iterations
        if iterations == -1:
            flag=1
            quit()  
        print("State of the grid after iteration\n")
        if sum > (N-A):
	        sum = N-A-1
        for x in range(1, 1+sum, 1):
	        if t[M-B][x-1] == 'X':
		        t[M-B][x] = 'X' 
        with open("output.txt", "w") as o:
        # print(t)
          for i in range(M):
            for j in range(N):
                if str(t[i][j])=='X':
                 o.write("X")
                else:
                 o.write("O")
            o.write("\n")
        o.close()
        time.sleep(0.2)
        print(t)
        
