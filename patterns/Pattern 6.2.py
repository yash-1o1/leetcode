# in  this file we will see how to draw a pattern which is an intverted triangle pattern but with a different approach
#   *
#  **
# ***
# we'll use this appraoch to solve problems with preceeding spaces as it's easier to undrestand.
# instead of using two loo[s, we'll use one loop to interate through the rows and multiple loops within that to go through the columns 
def main(n):
    i = 0;
    j = 0;
    for i in range(n):
        spaces = n-i-1;
        for k in range(spaces):
            print(' ', end='');
            j = j+1;
        stars = n-spaces;
        for k in range(stars):
            print('*', end='');
        #print a new line
        print('');

## call for the function created above
if __name__ == '__main__':
    main(3);