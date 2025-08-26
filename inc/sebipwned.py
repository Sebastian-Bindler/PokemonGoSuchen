# Import
candyI = 'input/sebipwned/candy.txt'
hundoI = 'input/sebipwned/hundo.txt'
luckyI = 'input/sebipwned/lucky.txt'
shinyI = 'input/sebipwned/shiny.txt'
xxlI = 'input/sebipwned/xxl.txt'
xxsI = 'input/sebipwned/xxs.txt'



# Export
bwwlE = 'output/sebipwned/bwwl.txt'
deleteE = 'output/sebipwned/delete.txt'
deletetradeE = 'output/sebipwned/deletetrade.txt'
hundoE = 'output/sebipwned/eddy.txt'
fakehundosE = 'output/sebipwned/fakehundos.txt'
hundocheckE = 'output/sebipwned/hundo.txt'
kmE = 'output/sebipwned/km.txt'
nontagE = 'output/sebipwned/nontag.txt'
perlinaE = 'output/sebipwned/perlina.txt'
perlinalevel1E = 'output/sebipwned/perlinalevel1.txt'
pvpE = 'output/sebipwned/pvp.txt'
ratandfishE = 'output/sebipwned/ratandfish.txt'
xlcandyE = 'output/sebipwned/xlcandy.txt'
xxlE = 'output/sebipwned/xxleddy.txt'
xxsE = 'output/sebipwned/xxseddy.txt'

hundoE_Edward = 'output/edwardeelric/hundoSebi.txt'
hundoE_Perlina = 'output/perlibug/hundoKlozy.txt'
hundoE_Bwwl = 'output/bwwl/hundoKlozy.txt'

#Relations
countCandyXL = 'input/relation/countCandyXL.txt'
disableDE = 'input/relation/disableDE.txt'
disableEN = 'input/relation/disableEN.txt'
fakehundosDE = 'input/relation/fakehundosDE.txt'
hundoR = 'input/relation/hundo.txt'
level1 = 'input/relation/level1.txt'
luckyCheck = 'input/relation/luckyCheck.txt'
pvpDE = 'input/relation/pvpDE.txt'
ratandfish = 'input/relation/ratandfish.txt'

def main():
    func("", "", hundocheckE, hundoR, "", "", "", "") #hundo check
    func("", "", fakehundosE, fakehundosDE, "", "", "", "") #fackehundos check
    func("", "", fakehundosE, pvpDE,  "", "", "", "") #pvp
    func(ratandfish, "", ratandfishE, disableDE,  "!XXL&!XXS&", "", "", "") #Small Rattata and Big Magikarp
    func(countCandyXL, "", xlcandyE, disableDE,  "", "", "", "") #XL Candys
    
    func(hundoI, "", hundoE_Edward, disableDE, "", "", "", "")
    func(hundoI, "", hundoE_Perlina, disableEN, "", "", "", "")
    func(hundoI, "", hundoE_Bwwl, disableEN, "", "", "", "")
    
    func(luckyI, "", hundoE_Edward, disableDE, "", "", "", "")
    func(luckyI, "", hundoE_Perlina, disableEN, "", "", "", "")
    func(luckyI, "", hundoE_Bwwl, disableEN, "", "", "", "")
    
    #Delete Traded Pokemon
    func("", "", xlcandyE, disableDE.replace("Entfernung0-101&",""),  "!Getauscht", "Getauscht", "!Jahr2016&!Jahr2017&!Jahr2018&!Jahr2019&!Jahr2020&!Jahr2021&!Jahr2022&!Jahr2023&!Jahr2024&", "") #DeleteTrade
    func(luckyI, "", luckyCheck, )

def func(_input, _input2, _output, _reltion, _replaceOLD, _replaceNEW, _replace2OLD, _replace2NEW):
    __output = ""
    with open(_input,'r') as file:
        __input = " ".join(line.rstrip() for line in file)
    with open(_input2,'r') as file:
        __input2 = " ".join(line.rstrip() for line in file)
    with open(_reltion,'r') as file:
        __relation = " ".join(line.rstrip() for line in file)
        
    if _input != "":
        __output = __output + __input
    if _input2 != "":
        __output = __output + "," + __input2
    if _reltion != "":
        __output = __output + "," + __relation
    if _replaceOLD != _replaceNEW:
        __output = __output.replace(_replaceOLD, _replaceNEW)
    if _replace2OLD != _replace2NEW:
        __output = __output.replace(_replace2OLD, _replace2NEW)
        
    
    f = open(_output, 'w')
    f.write(__output)
    f.close()

if __name__ == "__main__":
    func()