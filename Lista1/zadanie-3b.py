import sys
import base64
import json

def RSA():
	if(len(sys.argv)!=3):
		print("Niepoprawne uzycie programu")
		print("python zadanie-3b.py <x> <plik>")
		return -1
	else:
		x = int(sys.argv[1])

		with open(sys.argv[2], 'r') as f:
			data_list = json.load(f)
			p_txt=data_list["p"].replace("-","+").replace("_","/")
			q_txt=data_list["q"].replace("-","+").replace("_","/")
			dp_txt=data_list["dp"].replace("-","+").replace("_","/")
			dq_txt=data_list["dq"].replace("-","+").replace("_","/")
			qi_txt=data_list["qi"].replace("-","+").replace("_","/")
			padding_factor = (4 - len(p_txt) % 4) % 4
			p_txt += "="*padding_factor
			padding_factor = (4 - len(q_txt) % 4) % 4
			q_txt += "="*padding_factor 
			padding_factor = (4 - len(dp_txt) % 4) % 4
			dp_txt += "="*padding_factor 
			padding_factor = (4 - len(dq_txt) % 4) % 4
			dq_txt += "="*padding_factor 
			padding_factor = (4 - len(qi_txt) % 4) % 4
			qi_txt += "="*padding_factor 
			p = int.from_bytes(base64.b64decode(p_txt), 'big')
			q = int.from_bytes(base64.b64decode(q_txt), 'big')
			dp = int.from_bytes(base64.b64decode(dp_txt), 'big')
			dq = int.from_bytes(base64.b64decode(dq_txt), 'big')
			qi = int.from_bytes(base64.b64decode(qi_txt), 'big')
			yp = pow(x,dp,p)
			yq=pow(x,dq,q)
			h=qi*(yp-yq)%p
			return yq+h*q

def main():
	result=RSA()
	print(result)
	
if __name__=='__main__':
	main()