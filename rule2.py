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
co_ordinate_array = [['O']*(2)for i in range(no_blacks)]
a = 0
for i in range(no_blacks):
    for j in range(2):
        co_ordinate_array[i][j] = array[3+a]
        a = a+1
# print(N)
# print(M)
# print(iterations)
# print(no_blacks)
# for i in range(no_blacks):
#     for j in range(2):
#         print(co_ordinate_array[i][j])
temp_array1 = [[0]*(N+2)for i in range(M+2)]
temp_array2 = [[0]*(N+2)for i in range(M+2)]
for i in range(no_blacks):
    temp_array2[M-co_ordinate_array[i][1]+1][co_ordinate_array[i][0]] = 1
    temp_array1[M-co_ordinate_array[i][1]+1][co_ordinate_array[i][0]] = 1

# o= open("output.txt", "a") 
#  we will always make changes in array 1 and compare it to array 2
# o.write("intial grid")
# for i in range(M+2):
#     for j in range(N+2):
#         o.write(str(temp_array2[i][j]))
#     o.write("\n")
sum=0
print("Initial state of the grid\n")
print(temp_array2)
def rule(i,j):
        a=(temp_array2[i] [(j-1)])  
        b= (temp_array2[i][(j+1)]) 
        c=(temp_array2[(i-1)][j]) 
        d=(temp_array2[(i+1)][j] ) 
        e=( temp_array2[(i-1)][(j-1)]) 
        f= (temp_array2[(i-1)][(j+1)]) 
        g= ( temp_array2[(i+1)][(j-1)])
        h= (temp_array2[(i+1)][(j+1)])
        return a+b+c+d+e+f+g+h
while 1:
    iterations = int(input("Enter Number of Iterations\n"))
    if iterations == -1:
        quit()
    print("State of the grid after iteration\n")
    sum=sum+iterations
    for hello in range(iterations):
    # print("HEY")
        for i in range(1,N+1,1):
            for j in range(1,M+1,1):
                 total = int(((temp_array2[i] [(j-1)])  + (temp_array2[i][(j+1)]) +
                         (temp_array2[(i-1)][j]) + (temp_array2[(i+1)][j] ) +
                        ( temp_array2[(i-1)][(j-1)]) + (temp_array2[(i-1)][(j+1)]) +
                        ( temp_array2[(i+1)][(j-1)]) + (temp_array2[(i+1)][(j+1)])))
 
                 if temp_array2[i][j]  == 1:
                    if (total < 2) or (total > 3):
                     temp_array1[i][j] = 0
                 else:
                     if total == 3:
                      temp_array1[i][j] = 1
        for me in range(M+2):
         for mee in range(N+2):
            temp_array2[me][mee]=temp_array1[me][mee]
    # o.write("temp_2 now is\n" )
    # for i in range(M+2):
    #     for j in range(N+2):
    #         o.write(str(temp_array2[i][j]))
    #     o.write("\n")
        with open('output.txt', 'w') as o:
            for i in range(1,M+1,1):
                for j in range(1,N+1,1):
                 if(temp_array2[i][j]==1):
                     o.write("X")
                 else:
                     o.write("O")
                o.write("\n")
        o.close();
        time.sleep(0.2)
    print(temp_array2)

