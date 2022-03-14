print("\033[0;39mDesigned By \033[0;34m: \033[0;32mAnas Pro")
print()
import random,requests,time
a = 'Ahamad','Abdullah','Aabdulrhman','Mohammed','Malik','Hussam','Turki','Ali','Talal','Tariq','Samy','Sultan','Saleh','Salem','Fahad','Khaled','Salman','Mansour','Faisal','Bader','Majed','Yasser','Osama','Abdulaziz','Basm','Bassam','Naif','Nawaf','Ibrahim','Yazeed','Mussab'
b = 'abcdefghijklmnopqrstuvwxyz'
c = '0123456789'
code = input('\033[0;39m* \033[0;32mEnter Your Code \033[0;34m:\033[0;39m ')
refcount = int(input('\033[0;39m* \033[0;32mEnter The Number Of Invitations \033[0;34m:\033[0;39m '))
sc = input('\033[0;39m* \033[0;32mEnter Sc_Id \033[0;34m:\033[0;39m ')
bd = input('\033[0;39m* \033[0;32mEnter Bd_Id \033[0;34m:\033[0;39m ')
print()
for ad in range(refcount) :
    print('\033[0;36m-'*40)
    num = ad+1
    print(f"\033[0;39m••••••••••••••• \033[0;32mThe Account \033[0;34m{num} \033[0;39m•••••••••••••••")
    print()
    user = random.choice(a)+random.choice(a)+random.choice(b)+random.choice(b)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)
    phone = '01'+random.choice('0125')+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)
    key = random.choice(c)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(b)+random.choice(c)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(b)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(b)+random.choice(c)+random.choice(c)+random.choice(c)+random.choice(b)+random.choice(c)+random.choice(c)+random.choice(b)
    anas = requests.post('https://api.ifa2012.com/login/register',headers={'Host':'api.ifa2012.com','content-length':'167','lang':'EGY','content-type':'application/x-www-form-urlencoded','accept':'*/*','origin':'https://www.ifa2012.com','x-requested-with':'mark.via.gp','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.ifa2012.com/','accept-encoding':'gzip, deflate','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'},data={'lang':'EGY','username':user,'password':user,'code_value':'','code_key':key,'areacode':'20','phone':phone,'code':'','rec_code':code,'mail':'','mail_code':''})
    if"عملية ناجحة" in anas.text :
        print(f"\033[0;39m» \033[0;32mDone Create Account \033[0;34m{user} \033[0;32mSuccessfully \033[0;39m")
    else :
        print("\033[0;31mError\033[0;39m")
    l = 'https://api.ifa2012.com/login/login'
    h = {'Host':'api.ifa2012.com',
    'Connection':'keep-alive',
    'Content-Length':'108',
    'lang':'EGY',
    'noToken':'true',
    'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585 Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.58 Safari/537.36',
    'content-type':'application/x-www-form-urlencoded',
    'Accept':'*/*',
    'Origin':'https://ifa2012.com',
    'X-Requested-With':'mark.via.gp',
    'Sec-Fetch-Site':'same-site',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Dest':'empty',
    'Referer':'https://ifa2012.com/',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
    d = {'lang':'EGY',
    'username':user,
    'password':user,
    'code_value':'',
    'code_key':key}
    r = requests.post(l,headers=h,data=d)
    if"عملية ناجحة" in r.text :
        print(f"\033[0;39m» \033[0;32mDone Login Account \033[0;34m{user} \033[0;32mSuccessfully \033[0;39m")
    else :
        print("\033[0;31mError\033[0;39m")
    pp = r.json()['data']['token']
    kk = r.json()['data']['token_key']
    ll = 'https://api.ifa2012.com/action/apply'
    dd = {'lang':'EGY',
    'action_id':'1'}
    hh = {'Host':'api.ifa2012.com',
    'Connection':'keep-alive',
    'Content-Length':'20',
    'lang':'EGY',
    'usertoken':pp,
    'usertokenkey':kk,
    'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585 Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.58 Safari/537.36',
    'content-type':'application/x-www-form-urlencoded',
    'Accept':'*/*',
    'Origin':'https://ifa2012.com',
    'X-Requested-With':'mark.via.gp',
    'Sec-Fetch-Site':'same-site',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Dest':'empty',
    'Referer':'https://ifa2012.com/',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',}
    rr = requests.post(ll,headers=hh,data=dd).text
    if"عملية ناجحة" in rr :
        print(f"\033[0;39m» \033[0;32mDone Take The Reward  Account \033[0;34m{user} \033[0;32mSuccessfully\033[0;39m")
    else :
        print("\033[0;31mError\033[0;39m")
    lll = 'https://api.ifa2012.com/match/buy'
    ddd = {'lang':'EGY',
    'sc_id':sc,
    'bd_id':bd,
    'zd_type':'2',
    'money':'18.00',
    'money_type':'1'}
    rrr = requests.post(lll,headers=hh,data=ddd)
    if"عملية ناجحة" in rrr.text :
        print(f"\033[0;39m» \033[0;32mDone Invested Account  \033[0;34m{user} \033[0;32mSuccessfully\033[0;39m")
        f = open('ifa2012.txt','a+')
        f.write(f'{user}\n')
        f.close()
        time.sleep(1)
        print(f"\033[0;39m√ \033[0;32mDone Saved The Account Successfully\033[0;39m")
    else :
        print("\033[0;31mError\033[0;39m")
    print('\033[0;36m-'*40)
    print()
