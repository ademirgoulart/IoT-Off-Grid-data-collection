import os
import time
from datetime import datetime
hostname1 = "192.168.4.1" #  first  server
hostname2 = "192.168.5.1"  # second server
hostname3 = "192.168.6.1"  # third server 
i = 1  
n1 = 0
n2 = 0
n3 = 0
#and then check the response...
while i > 0 :
	response = os.system("ping -c 1 " + hostname1)
	if response == 0 and n1 == 0:
	  	print (hostname1, 'is up!')
	  	print ("vai chamar scp")
	  	data_hora_atual =  datetime.now()
		dh_texto = data_hora_atual.strftime ('%d/%m/%Y  %H:%M')
		print(dh_texto)
		resp= os.system("scp -p pi@192.168.4.1:/home/pi/arquivos/*.*  /home/pi/Doutorado/no_01/" )
		data_hora_atual =  datetime.now()
		dh_texto = data_hora_atual.strftime ('%d/%m/%Y  %H:%M')
		print(dh_texto)	
		n1=1


	response = os.system("ping -c 1 " + hostname2)
	if response == 0 and n2 == 0:
	  	print (hostname2, 'is up!')
	  	print ("vai chamar scp")
	  	data_hora_atual =  datetime.now()
		dh_texto = data_hora_atual.strftime ('%d/%m/%Y  %H:%M')
		print(dh_texto)
		resp= os.system("scp -p pi@192.168.5.1:/home/pi/arqs_no_02/*.* /home/pi/Doutorado/no_02/" )
		data_hora_atual =  datetime.now()
		dh_texto = data_hora_atual.strftime ('%d/%m/%Y  %H:%M')
		print(dh_texto)
		n2=1

	response = os.system("ping -c 1 " + hostname3)
	if response == 0 and n3 == 0:
	  	print (hostname3, 'is up!')
	  	print ("vai chamar scp")
	  	data_hora_atual =  datetime.now()
		dh_texto = data_hora_atual.strftime ('%d/%m/%Y  %H:%M')
		print(dh_texto)
		resp= os.system("scp -p pi@192.168.6.1:/home/pi/arquivos/*.* /home/pi/Doutorado/no_03/" )
		data_hora_atual =  datetime.now()
		dh_texto = data_hora_atual.strftime ('%d/%m/%Y  %H:%M')
		print(dh_texto)
		n3=1
	print ('intervalo de espera 20 segundos')
	time.sleep(20)


