import pandas as pd
import json
import os
import datetime as dt
import time
import Orders
from decimal import ROUND_UP,Context
import requests

main_path_data = os.path.abspath("./data")
start11 = time.process_time()
def avtomat(dft, valuta, start11):

    ##########################    Telegram    ################################

    ad = open(main_path_data + "\\keys.json", "r")
    js_object = json.load(ad)
    ad.close()
    input1 = js_object["4"]['key']
    input2 = js_object["4"]['api']
    def bot_sendtext(bot_message):
        ### Send text message
        bot_token = input1
        bot_chatID = input2
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        requests.get(send_text)
        return




    def all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol, reponse_b1, reponse_b2):

        ###################    APPEND to CSV   all_data    #####################

        done = (time.process_time() - start11)
        now = dt.datetime.now()
        df_all = pd.read_csv(main_path_data + "\\all_data.csv")
        timer2 = now.strftime("%H:%M:%S")
        df2 = pd.DataFrame({"TIME": [timer2],
                            "birga_x": [birga_1],
                            "birga_y": [birga_2],
                            "rates_x": [rate1],
                            "rates_y": [rate2],
                            "valin_x": [val1],
                            "valin_y": [val2],
                            "valout_y": [val4],
                            "start": [val1_vol],
                            "step": [val2_vol],
                            "back": [val4_vol],
                            "profit": [(float(val4_vol) - float(val1_vol))],
                            "perc": [(((float(val4_vol) - float(val1_vol)) / float(val1_vol)) * 100)],
                            "res_birga1": [reponse_b1],
                            "res_birga2": [reponse_b2],
                            "timer": [done],
                            }, index=[0])
        df_all = df2.append(df_all)
        df_all.to_csv(main_path_data + "\\all_data.csv", header=True, index=False)
        profit = (float(val4_vol) - float(val1_vol))
        perc = (((float(val4_vol) - float(val1_vol)) / float(val1_vol)) * 100)
        nl = '\n'
        val1_vol = ("{:.6f}".format(val1_vol))
        val2_vol = ("{:.6f}".format(val2_vol))
        val4_vol = ("{:.6f}".format(val4_vol))
        profit = ("{:.6f}".format(profit))
        perc = ("{:.2f}".format(perc))
        bot_sendtext(f" ЕСТЬ ВИЛКА: {nl} {birga_1} / {birga_2} {nl} {val1} -> {val2} -> {val4} {nl} {val1_vol} -> {val2_vol} -> {val4_vol} {nl} {profit} {nl} {perc} {nl} ")
        return

    all_cardsBD = dft
    all_cardsBD.index += 1
    all_cardsBD['start'] = all_cardsBD['start'].apply(pd.to_numeric, errors='coerce')
    all_cardsBD['volume'] = all_cardsBD['volume'].apply(pd.to_numeric, errors='coerce')
    all_cardsBD['back'] = all_cardsBD['back'].apply(pd.to_numeric, errors='coerce')
    all_cardsBD['step'] = all_cardsBD['step'].apply(pd.to_numeric, errors='coerce')


    USD_fil = all_cardsBD[(all_cardsBD['valin_x'] == "USD") | (all_cardsBD['valin_x'] == "USDT")]
    BTC_fil = all_cardsBD[(all_cardsBD['valin_x'] == "BTC") & (all_cardsBD['valin_y'].isin(["USD", "USDT"]))]
    BTC_fil_main = all_cardsBD[(all_cardsBD['valin_x'] == "BTC") & (~all_cardsBD['valin_y'].isin(["USD", "USDT"]))]
    BTC_fil_main2 = all_cardsBD[(all_cardsBD['valin_y'] == "BTC") & (~all_cardsBD['valin_x'].isin(["USD", "USDT"]))]


    # print( 'BTC_fil', BTC_fil )


    def order(regims, birga_1, birga_2, val1_vol, val1, rate1, val2_vol, val2, val3_vol, val3, rate2, val4_vol, val4):

        # print('val1', val1)
        # print('val3', val3)
        # print('val2', val2)
        # print('val4', val4)

        filter1 = valuta[valuta['Valuta'] == val1]
        filter3 = valuta[valuta['Valuta'] == val3]

        if filter1.shape[0]<1:
            dict = {'Valuta': val1, 'alfa': 0, 'live': 0, 'hot': 0}
            filter1 = pd.DataFrame([dict])
        else:
            pass

        if filter3.shape[0]<1:
            dict = {'Valuta': val3, 'alfa': 0, 'live': 0, 'hot': 0}
            filter3 = pd.DataFrame([dict])
        else:
            pass

        # print('filter1', filter1)
        # print('filter3', filter3)

        a_file = open(main_path_data + "\\regim.json", "r")
        regim = json.load(a_file)
        a_file.close()
        parametr1 = "{}/{}".format(val1, val2)
        para1 = ['BTC/USD', 'LTC/USD', 'ETH/USD', 'XRP/USD', 'USDT/USD', 'BTC/USDT', 'ETH/USDT', 'XRP/BTC', 'ETH/BTC',
                 'LTC/BTC', 'BCH/BTC', 'ZEC/BTC', 'PZM/USD', 'PZM/USDT', 'PZM/BTC']
        for i in para1:
            if i == parametr1:
                parad = "ok"
                pass
            else:
                parad = "no"
                pass

        # print('regim', regim)
        # print('regims', regims)
        # print('regims type', type(regims))


        # print('regim[regims]["order"]',  regim[str(regims)]["order"])

        if parad == 'ok':
            kurs = (float(rate1) / float(val1_vol))
            kurs2 = (float(val3_vol) / float(val4_vol))
            kurs0 = (float(val2_vol) / float(val1_vol))
            minA = regim[str(regims)]["order"]
            minB = minA * kurs0


            # print("filter1.iloc[0][birga_1]", filter1.iloc[0][birga_1])

            if filter1.iloc[0][birga_1] > float(val1_vol) and filter3.iloc[0][birga_2] > float(val3_vol):

                minbeta = (((float(val1_vol) - float(val2_vol) * float(rate1)) / (
                        float(val2_vol) * float(rate1))) * 100)
                minbeta = Context(prec=2, rounding=ROUND_UP).create_decimal(minbeta)
                minbeta = float(minbeta)

                if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                    if birga_1 == 'alfa' and birga_2 == 'live':
                        if val2 != 'USD' or val2 != 'USDT':
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'live' and birga_2 == 'alfa':
                        if val2 != 'USD' or val2 != 'USDT':
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'alfa' and birga_2 == 'hot':
                        if val2 != 'USD' or val2 != 'USDT':
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'hot' and birga_2 == 'alfa':
                        if val2 != 'USD' or val2 != 'USDT':
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'hot' and birga_2 == 'live':
                        if val2 != 'USD' or val2 != 'USDT':
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'live' and birga_2 == 'hot':
                        if val2 != 'USD' or val2 != 'USDT':
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    else:
                        return
                elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                    if birga_1 == 'alfa' and birga_2 == 'live':
                        if val2 != "BTC":
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'live' and birga_2 == 'alfa':
                        if val2 != "BTC":
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'alfa' and birga_2 == 'hot':
                        if val2 != "BTC":
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'hot' and birga_2 == 'alfa':
                        if val2 != "BTC":
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'hot' and birga_2 == 'live':
                        if val2 != "BTC":
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'live' and birga_2 == 'hot':
                        if val2 != "BTC":
                            val2_vol = val2_vol + (val2_vol * minbeta / 100)
                            reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    else:
                        return
            elif filter1.iloc[0][birga_1] < float(val1_vol) and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][
                birga_1] > minA or filter3.iloc[0][birga_2] < float(val3_vol) and filter3.iloc[0][birga_2] > minB and \
                    filter1.iloc[0][birga_1] > minA:
                # if filter1.iloc[0][birga_1] > minA and filter3.iloc[0][birga_2] > minB:
                minOrder1 = float(filter1.iloc[0][birga_1] * kurs)
                minOrder2 = float(filter3.iloc[0][birga_2])
                if minOrder2 > minOrder1:
                    val1_vol = filter1.iloc[0][birga_1]
                    val2_vol = minOrder1
                    val3_vol = minOrder1
                    val4_vol = minOrder1 / kurs2

                    print("val1_vol :", val1_vol)
                    print("val2_vol :", val2_vol)
                    print("val3_vol :", val3_vol)
                    print("val4_vol :", val4_vol)
                    print("val4_vol :", val4_vol)
                    print("val4_vol :", val4_vol)
                    print("kurs :", kurs)
                    print("kurs2 :", kurs2)
                    print("kurs0 :", kurs0)
                    print("minA :", minA)
                    print("minB :", minB)

                    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        else:
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    "No Such Command", "No Such Command")
                            return
                    elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        else:
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val3_vol, val4_vol,
                                    "No Such Command", "No Such Command")
                            return
                elif minOrder2 < minOrder1:
                    val1_vol = minOrder2 / kurs
                    val2_vol = minOrder2
                    val3_vol = minOrder2
                    val4_vol = minOrder2 / kurs2

                    print("val1_vol :", val1_vol)
                    print("val2_vol :", val2_vol)
                    print("val3_vol :", val3_vol)
                    print("val4_vol :", val4_vol)
                    print("val4_vol :", val4_vol)
                    print("val4_vol :", val4_vol)
                    print("kurs :", kurs)
                    print("kurs2 :", kurs2)
                    print("kurs0 :", kurs0)
                    print("minA :", minA)
                    print("minB :", minB)

                    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        else:
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    "No Such Command", "No Such Command")
                            return
                    elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        else:
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    "No Such Command", "No Such Command")
                            return
                else:
                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                            "Not Enough Money", "Not Enough Money")
                    return
            elif filter1.iloc[0][birga_1] < minA or filter3.iloc[0][birga_2] < minB:
                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                        "Not Enough Money", "Not Enough Money")
                return
            else:
                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                        "Not Enough Money", "Not Enough Money")
                return
        elif parad == 'no':
            kurs = (float(val1_vol) * float(val2_vol))
            kurs2 = (float(val4_vol) / float(val3_vol))
            kurs0 = (float(val1_vol) / float(val2_vol))
            minB = regim[str(regims)]["order"]
            minA = minB * kurs0
            if filter1.iloc[0][birga_1] > float(val1_vol) and filter3.iloc[0][birga_2] > float(val3_vol):
                if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                    if birga_1 == 'alfa' and birga_2 == 'live':
                        if val2 != 'USD' or val2 != 'USDT':
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'live' and birga_2 == 'alfa':
                        if val2 != 'USD' or val2 != 'USDT':
                            reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'alfa' and birga_2 == 'hot':
                        if val2 != 'USD' or val2 != 'USDT':
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'hot' and birga_2 == 'alfa':
                        if val2 != 'USD' or val2 != 'USDT':
                            reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'hot' and birga_2 == 'live':
                        if val2 != 'USD' or val2 != 'USDT':
                            reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'live' and birga_2 == 'hot':
                        if val2 != 'USD' or val2 != 'USDT':
                            reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    else:
                        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                "No Such Command", "No Such Command")
                        return
                elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                    if birga_1 == 'alfa' and birga_2 == 'live':
                        if val2 != "BTC":
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'live' and birga_2 == 'alfa':
                        if val2 != "BTC":
                            reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'alfa' and birga_2 == 'hot':
                        if val2 != "BTC":
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'hot' and birga_2 == 'alfa':
                        if val2 != "BTC":
                            reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'hot' and birga_2 == 'live':
                        if val2 != "BTC":
                            reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    elif birga_1 == 'live' and birga_2 == 'hot':
                        if val2 != "BTC":
                            reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                        else:
                            reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                            reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    reponse_b1, reponse_b2)
                            return
                    else:
                        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                "No Such Command", "No Such Command")
                        return
            elif filter1.iloc[0][birga_1] < float(val1_vol) and filter3.iloc[0][birga_2] > minB and filter1.iloc[0][
                birga_1] > minA or filter3.iloc[0][birga_2] < float(val3_vol) and filter3.iloc[0][birga_2] > minB and \
                    filter1.iloc[0][birga_1] > minA:
                minbeta = (((float(val1_vol) - float(val2_vol) * float(rate1)) / (
                        float(val2_vol) * float(rate1))) * 100)
                minbeta = Context(prec=2, rounding=ROUND_UP).create_decimal(minbeta)
                minbeta = float(minbeta)
                min1 = (float(filter1.iloc[0][birga_1]) - (float(filter1.iloc[0][birga_1]) * minbeta / 100)) / float(
                    rate1)
                min2 = float(filter3.iloc[0][birga_2])

                if min2 > min1:
                    val1_vol = filter1.iloc[0][birga_1]
                    val2_vol = min1
                    val3_vol = min1 - (min1 * minbeta / 100)
                    val4_vol = min1 * kurs2

                    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        else:
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                    val4_vol,
                                    "No Such Command", "No Such Command")
                            return
                    elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol,
                                        val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        else:
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    "No Such Command", "No Such Command")
                            return
                elif min2 < min1:
                    val1_vol = (float(filter3.iloc[0][birga_2]) + (
                                float(filter3.iloc[0][birga_2]) * minbeta / 100)) * float(rate1)
                    val2_vol = (float(filter3.iloc[0][birga_2]) + (float(filter3.iloc[0][birga_2]) * minbeta / 100))
                    val3_vol = float(filter3.iloc[0][birga_2])
                    val4_vol = float(filter3.iloc[0][birga_2]) * kurs2

                    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != 'USD' or val2 != 'USDT':
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        else:
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    "No Such Command", "No Such Command")
                            return
                    elif val1 != 'USD' or val1 != 'USDT' or val2 != 'USD' or val2 != 'USDT':
                        if birga_1 == 'alfa' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'alfa' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.alfa(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'alfa':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.alfa(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'hot' and birga_2 == 'live':
                            if val2 != "BTC":
                                reponse_b1 = Orders.hot(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.hot(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.live(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        elif birga_1 == 'live' and birga_2 == 'hot':
                            if val2 != "BTC":
                                reponse_b1 = Orders.live(val1, val2, rate1, val2_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val3_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                            else:
                                reponse_b1 = Orders.live(val1, val2, rate1, val1_vol)
                                reponse_b2 = Orders.hot(val3, val4, rate2, val4_vol)
                                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                        reponse_b1, reponse_b2)
                                return
                        else:
                            all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                                    "No Such Command", "No Such Command")
                            return
                else:
                    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                            "No Such Command", "No Such Command")
                    return
            elif filter1.iloc[0][birga_1] < minA or filter3.iloc[0][birga_2] < minB:
                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                        "Not Enough Money", "Not Enough Money")
                return
            else:
                all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                        "Not Enough Money", "Not Enough Money")
                return
        else:
            pass

        return


    if USD_fil.shape[0]>0:
        for ind in USD_fil.index:
            rate11 = (USD_fil['start'][ind] / USD_fil['step'][ind])
            rate22 = (USD_fil['back'][ind] / USD_fil['step'][ind])
            step = (USD_fil['volume'][ind] * rate11)
            step2 = (rate22 * USD_fil['volume'][ind])

            regims = USD_fil['regim'][ind]
            birga_1 = USD_fil['birga_x'][ind]
            birga_2 = USD_fil['birga_y'][ind]


            val1_vol = step
            val1 = USD_fil['valin_x'][ind]
            rate1 = USD_fil['rates_x'][ind]
            val2_vol = USD_fil['volume'][ind]
            val2 = USD_fil['valin_y'][ind]

            val3_vol = USD_fil['volume'][ind]
            val3 = USD_fil['valin_y'][ind]
            rate2 = USD_fil['rates_y'][ind]
            val4_vol = step2
            val4 = USD_fil['valout_y'][ind]

            order(regims, birga_1, birga_2, val1_vol, val1, rate1, val2_vol, val2, val3_vol, val3, rate2, val4_vol, val4)
        return
    else:
        pass
    if BTC_fil.shape[0] > 0:
        for ind in BTC_fil.index:
            rate11 = (BTC_fil['step'][ind] / BTC_fil['start'][ind])
            rate22 = (BTC_fil['step'][ind] / BTC_fil['back'][ind])
            step = (BTC_fil['volume'][ind] * rate11)
            step2 =(step / rate22)
            regims = BTC_fil['regim'][ind]
            birga_1 = BTC_fil['birga_x'][ind]
            birga_2 = BTC_fil['birga_y'][ind]
            val1_vol = BTC_fil['volume'][ind]
            val1 = BTC_fil['valin_x'][ind]
            rate1 = BTC_fil['rates_x'][ind]
            val2_vol = step
            val2 = BTC_fil['valin_y'][ind]
            val3_vol = step
            val3 = BTC_fil['valin_y'][ind]
            rate2 = BTC_fil['rates_y'][ind]
            val4_vol = step2
            val4 = BTC_fil['valout_y'][ind]
            order(regims, birga_1, birga_2, val1_vol, val1, rate1, val2_vol, val2, val3_vol, val3, rate2, val4_vol,
                  val4)
            return
    else:
        pass
    if BTC_fil_main.shape[0]>0:
        for ind in BTC_fil_main.index:
            rate11 = (BTC_fil_main['start'][ind] / BTC_fil_main['step'][ind])
            rate22 = (BTC_fil_main['back'][ind] / BTC_fil_main['step'][ind])
            step = (BTC_fil_main['volume'][ind] * rate11)
            step2 = (rate22 * BTC_fil_main['volume'][ind])

            regims = BTC_fil_main['regim'][ind]
            birga_1 = BTC_fil_main['birga_x'][ind]
            birga_2 = BTC_fil_main['birga_y'][ind]


            val1_vol = step
            val1 = BTC_fil_main['valin_x'][ind]
            rate1 = BTC_fil_main['rates_x'][ind]
            val2_vol = BTC_fil_main['volume'][ind]
            val2 = BTC_fil_main['valin_y'][ind]

            val3_vol = BTC_fil_main['volume'][ind]
            val3 = BTC_fil_main['valin_y'][ind]
            rate2 = BTC_fil_main['rates_y'][ind]
            val4_vol = step2
            val4 = BTC_fil_main['valout_y'][ind]


            order(regims, birga_1, birga_2, val1_vol, val1, rate1, val2_vol, val2, val3_vol, val3, rate2, val4_vol,
                  val4)
            return
    else:
        pass
    if BTC_fil_main2.shape[0] > 0:
        for ind in BTC_fil_main2.index:
            rate11 = (BTC_fil_main2['step'][ind] / BTC_fil_main2['start'][ind])
            rate22 = (BTC_fil_main2['step'][ind] / BTC_fil_main2['back'][ind])
            step = (BTC_fil_main2['volume'][ind] * rate11)
            step2 =(step / rate22)

            regims = BTC_fil_main2['regim'][ind]
            birga_1 = BTC_fil_main2['birga_x'][ind]
            birga_2 = BTC_fil_main2['birga_y'][ind]
            val1_vol = BTC_fil_main2['volume'][ind]
            val1 = BTC_fil_main2['valin_x'][ind]
            rate1 = BTC_fil_main2['rates_x'][ind]
            val2_vol = step
            val2 = BTC_fil_main2['valin_y'][ind]
            val3_vol = step
            val3 = BTC_fil_main2['valin_y'][ind]
            rate2 = BTC_fil_main2['rates_y'][ind]
            val4_vol = step2
            val4 = BTC_fil_main2['valout_y'][ind]
            order(regims, birga_1, birga_2, val1_vol, val1, rate1, val2_vol, val2, val3_vol, val3, rate2, val4_vol,
                  val4)
            return
    else:
        pass

# dft = pd.read_csv(main_path_data + "\\test.csv")
# valuta = pd.read_csv(main_path_data + "\\balance.csv")
#
# print('dft', dft)
#
# avtomat(dft, valuta, start11)