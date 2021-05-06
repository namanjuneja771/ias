import sensormanager as f1
import platformmanager as f2
import threading
def runall(n):
	print("before")
	if(n==1):
		f1.main()
	if(n==2):
		f2.main()
	print("after")
for i in range(1,3):
	if(i==1):
		t1=threading.Thread(target=runall, args=(i,))
		t1.start()
		#t1.join()
	if(i==2):
		t2=threading.Thread(target=runall, args=(i,))
		t2.start()
		#t2.join()
#print("before")
#t2 = threading.Thread(runall(2), name='t2')
# starting threads
#t1.start()
#t2.start()
# wait until all threads finish
#t1.join()
#t2.join()

#f1.main()
