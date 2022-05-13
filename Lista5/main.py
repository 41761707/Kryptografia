import random
import time
import matplotlib.pyplot as plt

def RSA(x,n,e):
    return pow(x,e,n)

def RSAwCRT(x,p,q,dp,dq,qi):
    yp = pow(x,dp,p)
    yq = pow(x,dq,q)
    h=qi * (yp-yq) % p
    return yq + h*q

def test_prime(number):
    for _ in range(5):
        a=random.randint(2,number-1)
        if(pow(a,number-1,number) != 1):
            return False
    return True

def generate(n):
    primes = []
    start = pow(2, n-1)
    while(len(primes)<100):
        p = random.randint(start+1, 2*start - 1)
        if(test_prime(p)):
            primes.append(p)
    return primes
    
def func(primes):
    rsa = 0
    crt = 0
    for i in range(len(primes)):
        p = primes[i][0]
        q = primes[i][1]
        e = 65537

        n = p*q
        d = pow(e, -1, (p-1)*(q-1))
        dp = d % (p-1)
        dq = d % (q-1)
        qi = pow(q, -1, p)

        encrypted=RSA(10,n,e)
        start=time.time()
        _ = pow(encrypted, d, n)

        rsa += (time.time()-start)

        start=time.time()
        _ = RSAwCRT(encrypted, p, q, dp, dq, qi)
        crt += (time.time()-start)
    
    rsa /= len(primes)
    crt /= len(primes)
    return (rsa, crt)



def main():
    modes = [128, 256, 512, 1024, 1536,2048]
    result_rsa = []
    result_crt = []
    for item in modes:
        primes=generate(item)
        chosen=[]
        while(len(chosen) < 1000):
            chosen.append(random.sample(primes,2))
        result=func(chosen)
        result_rsa.append(result[0])
        result_crt.append(result[1])
        print("{} - {} ; {}".format(item,result_rsa,result_crt))
    file3072=open('p_3072.txt')
    numbers=file3072.read().split('\n')
    primes3072=[int(x) for x in numbers[:-1]]
    chosen=[]
    while(len(chosen) < 1000):
        chosen.append(random.sample(primes3072,2))
    result=func(chosen)
    result_rsa.append(result[0])
    result_crt.append(result[1])

    file4096=open('p_4096.txt')
    numbers=file4096.read().split('\n')
    primes4096=[int(x) for x in numbers[:-1]]
    chosen=[]
    while(len(chosen) < 1000):
        chosen.append(random.sample(primes4096,2))
    result=func(chosen)
    result_rsa.append(result[0])
    result_crt.append(result[1])
    modes.extend([3072,4096])

    print("{} ; {}".format(result_rsa,result_crt))


    plt.plot(modes, result_rsa, color = 'b', linestyle = 'dashed',
         marker = 'o',label = "Normal decoding")
    plt.plot(modes, result_crt, color = 'r', linestyle = 'dashed',
         marker = 'o',label = "CRT decoding")
    plt.xticks(rotation = 25)
    plt.xlabel('bits')
    plt.ylabel('time')
    plt.title('RSA', fontsize = 20)
    plt.grid()
    plt.legend()
    plt.show()
    
    '''for iterator, item1, item2 in zip(modes, result_rsa, result_crt):
        print(iterator, item1, item2)
    '''

if __name__=='__main__':
    main()