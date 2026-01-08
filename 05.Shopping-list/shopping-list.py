import os

def shopping_list():
    """
    Shopping List - adds, lists, and deletes items using CRUD
    """
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
            choice_d = input('Choose an item to delete: ')
            
            try: 
                index = int(choice_d)
                del user_items[index]
                print('Item deleted!')
            except ValueError:
                print('Please enter a valid integer number.')
            except IndexError:
                print('This index does not exist in the list.')
            except Exception:
                print('An unknown error occurred. Please try again.')

if __name__ == '__main__':
    shopping_list()
