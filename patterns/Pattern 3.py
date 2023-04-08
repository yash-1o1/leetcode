# there could be another variation of the pattern which is called the triangle pattern
# # *
# # **  
# # ***

# the follwoing pattern is created using nested for loop
def main(n):
    i = 0;
    j = 0;
    for i in range(n):
        for j in range(n):
            if j <= i:
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