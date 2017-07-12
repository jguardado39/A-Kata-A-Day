class Solution():
	"""
	https://www.codewars.com/kata/586a1af1c66d18ad81000134	

	Introduction

	In the United Kingdom, the driving licence is the official document which authorises 
	its holder to operate various types of motor vehicle on highways and some other roads 
	to which the public have access. In England, Scotland and Wales they are administered 
	by the Driver and Vehicle Licensing Agency (DVLA) and in Northern Ireland by the Driver 
	& Vehicle Agency (DVA). A driving licence is required in the UK by any person driving a 
	vehicle on any highway or other road defined in s.192 Road Traffic Act 1988[1] irrespective 
	of ownership of the land over which the road passes, thus including many which allow 
	the public to pass over private land; similar requirements apply in Northern Ireland 
	under the Road Traffic (Northern Ireland) Order 1981. (Source Wikipedia)


	Task

	The UK driving number is made up from the personal details of the driver. The 
	individual letters and digits can be code using the below information


	Rules

	1–5: The first five characters of the surname (padded with 9s if less than 5 
	characters)

	6: The decade digit from the year of birth (e.g. for 1987 it would be 8)

	7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 
	51–62 instead of 01–12)

	9–10: The date within the month of birth

	11: The year digit from the year of birth (e.g. for 1987 it would be 7)

	12–13: The first two initials of the first names, padded with a 9 if no middle name

	14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the 
	first 13 characters in common. We will always use 9

	15–16: Two computer check digits. We will always use "AA"


	Your task is to code a UK driving license number using an Array of data. The Array 
	will look like

	
	data = ["John","James","Smith","01-Jan-2000","M"]

	
	Where the elements are as follows


	0 = Forename

	1 = Middle Name (if any)

	2 = Surname

	3 = Date of Birth (In the format Day Month Year, this could include the full Month 
	ame or just shorthand ie September or Sep)

	4 = M-Male or F-Female	


	You will need to output the full 16 digit driving license number.

	"""

	def __init__(self):
		pass

	def driver(data):    
	    dict = {
	        'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
	        'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'
	        }

	    surname, decade, gender, month, date, last_number_of_year = data[2].upper(), data[3][-2], data[4], data[3][3:6], data[3][0:2], data[3][-1]
	    
	    if len(surname) < 5:
	        surname = str(surname) + (5- len(surname)) * (str(9))
	    surname = surname[0:5]

	    month = dict.get(month)
	    if gender == 'F':
	        month = str(int(month) + 50)
	    month = month

	    middle_name = data[1]
	    if len(middle_name) == 0:
	        middle_name = '9'
	    initial = data[0][0] + middle_name[0]

	    return surname + decade + month + date + last_number_of_year + initial +'9AA'

	def driver_alt(data):
		f, m, l, dob, s =  [w.upper() for w in data]
		mon = '%02d' % ('JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC'.index(dob[3:6]) / 3 + (1 if s == 'M' else 51))
		return l[:5].ljust(5, '9') + dob[-2] + mon + dob[:2] + dob[-1] + f[0] + (m[0] if m else '9') + '9AA'

if __name__ == '__main__'
	sol = Solution()