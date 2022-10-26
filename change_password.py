import time
from read_file import read_file


def gate_x(t_password):
    # Yeni şifreyi onaylamak için eski şifreyi girin
    wrong_flag = True  # Tüm denemeler yanlışsa 

    print("\nGeri dönmek istiyorsanız \"Çıkış\" yazın\n")
    for i in range(3):  # Şifreyi girme denemesini sınırlayın
        entered_password = input('\nEski Şifreyi Girin :')
        if entered_password == "Exit":  # Çıkış bayrağını döndür
            return '-1'
        if entered_password == t_password:  # Girilen parola = doğru password ise karşılaştırın
            wrong_flag = False  # Yanlış olarak ayarla, girilen şifrenin onaylandığı anlamına gelir
            break

    if wrong_flag:  # Yanlış bayrağı döndür
        return '1'
    else:  # Gerçek bayrağı döndür
        return '0'

    # Şifre değiştir


def change_password(ls):
    # eski şifreyi al
    old_password = ls[2]

    # Yenisini girmek için eski şifreye sor
    flag = gate_x(old_password)
    # Güvenlik bayrağı çıktı bayrağını al
    if flag == '0':
        new_password = input("\nYeni şifreyi girin:")
        '''yeni şifreyi al'''
        file_name = ls[0] + '.txt'
        process_list = read_file(file_name)
        id_file = open(file_name, 'a')

        if len(process_list) == 0:  # dosyada herhangi bir işlem yoksa
            last_id = 1
        else:
            last_id = int(process_list[len(process_list) - 1][0]) + 1  

        id_file.write(
            '{0}\tchange_password\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), old_password, str(new_password)))
        # işlem kimliği türünü önce sonra yaz
        id_file.close()

        # Farklı negatif değer olup olmadığını kontrol edin
        ls[2] = new_password

        # Yeni şifreyi yaz
    elif flag == '1':
        input("Deneme aralığı dışında ... Enter'a basın")
