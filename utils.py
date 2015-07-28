def getparam(str):
	params=str.split("&")
	l1=[]
	l2=[]
	for param in params:
		l1.append(param.split("=")[0])
		l2.append(param.split("=")[1])
	resultmap=dict(zip(l1,l2))
	return resultmap

if __name__ == '__main__':
	params=getparam("a=111&b=222")
	print params