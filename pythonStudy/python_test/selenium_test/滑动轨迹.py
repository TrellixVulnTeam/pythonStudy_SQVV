# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 18:58
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : 滑动轨迹.py
# @Software: PyCharm
import numpy as np
import math


def ease_out_quad(x):
    return 1 - (1 - x) * (1 - x)


def ease_out_quart(x):
    return 1 - pow(1 - x, 4)


def ease_out_expo(x):
    if x == 1:
        return 1
    else:
        return 1 - pow(2, -10 * x)


def get_tracks(distance, seconds, ease_func):
    tracks = [0]
    offsets = [0]
    for t in np.arange(0.0, seconds, 0.1):
        ease = globals()[ease_func]
        offset = round(ease(t / seconds) * distance)
        tracks.append(offset - offsets[-1])
        offsets.append(offset)
    return offsets, tracks


# def drag_and_drop(browser, offset):
#     knob = browser.find_element_by_class_name("gt_slider_knob")
#     offsets, tracks = easing.get_tracks(offset, 12, 'ease_out_expo')
#     ActionChains(browser).click_and_hold(knob).perform()
#     for x in tracks:
#         ActionChains(browser).move_by_offset(x, 0).perform()
#     ActionChains(browser).pause(0.5).release().perform()

if __name__ == '__main__':
    print(get_tracks(100,5,'ease_out_expo'))