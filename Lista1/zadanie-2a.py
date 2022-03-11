import sys

def RSA():
	if(len(sys.argv)!=4):
		print("Niepoprawne uzycie programu")
		print("python zad1a.py <x> <n> <e>")
		return -1
	else:
		x = int(sys.argv[1])
		n = int(sys.argv[2])
		e = int(sys.argv[3])
		return pow(x,e)%n

def main():
	result=RSA()
	print(result)
	
if __name__=='__main__':
	main()