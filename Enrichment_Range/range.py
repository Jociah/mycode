num_bottles = int(input("Enter the number of bottles of beer: "))
if num_bottles > 100:
    print("Sorry, you can't count down from more than 100 bottles of beer.")
else:
    for i in range(num_bottles, 0, -1):
        print(f"{i} bottles of beer on the wall!")
        print(f"{i} bottles of beer! You take one down, pass it around!")
        print(f"{i-1} bottles of beer on the wall!")
