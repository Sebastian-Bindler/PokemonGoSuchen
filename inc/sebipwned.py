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

from inc import func as fu

names = ['sebipwned', 'edwardxelric', 'perlibug', 'bwwl', 'Klozy']
lang = [0, 0, 1, 1, 0]

# Import
hundoI = 'input/' + names[0] + '/hundo.txt'
luckyI = 'input/' + names[0] + '/lucky.txt'
shinyI = 'input/' + names[0] + '/shiny.txt'
xxlI = 'input/' + names[0] + '/xxl.txt'
xxsI = 'input/' + names[0] + '/xxs.txt'

# Export
deleteE = 'output/' + names[0] + '/delete.txt'
deletetradeE = 'output/' + names[0] + '/deletetrade.txt'
fakehundosE = 'output/' + names[0] + '/fakehundos.txt'
newhundoE = 'output/' + names[0] + '/hundo.txt'
kmE = 'output/' + names[0] + '/trade/km.txt'
nontagE = 'output/' + names[0] + '/nontag.txt'
perlinalevel1E = 'output/' + names[0] + '/trade/perlinalevel1.txt'
pvpE = 'output/' + names[0] + '/pvp.txt'
pvptradeE = 'output/' + names[0] + '/trade/pvptrade.txt'
ratandfishE = 'output/' + names[0] + '/trade/ratandfish.txt'
xlcandyE = 'output/' + names[0] + '/trade/xlcandy.txt'

xxlE = 'output/' + names[4] + '/xxl' + names[0] +'.txt'
xxsE = 'output/' + names[4] + '/xxs' + names[0] +'.txt'

luckycheckE = 'output/' + names[0] + '/check/lucky.txt'
hundocheckE = 'output/' + names[0] + '/check/hundo.txt'
xxlcheckE = 'output/' + names[0] + '/check/xxl.txt'
xxscheckE = 'output/' + names[0] + '/check/xxs.txt'
shinycheckE = 'output/' + names[0] + '/check/shiny.txt'

listE = 'output/'+ names[4] + '/lucky+hundo_' + names[0] +'.txt'


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
    fu.func("", "", newhundoE, hundoR, "", "", "", "", "") #hundo check
    fu.func("", "", fakehundosE, fakehundosDE, "", "", "", "", "") #fackehundos check
    fu.func("", "", pvpE, pvpDE,  "", "", "", "", "") #pvp
    fu.func(countCandyXL, "", pvptradeE, pvpDE,  ",0-2", "&0-2", "", "", "") #pvp
    fu.func(ratandfish, "", ratandfishE, disableDE,  "!XXL&!XXS&", "", "", "", "") #Small Rattata and Big Magikarp
    fu.func(countCandyXL, "", xlcandyE, disableDE,  "", "", "", "", "") #XL Candys
    
    index = 1
    for i in names[1:-1]:
        print(lang[index])
        if lang[index] == 0:
            fu.func(hundoI, luckyI, listE.replace('Klozy', i), disableDE, "", "", "", "", "")
        else:
            fu.func(hundoI, luckyI, listE.replace('Klozy', i), disableEN, "", "", "", "", "") 
        index = index + 1
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
    
    index = 1
    for i in names[1:-1]:
        if lang[index] == 0:
            fu.func(xxlI, "", xxlE.replace('Klozy', i), disableDE, ",&", "&", "!XXL", "XXL", "")
        else:
            fu.func(xxlI, "", xxlE.replace('Klozy', i), disableEN, ",&", "&", "!XXL", "XXL", "")
        index = index + 1
        

if __name__ == "__main__":
    fu.func()