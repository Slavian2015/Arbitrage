import Hot_parser
import Live_parser
import A_parser
import pandas as pd
from functools import reduce

##############################        BALANCE          #############################

def balance():
    Alfa = A_parser.wallet_a()
    Hot = Hot_parser.wallet_h()
    Live = Live_parser.wallet_l()

    dfa = pd.DataFrame(Alfa.items(), columns=['Valuta', 'alfa'])
    dfh = pd.DataFrame(Hot.items(), columns=['Valuta', 'hot'])
    dfl = pd.DataFrame(Live.items(), columns=['Valuta', 'live'])


    data_frames = [dfl, dfh, dfa]
    valuta = reduce(lambda left, right: pd.merge(left, right, on=['Valuta'],
                                                 how='outer'), data_frames).fillna('0')

    valuta['alfa'] = valuta['alfa'].apply(pd.to_numeric, errors='coerce')
    valuta['live'] = valuta['live'].apply(pd.to_numeric, errors='coerce')
    valuta['hot'] = valuta['hot'].apply(pd.to_numeric, errors='coerce')

    valuta.loc[:,"Summa"] = (valuta.loc[:,"alfa"] + valuta.loc[:,"live"] + valuta.loc[:,"hot"])

    valuta = valuta[['Valuta', 'alfa', 'hot', 'live', 'Summa']]



    return valuta