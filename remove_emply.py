#  كود لي حذف الملفات الفرغة من الديسك
import os

for dirpath , dirnames , filennames in os.walk('.'):
    if not dirnames and not filennames:
        os.rmdir(dirpath)
        