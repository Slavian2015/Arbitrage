
import json
import os





main_path_data = os.path.abspath("./data")


def com():
    #################################   COMMISSIONS   ##########################################
    if os.path.isfile(main_path_data + "\\commis.json"):
        pass
    else:
        dictionary= {"main": {
            "hot": 1.0006,
            "alfa": 1.002,
            "live": 1.0018
                            }}
        com = json.dumps(dictionary, indent=4)

        # Writing to sample.json
        with open(main_path_data + "\\commis.json", "w") as outfile:
            outfile.write(com)
            outfile.close()
            pass
    return

def reg():

    #################################      REGIMS      ##########################################

    if os.path.isfile(main_path_data + "\\regim.json"):
        pass
    else:
        dictionary = {"1": {"option": "off",
                           "val1": "",
                           "val2": "",
                           "val3": "",
                           "birga1": "",
                           "birga2": "",
                           "profit": "",
                           "order": "",
                            "per": ""
                            }}
        regim = json.dumps(dictionary, indent=4)

        # Writing to sample.json
        with open(main_path_data + "\\regim.json", "w") as outfile:
            outfile.write(regim)
            outfile.close()
            pass

    return