from menu2 import clear_screen, menu2


def login(acc_list):

    login_id = input('Lütfen bilgilerinizi girin(geri dönmek için "Ctrl+C"ye basın) \n>>Id:')
    login_password = input('>>Sifre: ')
    found = False
    for account in acc_list:
        if account[0] == login_id and account[2] == login_password:
            found = True
            clear_screen()
            menu2(account)
            break
        else:
            continue

    if not found:
        clear_screen()
        print('Yanlıs Sifre Girisi')
        login(acc_list)

    else:
        acc_file = open('Accounts.txt', 'w')
        print('Sifre Kaydedildi...')
        # hesaptan çıkış yaptıktan sonra
        #  accounts.txt dosyasına değişiklikleri yazdırın
        for acc in acc_list:
            for elements in acc:
                acc_file.write("%s\t" % elements)
            acc_file.write('\n')
