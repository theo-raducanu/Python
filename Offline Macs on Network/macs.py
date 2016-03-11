import subprocess,threading,time

def getUniqueItems(iterable):
	    seen = set()
	    result = []
	    for item in iterable:
	        if item not in seen:
	            seen.add(item)
	            result.append(item)
	    return result

def runit():
	scanedList=[] #adresele mac de pe retea
	dic=[] #lista dictionar
	T = 5.0
	threading.Timer(T, runit).start()
	#Citirea din consola a MAC-urilor actuale in windows arp -a
	PIPE, STDOUT = subprocess.PIPE, subprocess.STDOUT
	arpA_req = subprocess.Popen(
		['arp', '-a'], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
	for line in iter(arpA_req.stdout.readline, ''):
		#extragere macuri din arp
		s = list(line.split())
		if s:
			if "I" not in s[0]:
					scanedList.insert(len(scanedList),s[1])				
	arpA_req.terminate()

	with open("macs_dictionary.txt","r") as f: #citire dictionar
		old = f.readlines()
		for item in old:
			dic.insert(len(dic),item.strip('\n'))

		l = getUniqueItems(scanedList) #eliminare dubluri
		l2 = list(set(dic) - set(l)) #MAC-uri Offline
		mergedList = l + l2;
		clearedList = getUniqueItems(mergedList) #dictionar updatat

	with open("macs_dictionary.txt","w+") as f:
		f.write('\n'.join(str(x) for x in clearedList ) )
	localtime = time.asctime( time.localtime(time.time()) )
	if l2:
		print "Adrese MAC disponibile : ",localtime
		print('\n'.join(str(x) for x in l2 ) )
	else:
		print "Adrese MAC indisponibile(toate sunt pe retea) : ",localtime
runit()


