import sys


def RSAwCRT():
	if(len(sys.argv)!=7):
		print("Niepoprawne uzycie programu")
		print("python zad1b.py <x> <p> <q> <dp> <dq> <qi>")
		return -1
	else:
		x = int(sys.argv[1])
		p = int(sys.argv[2])
		q = int(sys.argv[3])
		dp = int(sys.argv[4])
		dq = int(sys.argv[5])
		qi= int(sys.argv[6])
		yp = pow(x,dp)%p 
		yq=pow(x,dq)%q
		h=qi*(yp-yq)%p
		return yq+h*q

def main():
	result=RSAwCRT()
	print(result)

if __name__=='__main__':
	main()