
questions=["What is the powerhouse of the cell?",
"What is the Capital of Pakistan?",                     #Questions
"What is 5^2?"]                                     

options=[]              #Empty list for Options

count=0
reward=0

while(count<len(questions)):                    #Play until all Questions in the list have been asked 
    
    if(count==0):
        options.append("1. Cell")
        options.append("2. Muscle")             #Options for Q1
        options.append("3. Mitchondria")
        options.append("4. Hippocampus")
        correctans=3
    
    elif(count==1):
        options.append("1. Karachi")
        options.append("2. Islamabad")          #Options for Q2
        options.append("3. Rawalpindi")
        options.append("4. Lahore")
        correctans=2
    
    elif(count==2):
        options.append("1. 25")
        options.append("2. 525")
        options.append("3. 5625")               #Options for Q3
        options.append("4. 35")
        correctans=1

    print("\n", questions[count])               #Printing Question
    print(options[:], "\n")                     #printing options according to question
    
    ans=int(input("Enter your answer: "))
    while(ans>4):                               #Answer Should be 1,2,3 or 4
        print("Invalid choice")
        ans=int(input("Please Make valid choice: "))
    

    if(ans==correctans):
        reward+=10000                                       #Adding Reward
        print("Correct Answer \nYou have won $", reward)
    else:
        print("Incorrect Answer \nYou lost the game")
        print("Your Total Reward is ", reward)                      
        break

    options.clear()                 #Clearing Options list

    count+=1


