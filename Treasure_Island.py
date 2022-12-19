#Welcome to trasure Island. 
#Your mission is tofind the trasure

q1 = input("left or right: ").lower().strip()

if q1 == "left":
    q2 = input('swim or wait: ').lower().strip()
    if q2 == "wait":
        q3 = input('wich door? Red, Blue or Yellow: ').lower().strip()

        if q3 == "yellow":
            print("you win!")
        else:
            print("game over") 

    else:
        print('Game over')   

else:
    print("Game over")

