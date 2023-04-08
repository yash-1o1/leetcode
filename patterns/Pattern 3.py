# there could be another variation of the pattern where the if statement to print he star is replaced to check if j <= i
# # *
# # **  
# # ***

# the follwoing pattern is created using nested for loop
def main():
    i = 0;
    j = 0;
    for i in range(3):
        for j in range(3):
            if j <= i:
                print('*', end='');
            else:
                print(' ', end='');
            j = j+1;
        #print a new line
        print('');
        i = i+1;

# let's try a little more complex pattern

## call for the function created above
if __name__ == '__main__':
    main();

# let's try a little more complex pattern than compared to the above pattern, here we will print the pattern in reverse order
# # ***
# # **
# # *