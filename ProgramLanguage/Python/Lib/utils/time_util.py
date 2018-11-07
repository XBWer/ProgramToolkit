# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：		time_util
   Description :	
   Author :			bowenxu
   Create date：		12/9/18
   Update date:		12/9/18
-------------------------------------------------
"""

def time_record(fun):
    import time
    import datetime
    print('start time : %s'%datetime.datetime.now())
    fun()
    print('end time : %s'%datetime.datetime.now())

@time_record
def fun():
	'''
	This is an example to use @ to record start and end time for a specific function
	'''
	# do something here





def get_current_time():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
