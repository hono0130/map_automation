import urllib
import urllib.error
import urllib.request


def get_image(dic, googleapikey):

    lat = dic["lat"]
    lng = dic["lng"]
    loc = dic["loc"]

    # htmlの設定
    html1 = "https://maps.googleapis.com/maps/api/staticmap?center="

    # maptypeで取得する地図の種類を設定
    html2 = "&maptype=terrain"

    # sizeでピクセル数を設定
    html3 = "&size=640x480"

    # sensorはGPSの情報を使用する場合にtrueとするので今回はfalseで設定
    html4 = "&sensor=false"

    # zoomで地図の縮尺を設定
    html5 = "&zoom=13"

    # マーカーの位置の設定（マーカーを表示させてくなければ無でも大丈夫）
    html6 = "&markers="

    # key="googleから取得したキーコード"となるように設定
    html7 = "&key="

    html8 = "&style=feature:poi|visibility:off"

    axis = str(lat) + "," + str(lng)

    url = (
        html1
        + axis
        + html2
        + html3
        + html4
        + html5
        + html6
        + axis
        + html7
        + googleapikey
        + html8
    )

    dst_path = str(loc) + ".png"

    try:
        data = urllib.request.urlopen(url).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)

    except urllib.error.URLError as e:
        print(e)
