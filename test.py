import time, os

def bersih():
    if os.name=="nt":
        os.system("clear")
    else:
        os.system("clear")

logo = """

⋱ ⋮ ⋰
⋯ ◯ ⋯ ︵ 　　　　　　^v^
¸︵︵( ░░ )︵.︵.︵
(´░░░░░░ ') ░░░' )
`´︶´¯`︶´`︶´︶´`　^v^　　^v^
╔┓┏╦━━╦┓╔┓╔━━╗╔╗
║┗┛║┗━╣┃║┃║╯╰║║║
║┏┓║┏━╣┗╣┗╣╰╯║╠╣    Program Tes Kecepatan Ketik
╚┛┗╩━━╩━╩━╩━━╝╚╝           by AsukaDev

"""
class Test:
    def __init__(self, logo):
        self.logo = logo
    def jalan(self):
        mulai = time.time()
        print(logo)
        print('waktu :', time.asctime, '\n')
        while True:
            bersih()
            print(logo)
            siap=input('[ Enter untuk mulai ]')
            waktuawal = time.time()
            karakter=input('> ')
            waktuakhir = time.time()
            print('jumlah karakter :',len(karakter))
            print('waktu pengerjaan : ',round((waktuakhir-waktuawal)),'detik')
            print('kecepatan : ',round(len(karakter)/(waktuakhir-waktuawal)),'karakter perdetik')
            ulang=input('Masukan (s) untuk berhenti : ')
            if ulang == "s": break

if __name__=="__main__":
    bersih()
    banner = logo
    Test(banner).jalan()
    bersih()

            

