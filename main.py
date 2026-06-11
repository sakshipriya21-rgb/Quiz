import time
questions=[
    {
        "question":"Who invented the differential and integral calculus?",
        "options":["A.Albert Einstein\n","B.Sir Isaac Newton\n","C.Kepler\n","D.Aristotle"],
        "answer":"B"
    },
    {
        "question":"Who was the first person to win two Nobel Prizes and that too in completely different domains?",
        "options":["A.Madam Marie Curie\n","B.Alexander Fleming\n","C.Huygens\n","D.Pythagoras"],
        "answer":"A"
    },
    {
        "question":"What does 'interstellar space' mean?",
        "options":["A.The space between the earth's crust and mantle\n","B.The space between two stars\n","C.The space between two planets\n","D.Any space in this universe"],
        "answer":"B"
    },
    {
        "question":"Which scientist believed that there were irrigation canals on Mars which he believed were built by intelligent species?",
        "options":["A.Albert Einstein\n","B.Percival Lowell\n","C.Edwin Aldrin\n","D.Pythagoras"],
        "answer":"B"
    },
    {
        "question":"How many microbiology experiments were sent to the surface of the Mars by the Viking Mission?",
        "options":["A.5\n","B.8\n","C.2\n","D.3"],
        "answer":"D"
    },
    {
        "question":"Who invented the microscope?",
        "options":["A.Galileo\n","B.Leeuwenhoek\n","C.Huygens\n","D.Darwin"],
        "answer":"B"
    },
    {
        "question":"What are the four moons of Jupiter called which were the first to be discovered?",
        "options":["A.Jovian Satellites\n","B.Europa\n","C.Galilean Satellites\n","D.Io"],
        "answer":"C"
    },
    {
        "question":"What is the estimated age of the Solar System?",
        "options":["A.1 billion years\n","B.2.3 billion years\n","C.6.3 billion years\n","D.4.6 billion years"],
        "answer":"D"
    },
    {
        "question":"Which of the following is not a planet of the solar system?",
        "options":["A.Neptune\n","B.Pluto\n","C.Titan\n","D.Both B and C"],
        "answer":"D"
    },
    {
        "question":"Which was the first country to complete a successful mission to the Mars in its first attempt?",
        "options":["A.India\n","B.USA\n","C.Japan\n","D.China"],
        "answer":"A"
    }
]
score=0
count=1
timee=0
print("Let's start the QUIZ!")
print("You have got 15 seconds per question!")
for q in questions:
    print("Q",count,".",q["question"])
    print(q["options"])
    start=time.time()
    userInput=input("Enter your answer :").upper()
    end=time.time()
    print("You took",end-start,"seconds time.")
    timee+=end-start
    if end-start>15:
        print("Time is up!")
        continue
    else:
        if(userInput==q["answer"]):
            score+=1
            print("CORRECT ANSWER!")
        else:
            print("WRONG ANSWER!")
    count+=1
print("Your score is :",score,"/10")
print("Total time taken is :",timee)