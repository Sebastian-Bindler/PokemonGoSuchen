# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:48:58 2025

@author: Sebi
"""
import shutil
import os

from inc import sebipwned

if __name__ == '__main__': 
    
    
    
    with open('input/sebipwned/hundo.txt','r') as file:
        hundoSebi = " ".join(line.rstrip() for line in file)
        print(hundoSebi)
    with open('input/edwardxelric/hundo.txt','r') as file:
        hundoEdward = " ".join(line.rstrip() for line in file)
        print(hundoEdward)
    with open('input/perlibug/hundo.txt','r') as file:
        hundoPerlina = " ".join(line.rstrip() for line in file)
        print(hundoPerlina)
    with open('input/bwwl/hundo.txt','r') as file:
        hundoBwwl = " ".join(line.rstrip() for line in file)
        print(hundoPerlina)
        
    with open('input/sebipwned/candy.txt','r') as file:
        candySebi = " ".join(line.rstrip() for line in file)
        print(candySebi)
    with open('input/edwardxelric/candy.txt','r') as file:
        candyEdward = " ".join(line.rstrip() for line in file)
        print(candyEdward)
    with open('input/perlibug/candy.txt','r') as file:
        candyPerlina = " ".join(line.rstrip() for line in file)
        print(candyPerlina)
    with open('input/bwwl/candy.txt','r') as file:
        candyBwwl = " ".join(line.rstrip() for line in file)
        print(candyBwwl)
        
    with open('input/sebipwned/lucky.txt','r') as file:
        luckySebi = " ".join(line.rstrip() for line in file)
        print(luckySebi)
    with open('input/edwardxelric/lucky.txt','r') as file:
        luckyEdward = " ".join(line.rstrip() for line in file)
        print(luckyEdward)
    with open('input/perlibug/lucky.txt','r') as file:
        luckyPerlina = " ".join(line.rstrip() for line in file)
        print(luckyPerlina)
    with open('input/bwwl/lucky.txt','r') as file:
        luckyBwwl = " ".join(line.rstrip() for line in file)
        print(luckyBwwl)
        
    with open('input/relation/hundo.txt','r') as file:
        hundo = " ".join(line.rstrip() for line in file)
        print(hundo)
    with open('input/relation/fakehundosDE.txt','r') as file:
        fakehundosDE = " ".join(line.rstrip() for line in file)
        print(fakehundosDE)
    with open('input/relation/pvpDE.txt','r') as file:
        pvpDE = " ".join(line.rstrip() for line in file)
        print(pvpDE) 
    with open('input/relation/ratandfish.txt','r') as file:
        ratandfish = " ".join(line.rstrip() for line in file)
        print(ratandfish)
    with open('input/relation/luckyCheck.txt','r') as file:
        luckyCheck = " ".join(line.rstrip() for line in file)
        print(luckyCheck)
    with open('input/relation/level1.txt','r') as file:
        level1 = " ".join(line.rstrip() for line in file)
        print(level1)
    with open('input/relation/countCandyXL.txt','r') as file:
        countCandyXL = " ".join(line.rstrip() for line in file)
        print(countCandyXL)    
        
    with open('input/relation/disableDE.txt','r') as file:
        disableDE = " ".join(line.rstrip() for line in file)
        print(disableDE) 
    with open('input/relation/disableEN.txt','r') as file:
        disableEN = " ".join(line.rstrip() for line in file)
        print(disableEN)
        
        
        
        
        
    with open('input/sebipwned/xxl.txt','r') as file:
        xxlSebi = " ".join(line.rstrip() for line in file)
        print(xxlSebi)
    with open('input/edwardxelric/xxl.txt','r') as file:
        xxlEdward = " ".join(line.rstrip() for line in file)
        print(xxlEdward)
    with open('input/edwardxelric/xxl.txt','r') as file:
        xxlPerlibug = " ".join(line.rstrip() for line in file)
        print(xxlPerlibug)
    with open('input/edwardxelric/xxl.txt','r') as file:
        xxlBwwl = " ".join(line.rstrip() for line in file)
        print(xxlBwwl)        
        
        
    with open('input/sebipwned/xxs.txt','r') as file:
        xxsSebi = " ".join(line.rstrip() for line in file)
        print(xxsSebi)
    with open('input/edwardxelric/xxs.txt','r') as file:
        xxsEdward = " ".join(line.rstrip() for line in file)
        print(xxsEdward) 
    with open('input/edwardxelric/xxs.txt','r') as file:
        xxsPerlibug = " ".join(line.rstrip() for line in file)
        print(xxsPerlibug) 
    with open('input/edwardxelric/xxs.txt','r') as file:
        xxsBwwl = " ".join(line.rstrip() for line in file)
        print(xxsBwwl) 

    with open('input/perlibug/level1.txt','r') as file:
        level1Perlina = " ".join(line.rstrip() for line in file)
        print(level1Perlina)
        
    shutil.rmtree('output/sebipwned')
    os.mkdir("output/sebipwned")
    os.mkdir("output/sebipwned/check")
    os.mkdir("output/sebipwned/test")
    shutil.rmtree('output/edwardxelric')
    os.mkdir("output/edwardxelric")
    shutil.rmtree('output/perlibug')
    os.mkdir("output/perlibug")
    shutil.rmtree('output/bwwl')
    os.mkdir("output/bwwl")
        
        
#Sebi

    f = open( 'output/sebipwned/hundo.txt', 'w' )
    f.write(hundo)
    f.close()
    f = open( 'output/sebipwned/fakehundos.txt', 'w' )
    f.write(fakehundosDE)
    f.close()
    f = open( 'output/sebipwned/pvp.txt', 'w' )
    f.write(pvpDE)
    f.close()
    f = open( 'output/sebipwned/ratandfish.txt', 'w' )
    ratandfish = ratandfish + disableDE
    ratandfish = ratandfish.replace("!XXL&!XXS&", "")
    f.write(ratandfish)
    f.close()
    
    f = open( 'output/sebipwned/perlina.txt', 'w' )
    f.write(hundoPerlina + "," + luckyPerlina + disableDE)
    f.close()
    f = open( 'output/sebipwned/bwwl.txt', 'w' )
    f.write(hundoBwwl + "," + luckyBwwl + disableDE)
    f.close()
    f = open( 'output/sebipwned/xlcandy.txt', 'w' )
    f.write(disableDE.replace("4*", "4*" + candySebi))
    f.close()
    f = open( 'output/sebipwned/eddy.txt', 'w' )
    f.write(luckyEdward + "," + hundoEdward + disableDE)
    f.close()

    f = open( 'output/sebipwned/deletetrade.txt', 'w' )
    DeleteTrade = disableDE.replace("Entfernung0-101&","")
    DeleteTrade = DeleteTrade.replace("!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Jahr2024&","")
    DeleteTrade = DeleteTrade.replace("!Getauscht","Getauscht")
    DeleteTrade = DeleteTrade[1:]
    f.write(DeleteTrade)
    f.close() 
    f = open( 'output/sebipwned/delete.txt', 'w' )
    f.write(disableDE)
    f.close()
    f = open( 'output/sebipwned/check/xxl.txt', 'w' )
    f.write(xxlSebi + "&XXL")
    f.close()
    f = open( 'output/sebipwned/check/xxs.txt', 'w' )
    f.write(xxsSebi + "&XXS")
    f.close()
    f = open( 'output/sebipwned/xxleddy.txt', 'w' )
    f.write(xxlEdward + "&XXL&!getauscht")
    f.close()
    f = open( 'output/sebipwned/xxseddy.txt', 'w' )
    f.write(xxsEdward + "&XXS&!getauscht")
    f.close()
    f = open( 'output/sebipwned/nontag.txt', 'w' )
    f.write("!#")
    f.close()
    f = open( 'output/sebipwned/perlinalevel1.txt', 'w' )
    f.write(level1Perlina + disableDE + level1)
    f.close()
    
    f = open( 'output/sebipwned/check/hundo.txt', 'w' )
    f.write(hundoSebi + "&4*")
    f.close()
    f = open( 'output/sebipwned/check/lucky.txt', 'w' )
    f.write(luckySebi + luckyCheck)
    f.close()
    f = open( 'output/sebipwned/km.txt', 'w' )
    f.write(disableDE.replace("&Entfernung0-101", "!Entfernung0-101"))
    f.close()
    
 #Edward

    f = open( 'output/edwardxelric/1Hundo.txt', 'w' )
    f.write(hundo)
    f.close()
    f = open( 'output/edwardxelric/2Fakehundos.txt', 'w' )
    f.write(fakehundosDE)
    f.close()
    f = open( 'output/edwardxelric/3PVP.txt', 'w' )
    f.write(pvpDE)
    f.close()
    f = open( 'output/edwardxelric/4Ratten&Fische.txt', 'w' )
    ratandfish = ratandfish + disableDE
    ratandfish = ratandfish.replace("!XXL&!XXS&", "")
    f.write(ratandfish)
    f.close()
    
    f = open( 'output/edwardxelric/5LuckySebi.txt', 'w' )
    f.write(luckySebi + disableDE)
    f.close()
    
    f = open( 'output/edwardxelric/6Trade.txt', 'w' )
    f.write(candyEdward + disableDE)
    f.close()
    
    f = open( 'output/edwardxelric/7HundoTrade.txt', 'w' )
    f.write(hundoSebi + disableDE)
    f.close()
    
    f = open( 'output/edwardxelric/8Perlina.txt', 'w' )
    f.write(hundoPerlina + "," + luckyPerlina + disableDE)
    f.close()

    """
    f = open( 'output/edwardxelric/7PvpTrade.txt', 'w' )
    f.write(pvpDE + disableDE)
    f.close()
    """
	
    f = open( 'output/edwardxelric/8LuckyCheck.txt', 'w' )
    f.write(luckyEdward + luckyCheck)
    f.close()
    
    f = open( 'output/edwardxelric/Level1Perlina.txt', 'w' )
    f.write(level1Perlina + disableDE + level1)
    f.close()
    
    


    f = open( 'output/edwardxelric/9DeleteTrade.txt', 'w' )
    DeleteTrade = disableDE.replace("Entfernung0-101&","")
    DeleteTrade = DeleteTrade.replace("!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Jahr2024&","")
    DeleteTrade = DeleteTrade.replace("!Getauscht","Getauscht")
    DeleteTrade = DeleteTrade[1:]
    f.write(DeleteTrade)
    f.close() 
    f = open( 'output/edwardxelric/10Delete.txt', 'w' )
    f.write(disableDE)
    f.close()
    f = open( 'output/edwardxelric/11NonTag.txt', 'w' )
    f.write("!#")
    f.close()
    f = open( 'output/edwardxelric/13XXL.txt', 'w' )
    f.write(xxlEdward + "&XXL")
    f.close()
    f = open( 'output/edwardxelric/14XXS.txt', 'w' )
    f.write(xxsEdward + "&XXS")
    f.close()
    f = open( 'output/edwardxelric/15XXLSebi.txt', 'w' )
    f.write(xxlSebi + "&XXL&!getauscht")
    f.close()
    f = open( 'output/edwardxelric/16XXSSebi.txt', 'w' )
    f.write(xxsSebi + "&XXS&!getauscht")
    f.close()
    
    f = open( 'output/perlibug/KlausiesHundoAndLucky.txt', 'w' )
    f.write(hundoSebi + "," + luckySebi + disableEN)
    f.close()
    
    f = open( 'output/perlibug/EdwardHundoAndLucky.txt', 'w' )
    f.write(hundoEdward + "," + luckyEdward + disableEN)
    f.close()
    
    f = open( 'output/bwwl/KlausiesHundoAndLucky.txt', 'w' )
    f.write(hundoSebi + "," + luckySebi + disableEN)
    f.close()
    
    f = open( 'output/bwwl/EdwardHundoAndLucky.txt', 'w' )
    f.write(hundoEdward + "," + luckyEdward + disableEN)
    f.close()
    

    
    
    
    
    