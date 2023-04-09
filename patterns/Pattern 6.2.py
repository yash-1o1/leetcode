# here we'll see how to draw a pattern which is an intverted triangle pattern but with a different approach
#   *
#  **
# ***

# we'll use this appraoch to solve problems with preceeding spaces as it's easier to undrestand.
# instead of using two loops, we'll use one loop to interate through the rows and multiple loops within that to go through the columns.
def main(n):
    i = 0;
    j = 0;
    for i in range(n):
        #print spaces
        spaces = n-i-1;
        for k in range(spaces):
            print(' ', end='');
            j = j+1;
        #print stars
        stars = n-spaces;
        for k in range(stars):
            print('*', end='');
        #print a new line
        print('');

# call for the function created above
if __name__ == '__main__':
    main(3);

# how did we get this pattern?
# we broke the pattern into two parts, the first part is the spaces and the second part is the stars
# ___
#|  //|
#| // |
#|//__|
# these are the thwo parts of the pattern, the first traingle respresents the spaces and the second triangle represents the stars.
# most of the questions can be broken down into trangles and then we can solve them using the same logic.
# each loop within the outer loop represents a traingle shown above.