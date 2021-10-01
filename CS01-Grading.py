A = int(input("accumulated score : "))
B = int(input("mid exam score : "))
C = int(input("final exam score : "))
D = A + B + C
if(90<=D<=100):
    print('Grade A+')
elif(80<=D<=89):
    print('Grade A')
elif(75<=D<=79):
    print('Grade B+')
elif(70<=D<=74):
    print('Grade B')
elif(65<=D<=69):
    print('Grade C+')
elif(60<=D<=64):
    print('Grade C')
elif(55<=D<=59):
    print('Grade D+')
elif(50<=D<=54):
    print('Grade D')
elif(0<=D<=49):
    print('Grade F')