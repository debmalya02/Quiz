from question import Question

question_promt = [
    "\nThe Battle of Plassey was fought in \n(a) 1757 \n(b) 1782 \n(c) 1748 \n(d) 1764\n",
    "\nGolden Temple is situated in \n(a) New Delhi \n(b) Agra \n(c) Amritsar \n(d) Mumbai\n",
    "\nThe words 'Satyameva Jayate' inscribed below the base plate of the emblem of India are taken from \n(a) Rigveda \n(b) Satpath Brahmana \n(c) Mundak Upanishad \n(d) Ramayana\n",
    "\nWhere did India play its 1st one day international match? \n(a) Lords \n(b) Headingley \n(c) Taunton \n(d) The Oval\n",
    "\nHitler party which came into power in 1933 is known as \n(a) Labour Party \n(b) Nazi Party \n(c) Ku-Klux-Klan \n(d) Democratic Party\n",
]

questions = [
    Question(question_promt[0], "a"),
    Question(question_promt[1], "c"),
    Question(question_promt[2], "c"),
    Question(question_promt[3], "b"),
    Question(question_promt[4], "b"),
]

def main():
    name = input("Enter your name : ")
    print(f"\nHi {name}, This is a quiz contest, press enter to start the contest")
    run_test(questions)
    rating = input(f"\n{name} Please give a rating from 1 to 10 : ")
    if rating >= "5" :
        print(f"\nThank you very much {name}:)\n")
    else:
        print("\nWe will try to improve :(\n")
    comment = input("Please leave a comment\n")
    file_comment(comment,name,rating)
    print(f"Thank you {name}, Goodbye")

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.promt)
        if answer == question.answer:
            score += 1
            print("\nCORRECT")
        else:
            print(f"\nWrong\nCorrect answer is : {question.answer}")
    print(f"\nYou have got {score}/{len(question_promt)} correct answers")

def file_comment(comments,name,ratings):
    with open("comments.txt",'a') as f:
        f.write(f">> Name : {name} \nRating : {ratings} \nComment : {comments}\n")


main()