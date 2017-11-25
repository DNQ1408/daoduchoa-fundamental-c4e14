# Boolean is computer logic. Boolean values are true and false, both of which are produced by Boolean expression
# 3 example:
#             >>> 1==1
#             True
#             >>> "Good"+"job" == "Goodjob"
#             True
#             >>> 1+2 == 1000
#             False
#
# Flow chart is a step-by-step graphical representation of clauses and statements
#
# Nested conditional is the conditional which are in a branch of / within another conditional
gra = float(input("Your grade for this homework?"))
if gra >= 9:
    if gra == 10:
        print("Oh year! H'about last time?")
    elif gra <=9.5:
        print("Ok! Why?")
else:
    if gra < 8.5:
        print("Really? Plz tell me why?")
print("Thank you for grading me!")
