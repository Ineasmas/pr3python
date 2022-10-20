from ast import Constant
from asyncio import constants
import os
import multiprocessing
from multiprocessing import Process
from RandomWordGenerator import RandomWord
import random
#ограничение на длину слова
rw=RandomWord(max_word_size=10,constant_word_size=False)
#функция для статистики
def stats(falename):
    with open(falename, "r") as f:
        vsego_sim=0
        max_dl_slov=0
        min_dls_lov=100
        kolvo_glas=0
        kolvo_sogl=0
        sim1=0
        sim2=0
        sim3=0
        sim4=0
        sim5=0
        sim6=0
        sim7=0
        sim8=0
        sim9=0
        sim10=0
        dlina_vseh_slov=0
        kolvo_slov=0

        for mas in f:
            kolvo_slov+=len(mas.split())
            vsego_sim+=len(mas)
    
            for slovo in mas.split():
                if max_dl_slov < len(slovo):
                    max_dl_slov=len(slovo)  
                if min_dls_lov > len(slovo):
                    min_dls_lov=len(slovo)  
                dlina_vseh_slov+=len(slovo)

                if len(slovo)==1:
                    sim1+=1
                elif len(slovo)==2:
                    sim2+=1
                elif len(slovo)==3:
                    sim3+=1
                elif len(slovo)==4:
                    sim4+=1
                elif len(slovo)==5:
                    sim5+=1
                elif len(slovo)==6:
                    sim6+=1
                elif len(slovo)==7:
                    sim7+=1
                elif len(slovo)==8:
                    sim8+=1
                elif len(slovo)==9:
                    sim9+=1
                elif len(slovo)==10:
                    sim10+=1

        
            for char in mas:
                if char.lower() in "aeiouy":
                    kolvo_glas+=1
                else:
                    kolvo_sogl+=1


        midle_dl_slov=round(kolvo_slov/dlina_vseh_slov)
            
#Вывод статистики
    vivodstat = f"""
***********************************************
  Аналитика для файла {falename}
***********************************************
 1. Всего символов => {vsego_sim}
 2. Максимальная длина слова => {max_dl_slov}
 3. Минимальная длина слова => {min_dls_lov}
 4.  Средняя длина слова => {midle_dl_slov}
 5. Кол-во гласных => {kolvo_glas}
 6. Кол-во согласных => {kolvo_sogl}
 7. Кол-во повторений слов с одинаковой длиной:
  
    * 1 сим. => {sim1}
    * 2 сим. => {sim2}
    * 3 сим. => {sim3}
    * 4 сим. => {sim4}
    * 5 сим. => {sim5}
    * 6 сим. => {sim6}
    * 7 сим. => {sim7}
    * 8 сим. => {sim8}
    * 9 сим. => {sim9}
    * 10 сим. => {sim10}
"""
    print(vivodstat)
#фукция многопотока
def crfi(x):
    i=0
    folename = str(os.getpid())+'.txt'
    f=open(str(os.getpid())+'.txt','w')
    while i<random.randint(100000, 5000001):
     i+=1
     f.write(rw.generate()+ ' ')
    f.close()
    stats(folename)
#Вызываю ее
if __name__ == '__main__':
    print('kol-vo pokov = ',multiprocessing.cpu_count())
    print('всё гатова, файл создался')
    pool =multiprocessing.Pool(processes=12)
    pool.map(crfi,range(12))

