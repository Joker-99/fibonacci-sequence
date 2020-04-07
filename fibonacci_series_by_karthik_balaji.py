#fibinacci series

#step 1: take input from user.
num = int(input('Please enter the required range n:'))

#step 2: initial the frst value and second value in the series
frst_val = 0
scnd_val = 1

#step 3: using for loop to print the fibinacci sequence.
for x in range(0,num):
    if(x<=1):
        Next_num =x
    else:
        Next_num = frst_val + scnd_val
        frst_val = scnd_val
        scnd_val = Next_num
    print(Next_num)

   
    
        
