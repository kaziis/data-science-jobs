import datetime

date = ['Tue, 23 Nov 2021 22:45:32 GMT', '2023-03-04T12:50:08', '726, 734', 'Tue, 30 Nov 2021 22:45:32 GMT']

for date in date:
    try:
        try:
            format = '%a, %d %b %Y %H:%M:%S %Z'
            new = datetime.datetime.strptime(date, format)
        except:
            format = '%Y-%m-%dT%H:%M:%S'
            new = datetime.datetime.strptime(date, format)
    except:
        new = None
    print (new)
print ()
print (datetime.datetime.now().strftime("%m%d%Y"))