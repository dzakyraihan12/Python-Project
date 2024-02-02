import xmlrpc.client
import xmlrpc.client as xmlrpclib
import os
import socket

#function untuk mengunggah file ke server
def upload(fileName,host):
    print("Sedang mengupload")
    try:
        with open(fileName,'rb') as handle:
            file = xmlrpc.client.Binary(handle.read())
            server.upload(file,fileName,host)
            print('File telah terupload !')
    except Exception as e:
        print(e)
        
#function untuk mengunduh file dari server
def download(fileName,host):
    print("Sedang mendownload")
    try:
        with open('download_{}'.format(fileName),'wb') as handle:
            handle.write(server.download(fileName,host).data)
            handle.close()
            print('File telah terdownload !')
    except Exception as e:
        print(e)

#function unutk menampilkan daftar file yang ada di server
def listFile():
    list = server.view()
    for i in list:
        print(i)

#function untuk menndapatkan nama/id host
def cariHost():
    return socket.gethostname()

server = xmlrpc.client.ServerProxy ("http://26.122.28.120:4899/") #alamat IP server
host = cariHost() #menyimpan nama/id host
server.adaclient(host) #memeriksa status client
clear = lambda: os.system("cls")

while True:
    print("Halo", host)
    print('Selamat datang di FTP Spontan Uhuy')
    print(' ')
    print('-------------------------------------------')
    print('PILIH MENUMU YA GES YA!')
    print('1. Upload ')
    print('2. Download ')
    print('3. List File')
    print('4. Keluar dari Program')
    print('-------------------------------------------')

    pilih = input('Pilihan : ')

    if(pilih=='1'):
        file = input('Pilih File: ')
        upload(file,host)
        clear()
        input()
        clear()
    elif(pilih=='2'):
        listFile()
        file = input('Pilih File: ')
        download(file,host)
        clear()
        input()
        clear()
    elif(pilih=='3'):
        print('Berikut merupakan list file yang ada di dalam server: ')
        listFile()
        input()
        clear()
    elif (pilih=='4'):
        clear()
        break
    else:
        clear()
        break
