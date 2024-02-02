def show_topic(list_topic, dict_activity):
    '''
    Menampilkan setiap topik beserta detil aktifitasnya
    '''
    print('----Fungsi "show_topic" dijalankan----')
    #jawaban anda di bawah ini
    
    

def add_topic(list_topic, dict_activity, id_activity):
    '''
    Meminta data topik baru. Menambahkan topik baru ke list_topic.
    Tanya jika ingin sekaligus menambahkan actifitas. Jika menambahkan aktifitas, naikkan counter id_activity dengan 1,
    baru dijadikan sebagai key activity baru.

    Return id_activity yang terakhir digunakan

    '''
    print('----Fungsi "add_topic" dijalankan----')
    #jawaban anda di bawah ini
    

def delete_topic(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin dihapus.
    Lalu hapus topik beserta semua aktivitasnya, hapus juga data di activity, submission, dan grade untuk id aktivitas yang terdapat di topik ini
    '''
    print('----Fungsi "delete_topic" dijalankan----')
    #jawaban anda di bawah ini
    if len(list_topic) == 0:
        print("Daftar topik kosong.")
    else:
        print("Daftar topik: ")
        for i in range(len(list_topic)):
            print('{}: {}'.format(i+1, list_topic[i]["Title"]))
        pilih_topic = int(input("Masukkan nomor topic yang ingin dihapus: "))
        list_len_topic = list(range(len(list_topic)))
        pilih_topic -= 1
        if pilih_topic in list_len_topic :
            for x in list_topic[pilih_topic]["Activities"]:
                if x in dict_activity:
                    dict_activity.pop(x)
                if x in dict_submission:
                    dict_submission.pop(x)
                if x in dict_grade:
                    dict_grade.pop(x)
            list_topic.pop(pilih_topic)
            print("Delete topic selesai")
        else:
            print("Maaf pilihan topic yang dipilih tidak tersedia")
    tekan_enter=input("Tekan Enter untuk kembali ke menu utama.")
    





def update_topic(list_topic):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Tampilkan data eksisting.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "update_topic" dijalankan----')
    #jawaban anda di bawah ini
    
    

def add_activity(list_topic, dict_activity, id_activity):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin tambah aktifitas.
    Minta data aktifitas baru, tambahkan counter id_activity dengan 1, lalu tambahkan ke dalam dict_activity.
    Tambahkan juga id_activity ke dalam list aktifitas topik.
    Tanya jika ingin menambah aktifitas lagi

    Return: id_activity yang terakhir digunakan
    '''

    print('----Fungsi "add_activity" dijalankan----')
    #jawaban anda di bawah ini

    

def udpate_activity(list_topic, dict_activity):
    '''
    Menampilkan semua topik, meminta inputan topik yang ingin diupdate.
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Minta data update ke user, jika field tidak ingin diupdate, user cukup mengosongkan field
    '''
    print('----Fungsi "udpate_activity" dijalankan----')
    #jawaban anda di bawah ini
    


def delete_activity(list_topic, dict_activity, dict_submission, dict_grade):
    '''
    Menampilkan semua topik, minta inputan topik. 
    Menampilkan data activity pada topik yang dipilih, minta inputan activity.
    Hapus activity, submission, dan grade dengan id activity yang dipilih
    '''
    print('----Fungsi "delete_activity" dijalankan----')
    #jawaban anda di bawah ini
    
    
      

    



def print_topic_to_file(list_topic, dict_activity):
    '''
    Minta nama file.
    Print setiap detail topik, beserta list aktifitasnya ke file.
    '''

    print('----Fungsi "print_topic_to_file" dijalankan----')
    #jawaban anda di bawah ini

    




    
if __name__ == "__main__":
    #type_activity = ['assignment', 'material']
    #id_activity adalah variable global untuk id unik semua activity di semua topic
    LAST_ID_ACTIVITY = 2
    NIM_LOGIN = ''
    ADMIN_LOGIN = False


    #key pada dict_mhs['data'] adalah NIM
    dict_mhs = {'field' : [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                           ('Email', '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                           ('Password', '^[a-zA-Z0-9]{8,12}$')],
             'data' : {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                       '114': {'Nama': 'Joni', 'Email': 'joni@telU.com', 'Password': '12345678'},
                       '115': {'Nama': 'jeje', 'Email': 'jeje@telU.com', 'Password': '12345678'}

                       }           
            }

    #Value pada key 'Activities' berupa list berisi id_activity
    list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities':[0, 1]},
                    {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities':[2]}
                  ]

    # key pada dict_activity adalah id_activity 
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                         1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                         2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                         }

    # key pada dict_submission adalah id_activity 
    dict_submission = {0: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                        2: {'113' : 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'}
                       }

    # key pada dict_grade adalah id_activity 
    dict_grade = {0: {'113' : 100}
                        
                  }

    
     
