
#this is a function for a basic patter 
# ***
# ***
# ***

def main():
    i = 0;
    j = 0;
    for i in range(3):
        for j in range(3):
            print('*', end='');
            j = j+1;
        #print a new line
        print('');
        i = i+1;

## call for the function created above
if __name__ == '__main__':
    main();

## print in python witgout new line

