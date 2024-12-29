#import datetime
import os

#print(dir(os))
#print(os.getcwd()) 
#print(os.listdir())

#كود تغيير مسار الملف 
#os.chdir('django/')

#انشاء مجلد جديد
#os.mkdir('code')

#لو بدي انشاء مجلد في مسار موعين
#os.makedirs('Python/Basics')

#حذف ملف 
#os.rmdir('code')
#os.removedirs('Python/Basics')

#اذا بدي ابدل اسم مجلد او ملف 
#os.rename('test.txt' , 'python.txt')

#اذا بدي اعرف حالة ملف 
#print(os.stat('test.txt').st_size)
#print(datetime.fromtimestamp(os.stat('test.txt').st_mtime))


#اذا بدي طبع جميع مسارات الملفات والمجلد

#for dirpath , dirnames , filennames in os.walk('.'):
    #print(filennames)

#كيف العرف اسم يوزر 
#print(os.environ.get('HOME')) 

#path = 'test/test'
#print (os.path.split(path))
#نوع الملف 
#print (os.path.splitext(path))

#لو انا بدي اروح على مسار معين بدي اشوف اذا موجود او لا
#print(os.path.exists(path))

#اذا بدي اعرف هذا ملف او مجلد   

#print(os.path.isfile('test.txt'))

#print(os.path.isdir('test'))

#path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#path2 = os.path.dirname(os.getcwd()) #1

#print(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))
#print(path2)
#print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#اذا بدي انسخ ملف مكان

#import shutil

#shutil.copy('python.txt' , 'test/')

#shutil.move('python.txt' , 'test/')

#shutil.copytree('test' , 'test2')

#-----------------------------------

import schedule
import time

def print_path():
    for dirpath , dirnames , filennames in os.walk('.'):
        print(filennames)



schedule.every(1).minutes.do(print_path)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
#schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
  



