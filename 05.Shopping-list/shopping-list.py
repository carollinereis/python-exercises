import os

def shopping_list():
    user_items = [ ]

    while True:
        user_choice = input('Please choose [a]dd, [d]elete, [l]ist: ').strip().lower()
        os.system('clear')

        if user_choice == 'a':
            choice_a = input('Enter an item: ')
            user_items.append(choice_a)
            print(user_items)
        elif user_choice == 'l':
            for item in enumerate(user_items):
                index, name = item
                print(index, name)

        elif user_choice == 'd':
            choice_d = int(input('Choose an item to delete: '))
        
            if choice_d >= len(user_items) or choice_d < 0:
                print("This item doesn't exist.")
            else:
                del user_items[choice_d]
                print('Item deleted!')
        else:
            print('Oops, please choose a, d, or l.')

if __name__ == '__main__':
    shopping_list()
