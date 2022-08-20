import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image
from geopy.distance import geodesic


def ll_to_pixel(O_dic: dict[str, float], dic: dict[str, float]):
    O_tup = (O_dic["lat"], O_dic["lng"])
    dis_km_x = geodesic((O_dic["lat"], dic["lng"]), O_tup).km
    dis_km_y = geodesic((dic["lat"], O_dic["lng"]), O_tup).km
    if O_dic["lng"] >= dic["lng"]:
        dis_km_x *= -1
    if O_dic["lat"] <= dic["lat"]:
        dis_km_y *= -1

    dis_pixel = (dis_km_x * (2 ** 21) / 40000, dis_km_y * (2 ** 21) / 40000)
    return dis_pixel


def plot(O_dic, loc_dicts, keyword, file):
    x = []
    y = []

    for dic in loc_dicts:
        x.append(ll_to_pixel(O_dic, dic)[0] + 320)
        y.append(ll_to_pixel(O_dic, dic)[1] + 240)

    fig = plt.figure(figsize=(6.4, 4.8), dpi=100)
    ax = fig.add_subplot(111)

    im = Image.open(f"./{keyword}.png")
    ax.imshow(im)

    ax.scatter(x, y, s=10, color="b")
    ax.set_xlim([0, 640])
    ax.set_ylim([480, 0])

    c1 = patches.Circle(xy=(320, 240), radius=60, fc="None", ec="r")
    ax.add_patch(c1)
    c2 = patches.Circle(xy=(320, 240), radius=120, fc="None", ec="r")
    ax.add_patch(c2)
    c3 = patches.Circle(xy=(320, 240), radius=180, fc="None", ec="r")
    ax.add_patch(c3)
    c4 = patches.Circle(xy=(320, 240), radius=240, fc="None", ec="r")
    ax.add_patch(c4)
    c5 = patches.Circle(xy=(320, 240), radius=300, fc="None", ec="r")
    ax.add_patch(c5)

    # ax.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)

    fig.savefig(file[:-5] + ".png")

