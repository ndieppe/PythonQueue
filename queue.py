import time

queue = ["Pineapple", "apple", "mango", "watermelon", "grape", "pear"]
fPointer = 0
rPointer = 5
carryOn = True
element = 0


def enqueue(rear,item,element,front):
    if rear == 5 and "." in queue:
        added = False
        while added == False:
            if queue[element] == ".":
                queue[element] = item
                rear = element
                element = 0
                added = True
                return rear
            else:
                element += 1
    elif front-rear == 1 or rear-front == 1 or rear == 5:
        print("Error: queue is full...")
        return rear
    else:
        rear += 1
        queue[rear] = item
        return rear

def dequeue(front, rear):
    if front > 5:
        front = 0
    if rear < 0:
        print("Error: queue is empty...")
        return front, 0
    else:
        dequeuedItem = queue[front]
        queue[front] = "."
        front += 1
        return front, dequeuedItem
#main program -------------------------------------------------------------------------------------------------
while carryOn == True:
    z=0
    print(" ___________")
    for item in queue:
        if z == fPointer:
            print(f"f-->| {queue[z]}")
        elif z == rPointer:
            print(f"r-->| {queue[z]}")
        else:
            print(f"    | {queue[z]}")
        z+=1
    time.sleep(1)
    print("Enter:\nEnqueue if you want to add an item to the queue(1)\nDequeue if you want to remove the item from the front of the queue(2)\nEnd if you want to end the program(3)")
    choice = int(input("\nEnter your decision: ").title())
    if choice == 2:
        fPointer, dequeuedItem = dequeue(fPointer, rPointer)
    elif choice == 1:
        item = input("Enter item you want to enqueue: ")
        rPointer = enqueue(rPointer,item,element,fPointer)
    elif choice == 3:
        carryOn = False
        print("\nHave a good day")
    else:
        print("Please try again.")
    print("-------------------------------------------------------------------------")