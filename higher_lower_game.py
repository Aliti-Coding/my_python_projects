from data.higher_lower_data import data, vs, logo
import random

score = 0

#select two random items from the list
while True:
    if score > 0:
        print(f"You're right! Current score: {score}")
    random_1 = random.choice(data)
    random_2 = random.choice(data)

    print(f"Compare A: {random_1['name']}, a {random_1['description']}, from {random_1['country']}.")
    print(vs)
    print(f"Against B: {random_2['name']}, a {random_2['description']}, from {random_2['country']}.")

    random_1_follower = random_1['follower_count']
    random_2_follower = random_2['follower_count']
   
    input_user = input("who has more followers, A or B?:  ").strip().upper()
    if input_user == 'A':
        if random_1_follower > random_2_follower:
            score += 1
        elif random_1_follower < random_2_follower:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
          
    elif input_user == 'B':
        if random_2_follower > random_1_follower:
            score += 1 
        elif random_2_follower < random_1_follower:
            print(f"Sorry, that's wrong. Final score: {score}")
            break         
 





#compare two idx to each other. wich one has more followers

#if you guess correct score +  1, else gameover 




