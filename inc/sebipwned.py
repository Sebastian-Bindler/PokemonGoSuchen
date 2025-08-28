# Import
hundoI = 'input/sebipwned/hundo.txt'
luckyI = 'input/sebipwned/lucky.txt'
shinyI = 'input/sebipwned/shiny.txt'
xxlI = 'input/sebipwned/xxl.txt'
xxsI = 'input/sebipwned/xxs.txt'

# Import others


# Export
bwwlE = 'output/sebipwned/bwwl.txt'
deleteE = 'output/sebipwned/delete.txt'
deletetradeE = 'output/sebipwned/deletetrade.txt'
hundoE = 'output/sebipwned/eddy.txt'
fakehundosE = 'output/sebipwned/fakehundos.txt'
newhundoE = 'output/sebipwned/hundo.txt'
kmE = 'output/sebipwned/km.txt'
nontagE = 'output/sebipwned/nontag.txt'
perlinaE = 'output/sebipwned/perlina.txt'
perlinalevel1E = 'output/sebipwned/perlinalevel1.txt'
pvpE = 'output/sebipwned/pvp.txt'
ratandfishE = 'output/sebipwned/ratandfish.txt'
xlcandyE = 'output/sebipwned/xlcandy.txt'


xxlE = 'output/sebipwned/xxleddy.txt'
xxsE = 'output/sebipwned/xxseddy.txt'

luckycheckE = 'output/sebipwned/check/lucky.txt'
hundocheckE = 'output/sebipwned/check/hundo.txt'
xxlcheckE = 'output/sebipwned/check/xxl.txt'
xxscheckE = 'output/sebipwned/check/xxs.txt'
shinycheckE = 'output/sebipwned/check/shiny.txt'

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
    func("", "", newhundoE, hundoR, "", "", "", "", "") #hundo check
    func("", "", fakehundosE, fakehundosDE, "", "", "", "", "") #fackehundos check
    func("", "", fakehundosE, pvpDE,  "", "", "", "", "") #pvp
    func(ratandfish, "", ratandfishE, disableDE,  "!XXL&!XXS&", "", "", "", "") #Small Rattata and Big Magikarp
    func(countCandyXL, "", xlcandyE, disableDE,  "", "", "", "", "") #XL Candys
    
    func(hundoI, luckyI, listE_Edward, disableDE, "", "", "", "", "")
    func(hundoI, luckyI, listE_Perlina, disableEN, "", "", "", "", "")
    func(hundoI, luckyI, listE_Bwwl, disableEN, "", "", "", "", "")
    
    #Delete Traded Pokemon
    func("", "", xlcandyE, disableDE.replace("Entfernung0-101&",""),  "!Getauscht", "Getauscht", "!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Jahr2024&", "", "") #DeleteTrade
    
    # Delete
    func("", "", deleteE, disableDE, "", "", "", "", "")
    
    #km
    func("", "", kmE, disableDE, "Entfernung0-101", "!Entfernung0-101", "", "", "")
    
    # no tag
    func("", "", nontagE, "", "", "!#", "", "", "")
    
    #checks
    func(luckyI, "", luckycheckE, luckyCheckDE, "", "", "", "", "")
    func(hundoI, "", hundocheckE, "", "", "", "", "", "&4*")
    func(xxlI, "", xxlcheckE, "", "", "", "", "", "&xxl")
    func(xxsI, "", xxscheckE, "", "", "", "", "", "&xxs")
    func(shinyI, "", shinycheckE, "", "", "", "", "", "&shiny")
    
    #XXL
    

def func(_input, _input2, _output, _reltion, _replaceOLD, _replaceNEW, _replace2OLD, _replace2NEW, _StringAddOn):
    __output = ""
    if _input != "":
        with open(_input,'r') as file:
            __input = " ".join(line.rstrip() for line in file)
        __output = __output + __input
    if _input2 != "":
        with open(_input2,'r') as file:
            __input2 = " ".join(line.rstrip() for line in file)
        __output = __output + "," + __input2
    if _reltion != "":
        with open(_reltion,'r') as file:
            __relation = " ".join(line.rstrip() for line in file)
        __output = __output + "," + __relation
    if _replaceOLD != _replaceNEW:
        __output = __output.replace(_replaceOLD, _replaceNEW)
    if _replace2OLD != _replace2NEW:
        __output = __output.replace(_replace2OLD, _replace2NEW)
        
    f = open(_output, 'w')
    print(_output)
    f.write(__output + _StringAddOn)
    f.close()

if __name__ == "__main__":
    func()