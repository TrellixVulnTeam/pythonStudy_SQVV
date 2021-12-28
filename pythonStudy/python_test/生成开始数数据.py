# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 15:28
# @Author  : sunfukai
# @Email   : zcshiyonghao@163.com
# @File    : 生成开始数数据.py
# @Software: PyCharm
import json
# 下单链接
url = '4710860528288147'

# 开始数采集数据
_res = {'code': 0, 'data': {'pc_url': 'https://weibo.com/3867347143/L4wtx7ydZ', 'mweb_url': 'https://m.weibo.cn/3867347143/4710781511799859', 'blog': {'attitudes_count': 21152, 'comments_count': 838, 'reposts_count': 492, 'nickname': '雅思预测教育', 'text': '⏱临近年底,12.4旧题考试季正当时!本场难度在前几场的基础上进一步下调!即便平时基础一般的同学们在难度降低的大背景与旧题的加持下反馈能够剩余足够的检查时间!\n\n✍🏻错过12.4的考生们也不用过于惋惜,年末时段接下来仍有富余的时间供大家复习!珍惜当下预测备考的每一秒,考场上的你便能继续迎来旧题所带来的惊喜!\n\n📍中国大陆考区命中快报:\n🎯12.4听力原题命中S2/3!!! \n（S2:科技博物馆、S3:职业规划）\nS2/3＝考前突击小范围\n☆本场听力整体综合难度偏低,同时S2、S3两篇连续旧题锦上添花!由于填空题较多,同学们在考场上回忆时务必多注意答案词拼写、单复数等细节!\n\n🎯12.4阅读原题命中两篇!!!\n(P2:文学、P3:蜜蜂)\n蜜蜂＝考前极重点篇目\n文学＝考前突击小范围\n☆本场大赦天下同时体现在将难度较大的P2与压轴P3投放旧题,这也直接削减了阅读科目大部分难题!剩余一篇低于两星难度的新题文章基础一般的同学们也皆可较为轻松应对!\n\n🎯12.4写作Task1 教育类柱图原题类似命中!!!\n男女生完成作业时间与成绩对比＝考前极重点篇目\n☆常规对比类柱图题型,根据例文对比框架作答即可.\n\n（🤗接下来的同学们可自行进入预测链接找到今天12.4考试的预测篇目并删除,不用再准备,考过的题目同一考区两年内不会再考）', 'uid': 3867347143, 'blog_id': 'L4wtx7ydZ'}, 'count': 0, 'nickname': 'Yolandaery', 'text': '有旧题做起来爽到爆完全不用担心时间不够[哈哈]跟我平时做题完全两个体验 http://t.cn/RnwGFSR', 'uid': 1705949337}}

parameter={}

# 分类商品的参数格式
parameter["start_number"] = _res.get('data', {})['count']
parameter["weibo_nickname"] = _res.get('data', {})['nickname']
parameter["content"] = _res.get('data', {})['text']
parameter["second_url"] = url
parameter["uid"] = _res.get('data', {})['uid']
parameter["pc_url"] = _res.get('data', {}).get('pc_url', '')
parameter["mweb_url"] = _res.get('data', {}).get('mweb_url', '')
parameter["info"] = json.dumps(_res['data'])
parameter['start_info'] = _res['data']
print(parameter)