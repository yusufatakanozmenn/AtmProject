import os
import withdraw
import deposit
import show_history
import change_password


def clear_screen():
    # ekranın çıktısını temizleme işlevi
    os.system('clear')
    print()  # ekranı temizledikten sonra boş satır yazdır


def menu2(account):
    # hesap, hesap bilgilerinin bir listesidir
    # account[0] id
    # account[1] name
    # account[2] password
    # account[3] balance

    print("\n---------Hello, {0}--------- ".format(account[1]))
    ch = int(input("\n1) Bilgi göster \n2) Süreç geçmişini göster\n3) Para Yatırma\n4) Para Çekme\n"
                   "5) Sifre değiştirme \n6) Çıkış\n\Secim Yapınız>> "))

    clear_screen()
    if ch == 1:
        print("ID: {}\nName: {}\nBalance: {}\n".format(account[0], account[1], account[3]))
    elif ch == 2:
        show_history.show_history(account)
    elif ch == 3:
        deposit.deposit(account)
    elif ch == 4:
        withdraw.withdraw(account)
    elif ch == 5:
        change_password.change_password(account)
    elif ch == 6:
        return
        # çıkış - menu1'e geri dön
    else:
        print("HATA: Yanlış seçim\n")

    menu2(account)
