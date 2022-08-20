import pandas as pd
import googlemaps


def get_ll_by_name(keyword, googleapikey):
    gmaps = googlemaps.Client(key=googleapikey)
    result = gmaps.geocode(keyword)
    lat = result[0]["geometry"]["location"]["lat"]
    lng = result[0]["geometry"]["location"]["lng"]
    dic = {"loc": keyword, "lat": lat, "lng": lng}
    return dic


def get_ll_by_address(file, googleapikey):
    df = pd.read_excel(file)
    address_list = []

    # もらったエクセルファイルから完全なデータフレームが得られなかったため
    # 条件を用いて全探索し住所を抽出した
    for column in df.columns:
        for i in range(len(df[column])):
            if ("東京都" in str(df[column][i])) or ("県" in str(df[column][i])):
                address_list.append(df[column][i])

    loc_dicts = []
    gmaps = googlemaps.Client(key=googleapikey)

    for address in address_list:
        geocode_result = gmaps.geocode(address)

        loc = address

        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]

        loc_dicts.append({"loc": loc, "lat": lat, "lng": lng})

    return loc_dicts
