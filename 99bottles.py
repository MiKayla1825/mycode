def bottles_of_beer(num):
    if num == 1:
        return "1 bottle of beer on the wall!"
    elif num == 0:
        return "No more bottles of beer on the wall!"
    else:
        return f"{num} bottles of beer on the wall!"


def song(num_bottles):
    if num_bottles > 100:
        print("You can't count down from more than 100 bottles of beer!")
        return
    for i in range(num_bottles, -1, -1):
        if i == 0:
            print(bottles_of_beer(i))
        else:
            print(bottles_of_beer(i), f"{i} bottles of beer! You take one down, pass it around!",
                  bottles_of_beer(i - 1))


num_bottles = int(input("How many bottles of beer are you counting down from? "))
song(num_bottles)

