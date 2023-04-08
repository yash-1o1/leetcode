# let's try a little more complex pattern than compared to the last pattern, here we will try to print a reverse triangle pattern and this will require us to pass a 
# parameter to the function which will be used to determine the number of rows in the pattern
# for the following pattern we will pass 3 as the parameter
# # ***
# # **
# # *

# the follwoing pattern is created using nested for loop
def main(n):
    i = 0;
    j = 0;
    for i in range(n):
        for j in range(n):
            if j < n-i:
                print('*', end='');
            else:
                print(' ', end='');
            j = j+1;
        #print a new line
        print('');
        i = i+1;

## call for the function created above
if __name__ == '__main__':
    main(3);