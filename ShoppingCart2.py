from IPython.display import clear_output

class Shopping():
    def __init__(self):
        self.shop_list = []
        print("Welcome!")
        print("You can add, delete, see items in list,")
        print("or even quit shopping.")
        print()
        print("please write add / delete / see / quit ")


    def add(self):
        item = input("Type an item: ")
        self.shop_list.append(item)

    def delete(self):
        item = input("Type an item: ")
        if item in self.shop_list:
            self.shop_list.remove(item)
        else:
            print("Type again!")

    def see(self):
        if len(self.shop_list) == 0:
            print("The cart is empty!!")

        for shop in self.shop_list:
            print(shop)


my_shopping = Shopping()

while True:
    select = input("What will you choose - add, delete, see, quit: ")
    if select == "add":
        my_shopping.add()

    elif select == "delete":
        my_shopping.delete()

    elif select == "see":
        my_shopping.see()

    elif select == "quit":
        break

    else:
        print("Wrote wrong, try again!")
