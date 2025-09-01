# -*- coding: utf-8 -*-

# shared_main.py
from inc import func as fu

def run_main(users, main_user):

    # Import
    hundoI = f'input/{main_user}/hundo.txt'
    luckyI = f'input/{main_user}/lucky.txt'
    shinyI = f'input/{main_user}/shiny.txt'
    xxlI = f'input/{main_user}/xxl.txt'
    xxsI = f'input/{main_user}/xxs.txt'
    level1I = 'input/perlibug/level1.txt'
    
    # Export
    deleteE = f'output/{main_user}/delete.txt'
    deletetradeE = f'output/{main_user}/deletetrade.txt'
    fakehundosE = f'output/{main_user}/fakehundos.txt'
    newhundoE = f'output/{main_user}/newhundo.txt'
    kmE = f'output/{main_user}/trade/km.txt'
    nontagE = f'output/{main_user}/nontag.txt'
    perlinalevel1E = f'output/{main_user}/trade/perlibug_level1.txt'
    pvpE = f'output/{main_user}/pvp.txt'
    pvptradeE = f'output/{main_user}/trade/pvptrade.txt'
    ratandfishE = f'output/{main_user}/trade/ratandfish.txt'
    xlcandyE = f'output/{main_user}/trade/tag_xlcandy.txt'
    gmaxxlcandyE = f'output/{main_user}/trade/gmaxxlcandy.txt'
    
    xxlE = f'output/Klozy/{main_user}/xxl.txt'
    xxsE = f'output/Klozy/{main_user}/xxs.txt'
    
    luckycheckE = f'output/{main_user}/check/lucky.txt'
    hundocheckE = f'output/{main_user}/check/hundo.txt'
    xxlcheckE = f'output/{main_user}/check/xxl.txt'
    xxscheckE = f'output/{main_user}/check/xxs.txt'
    shinycheckE = f'output/{main_user}/check/shiny.txt'
    
    listE = f'output/Klozy/{main_user}/lucky+hundo.txt'
    listhundoE = f'output/Klozy/{main_user}/hundo.txt'
    listluckyE = f'output/Klozy/{main_user}/lucky.txt'
    trade_xlcandyE = f'output/Klozy/{main_user}/#trade_xlcandy.txt'
    trade_xlcandyKmE = f'output/Klozy/{main_user}/#Vietnam_xlcandy.txt'
    trade_hundoKmE = f'output/Klozy/{main_user}/#Vietnam_hundo.txt'
    
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
    pvpEN = 'input/relation/pvpEN.txt'
    ratandfish = 'input/relation/ratandfish.txt'
    gmax = 'input/relation/gmax.txt'
    gmaxcandyxl = 'input/relation/gmaxcandyxl.txt'
    
    def main():
        fu.func("", "", newhundoE, hundoR, ",4*", "4*", "", "", "") # hundo check
        
        if users[main_user] == 0:
            fu.func("", "", fakehundosE, fakehundosDE, ",+Raupy", "+Raupy", "", "", "")
        # else: nichts machen
    
        # pvp
        if users[main_user] == 0:
            fu.func("", "", pvpE, pvpDE,  ",0-2", "0-2", "", "", "")
        else:
            fu.func("", "", pvpE, pvpEN,  ",0-2", "0-2", "", "", "")
            
        if users[main_user] == 0:
            fu.func(countCandyXL, "", pvptradeE, pvpDE,  ",0-2", "&0-2", "", "", "")
        else:
            fu.func(countCandyXL, "", pvptradeE, pvpEN,  ",0-2", "&0-2", "", "", "")
    
        if users[main_user] == 0:
            fu.func(ratandfish, "", ratandfishE, disableDE,  "!XXL&!XXS&", "", ",&", "&", "")
        else:
            fu.func(ratandfish, "", ratandfishE, disableEN,  "!XXL&!XXS&", "", ",&", "&", "")
        
        
            
        if users[main_user] == 0:
            fu.func(gmax, gmaxcandyxl, gmaxxlcandyE, disableDE,  ",&", "&", "", "", "")
        else:
            fu.func(gmax, gmaxcandyxl, gmaxxlcandyE, disableEN,  ",&", "&", "", "", "")
            
        # Listen für andere User (außer erster und letzter)
        other_users = list(users.keys())[1:-1]
        for i in other_users:
            fu.func(hundoI, "", trade_hundoKmE.replace('Klozy', i), "",  ",&", "&", "", "", "&#Vietnam") #trade tag and countcandy
            fu.func(countCandyXL, "", trade_xlcandyE.replace('Klozy', i), "",  ",&", "&", "", "", "&#trade") #trade tag and countcandy
            fu.func(countCandyXL, "", trade_xlcandyKmE.replace('Klozy', i), "",  ",&", "&", "", "", "&#Vietnam") #trade tag and countcandy
            if users[i] == 0:
                fu.func(hundoI, luckyI, listE.replace('Klozy', i), disableDE, ",&", "&", "", "", "")
                fu.func(hundoI, "", listhundoE.replace('Klozy', i), disableDE, ",&", "&", "", "", "")
                fu.func("", luckyI, listluckyE.replace('Klozy', i), disableDE, ",&", "&", "", "", "")
                
            else:
                fu.func(hundoI, luckyI, listE.replace('Klozy', i), disableEN, ",&", "&", "", "", "")
                fu.func(hundoI, "", listhundoE.replace('Klozy', i), disableEN, ",&", "&", "", "", "") 
                fu.func("", luckyI, listluckyE.replace('Klozy', i), disableEN, ",&", "&", "", "", "") 
        
        # Delete Traded Pokemon
        if users[main_user] == 0:
            fu.func("", "", deletetradeE, disableDE,  ",&!Getauscht", "Getauscht", "Entfernung0-101&", "", "")
        else:
            fu.func("", "", deletetradeE, disableEN,  ",&!Traded", "Traded", "", "", "")
        
        # Delete
        if users[main_user] == 0:
            fu.func("", "", deleteE, disableDE, ",&", "", "", "", "")
        else:
            fu.func("", "", deleteE, disableEN, ",&", "", "", "", "")
        
        # km
        if users[main_user] == 0:
            fu.func("", "", kmE, disableDE, "Entfernung0-101", "!Entfernung0-101", ",&", "", "")
        else:
            fu.func("", "", kmE, disableEN, "", "", ",&", "", "&!distance0-101")
    
        # no tag
        fu.func("", "", nontagE, "", "", "!#", "", "", "")
        
        # checks
        if users[main_user] == 0:
            fu.func(luckyI, "", luckycheckE, luckyCheckDE, "", "", "", "", "")
        else:
            fu.func(luckyI, "", luckycheckE, luckyCheckEN, "", "", "", "", "")
        
        fu.func(hundoI, "", hundocheckE, "", "", "", "", "", "&4*")
        fu.func(xxlI, "", xxlcheckE, "", "", "", "", "", "&xxl")
        fu.func(xxsI, "", xxscheckE, "", "", "", "", "", "&xxs")
        fu.func(shinyI, "", shinycheckE, "", "", "", "", "", "&shiny")
        
        # XXL
        for i in other_users:
            if users[i] == 0:
                fu.func(xxlI, "", xxlE.replace('Klozy', i), disableDE, ",&", "&", "!XXL", "XXL", "")
            else:
                fu.func(xxlI, "", xxlE.replace('Klozy', i), disableEN, ",&", "&", "!XXL", "XXL", "")
    
        # XXS
        for i in other_users:
            if users[i] == 0:
                fu.func(xxsI, "", xxsE.replace('Klozy', i), disableDE, ",&", "&", "!XXS", "XXS", "")
            else:
                fu.func(xxsI, "", xxsE.replace('Klozy', i), disableEN, ",&", "&", "!XXS", "XXS", "")
            
        # Spezialfall perlibug
        if main_user == 'perlibug':
            for i in other_users:
                if users[i] == 0:
                    fu.func(level1I, level1, perlinalevel1E.replace(main_user, i), disableDE, ",&", "&", "", "", "")
                else: 
                    fu.func(level1I, level1, perlinalevel1E.replace(main_user, i), disableEN, ",&", "&", "", "", "")
                    
        # trade
        if users[main_user] == 0:
            fu.func(countCandyXL, "", xlcandyE, disableDE,  ",&", "&", "", "", "")
        else:  
            fu.func(countCandyXL, "", xlcandyE, disableEN,  ",&", "&", "", "", "")

            
        
    main()            
    if __name__ == "__main__":
        main()