name = input ("Type Your name: ")
print(
"""                                                                                                                                               
       +--------------------------------------------------+        
       |Welcome", name, "to this adventure                |      
       |You are playing as Alice from Alice in Wonderland.|     
       |She needs to get back to her original size,       |      
       |but the mysterious cat says she needs to take a   |   
       |specific blue potion found in a house deep in the |  
       |woods. You have 100 minutes to take the correct   |  
       |      potion or else she'll be stuck forever.     | 
       |               Good Luck!                      |  
       +-----------------------------------------------+ 
                                                           """)
time = 100
while True:
    q1 =input("You wake up on a dirt road. Which way would you like to go?:(left/right)")
    if q1.lower() == "left":
        q11 = input("You come across an odd creature stopping your path. A small dragon but it has dragonfly wings like the insect, you can walk around it or swat it out your way:(swat/walk)")
        if q11.lower() == "swat":
            q12 = ("The dragonfly wakes up in a fuss. Do you fight or keep still:(fight/still)")
            if q12.lower() == 'fight':
                time -= 25
                print('You manage to fend off the dragonfly, but not without taking some damage.')
                break
            elif q12.lower() == 'still':
                print('You try to keep still and act like it was not you but the dragonfly knows it was. he takes a big bite out of your leg before you reach the other side.')
                time -=22
                break
            else:
                print("error")
        elif q11.lower() == "walk":
            q13 = input("A caterpillar smoking on a mushroom makes eye contact with you. Do you approach it or ignore?")
            if q13.lower() == 'ignore':
                time -=25
                print('The smoke you walk through makes you sluggish and move slower, but you are on the right path.')
                break
            elif q13.lower() == 'approach':
                time -=10
                print('Good choice! The caterpillar knows a shortcut and tells you the route.')
                break
            else:
                print("error")
        else:
            print("error")
    elif q1.lower() == "right":
        q14 = input('You come across a large mountain. Do you go over or around:(over/around)')
        if q14.lower() == 'over':
            q15 = input('As you climb, you encounter a sleeping boar of sorts. Do you want to appraoch it?(yes/no)')
            if q15.lower() == 'yes':
                time -=10
                print('You have made a new friend! You are very careful when aproaching and the boar decides not to eat you for lunch. It has such soft fur!')
                break
            elif q15.lower() == 'no':
                time -=27
                print('taking a long climb over the mountain to get away from the boar has made the expedition harder. You notice you are quite exhausted because of it. But you must move on.')
                break
            else:
                print("error")
                
        elif q14.lower() == 'around':
            q16 = input('Oh my god! What a strangely large lizard! Do you try to intimidate it or do you want to fight?(intimidate/fight)')
            if q16.lower() == 'fight':
                time-=20
                print('you manage to find a stick and impale the lizard in the chest. The lizard bleeds out.')
                break
            elif q16.lower() == 'intimidate':
                time-=26
                print('big mistake. The lizard snaps at you twice. Do you continue to fight or do you try to run away(stay/run)')
                break
            else:
                print("error")
        else:
                print("error")
    else:
        print("error")
                   
                      
def time_check():
    if time > 9:
            game_over = print("You drank the potion with time to spare! Thank you for playing!")
            quit()
    elif time < 1:
            game_over = print("You are out of time, " + name + ". Alice is doomed to be like this forever...")
            quit()
    else:
            game_over = print("You made it just in time! Next time, dont be so curious. You know the saying, curiosity killed the cat!")
            quit()  
                      
                      
if time < 20:
    answer = input('Youve finally made it on campus... And with a few minutes left to spare! However, You start to feel a dark presence in the air. All of a sudden, Radagon from Elden Ring appears. Choose either magic, fire, lightning, or holy:')
    if answer.lower() == 'magic':
        print('You are able to defeat him.')
        time -=15
        time_check()
    elif answer.lower() == 'fire':
        print('good choice! He seems to be weak to fire so you beat him quicker.')
        time -=10
        time_check()
    elif answer.lower() == 'lightning':
        print('You are able to defeat him.')
        time -=15
        time_check()
    elif answer.lower() == 'holy':
        print('Oh no! It seems as though he is resistant to holy!')
        time -=20 
        time_check()

if time > 20 and time < 60:
    q41 = input('Scrappy finds himself walking in a canyon and see a plumber and little pink warrior fighting off aliens from a spaceship overlooking the canyon. They introduce themselve as Kirby and Mario and desire Scrappys help but they can only go with one of the warriors. Does Scrappy choose Mario or Kirby?(Mario/Kirby)')
    if q41.lower().startswith('mar'):
        q42 = input('The aliens have stolen the Big Owl Bus. Mario and Scrappy get on Go-Karts in a hot pursuit. Which Kart do you choose?')
        q43 = input("You hit an item box. What item do you receive?(flower, shell, blooper)")
        if q43 == 'flower':
            time -=25
            print('The aliens throw a blue shell and it hits Mario busting two of his tires. Mario throws a fire flower and tells Scrappy to eat it imediately. Scrappy turns into Fire Scrappy and continues to chase the Owl Bus. Scrappy throws a fireball that burns the aliens on top of the bus. Scrappy retrives the Big Owl Bus.')
        elif q43 == 'shell':
            time -=30
            print('Just your luck! its a blue shell! The aliens throw back a banana and it hits Mario spiraling his car out of control. You come to the rescue and throw the blue shell at the aliens, exploding them. Scrappy retrives the Big Owl Bus.')
        elif q43 == 'blooper':
            time -=35
            print('The aliens throw a blue shell and it hits Mario busting two of his tires. Mario activates the blooper, blinding the aliens. Nows your chance! You take back the Big Owl Bus and drive to campus.')
    else:
        time -=30
        print ('Kirby takes Scrappy on his star straight to the spaceship to potentially destroy it. Kirby fights off as many aliens as possible but is overwhelmed. Kirby throws a sword towards Scrappy and he catches it. Scrappy enters a room to find the greatest swordsman know as Meta Knight. They fight for awhile and Scrappy best Meta Knight. Scrappy soon finds the control room and finds the self destruct button. Scrappy and Kirby escape the spaceship with only seconds to spare.')
if time > 60 and time < 80:
    q69 = input('you are left in a dark forest alone with your thoguths. Do you walk further in the forest or turn back?(walk/turn)')
    if q69.lower().startswith('w'):
        time -=35
        print('Scrappy finds a women tending to her garden in the woods. She gestures you over and gives you apples since she can tell that he is tired. She has a cabin nearby and gives you a phone to call for help to leave the forest')
    else:
        time -=40
        print('you manage to get out of the forest and find the police')
if time > 80:
    q81 = input('As you are running through the forest you trip over the portal gun and it fires a portal which you fall into. you sudenly find yourself in the marvels new your city. Do you walk towards avengers tower or the sanctum sanctorum?(Avengers Tower/Sanctum Sanctorum)')          
    if q81.lower().startswith('Ave'):         
        q82 = input('You find Captain America and Iron Man onlooking a giant army of symbiotes about to attack the city. Who dod you talk to?(iron/captain)')
        if q82.lower.startswith('ir'):
            q83 = input('Iron Man offers to give you one of his suits to help fight the symbiotes. which one do you choose?(7/15/39)')
            if q83 == '7':
                time-=40
                print('Ahh a classic! good choice. Scrappy and Iron Man fight off the symbiotes threatning the city. Iron Man uses technology inspired by the space stone to send scrappy back to his world.')
            elif q83 == '15':
                time -=45
                print('That armor is useless against them! However, Scrappy and Iron Man fight off the symbiotes threatning the city. Iron Man uses technology inspired by the space stone to send scrappy back to his world.')
            elif q83 == '39':
                time-=39
                print('This armor has incredible cosmic strength! Scrappy and Iron Man fight off the symbiotes threatning the city EASILY. Iron Man uses technology inspired by the space stone to send scrappy back to his world.')
        else:
            time-=41
            print('He looks at Scrappy and says that their is no time to waste and gives him a shield. Scrappy and Captain America fight off the symbiotes threatning the city. Captain America uses technology inspired by the space stone to send scrappy back to his world.')  
    else:
        time-=40
        print('You find Doctor Strange and Wong seeing the symbiotes ooze through the city. Wong sees that Scrappy is strong and magically inclined and gives him a sling ring. Scrappy, Doctor Strange, and Wong all open up a huge portal that sends the symbiote army into the sun. Doctor Strange opens up a portal to send you back to you back to your world.') 
