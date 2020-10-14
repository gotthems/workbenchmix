import csv
import pandas as pd
import datetime 
import numpy as np
import os
print(datetime.datetime.now(),'okuma öncesi')

csv_path = os.path.expanduser("~/Desktop/dataset/traffic-crashes-vehicles-1.csv")
data = pd.read_csv(csv_path) 
print(datetime.datetime.now(),'okuma sonrası')
class pandasdata:
    def __init__(self,data,showlist=None):
        self.data = data
        self.showlist = showlist
        

    def datashow(self):
        listcol =  self.data.columns
        if type(self.showlist) == list:
            self.data = data[self.showlist]
            print('filtreleme yapıldı : ', self.showlist)
        else:
            self.data = data
        return self.data,listcol

    def clean_data(self):
        self.data = self.data.dropna()
        
    def columnindexfilter(self):
        self.data = self.data[(~self.data['MAKE'].isin(['DODGE', 'VOLVO'])) & (self.data['VEHICLE_YEAR'].isin([2015]))]
        return self.data

    def indexandcolumn(self):
        print(self.data)


    def createfiledb(self):
        pass


print(datetime.datetime.now(),'df create')
df = pd.DataFrame(data=data)
print(datetime.datetime.now(),'while başlangıcı')
a = 0
while a==0:
    liste = ['MAKE']
    listeinput = input('Filtrelenecek Verileri giriniz').upper()
    liste.append(listeinput)

    print(datetime.datetime.now(),'main başlangıcı')
    manins  =pandasdata(df,liste)
    print(datetime.datetime.now(),'main bitti')

    chooseColShow,listcolshow = manins.datashow()
    print(datetime.datetime.now(),'data seçildi')
    fdata = chooseColShow[chooseColShow != 'UNKNOWN'].dropna()
    print(datetime.datetime.now(),'unkown ve drop filtresi')
    tt = manins.columnindexfilter()

    print(tt)
    #manins.clean_data()
    #print(datetime.datetime.now(),'clean data')
    #print(fdata)
    print(datetime.datetime.now(),'son')
    continue

"""
WHİLE DÖNGÜSÜNE GİRDİĞİNİ VARSAYARSAK;
    İstediğim fonksiyonu değiştirerek listeyi güncelleyebiliriz.
    Dataframe'i sırasına göre düzenlemeli.
    yani liste istenilen şekilde düzenlenmeli, kaydedilmeli, paylaşılmalı, görselleştrilmeli.
    Ancak bu hataya neden olmamalı


"""