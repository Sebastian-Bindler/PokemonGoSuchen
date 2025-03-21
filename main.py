# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:48:58 2025

@author: Sebi
"""

if __name__ == '__main__': 
    

    with open('relation/hundoSebi.txt','r') as file:
        hundoSebi = " ".join(line.rstrip() for line in file)
        print(hundoSebi)
    with open('relation/hundoEdward.txt','r') as file:
        hundoEdward = " ".join(line.rstrip() for line in file)
        print(hundoEdward)
    with open('relation/hundoPerlina.txt','r') as file:
        hundoPerlina = " ".join(line.rstrip() for line in file)
        print(hundoPerlina)
        
    with open('relation/tradeSebi.txt','r') as file:
        tradeSebi = " ".join(line.rstrip() for line in file)
        print(tradeSebi)
    with open('relation/tradeEdward.txt','r') as file:
        tradeEdward = " ".join(line.rstrip() for line in file)
        print(tradeEdward)
    with open('relation/tradePerlina.txt','r') as file:
        tradePerlina = " ".join(line.rstrip() for line in file)
        print(tradePerlina)
        
    with open('relation/luckySebi.txt','r') as file:
        luckySebi = " ".join(line.rstrip() for line in file)
        print(luckySebi)
    with open('relation/luckyEdward.txt','r') as file:
        luckyEdward = " ".join(line.rstrip() for line in file)
        print(luckyEdward)
    with open('relation/luckyPerlina.txt','r') as file:
        luckyPerlina = " ".join(line.rstrip() for line in file)
        print(luckyPerlina)
        
    with open('relation/hundo.txt','r') as file:
        hundo = " ".join(line.rstrip() for line in file)
        print(hundo)
    with open('relation/fakehundosDE.txt','r') as file:
        fakehundosDE = " ".join(line.rstrip() for line in file)
        print(fakehundosDE)
    with open('relation/pvpDE.txt','r') as file:
        pvpDE = " ".join(line.rstrip() for line in file)
        print(pvpDE) 
    with open('relation/ratandfish.txt','r') as file:
        ratandfish = " ".join(line.rstrip() for line in file)
        print(ratandfish)
    with open('relation/luckyCheck.txt','r') as file:
        luckyCheck = " ".join(line.rstrip() for line in file)
        print(luckyCheck)
        
    with open('relation/disableDE.txt','r') as file:
        disableDE = " ".join(line.rstrip() for line in file)
        print(disableDE) 
    with open('relation/disableEN.txt','r') as file:
        disableEN = " ".join(line.rstrip() for line in file)
        print(disableEN) 
        
        
        
        
#Sebi

    f = open( 'sebi/1Hundo.txt', 'w' )
    f.write(hundo)
    f.close()
    f = open( 'sebi/2Fakehundos.txt', 'w' )
    f.write(fakehundosDE)
    f.close()
    f = open( 'sebi/3PVP.txt', 'w' )
    f.write(pvpDE)
    f.close()
    f = open( 'sebi/4Ratten&Fische.txt', 'w' )
    ratandfish = ratandfish + disableDE
    ratandfish = ratandfish.replace("!XXL&!XXS&", "")
    f.write(ratandfish)
    f.close()
    f = open( 'sebi/5Perlina.txt', 'w' )
    f.write(hundoPerlina + "," + luckyPerlina + disableDE)
    f.close()
    f = open( 'sebi/6Trade.txt', 'w' )
    f.write(tradeSebi + disableDE)
    f.close()
    f = open( 'sebi/7PvpTrade.txt', 'w' )
    f.write(pvpDE + disableDE)
    f.close()
    f = open( 'sebi/8LuckyCheck.txt', 'w' )
    f.write(luckySebi + luckyCheck)
    f.close()
    f = open( 'sebi/9DeleteTrade.txt', 'w' )
    DeleteTrade = disableDE.replace("Entfernung0-101&","")
    DeleteTrade = DeleteTrade.replace("!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Jahr2024&","")
    DeleteTrade = DeleteTrade.replace("!Getauscht","Getauscht")
    DeleteTrade = DeleteTrade[1:]
    f.write(DeleteTrade)
    f.close() 
    f = open( 'sebi/10Delete.txt', 'w' )
    f.write(disableDE)
    f.close()
    f = open( 'sebi/11NonTag.txt', 'w' )
    f.write("!#")
    f.close()
    
    
 #Edward

    f = open( 'Edward/1Hundo.txt', 'w' )
    f.write(hundo)
    f.close()
    f = open( 'Edward/2Fakehundos.txt', 'w' )
    f.write(fakehundosDE)
    f.close()
    f = open( 'Edward/3PVP.txt', 'w' )
    f.write(pvpDE)
    f.close()
    f = open( 'Edward/4Ratten&Fische.txt', 'w' )
    ratandfish = ratandfish + disableDE
    ratandfish = ratandfish.replace("!XXL&!XXS&", "")
    f.write(ratandfish)
    f.close()
    
    f = open( 'Edward/5LuckySebi.txt', 'w' )
    f.write(luckySebi + disableDE)
    f.close()
    
    f = open( 'Edward/6Trade.txt', 'w' )
    f.write(tradeEdward + disableDE)
    f.close()
    
    f = open( 'Edward/7HundoTrade.txt', 'w' )
    f.write(hundoSebi + disableDE)
    f.close()
    
    f = open( 'Edward/8Perlina.txt', 'w' )
    f.write(hundoPerlina + "," + luckyPerlina + disableDE)
    f.close()

    """
    f = open( 'Edward/7PvpTrade.txt', 'w' )
    f.write(pvpDE + disableDE)
    f.close()
    
    f = open( 'Edward/8LuckyCheck.txt', 'w' )
    f.write(luckyEdward + luckyCheck)
    f.close()
    """

    f = open( 'Edward/9DeleteTrade.txt', 'w' )
    DeleteTrade = disableDE.replace("Entfernung0-101&","")
    DeleteTrade = DeleteTrade.replace("!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Jahr2024&","")
    DeleteTrade = DeleteTrade.replace("!Getauscht","Getauscht")
    DeleteTrade = DeleteTrade[1:]
    f.write(DeleteTrade)
    f.close() 
    f = open( 'Edward/10Delete.txt', 'w' )
    f.write(disableDE)
    f.close()
    f = open( 'Edward/11NonTag.txt', 'w' )
    f.write("!#")
    f.close()   
    
    f = open( 'perlina/KlausiesHundoAndLucky.txt', 'w' )
    f.write(hundoSebi + "," + luckySebi + disableEN)
    f.close()
    
    f = open( 'perlina/EdwardHundoAndLucky.txt', 'w' )
    f.write(hundoEdward + "," + luckyEdward + disableEN)
    f.close()
    
    
    
    
    
    
    
    