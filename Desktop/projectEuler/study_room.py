from urllib import urlopen
import re


def findrm(date,current_time):
	"""
	Legit inputs would be "12/01/2012" and "12:00 AM-12:30 AM".
	"""
	
	possible = {'12:00 AM-12:30 AM':1,'12:30 AM-1:00 AM':2,'1:00 AM-1:30 AM':3,'1:30 AM-2:00 AM':4,'2:00 AM-2:30 AM':5,'2:30 AM-3:00 AM':6,'3:00 AM-3:30 AM':7,
				'3:30 AM-4:00 AM':8,'4:00 AM-4:30 AM':9,'4:30 AM-5:00 AM':10,'5:00 AM-5:30 AM':11,'5:30 AM-6:00 AM':12,'6:00 AM-6:30 AM':13,'6:30 AM-7:00 AM':14,
				'7:00 AM-7:30 AM':15,'7:30 AM-8:00 AM':16,'8:00 AM-8:30 AM':17,'8:30 AM-9:00 AM':18,'9:00 AM-9:30 AM':19,'9:30 AM-10:00 AM':20,'10:00 AM-10:30 AM':21,
				'10:30 AM-11:00 AM':22,'11:00 AM-11:30 AM':23,'11:30 AM-12:00 PM':24,'12:00 PM-12:30 PM':25,'12:30 PM-1:00 PM':26,'1:00 PM-1:30 PM':27,'1:30 PM-2:00 PM':28,
				'2:00 PM-2:30 PM':29,'2:30 PM-3:00 PM':30,'3:00 PM-3:30 PM':31,'3:30 PM-4:00 PM':32,'4:00 PM-4:30 PM':33,'4:30 PM-5:00 PM':34,'5:00 PM-5:30 PM':35,
				'5:30 PM-6:00 PM':36,'6:00 PM-6:30 PM':37,'6:30 PM-7:00 PM':38,'7:00 PM-7:30 PM':39,'7:30 PM-8:00 PM':40,'8:00 PM-8:30 PM':41,'8:30 PM-9:00 PM':42,
				'9:00 PM-9:30 PM':43,'9:30 PM-10:00 PM':44,'10:00 PM-10:30 PM':45,'10:30 PM-11:00 PM':46,'11:00 PM-11:30 PM':47,'11:30 PM-12:00 AM':48}
                
	rooms = {31:'Room 201',12:'Room 202',32:'Room 203',33:'Room 204',34:'Room 205',10:'Room 207',3:'Room 251',4:'Room 252',5:'Room 253',51:'Room 254',8:'Room 261',
			9:'Room 262',36:'Room 263',15:'Room 362',39:'Room 363',38:'Room 364',53:'Room 404',23:'Room 415',24:'Room 421',49:'Room 422',25:'Room 430',
			26:'Room 431',42:'Room 432',43:'Room 433',44:'Room 435',28:'Room 436',29:'Room 437',40:'Room 438',50:'Room 451',16:'Room 452',41:'Room 453',18:'Room 461',
			19:'Room 462',20:'Room 463',21:'Room 464',46:'Room 601',52:'Room 603'}
	Result = {}
	for RoomID in rooms.keys():
		URL = 'https://tx.evanced.info/rice/lib/roomrequest.asp?command=getResultWin&vm=%d&res=wz19&SelectedDate=' + date + '&room=' + str(RoomID) + '&pointer=&rowchange=&entitytype=0&LangType=0&mm=1&timestamp=' 
    
		result = []           
		data = []

		dataset = urlopen(URL).read()
		print dataset
		p = re.compile(r'<.*?>')
		dataset = p.sub('', dataset) 
		p = re.compile(r'\s+')
		dataset = p.sub(' ', dataset)
	
		index = 0
		for index in range(len(dataset)):
			if dataset[index:index+4] == 'OPEN':
				for time in possible.keys():
					if time in dataset[index-18:index-1]:
						data.append(time)
			else:
				index += 1

		for time in data:
			if possible[time] > possible[current_time]:
				result.append(time)

		Result[rooms[RoomID]] = result
	
	return Result
    
