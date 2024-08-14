eng = int(input("please enter the eng marks: "))
sci = int(input("please enter the sci marks: "))
mat = int(input("please enter the mat marks: "))

total_percentage = (100*(eng + sci + mat))/300

if(total_percentage>=40 and eng>=33 and sci>=33 and mat>=33):
    print("student is passed the exam and his/her percentage is: ", total_percentage)

else:
    print("student is failed the exam")


