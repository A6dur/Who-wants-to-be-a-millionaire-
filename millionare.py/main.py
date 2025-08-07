questions = [
    [ "What is the capital of Australia?","Sydney","Canberra"," Melbourne"," Perth",2] , 
    [ "Who discovered gravity?","Albert Einstein","Isaac Newton"," Galileo Galilei"," Stephen Hawking",2] , 
    [ "What is the largest planet in our solar system?","Earth","Mars"," Jupiter"," Saturn",3] , 
    [ " Which country is known as the Land of the Rising Sun?"," China","South Korea"," Japan"," Thailand",3] , 
    [ "What is the chemical symbol for water?"," O₂","H₂","  CO₂","  H₂O",4] 
]

prizes = [100000,200000,300000,400000,500000 ] 
i = 0 

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Enter the option : 1 for a , 2 for b ,3 for c , 4 for d : \n"))
    if(question[5] == a) :
        print("Correct answer")
        print(f"prize = {prizes[i]}")
        i+=1
    else : 
        print("Wrong answer better luck next time")
        print("prize = 0")
        break
