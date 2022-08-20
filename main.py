from map_automation.api import get_ll_by_name, get_ll_by_address
from map_automation.fig import get_image
from map_automation.plot import plot

import sys

def main(keyword, file, googleapikey):

    O_dic = get_ll_by_name(keyword, googleapikey)
    loc_dicts = get_ll_by_address(file, googleapikey)

    get_image(O_dic, googleapikey)

    plot(O_dic, loc_dicts, keyword, file)


if __name__ == "__main__":
    args = sys.argv
    main(args[1], args[2], args[3])
