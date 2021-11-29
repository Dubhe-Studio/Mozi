from . import pro_dir
from threading import Thread
import os
import imp


def runPlugins():
    plugin_dir = pro_dir + "\\plugins"
    if not os.path.isdir(plugin_dir):
        os.mkdir(plugin_dir)
    x = os.listdir(plugin_dir)
    if '__pycache__' in x:
        x.remove('__pycache__')
    if '__init__.py' in x:
        x.remove('__init__.py')
    if '__main__.py' in x:
        x.remove('__main__.py')
    plugin_list = []
    for i in range(len(x)):
        if '.py' in x[i]:
            plugin_list.append(plugin_dir + '\\' + x[i])
        else:
            y = os.listdir(plugin_dir + '\\' + x[i])
            if '__init__.py' in y:
                y.remove('__init__.py')
            if '__main__.py' in y:
                y.remove('__main__.py')
            for n in range(len(y)):
                if '.py' in y[n]:
                    plugin_list.append(plugin_dir + '\\' + x[i] + '\\' + y[n])
    for i in range(len(plugin_list)):
        temp = plugin_list[i]
        function = imp.load_source('plugin-' + str(i), temp)
        try:
            Thread(target=function.onStart(), args=("Thread-"+str(i), i)).start()
        except:
            print("Error: unable to start thread")

