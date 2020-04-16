import requests

# Ваш API-ключ: gT5fA5uh2f3vbkYxprGU6UYmQxD7uQA4
# Новый секретный ключ: dV3dGBU6zC85WE53ezNBZSKRVTkA8hxG

#{'BTC/USD': {'sell': [['7174.26', '0.00860289', 1586525126877], ['7174.279', '0.04612', 1586525124719], ['7174.80407', '0.00122252', 1586524622557], ['7178.36874', '0.0219342', 1586525126440], ['7178.37008', '0.00122422', 1586524507522], ['7178.37008', '0.00107308', 1586524349059], ['7182.01055', '0.026321', 1586525127303], ['7182.012', '0.00486288', 1586524169944], ['7188.16088', '0.0152321', 1586525128284], ['7188.16211', '0.0096', 1586519404809]], 'buy': [['7132.012', '0.01923689', 1586524310867], ['7126', '0.04997818', 1586522578121], ['7125', '0.0418895', 1586433963952], ['7121.96436', '0.002', 1586512140558], ['7.12E+3', '0.00028039', 1586514632078], ['7113.64202', '0.00175647', 1586194888611], ['7111.5652', '0.003', 1586221740451], ['7104.22462', '0.0175', 1586523928436], ['7101.05832', '0.0006', 1586204584685], ['7101.05832', '0.0118079', 1586505633124]]}, 'LTC/USD': {'sell': [['44.15699', '3.2334', 1586525093524], ['44.157', '1.07051231', 1586525092612], ['44.21994', '3.379391', 1586525101210], ['44.22', '1.68', 1586524860915], ['44.35027', '0.24762482', 1586521331643], ['44.49996', '0.152321', 1586524932795], ['44.5', '0.95566374', 1586506853869], ['44.55', '1.82', 1586517261478], ['44.87758', '3.5', 1586524639978], ['44.87874', '1.4268728', 1586514732141]], 'buy': [['43.9', '0.09296978', 1586524272609], ['43.799', '1.11215597', 1586523940382], ['43.79302', '0.1859704', 1586521335081], ['43.56255', '1.955666', 1586525095296], ['43.56251', '0.04665345', 1586512421271], ['43.56', '1.78', 1586512053893], ['43.5', '0.02641704', 1586254556528], ['43.255', '4.996', 1586524882435], ['43.23', '0.951', 1586494873512], ['43.15576', '0.14571058', 1586506744436]]}, 'ETH/USD': {'sell': [['164.19974', '0.45862867', 1586525126573], ['164.19975', '0.8409007', 1586525125615], ['164.19999', '0.09199054', 1586525115853], ['164.2', '0.04990001', 1586524814046], ['164.39994', '0.5839588', 1586525123760], ['164.4', '1.99', 1586525073459], ['165', '0.402', 1586519268844], ['165', '0.00339749', 1586517969645], ['165.5431', '0.4752', 1586504251018], ['166.1', '1.2', 1586503726731]], 'buy': [['163.20329', '0.309966', 1586521820458], ['163.20328', '0.54734137', 1586512698423], ['162.80024', '0.47597133', 1586525127565], ['162.80023', '1.4530764', 1586525126432], ['162.8', '0.42307139', 1586517002625], ['162.36', '1.49253056', 1586525022597], ['162.32009', '0.36964', 1586514728282], ['162.31999', '0.0309', 1586290626892], ['162', '0.5', 1586517226952], ['162', '0.1', 1586242693404]]}, 'XRP/USD': {'sell': [['0.19791', '56.57201913', 1586524739623], ['0.19985', '39.334801', 1586504195047], ['0.19999', '21.89568566', 1586500682406], ['0.2', '7', 1586501048266], ['0.2', '7', 1586503012711], ['0.20239', '9.92230281', 1586421523729], ['0.20245', '444.31484728', 1586497435265], ['0.2025', '567.84560511', 1586420767736], ['0.206', '158.43503285', 1586330252519], ['0.2069', '106.21098472', 1586390088228]], 'buy': [['0.19136', '59.3682553', 1586525051947], ['0.19135', '35.30826726', 1586524744087], ['0.18602', '50.13873444', 1586513278506], ['0.18401', '3.6E+2', 1586370823841], ['0.18401', '46.11014341', 1586335324488], ['0.183', '54.54662481', 1586383077637], ['0.1805', '13.82552955', 1586327754535], ['0.18011', '8.31327994', 1586297503465], ['0.1801', '24.29552402', 1586361086668], ['0.1801', '1.70229897', 1586292495714]]}, 'USDT/USD': {'sell': [['1.03898', '2.9216783', 1586524790608], ['1.03898', '18.28369571', 1586524846826], ['1.03899', '69.22928463', 1586524780808], ['1.039', '30.74', 1586169064402], ['1.04', '5', 1586211052790], ['1.04', '0.84973518', 1586171234889], ['1.0411', '2.3355', 1586239266669], ['1.042', '2.2328', 1586165095737], ['1.045', '5', 1586211055817], ['1.0461', '2.324', 1586239180197]], 'buy': [['1.02', '477.90953734', 1586502994961], ['1.018', '124.25222026', 1586493900848], ['1.017', '215.57654432', 1586493870051], ['1.011', '2.4346', 1586503924809], ['1.006', '2.5513', 1586503908551], ['1.00311', '0.99988496', 1586507156509], ['1.0031', '27.24339534', 1586504636275], ['1.00305', '5.4E+2', 1586505679886], ['1.00305', '8.43539203', 1586505569302], ['1.00304', '353.13782057', 1586492422039]]}, 'BTC/USDT': {'sell': [['6989.60382999', '0.00466035', 1586511461895], ['7007.32948628', '0.00010789', 1586508040766], ['7007.32948632', '0.0111', 1586501311989], ['7.03E+3', '0.00692', 1586509561843], ['7042.36613376', '0.0116', 1586501313116], ['7077.57796443', '0.0122', 1586502272582], ['7104', '0.00965', 1586495765976], ['7148.89956761', '0.0083', 1586501291780], ['7163.51447788', '0.01683121', 1586501353441], ['7178', '0.00128', 1586495488290]], 'buy': [['6.91E+3', '0.45506647', 1586521674795], ['6908.24396964', '0.0207', 1586502275545], ['6900.00000006', '0.00154989', 1586501685889], ['6883.1196647', '0.00231057', 1586439328961], ['6823.57351343', '0.01', 1586508939269], ['6823.57351341', '0.00244715', 1586439334305], ['6815', '0.00990495', 1586495725534], ['6809', '0.06754376', 1586512046770], ['6808', '0.00795', 1586265054006], ['6808', '0.00015495', 1586160377407]]}, 'ETH/USDT': {'sell': [['169', '0.01', 1586506405813], ['174', '0.01342255', 1586490235984], ['174', '0.00746', 1586437001266], ['175.00000000', '1.96527417', 1586435360679], ['175', '0.14676869', 1586462647261], ['175', '0.01868008', 1586339575601], ['179.00000000', '0.10000000', 1584410525148], ['195', '0.04447061', 1586244620620], ['199.00000000', '0.00500000', 1584527064904], ['203', '0.05960529', 1586249909823]], 'buy': [['159', '0.00260760', 1586511640722], ['159', '0.006278', 1586511879244], ['158.1', '0.03156872', 1586511781373], ['158', '0.06813637', 1586511140965], ['157', '0.06813637', 1586511113904], ['156', '0.06813637', 1586511092496], ['155.00000001', '0.06813637', 1586509593090], ['155', '0.20197643', 1586506912654], ['155', '0.10054611', 1586464487637], ['155', '0.10143032', 1586463689862]]}, 'XRP/BTC': {'sell': [['0.00002727', '66.9088', 1586525128284], ['0.00002728', '53.41276099', 1586525128064], ['0.00002728', '1281.8428', 1586525123973], ['0.00002735', '3E+3', 1586524835515], ['0.00002736', '371.07767985', 1586524037854], ['0.00002737', '184.53257181', 1586518950069], ['0.00002747', '364', 1586525109898], ['0.00002748', '6.87370219', 1586509121910], ['0.00002749', '62.24190276', 1586521113052], ['0.00002754', '56.57201913', 1586524741031]], 'buy': [['0.0000269', '69.5662', 1586525108353], ['0.00002689', '278.21794034', 1586524958645], ['0.00002689', '65.98441359', 1586524502919], ['0.00002688', '80.73912729', 1586523977109], ['0.0000268', '88.85573132', 1586520851649], ['0.00002676', '7.5E+2', 1586524477900], ['0.00002676', '33.7507982', 1586518961240], ['0.00002663', '35.61133788', 1586518966444], ['0.00002651', '37.56108743', 1586518971220], ['0.00002651', '6.17118659', 1586519211460]]}, 'ETH/BTC': {'sell': [['0.02290193', '0.00789893', 1586525126807], ['0.02290194', '5.97', 1586525120750], ['0.02292196', '5.45432174', 1586523995471], ['0.0230276', '0.01595712', 1586505715081], ['0.0230461', '1.99', 1586519119141], ['0.02304932', '0.4254', 1586505510605], ['0.02304932', '1.32792', 1586517495337], ['0.02309679', '1.7144', 1586505370167], ['0.0231089', '0.0195002', 1586506180352], ['0.0231089', '170.97041014', 1586502764998]], 'buy': [['0.02284253', '1.0847', 1586525123596], ['0.02283253', '0.32774019', 1586525117108], ['0.0227914', '0.11630219', 1586516370736], ['0.0226738', '0.09954694', 1586525122218], ['0.02267027', '1.1271', 1586516249497], ['0.02263318', '0.1229651', 1586516376500], ['0.02262328', '0.26413279', 1586505872343], ['0.02261', '0.233', 1586505977036], ['0.0226', '0.73498587', 1586522565021], ['0.02251601', '0.04618935', 1586524771357]]}, 'LTC/BTC': {'sell': [['0.00618632', '0.299', 1586525078135], ['0.00618634', '0.0567978', 1586525084118], ['0.0061866', '4.996', 1586525083096], ['0.0062006', '2.41264313', 1586525087339], ['0.00620061', '0.12587678', 1586523053102], ['0.00620822', '0.8216', 1586506219093], ['0.00622181', '0.38559909', 1586503275226], ['0.006223', '1.65', 1586516548462], ['0.00622764', '0.24762482', 1586521333088], ['0.00623086', '0.42776255', 1586504533738]], 'buy': [['0.00616', '0.16204597', 1586524735244], ['0.00614401', '0.44786267', 1586524756682], ['0.006144', '0.32493594', 1586524162146], ['0.00614245', '0.43083004', 1586516020121], ['0.0061166', '0.18650727', 1586525081751], ['0.00611575', '0.8', 1586506211823], ['0.0061', '4.668', 1586514762150], ['0.0061', '0.3003168', 1586508547618], ['0.00609872', '0.43391952', 1586508020452], ['0.00608', '0.42', 1586513658595]]}, 'BCH/BTC': {'sell': [['0.0341', '3.2E-7', 1586524211694], ['0.03416', '0.208', 1586524831162], ['0.03443997', '1.5562', 1586524274840], ['0.03443998', '0.00753892', 1586524272793], ['0.03444', '0.213', 1586522565639], ['0.0346', '0.2', 1586512648335], ['0.03472', '0.687', 1586520911500], ['0.03472', '0.0072418', 1586492960917], ['0.03472282', '0.02922106', 1586489823494], ['0.035', '0.395', 1586489418386]], 'buy': [['0.03391999', '1.03418123', 1586503029907], ['0.0336', '0.0566', 1586491538081], ['0.0334', '0.02988632', 1585913902234], ['0.03333', '2', 1586506468440], ['0.03332', '0.145', 1586472968112], ['0.03321001', '0.03613368', 1586524528898], ['0.03321', '0.6318139', 1586501247445], ['0.0331', '0.00541864', 1585422976329], ['0.03304', '1.32', 1586483849443], ['0.0328', '0.305', 1586317731513]]}, 'ZEC/BTC': {'sell': [['0.00523275', '0.10700844', 1586520793823], ['0.00524318', '0.13801309', 1586523769690], ['0.00528093', '0.13801309', 1586523771225], ['0.00531867', '8.9426', 1586525092307], ['0.00531868', '0.13801309', 1586523772819], ['0.0053564', '0.30436243', 1586524998853], ['0.00535643', '0.13801309', 1586523774261], ['0.00539418', '0.13801309', 1586523775700], ['0.00543193', '0.13801309', 1586523777201], ['0.00546968', '0.13801309', 1586523778737]], 'buy': [['0.00521483', '0.14010881', 1586515876743], ['0.00520541', '0.08449418', 1586523732191], ['0.00518218', '0.5466', 1586525116874], ['0.00518217', '0.77878495', 1586525111724], ['0.0051731', '0.21446229', 1586524992853], ['0.00516793', '0.08510697', 1586523733697], ['0.00513045', '0.08572871', 1586523735206], ['0.00509297', '0.0863596', 1586523736683], ['0.00507617', '0.2', 1586456415539], ['0.00505549', '0.08699984', 1586523738185]]}}

def restart():
    url = 'https://api.livecoin.net/exchange/all/order_book'
    res = requests.request("GET", url)
    exam = res.json()

    valuta = ['BTC/USD','LTC/USD','ETH/USD','XRP/USD','USDT/USD','BTC/USDT','ETH/USDT','XRP/BTC','ETH/BTC','LTC/BTC','BCH/BTC','ZEC/BTC',]
    live = {}

    for i in valuta:
        for k,v in exam.items():
            if k == i:
                del v['timestamp']
                v['sell'] = v.pop('bids')
                v['buy'] = v.pop('asks')
                live.update({k: {'sell': [v['sell'][0][0], v['sell'][0][1]],
                          'buy': [v['buy'][0][0], v['buy'][0][1]]}})

    return live



# alfa = {
#     "USDBTC": {
#         "asks": [["7400"], ["7395"], ["7390"]],
#         "bids": [["7401"], ["7405"], ["7410"]],
#     }
# }