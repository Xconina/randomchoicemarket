#A veggie market
print("Welcome to the market!.")
import time
import random
def market():
    x = 0
    while x < 4:
        print("Here is what we have in stock today.")
        time.sleep(1)
       
        fruit = ["kiwi", "apple", "banana", "pear"]
        grain = ["bread", "pasta", "bagel", "rice"]
        veggies = ["carrot", "yam", "zucchini", "spinach"]
        drinks = ["soda", "bottled water", "iced tea", "coffee"]
        food = [veggies, fruit, grain, drinks]
        selection = (random.choice(food))

        for i in range(4):
            print(f"Item {i+1}: {selection[i]}")
        time.sleep(1)
        num = int(input("Which item would you like?"))

        print(f"Here is your {selection[num - 1]}. Enjoy!")
        x = x + 1
        
        
    print("Goodbye!")
market()
    
