import mysql.connector
import datetime
import sys

#ansible server_inform.yml playbook unun urettigi server_info.txt dosyasinin icini testportal dbye upload eder
mydb = mysql.connector.connect(host='10.248.72.40', user='ansible', passwd='xx', database='testportal')
mycursor = mydb.cursor()
rowcount=0
n = len(sys.argv)
if n==2 :
        filename=sys.argv[1]
        print(filename)
else :
    print("input dosya ismi giriniz. script ile ayni dizinde olmalidir")
    print("ornek : python csv2db.py mobilgb-serverinfo.txt ")
    exit()

def writeFile(filepath, text):
    f = open(filepath, "a")
    f.write(text + "\n")
    f.close()

def readAndInsert(filename):
    fileName = filename
    try:
        with open(fileName) as f:
            while line := f.readline():
                try:
                    parts = line.split(";",6)
                    queryStr = "insert into ansiblecmdb_sunucubilgileri(hostname , ip, platform , versiyon, cpu, ram, local_disk) values('" + parts[0] + "','"+parts[1] + "','" + parts[2] + "','"+parts[3] + "','" + parts[4] + "','"+parts[5] + "','"+parts[6] + "')"
                    print(queryStr)
                    mycursor.execute(queryStr)
                except:
                    print("Error")

            mycursor.close()
            mydb.commit()
            mydb.close

    except OSError as e:
        print(e)
        print("bilgilerin okunacagi dosya bulunamadi")
        exit(0)

readAndInsert(filename)
print("tabloya yazildi")

