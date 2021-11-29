import datetime
import os
from . import pro_dir


def Log(text: str = None, sender: str = '控制台'):
    utc_dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    asia_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
    log_text = asia_dt.strftime('[%Y-%m-%d %H:%M:%S]') + ' <' + sender + '> ' + text
    file = os.path.join(pro_dir + '\\logs\\latest.log')
    file_dir = os.path.join(pro_dir + '\\logs')
    if not os.path.isdir(file_dir):
        os.mkdir(file_dir)
    if os.path.isfile(file):
        file_handle = open(file, mode='a', encoding="utf-8")
        file_handle.write(log_text + '\n')
    else:
        file_handle = open(file, mode='w', encoding="utf-8")
        file_handle.close()
        file_handle = open(file, mode='a', encoding="utf-8")
        file_handle.write(log_text + '\n')

    print(log_text)
