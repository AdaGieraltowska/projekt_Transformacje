# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:23:53 2023

@author: Ada
"""

import numpy as np
from argparse import ArgumentParser

class Transformation:
    
    def __init__(self,elip):
        self.a = elip[0]
        self.e2 = elip[1]
        
    def Npu(self,fi):
        N = self.a / np.sqrt(1 - self.e2 * np.sin(fi)**2)
        return N
    
    def hirvonen(self,X,Y,Z):
        wyniki = []
        for X, Y, Z in zip(X, Y, Z):
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
            wyniki.append([np.rad2deg(fi), np.rad2deg(lam), h])
            
        return wyniki

    def hirvonen_odw(self,fi,lam,h):
        N = self.Npu(fi)
        Xk = (N+h)*np.cos(fi)*np.cos(lam)
        Yk = (N+h)*np.cos(fi)*np.sin(lam)
        Zk = (N*(1-self.e2)+h)*np.sin(fi)        
        return Xk, Yk, Zk
    
    
    def pl1992(self,fi,lama,m=0.9993):  
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
    
    def odczyt(self,plik_wsadowy, transformacja):
        dane = np.genfromtxt(plik_wsadowy,delimiter = " ")
        if transformacja == 'hirvonen':
            wyniki = self.hirvonen(dane[:,0], dane[:,1], dane[:,2])
            plik_wynikowy = np.savetxt('plik_wynikowy.txt', wyniki, delimiter=' ', fmt='%0.10f %0.10f %0.3f')

        return
    
if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument('-p', type=str) #przyjmuje plik
        parser.add_argument('-el', type=str) #przyjmuje nazwe elipsoidy
        parser.add_argument('-t', type=str) #przyjmuje jaka transformacje wykonac
        args = parser.parse_args()
        
        elipsoidy = {'WGS84':[6378137.000, 0.00669438002290], 'GRS80':[6378137.000, 0.00669438002290], 'Krasowski':[6378245.000, 0.00669342162296]}
        
        # te ify sa po to zeby dzialalo jesli nie odpalasz przez cmd albo nie uzywasz flag
        # jesli nie chcesz co chwila wpisywac danych to to odkomentuj i zmieniaj na co chcesz
        #args.el = 'GRS80'
        #args.p = 'plik_dane.txt'
        #args.t = 'hirvonen'
        
        if args.el==None:
            args.el = input(str('Podaj nazwe elipsoidy: '))
        
        obiekt = Transformation(elipsoidy[args.el])
    except KeyError:
        print('Zle podano nazwe elipsoidy')
    else:
        try:
            transformacje = {'hirvonen': 'hirvonen'}
            if args.p==None:
                args.p = input(str('Wklej sciezke do pliku txt z danymi: '))
    
            if args.t==None:
                args.t = input(str('Jaka transformacje wykonac?: '))
            
            dane = obiekt.odczyt(args.p, transformacje[args.t])
        except FileNotFoundError:
            print('Podany plik nie istnieje')
        except KeyError:
            print('Zle podana transformacja')
        else:
            print('Plik wynikowy zostal utworzony')
        finally:
            print('Koniec programu')