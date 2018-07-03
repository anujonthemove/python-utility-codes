# packages = ['numpy']
# try:
# 	for package in packages:
# 		print package

# except ImportError, e:

# 	print(e)
# 	print("-- installing missing module(s) --")
#!sudo pip install psutil

# PROCNAME = "python.exe"
# 

import psutil
import time
from pprint import pprint as pp

# for proc in psutil.process_iter():
    # check whether the process name matches
    # if proc.name() == PROCNAME:
        # proc.kill()
    # print(proc)

# mem = psutil.virtual_memory()

# print mem


# import os
# import psutil
# process = psutil.Process(os.getpid())
# print(process.memory_info())



from operator import itemgetter
one_gb = 1024*1024*1024

while True:
	mem = psutil.virtual_memory()
	mem_free = (mem[1])
	print(str(mem_free/one_gb) + "GB")

	# pp([(p.pid, p.info['name'], p.info['memory_info'].rss) for p in psutil.process_iter(attrs=['name', 'memory_info']) if p.info['memory_info'].rss > 2*one_gb])
	p_list = [(p.pid, p.info['name'], p.info['memory_info'].rss) for p in psutil.process_iter(attrs=['name', 'memory_info'])]
	p_list = sorted(p_list, key=itemgetter(2), reverse=True)
	
	# pp(p_list)
	# print one_gb
	# print mem_free
	if mem_free < 2*one_gb:
		proc_num, _, _ = p_list[0]
		print "killing: " + str(proc_num)
		# print p_list[0], proc_num
		p = psutil.Process(proc_num)
		p.terminate()  

	# time.sleep(1)
