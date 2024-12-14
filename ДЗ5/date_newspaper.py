from datetime import datetime

the_Moscow_Times = datetime.strptime("Wednesday, October 2, 2002", "%A, %B %d, %Y")
the_Guardian = datetime.strptime("Friday, 11.10.13", "%A, %d.%m.%y")
Daily_Newspaper = datetime.strptime("Thursday, 18 November 1975", "%A, %d %B %Y")

print(the_Moscow_Times)
print(the_Guardian)
print(Daily_Newspaper)
