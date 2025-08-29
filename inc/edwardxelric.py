'''
level1Perlina
hundo perlina
lucky perlina
hundo bwwl
lucky bwwl
xxs Eddy
xxl Eddy
lucky eddy
hundo eddy
lucky+hundo eddy


'''
import shutil
import os
from inc import func as fu

name = "edwardxelric"

# Import
hundoI = 'input/' + name + '/hundo.txt'
luckyI = 'input/' + name + '/lucky.txt'
shinyI = 'input/' + name + '/shiny.txt'
xxlI = 'input/' + name + '/xxl.txt'
xxsI = 'input/' + name + '/xxs.txt'


# Export
bwwlE = 'output/' + name + '/bwwl.txt'
deleteE = 'output/' + name + '/delete.txt'
deletetradeE = 'output/' + name + '/deletetrade.txt'
hundoE = 'output/' + name + '/eddy.txt'
fakehundosE = 'output/' + name + '/fakehundos.txt'
newhundoE = 'output/' + name + '/hundo.txt'
kmE = 'output/' + name + '/trade/km.txt'
nontagE = 'output/' + name + '/nontag.txt'
perlinaE = 'output/' + name + '/perlina.txt'
perlinalevel1E = 'output/' + name + '/trade/perlinalevel1.txt'
pvpE = 'output/' + name + '/pvp.txt'
pvptradeE = 'output/' + name + '/trade/pvptrade.txt'
ratandfishE = 'output/' + name + '/trade/ratandfish.txt'
xlcandyE = 'output/' + name + '/trade/xlcandy.txt'


xxlE = 'output/' + name + '/xxleddy.txt'
xxsE = 'output/' + name + '/xxseddy.txt'

luckycheckE = 'output/' + name + '/check/lucky.txt'
hundocheckE = 'output/' + name + '/check/hundo.txt'
xxlcheckE = 'output/' + name + '/check/xxl.txt'
xxscheckE = 'output/' + name + '/check/xxs.txt'
shinycheckE = 'output/' + name + '/check/shiny.txt'

listE_Edward = 'output/edwardxelric/Sebi.txt'
listE_Perlina = 'output/perlibug/Klozy.txt'
listE_Bwwl = 'output/bwwl/Klozy.txt'

#Relations
countCandyXL = 'input/relation/countCandyXL.txt'
disableDE = 'input/relation/disableDE.txt'
disableEN = 'input/relation/disableEN.txt'
fakehundosDE = 'input/relation/fakehundosDE.txt'
hundoR = 'input/relation/hundo.txt'
level1 = 'input/relation/level1.txt'
luckyCheckDE = 'input/relation/luckyCheckDE.txt'
luckyCheckEN = 'input/relation/luckyCheckEN.txt'
pvpDE = 'input/relation/pvpDE.txt'
ratandfish = 'input/relation/ratandfish.txt'
gmax = 'input/relation/gmax.txt'
gmaxcandyxl = 'input/relation/gmaxcandy.txt'

def main():
    shutil.rmtree('output/' + name + '')
    os.mkdir('output/' + name + '')
    os.mkdir('output/' + name + '/check')
    os.mkdir('output/' + name + '/trade')
    fu.func("", "", newhundoE, hundoR, "", "", "", "", "") #hundo check
    fu.func("", "", fakehundosE, fakehundosDE, "", "", "", "", "") #fackehundos check
    fu.func("", "", pvpE, pvpDE,  "", "", "", "", "") #pvp
    fu.func(countCandyXL, "", pvptradeE, pvpDE,  ",0-2", "&0-2", "", "", "") #pvp
    fu.func(ratandfish, "", ratandfishE, disableDE,  "!XXL&!XXS&", "", "", "", "") #Small Rattata and Big Magikarp
    fu.func(countCandyXL, "", xlcandyE, disableDE,  "", "", "", "", "") #XL Candys
    
    fu.func(hundoI, luckyI, listE_Edward, disableDE, "", "", "", "", "")
    fu.func(hundoI, luckyI, listE_Perlina, disableEN, "", "", "", "", "")
    fu.func(hundoI, luckyI, listE_Bwwl, disableEN, "", "", "", "", "")
    
    #Delete Traded Pokemon
    fu.func("", "", xlcandyE, disableDE.replace("Entfernung0-101&",""),  "!Getauscht", "Getauscht", "!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Jahr2024&", "", "") #DeleteTrade
    
    # Delete
    fu.func("", "", deleteE, disableDE, "", "", "", "", "")
    
    #km
    fu.func("", "", kmE, disableDE, "Entfernung0-101", "!Entfernung0-101", "", "", "")
    
    # no tag
    fu.func("", "", nontagE, "", "", "!#", "", "", "")
    
    #checks
    fu.func(luckyI, "", luckycheckE, luckyCheckDE, "", "", "", "", "")
    fu.func(hundoI, "", hundocheckE, "", "", "", "", "", "&4*")
    fu.func(xxlI, "", xxlcheckE, "", "", "", "", "", "&xxl")
    fu.func(xxsI, "", xxscheckE, "", "", "", "", "", "&xxs")
    fu.func(shinyI, "", shinycheckE, "", "", "", "", "", "&shiny")
    
    #XXL
    



if __name__ == "__main__":
    fu.func()