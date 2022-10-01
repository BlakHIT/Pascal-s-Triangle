If you do want to hold an in person event, there’s a few things to note: def _copy(l, l2):
    l2.clear()
    for i in l:
        l2.append(i)

        
def _ls(l):
    b = ''
    for i in l:
        c = str(i)
        b += '{} '.format(c)
    return b

# This execute the main operations to be done
def main(n):
    if n == 1:
        print(1)

    elif n == 2:
        print(1)
        print(1, 1)

    elif n > 2:

        lst = [1]
        lst2 = []
        a = 1

        for i in range(n - 1):

            if a == 1:
                print(_ls(lst))
            else:
                print(1, _ls(lst))

            if a == 1:
                print(1, 1)
                a += 1

            _copy(lst, lst2)

            lst3 = []

            for j in range(len(lst2)):
                elem = lst2[j - 1] + lst2[j]
                lst3.append(elem)

            lst3.append(1)
            _copy(lst3, lst)

print()
print('Welcome to the "PASCAL\'s TRIANGLE"')

# Main Loop Starts Here
while True:
    try:
        print()
        choice = int(input('Enter the number of rows you want to print(0 -> quit): '))

        if choice > 0:
            print()
            main(choice)
            print()

        elif choice == 0:
            print()
            print('Thanks for using :)')
            print()
            print('Bye!!!')
            break

        else:
            print()
            print('Invalid input :(')
            print()
            print('Value can\'t be Negative')
            print()
            print('Try Again')
            print()

        again = input('Would you like to print again(n -> no): ')
        if again == 'n' or again == 'N':
            print()
            print('Thanks for using :)')
            print()
            print('Bye!!!')
            break

    except ValueError:
        print()
        print('Invalid input :(')
        print()
        print('Try Again')
    
#code ends here
