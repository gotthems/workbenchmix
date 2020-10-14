import csv
import pandas as pd
import datetime 
import numpy as np
import os

print(datetime.datetime.now(),'okuma öncesi')
csv_path = os.path.expanduser("~/Desktop/dataset/traffic-crashes-vehicles-1.csv")

data = pd.read_csv(csv_path) 

"""listekabuledenframelericin= ['MAKE','VEHICLE_YEAR']

listr=['MAKE','VEHICLE_YEAR']
tekoge =str(listr).replace('[','').replace(']','').replace("'","")

print(tekoge)


simplelist= data['MAKE'].isin(['DODGE', 'VOLVO'])

gormekistenensutun = data[listekabuledenframelericin]

print(gormekistenensutun[~gormekistenensutun['MAKE'].isin(['DODGE', 'VOLVO'])])
"""

firstdatafilter = data[['MAKE','VEHICLE_YEAR','NUM_PASSENGERS']].dropna()

carbrand = firstdatafilter[firstdatafilter['MAKE'].isin(['VOLVO','HYUNDAI','DODGE','LEXUS'])]

passengerfilter = carbrand[carbrand['NUM_PASSENGERS'].isin([1,2])]

yearfilter =  passengerfilter[(passengerfilter['VEHICLE_YEAR'] <= 2020) &(carbrand['VEHICLE_YEAR'] >= 2019) ]

indexfind = yearfilter[yearfilter['MAKE'].isin(['DODGE'])].index.values


indexdel = yearfilter.drop([3100])

print(indexdel)












"""
örneği kullanıcı bu parametreleri düzenli rapor olarak kaydet dedi ve  filtrelemelerini kaydetti:
       - kullanıcı tekrar giriş yaptığında backupstore' da:
              - kayıtlı filtrelemelerini
                     - filtrelemeler ile ilgili:
                            -özet bilgi'ye
                            - detay bilgiye
                            - sunuma
                            -ön izlemeye sahip olmalıdır.
                            | tüm bunlara ulaşabilmelidir. |
       
       - Kullanıcı yeni rapor oluşturabilmeli
              - Rapor:
                     - Raporu görselleştirebilmeli.
                     - Rapor verilerini anlık olarak görebilmeli ve üzerinde oynayabilmeli
                     - Raporda düzeltme yapabilmeli 
                            - Düzeltmeleri loglayabilmeli 
                            - son haliyle güncelleyebilmeli
                            - Ayrı bir kayıt oluşturabilmeli
                            - Yaptığı her işlemle ilgili log oluşturabilmeli
                            - Bunları aktivitelerde görebilmeli
                            - Raporu Paylaşabilmeli
                            - Raporu Ana, Özet ve süreç bilgilendirme olarak ayırabilmeli
                     - Her yerden erişebilmeli. Online ortamda çalışabilmeli ve bunu local ile eşitleyebilmeli

       

if storage == backup:
       get = backup

       a = get.firstdata.data
       f = get.carbrand.data"""