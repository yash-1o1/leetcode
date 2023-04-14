# let's try a little more complex pattern
# *
#  *
#   *

def main(n):
    i = 0;
    j = 0;
    for i in range(n):
        for j in range(n):
            if i == j:
                print('*', end='');
            else:
                print(' ', end='');
        #print a new line
        print('');

# call for the function created above
if __name__ == '__main__':
    main(3);