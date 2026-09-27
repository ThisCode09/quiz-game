print("Hey welcome to the quiz game")

choices =["1.Start game","2.View Score","3.Exit"]
qAs = {"CPU full form": "Central processing unit","How many strings in a guitar ?":"6"}
c=0
while True:
    for i in choices:
        print(i)
    inp = int(input("\nEnter your choice : "))
    print("\n")
    if inp==1:
        for j in qAs.keys():
            ans = input(f'{j} ')
            if ans==qAs[j]:
                print("Correct Answer")
                c+=1
                if j==list(qAs)[-1]:
                    print(f"Game has ended with a score of {c}/{len(qAs)}")
            else:
                print("Incorrect Answer")       
    elif inp==2:
        print(c)
    elif inp==3:
        break
    else:
        print("Invalid choice")
