                # yoksa Accounts.txt oluşturun


try:
    # 'Accounts.txt' dosyasını okuyun
    # mevcut olmayan bir dosyayı okuma modunda açmaya çalışırsanız, bu bir hata verecektir.
    f = open('Accounts.txt', 'r')
    f.close()
except FileNotFoundError:
    # 'Accounts.txt' dosyası bulunamazsa, oluşturun
    f = open('Accounts.txt', 'w')
    f.close()

# modülleri içe aktar
import menu1
import os

os.system('clear')
menu1.menu1()  # programı başlatın - menu1() işlevini çağırın
