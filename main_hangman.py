
import random
import artforhangman
import imdb

stages = artforhangman.stages
logo = artforhangman.logo

ia = imdb.IMDb()
search = ia.get_top250_movies()
movies = []
for i in range(1,10):
    movies.append(search[i]['title'].lower())



display = []
wrong_list = []
word_list = movies
lives = 6
end_of_game = False

chosen_word = random.choice(word_list)
dashcount=len(chosen_word)


for i in range (dashcount):
    display.append("_")
    


# ---------------------------------------------------

def displayer():
    # print(display)
    print(f"{' '.join(display)}")

def dashreplacer(pos):
    display[pos] = guess
    

def checker():
    wrong = True
    global lives
    global wrong_list
    # global stages
    for i in range(dashcount):
        
        if(guess == chosen_word[i]):
            dashreplacer(i)
            
            wrong=False


    if(wrong == True):
        lives-=1
        wrong_list.append(guess)
        

        
for i in range (dashcount):
    if(" " == chosen_word[i]):
        display[i] = " "      
print(logo)   
      
while not end_of_game:

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # print(f"Lives ramineing: {lives}")
    print(stages[lives])  
    
    displayer()
    print("\n")
    guess = input("Enter a choice: ").lower()
    if(guess not in display and guess not in wrong_list):
        checker()
    else: 
        print("Already checked")
        # displayer()
    
    if "_" not in  display:
        end_of_game = True
        print(f"YOU WIN, The word was {chosen_word.upper()}")
    if lives ==0:
        
        end_of_game = True
        print(f"You lose, The word was {chosen_word}")













