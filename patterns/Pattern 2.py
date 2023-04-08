# let's try a little more complex pattern
# # *
# #  *
# #   *

# the follwoing pattern is created using nested for loop
def main():
    i = 0;
    j = 0;
    for i in range(3):
        for j in range(3):
            if i == j:
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