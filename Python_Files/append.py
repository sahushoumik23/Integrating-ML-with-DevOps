<<<<<<< HEAD
import os

acc=acc*100

if int(acc) > 80:
	os.system('curl --user "admin:toor" http://192.168.1.105:8080/view/Task%203/job/success/build?token=success')
else:
	os.system('curl --user "admin:toor" http://192.168.1.105:8080/view/Task%203/job/Failure/build?token=Fail')
=======
import os 

acc=acc*100

if int(acc) >80 :
	os.system(curl -u "admin:toor" 192.168.1.105:8080/view/Task%203/job/success/build?token=success)
else:
	os.system(curl -u "admin:toor" 192.168.1.105:8080/view/Task%203/job/Failure/build?token=Fail)
>>>>>>> 617c48b95847eb6d0e96aff04f089981487d2aef
