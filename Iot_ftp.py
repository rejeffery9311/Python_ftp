from ftplib import FTP
import datetime
import schedule
import time

class setUp:
    def __init__(self)
def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print("Error")


def job():
    now = datetime.datetime.now()
    if now.month<10:
        month='0'+str(now.month)
    else:
        month=str(now.month)

    if now.day<10:
        day='0'+str(now.day) 
    else:
        day=str(now.day)

    if now.hour<10:
        hour='0'+str(now.hour)
    else:
        hour=str(now.hour)
  


    ftp = FTP('192.72.189.223') 
    ftp.login('admin','Admin')

    Csv_folder='/LOG/Folder1/'+str(now.year)+month
    File_name=month+day+'_'+hour

    print('Will download:'+File_name)

    ftp.cwd(Csv_folder) 
    data = []
 
    ftp.dir(data.append)
 
 
    for line in data:
        print("-", line)
    getFile(ftp,File_name+'.csv')
    ftp.quit()
    ftp.close()

