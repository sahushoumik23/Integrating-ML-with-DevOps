
import os

acc=acc*100

if int(acc) > 80:
	os.system('curl --user "admin:toor" http://192.168.1.105:8080/view/Task%203/job/success/build?token=success')
else:
	os.system('curl --user "admin:toor" http://192.168.1.105:8080/view/Task%203/job/Failure/build?token=Fail')
