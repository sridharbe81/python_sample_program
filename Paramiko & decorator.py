# #Paramiko
# import paramiko:
#
# router = paramiko.SSHClient()
#     router.load_system_host_keys()
#     router.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     router.connect(host, username=user, password=passwd, allow_agent=False, look_for_keys=False)
#     print('Router SSH connected')
#     return router

#Decorator
import time
import datetime

def decorator(original_function):
    print("Started ")
    def new_function(*args,**kwargs):
        before = datetime.datetime.now()
        x = original_function(*args,**kwargs)
        print(x)
        time.sleep(5)
        after = datetime.datetime.now()
        print("Elapsed Time = {0}".format(after-before))
        return x
    print("End")
    return new_function

@decorator
def add(x,y):
    return x+y
