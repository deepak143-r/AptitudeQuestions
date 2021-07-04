weekList = ["Sunday", "Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday"]

monthList = [0,3,3,6,1,4,6,2,5,0,3,5]

def getYearCode(year):
	if year in range(1600, 1699):
		return 6
	elif year in range(1700, 1799):
		return 4
	elif year in range(1800, 1899):
		return 2
	elif year in range(1900, 1999):
		return 0
	elif year in range(2000, 2099):
		return 6

def calculate(dd, mm, yyyy):
	yy = int(str(yyyy)[-2:])
	yydiv = yy//4
	
	addUp =  yy+yydiv+dd+monthList[mm-1]+getYearCode(yyyy)

	modUp = addUp % 7
	return modUp

def dayOfWeek(dd, mm, yyyy):
	return weekList[(int(calculate(dd, mm, yyyy)))]

dd=int(input("enter the day    : "))
mm=int(input("enter the month  : "))
yyyy=int(input("enter the year : "))
#print(yyyy%4)
print(str(dd)+" / "+str(mm)+" / "+str(yyyy)+" was a "+dayOfWeek(dd,mm,yyyy))