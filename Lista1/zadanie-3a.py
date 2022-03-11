import sys
import base64
import json

def RSA():
	if(len(sys.argv)!=3):
		print("Niepoprawne uzycie programu")
		print("python zadanie-3a.py <x> <plik>")
		return -1
	else:
		x = int(sys.argv[1])

		with open(sys.argv[2], 'r') as f:
			data_list = json.load(f)
			n_txt=data_list["n"].replace("-","+").replace("_","/")
			e_txt=data_list["e"]
			padding_factor = (4 - len(n_txt) % 4) % 4
			n_txt += "="*padding_factor 
			padding_factor = (4 - len(e_txt) % 4) % 4
			e_txt += "="*padding_factor 
			n = int.from_bytes(base64.b64decode(n_txt), 'big')
			e = int.from_bytes(base64.b64decode(e_txt), 'big')
			return pow(x,e,n)

def main():
	result=RSA()
	print(result)
	
if __name__=='__main__':
	main()