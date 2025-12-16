amount=int(input("please enter the amount: "))
note_100=amount//100
note_50=(amount%100)//50
note_10=((amount%100)%50)//10
print("notes of 100:", note_100)
print("notes of 50:",note_50)
print("note of 10:", note_10)
