from contextlib import nullcontext
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os

#download file ke server
def download(file,host):
    try:
        with open(file, 'rb') as handle:
            Activity_Update(host)
            return xmlrpc.client.Binary(handle.read())
    except Exception as e:
        print(e)


#upload file ke server
def upload(file,fileName,host):
    try:
        with open('{}_{}'.format(host,fileName),'wb') as handle:
            handle.write(file.data)
            Activity_Update(host)
            return True
    except Exception as e:
        print(e)

#Function untuk melihat file yang tersedia pada server
def tampilfile():
    return os.listdir()

#Function untuk mengecek ada tidaknya client dan juga untuk menambah client pada database berupa array
def adaclient(host):
    door=True
    if ( len(arr)==0 ):
        arr.append(host)
        arr_act.append(0)
    else:
        for i in range(len(arr)):
            if ( arr[i] == host ):
                door=False
        if(door==True):
            arr.append(host)
            arr_act.append(0)


#Function untuk memperbarui banyaknya aktivitas yang dilakukan oleh para client sekaligus untuk menampilkan client yang sedang aktif & yang paling aktif
def Activity_Update(host):
    for i in range(len(arr)):
        if(host==arr[i]):
            arr_act[i] +=1

    for i in range(len(arr)):
        print(i+1, " NAMA HOST : ",arr[i])
        print("   Jumlah Aktivitas : ",arr_act[i])
    
    max=0
    if len(arr)>0:    
        for i in range(len(arr)):
            if(arr_act[i]>arr_act[max]):
                max=i
    
    print("")
    print("TOP USER: ")
    print("NAMA HOST : ",arr[max])
    print("Jumlah Aktivitas : ",arr_act[max])
        
#Function utama untuk menjalankan server
def serverMain():
    server = SimpleXMLRPCServer(("26.122.28.120", 4899), allow_none=True)
    print("Sedang mengkoneksikan")

    server.register_function(upload, "upload")
    server.register_function(download, "download")
    server.register_function(tampilfile, "view")
    server.register_function(adaclient, "adaclient")
    server.register_function(Activity_Update, "aktivitasclient")
    server.serve_forever()

#Pembuatan variabel dengan tipe data aarray untuk menyimpan info client
arr=[]
arr_act=[]

#Pemanggilan function fucntion utama
serverMain()
