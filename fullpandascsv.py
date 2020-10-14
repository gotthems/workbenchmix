import csv
import pandas as pd
import time
import numpy as np
import os
csv_path = os.path.expanduser("~/Desktop/dataset/traffic-crashes-vehicles-1.csv")
data = pd.read_csv(csv_path)

ilkbes= data.head()

makedata = data['MAKE']
CARRIER_CITY = data['CARRIER_CITY']
CARRIER_STATE = data['CARRIER_CITY']      
VEHICLE_YEAR =  data['VEHICLE_YEAR']






"""veri = data[['MAKE','VEHICLE_YEAR']].dropna()


with pd.ExcelWriter('veri.xlsx') as writer: 
       veri.to_excel(writer,sheet_name='Sheet3')"""


""" PANDAS NOTLARI"""
"""
print(yearfilter.set_index('MAKE'))


#index bulma ve silme
       yearfilter =  passengerfilter[(passengerfilter['VEHICLE_YEAR'] <= 2020) &(carbrand['VEHICLE_YEAR'] >= 2019) ]
       indexfind = yearfilter[yearfilter['MAKE'].isin(['DODGE'])].index.values
       indexdel = yearfilter.drop([3100])

#

        self.data = self.data[(~self.data['MAKE'].isin(['DODGE', 'VOLVO'])) & (self.data['VEHICLE_YEAR'].isin([2015]))]
        
#iki sütun içerisindeki verileri filtreleme

       self.data[(~self.data['MAKE'].isin(['DODGE', 'VOLVO'])) & (self.data['VEHICLE_YEAR'] >2017)&(self.data['VEHICLE_YEAR']<2021)]

# volvo yerine none değerini girecek
 asd.where(asd != 'VOLVO',None) 
 
#DODGE VE VOLVO OLMAYAN LİSTE
       asd.loc[~asd['MAKE'].isin(['DODGE', 'VOLVO'])]


#Sütunun altındaki verileri değiştirme. 9999 olan ifadeler önce none ile değiştiirip sonra nan olan verileri sildim
       ap[ap['VEHICLE_YEAR'] < 2021].shift(fill_value=None).dropna()

#Sütunun altındaki verileri bulma
   verileri getirir, diğerlerini siler ve geriye na kalır bunları dropna ile temizledim bu yüzden
   ap = asd[asd['MAKE'].isin(['DODGE','VOLVO'])].dropna()

#Sütun toplama
       sutuntoplama = veri['VEHICLE_YEAR'].sum()

#Aşağıda iki adet sütun filtrelenmiş son olarak istenmeyen kelime çıkarılmış ve boş sütunlar temizlenmiştir.
       veri = data[['MAKE','VEHICLE_YEAR']]

#birden fazla sütun filtreleyip sütun içerisinde filtreleme yapmak. İstenmeyen kelime veya tarihleri eksiltme
       
       multipleclean = veri[(veri['VEHICLE_YEAR'] > 2016.0) & (veri['MAKE'] != 'UNKOWN' )].dropna()

       print(veri[veri != 'DODGE'].dropna())
#birden fazla sütunun içindeki verinin o sütunda kaç adet geçtiğini saymak
       data[data['MAKE'].value_counts(),data['VEHICLE_YEAR'].value_counts()]

#seçilen sütun ve karşılık gelen değerlerin toplanması.örn; Dodge = 9999, Honda = 56777 gibi
       valucountsum =  veri.groupby('MAKE')['VEHICLE_YEAR'].sum().reset_index()

#Değeri büyükten küçüğe sıralama ascending=False ve 0.0 dan büyk olan değerleri göster ve indexi yeniden oluştur
       valucountsum[valucountsum['VEHICLE_YEAR']>0.0].sort_values(by='VEHICLE_YEAR',ascending=False).reset_index()

#istenmeyen satırı silme
       df[df.name != 'Tina']

#nullcolm = data['CARRIER_CITY'].isnull()


#notnullcolm = pd.notnull(data['CARRIER_CITY'])

#--> boş olan isnull boş olmayanları bulmak için notnull kullanılır.

# belirli bir sütunda aynı isimdeki ögelerin sayılarını toplar.
       data['MAKE'].value_counts()
# boş olmayan sütunları getirir.
       data['CARRIER_CITY'].dropna()
# birden fazla sütunda aynı anda eksik araması yapmak için
       df.dropna(subset=['name', 'born'])
# satır sütun sayısını verir
        data.shape[]
#data.index satırların örneğin 0 dan başlayıp 5 te bittiğini 1 er basamak atladığını öğrenebiliriz
#data.iloc[] istediğimiz satır aralığını getirir.
# data.head() belli bir satırı getirir
#excelden okunan bilgiyi dataframe'e çevirdikten sonra sütun çekme sütun başlığı yazarak o başlığa ait verileri çekme
#pd.DataFrame
#insertColumns = kd.insert(0, "Age", [21, 23, 24, 21],True ) 
#kd.insert(0,"Age", None, True) İstediği sütuna sütun ekleme
#kd["new_csol"]=None  boş sütun ekleme
#kd.loc[0,'new_csol'] = 1000 veri ekleme ilk veri satır sırasını ikinci veri sütunu son veri ise eklencek değeri gösteriyor
#film.loc[0:5,'title'] belirli bir sütunu ve belirli bir satır aralığını getirmek
"""


