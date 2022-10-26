"""para çekme işlevi: hesap bilgilerinin bir listesini alır ve hesap bilgilerini bir liste halinde döndürür"""
import time
import read_file


def withdraw(ls):
    # ls, hesap bilgilerinin bir listesidir.
    # ls[0] id
    # ls[1] name
    # ls[2] password
    # ls[3] balance

    current_balance = int(ls[3])
    # ls [3]'te önceki bakiyeyi değiştirmeden tutmak için başka bir değişkende değişiklik yapın
    # daha sonra yazdırmak için ls[3] = current_balance kaydedin
    print('Mevcut bakiyeniz:' + ls[3])

    withdraw_amount = int(input('Para çekme tutarını girin: '))

    if withdraw_amount > current_balance:
        print("HATA: Mevcut bakiyenizden fazlasını çekemezsiniz")
    else:
        current_balance -= abs(withdraw_amount)  # girilen değeri garanti etmek için

    file_name = ls[0] + '.txt'
    process_list = read_file.read_file(file_name)
    id_file = open(file_name, 'a')

    if len(process_list) == 0:
        # dosyada herhangi bir işlem yoksa
        last_id = 1
    else:
        last_id = int(process_list[len(process_list)-1][0]) + 1
        #son kimliği al ve artır

    id_file.write('{0}\twithdraw\t\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), ls[3], str(current_balance)))
    # write-> işlem kimliği işlem adı işlem tarih_ve_zamanı İşlem öncesi İşlem sonrası
    id_file.close()
    ls[3] = str(current_balance)
    print('Mevcut bakiyeniz: ' + ls[3])

    return ls
