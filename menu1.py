from login import login
from create_account import create_account
from read_file import read_file
from menu2 import clear_screen

accounts_list = read_file('Accounts.txt')


def menu1():
    print('>>>>>>>>WELCOME<<<<<<<<\n')
    choice = int(input('1) Giris\n2) Hesap oluştur\n3) Çıkış\n\nseçim Yapınız>> '))
    if choice == 1:
        clear_screen()
        try:
            # (ctrl+c) seçeneğinin geri gitmesini sağlamak için
            login(accounts_list)
        except KeyboardInterrupt:
            clear_screen()
    elif choice == 2:
        create_account(accounts_list)
    elif choice == 3:
        #programı kapat
        exit(0)
    else:
        clear_screen()
        print("HATA: Yanlış seçim\n")
    
    menu1()


if __name__ == '__main__':
    menu1()
