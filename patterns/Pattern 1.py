# the follwoing pattern is created using nested for loop and is the most basic example of a pattern 
# in all the patterns qquestion we will be passing in a parameter to the function which will be used to determine the number of rows in the pattern.
# however it's not really necessary to pass in a parameter to the function for each of the pattern question, 
# we could have just used a constant value to determine the number of rows in the pattern.
# ***
# ***
# ***

def main(n):
    i = 0;
    j = 0;
    for i in range(n):
        for j in range(n):
            print('*', end='');
            j = j+1;
        #print a new line
        print('');
        i = i+1;

# call for the function created above
if __name__ == '__main__':
    main(3);