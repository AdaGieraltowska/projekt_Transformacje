# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:23:53 2023

@author: Ada
"""

import numpy as np
import sys

class Transformation:
    
    def __init__(self,a,e2):
        self.a = a
        self.e2 = e2
    def Npu(self,fi):
        import numpy as np    
        N = self.a / np.sqrt(1 - self.e2 * np.sin(fi)**2)
        return N
    
    def hirvonen(self,X,Y,Z):
        import numpy as np    
        p = np.sqrt(X**2+Y**2)
        fi = np.arctan(Z/(p*(1-self.e2)))
            
        while True:
            N = self.Npu(fi)
            h = (p/np.cos(fi)) - N
            fi_poprzednia = fi
            fi = np.arctan((Z/p)/(1-((N*self.e2)/(N+h))))
            if abs(fi_poprzednia-fi)<(0.000001/206265):
                break
        N = self.Npu(fi)
        h = p/np.cos(fi) - N
        lam = np.arctan(Y/X)
        
        return fi, lam, h

    def hirvonen_odw(self,fi,lam,h):
        import numpy as np    
        N = self.Npu(fi)
        Xk = (N+h)*np.cos(fi)*np.cos(lam)
        Yk = (N+h)*np.cos(fi)*np.sin(lam)
        Zk = (N*(1-self.e2)+h)*np.sin(fi)        
        return Xk, Yk, Zk
    
    
    def pl1992(self,fi,lama,m=0.9993):
        import numpy as np    
        lama0 = np.deg2rad(19)
    # # 1 parametry elipsoidy     
        b2 = self.a**2*(1-self.e2)
        ep2 = (self.a**2-b2)/b2
    # # 2. Wielkosci pomocnicze     
        dellama = lama - lama0
        t = np.tan(fi)
        ni2 = ep2*(np.cos(fi)**2)
        N = self.Npu(fi)
    
    # # 3. Długosc luku poludnika 
        A0 = 1- (self.e2/4)-(3*self.e2**2/64)-(5*self.e2**3/256)
        A2 = (3/8)*(self.e2+(self.e2**2/4)+(15*self.e2**3/128))
        A4 = (15/256)*(self.e2**2+((3*self.e2**3)/4))
        A6 = (35*self.e2**3)/3072
        sigma = self.a *(A0*fi-A2*np.sin(2*fi)+A4*np.sin(4*fi)-A6*np.sin(6*fi))
    
    # # wsolrzedne prostokatne lokalne na plaszczyznie gaussa-krugera
    
        xgk =  sigma    +    ( ((dellama**2/2)*N*np.sin(fi)*np.cos(fi))    *    (1   +   ((dellama**2/12)*(np.cos(fi)**2)*(5 - t**2 + 9*ni2 + 4*ni2**2))      +         ((dellama**4/360)*(np.cos(fi)**4)*(61 - 58*t**2 + t**4 + 270*ni2 - 330*ni2*t**2))))
    
        ygk =  (dellama* N * np.cos(fi))  *   ( 1 +  ((dellama**2/6)   *   (np.cos(fi)**2)   *  (1 - t**2 + ni2))     +     (((dellama**4/120)*(np.cos(fi)**4)) * (5 - (18*t**2) + t**4 + (14 * ni2) - (58*ni2*t**2))))
    
        x92 = xgk * m - 5300000
        y92 = ygk*m + 500000
        return  x92, y92

    def pl2000(self,fi,lama,m=0.999923):
        import numpy as np    

        lama0 = 0
        strefa = 0
        if lama >np.deg2rad(13.5) and lama < np.deg2rad(16.5):
            strefa = 5
            lama0 = np.deg2rad(15)
        elif lama >np.deg2rad(16.5) and lama < np.deg2rad(19.5):
            strefa = 6
            lama0 = np.deg2rad(18)
        elif lama >np.deg2rad(19.5) and lama < np.deg2rad(22.5):
            strefa =7
            lama0 = np.deg2rad(21)
        elif lama >np.deg2rad(22.5) and lama < np.deg2rad(25.5):
            strefa = 8
            lama0 = np.deg2rad(24)
        # else:
        #     print("Punkt poza strefami odwzorowawczymi układu PL-2000")        
        
        # 1 parametry elipsoidy     
        b2 = self.a**2*(1-self.e2)    
        ep2 = (self.a**2-b2)/b2
        # 2. Wielkosci pomocnicze     
        dellama = lama - lama0
        t = np.tan(fi)
        ni2 = ep2*(np.cos(fi)**2)
        N = self.Npu(fi)
        
        # 3. Długosc luku poludnika 
        A0 = 1- (self.e2/4)-(3*self.e2**2/64)-(5*self.e2**3/256)
        A2 = (3/8)*(self.e2+(self.e2**2/4)+(15*self.e2**3/128))
        A4 = (15/256)*(self.e2**2+((3*self.e2**3)/4))
        A6 = (35*self.e2**3)/3072
        
        sigma = self.a *(A0*fi-A2*np.sin(2*fi)+A4*np.sin(4*fi)-A6*np.sin(6*fi))
        
        # wsolrzedne prostokatne lokalne na plaszczyznie gaussa-krugera
        
        xgk =  sigma    +    ( ((dellama**2/2)*N*np.sin(fi)*np.cos(fi))    *    (1   +   ((dellama**2/12)*(np.cos(fi)**2)*(5 - t**2 + 9*ni2 + 4*ni2**2))      +         ((dellama**4/360)*(np.cos(fi)**4)*(61 - 58*t**2 + t**4 + 270*ni2 - 330*ni2*t**2))))
        
        ygk =  (dellama* N * np.cos(fi))  *   ( 1 +  ((dellama**2/6)   *   (np.cos(fi)**2)   *  (1 - t**2 + ni2))     +     (((dellama**4/120)*(np.cos(fi)**4)) * (5 - (18*t**2) + t**4 + (14 * ni2) - (58*ni2*t**2))))
        
        x2000 = xgk * m 
        y2000 = ygk*m + (strefa *1000000) +500000
        return  x2000, y2000
        
    def hej(self):
        print("Czesc, jestem",self.name)
    
    
    ### COS NIE DZIALA NIE ZAPISUJE W PLIKU :(
    def odczyt(self,plik_wsadowy):
        import numpy as np
        dane = np.genfromtxt(plik_wsadowy,delimiter = "&")
        dane2 = dane*3
        plik_wynikowy = np.savetxt('plik_wynikowy.txt', dane2, delimiter=';')
        print("udało się")

        return dane
    
if __name__ == '__main__':
    nazwa = input(str('Wpisz nazwe: '))
    
    if nazwa == 'WGS84':
        a = 6378137.000
        e2 = 0.00669438002290
    elif nazwa == 'GRS80':
        a = 6378137.000
        e2 = 0.00669438002290
    elif nazwa == 'Krasowski':
        a = 6378245.000
        e2 = 0.00669342162296
    else:
        sys.exit('Podano zla nazwe elipsoidy')
    
    el = Transformation(a, e2)
    dane = el.odczyt("plik_wsadowy_proba1.txt") 