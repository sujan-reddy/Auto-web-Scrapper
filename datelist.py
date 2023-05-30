import datetime



K = 370
res = []
start = datetime.date(2003,1,1)
for day in range(K):
	date = (start + datetime.timedelta(days = day)).strftime('%d-%m-%Y')
	res.append(date)


start = datetime.date(2004,1,1)
for day in range(K):
	date = (start + datetime.timedelta(days = day)).strftime('%d-%m-%Y')
	res.append(date)

start = datetime.date(2002,1,1)
for day in range(K):
	date = (start + datetime.timedelta(days = day)).strftime('%d-%m-%Y')
	res.append(date)


    
date_list=[i.replace('-','') for i in res]

date_list_chunks = [date_list[x:x+100] for x in range(0, len(date_list), 100)]