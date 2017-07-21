#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#
# shodan_ips.py
# Search SHODAN and print a list of IPs matching the query
#
# Author: starnight

import shodan
import time
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Configuration
SHODAN_API_KEY = "P4lLw6oMythJiajvVNeMQb83hRBtv24C"
api = shodan.Shodan(SHODAN_API_KEY)


# 用来显示程序运行时间
def show_time(t):
    if t < 60:
        return str(t) + 's'
    if t < 3600:
        return str(t / 60) + 'm:' + str(t % 60) + 's'
    else:
        return str(t / 3600) + 'h:' + str(t % 3600 / 60) + 'm:' + str(t % 3600 % 60) + 's'


# 从Shodan获取数据
def getShodan():
    # 搜索 Shodan
    # Shodan.search(query, page=1, limit=None, offset=None, facets=None, minify=True)：查询Shodan数据clear
    # 输入查询语句
    query = raw_input('please input search query : ')
    filename = raw_input('please input file name to save data : ')

    starttime = time.time()                 # 开始计时

    results = api.search(query)             # 先获取一些总览信息
    total = results['total']                # 总的搜索结果数

    num = total / 100 + 1                   # 总的循环次数

    print 'Total results %d , pages : %d' % (total, num)
    file1 = filename + '.txt'                  # 构造文件名,保存搜索结果
    file2 = filename + '-full.txt'
    file3 = filename + '-all.txt'
    fp1 = open(file1, 'w+')                 # 打开文件
    fp2 = open(file2, 'w+')
    fp3 = open(file3, 'w+')

    for i in range(1, num, 1):
        try:
            results = api.search(query, page=i)                 # 逐页查询结果,不去重
            endtime = time.time()                               # 显示程序运行时间
            print 'page %d ... left: %d time: %s ' % (i, num - i, show_time(int(endtime - starttime)))
            for result in results['matches']:                   # 将想要的信息保存在文件中
                # fp1.write(result['ip_str'] + ':' + str(result['port']) + '\n')
                # *.txt只保存ip & port
                fp1.write(result['ip_str'] + ' | ' + str(result['port']) + '\n')
                # *.full 保存更多比较重要的内容,如:主机名、域名、国家、城市、经度、维度
                fp2.write(result['ip_str'] + ' | ' + str(result['port']) + ' | ' + result['transport'] + ' | ' +
                          str(result['hostnames']) + ' | ' + str(result['domains']) + ' | ' +
                          str(result['location']['country_name']) + ' | ' +
                          str(result['location']['city']) + ' | ' +
                          str(result['location']['longitude']) + ' | ' +
                          str(result['location']['latitude']) + '\n')
                # data保存能从shodan获取的最多的数据,某些字段无法获取
                data = {
                    # "asn": result['asn'],
                    # "ip": result['ip'],
                    "ip_str": result['ip_str'],
                    # "ip_str": result['ipv6'],
                    "port": result['port'],
                    "timestamp": result['timestamp'],
                    "hostnames": [
                        result['hostnames']
                    ],
                    "domains": [
                        result['domains']
                    ],
                    "location": {
                        "city": result['location']['city'],
                        "country_code": result['location']['country_code'],
                        "country_code3": result['location']['country_code3'],
                        "country_name": result['location']['country_name'],
                        "dma_code": result['location']['dma_code'],

                        "latitude": result['location']['latitude'],
                        "longitude": result['location']['longitude'],
                        "postal_code": result['location']['postal_code'],
                        "region_code": result['location']['region_code']
                    },
                    "org": result['org'],
                    "isp": result['isp'],
                    "os": result['os'],
                    "transport": result['transport'],
                    # "data": result['data'],
                }
                # print type(data)
                data_str = json.dumps(data)
                # 写入到文件
                json.dump(data, fp3)
                fp3.write('\n')

        # 如果出现像'Error: Unable to parse JSON response'的异常,表示无法从shodan获取数据,直接跳过,可能是网络原因,不必浪费时间
        except shodan.APIError, e:
            print 'Error: %s' % e
            continue

    # 输出程序运行时间,并关闭相关的文件
    endtime = time.time()
    print 'program time consuming : %s s' % show_time(int(endtime - starttime))
    fp1.close()
    fp2.close()
    fp3.close()

if __name__ == '__main__':
    getShodan()

