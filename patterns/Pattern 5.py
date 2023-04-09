# in  this file we will see how to draw a pattern which is an reversed intverted triangle pattern
# ***
# **
# *
def main(n):
    i = 0;
    j = 0;
    for i in range(n):
        for j in range(n):
            if j >= i:
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

# how did we get this pattern?
# we have used the same logic as in the previous pattern, but we have changed the condition in the inner for loop
# to find the condition we have used the following logic
# write all the possible outcomes and then try to find the pattern between i, j and n

# like this:
# when i = 0, j = 0, n = 3, print ' '
# when i = 0, j = 1, n = 3, print ' '
# when i = 0, j = 2, n = 3, print *
# when i = 1, j = 0, n = 3, print ' '
# when i = 1, j = 1, n = 3, print *
# when i = 1, j = 2, n = 3, print *
# when i = 2, j = 0, n = 3, print *   
# when i = 2,, j = 1, n = 3, print *
# when i = 2, j = 2, n = 3, print *