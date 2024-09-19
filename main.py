import requests
import re
import json
import webbrowser
import pyperclip
from collections import Counter

def 取角色uid(cookies):
    headers = {
        'Host': 'api-takumi.mihoyo.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; 23113RKC6C Build/PQ3A.190605.06200901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 miHoYoBBS/2.75.2',
        'Origin': 'https://act.mihoyo.com',
        'X-Requested-With': 'com.mihoyo.hyperion',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://act.mihoyo.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': '_MHYUUID=45512d30-0b96-445e-eaeb-133f0fa9291a; mi18nLang=zh-cn; aliyungf_tc=96e0012e3c4347d8a4e9dddfb6cfef0d4b756e5424dfed37eecbe9dff7a32662; DEVICEFP_SEED_ID=ac54b91d66bbeb59; DEVICEFP_SEED_TIME=1726622786449; DEVICEFP=38d7fe7840ff9; ltuid=158853294; login_ticket=W2rkreRJ0EF3jidetinfj9n4MtkCMjJlqUGbw7Ut; account_id=158853294; ltoken=kr2XoPV8LflVvrYoue3lCCWccPOhP4BVpnwzo0SS; cookie_token=5nEOYo9LLdGTKfsYOSzrE7UIi6BVEAtcF0rlgT22',
    }
    params = {'game_biz': 'nap_cn',}
    response = requests.get('https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie',params=params,cookies=cookies,headers=headers,verify=False)
    json = response.json()
    uid = json['data']['list'][0]['game_uid']
    return uid

def 取角色cookies():
    webbrowser.open('http://user.mihoyo.com/')
    cookies = {}
    文本 = r"var cookie=document.cookie;var ask=confirm('Cookie:'+cookie+'\n\nDo you want to copy the cookie to the clipboard?');if(ask==true){copy(cookie);msg=cookie}else{msg='Cancel'}"
    pyperclip.copy(文本)
    cookie_文本 = input('请粘贴浏览器返回的字符并按回车:')
    for cookie in cookie_文本.split(';'):
        key, value = cookie.strip().split('=')
        cookies[key] = value
    print(cookies)
    return cookies

def 取角色列表id(uid, cookies):
    headers = {
        'Host': 'api-takumi-record.mihoyo.com',
        'Connection': 'keep-alive',
        'x-rpc-platform': '2',
        'x-rpc-geetest_ext': '{"viewUid":"0","gameId":8,"page":"v1.1.4_#/zzz/roles/all","isHost":1}',
        'x-rpc-app_version': '2.75.2',
        'x-rpc-language': 'zh-cn',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; 23113RKC6C Build/PQ3A.190605.06200901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 miHoYoBBS/2.75.2',
        'x-rpc-device_id': '06770e63-c0e8-38da-89bd-1a1e504b6bfd',
        'Accept': 'application/json, text/plain, */*',
        'x-rpc-device_name': 'Redmi%2023113RKC6C',
        'x-rpc-page': 'v1.1.4_#/zzz/roles/all',
        'x-rpc-device_fp': '38d7fe73b1032',
        'x-rpc-lang': 'zh-cn',
        'x-rpc-sys_version': '9',
        'Origin': 'https://act.mihoyo.com',
        'X-Requested-With': 'com.mihoyo.hyperion',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://act.mihoyo.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    params = {'server': 'prod_gf_cn','role_id': uid,}
    response = requests.get('https://api-takumi-record.mihoyo.com/event/game_record_zzz/api/zzz/avatar/basic',params=params,cookies=cookies,headers=headers,verify=False)
    json = response.json()
    角色id字典 = {}
    for jso in json['data']['avatar_list']:
        键 = ''.join(re.findall(r'[\u4e00-\u9fff0-9]+', str(jso['full_name_mi18n'])))
        值 = str(jso['id'])
        角色id字典[键] = 值
    return 角色id字典

def 取角色装备(cookies, 角色id):
    headers = {
        'Host': 'api-takumi-record.mihoyo.com',
        'Connection': 'keep-alive',
        'x-rpc-platform': '2',
        'x-rpc-geetest_ext': f'{{"viewUid":"0","gameId":8,"page":"v1.1.4_#/zzz/roles/{角色id}/detail","isHost":1}}',
        'x-rpc-app_version': '2.75.2',
        'x-rpc-language': 'zh-cn',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; 23113RKC6C Build/PQ3A.190605.06200901; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 miHoYoBBS/2.75.2',
        'x-rpc-device_id': '06770e63-c0e8-38da-89bd-1a1e504b6bfd',
        'Accept': 'application/json, text/plain, */*',
        'x-rpc-device_name': 'Redmi%2023113RKC6C',
        'x-rpc-page': f'v1.1.4_#/zzz/roles/{角色id}/detail',
        'x-rpc-device_fp': '38d7fe73b1032',
        'x-rpc-lang': 'zh-cn',
        'x-rpc-sys_version': '9',
        'Origin': 'https://act.mihoyo.com',
        'X-Requested-With': 'com.mihoyo.hyperion',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://act.mihoyo.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    response = requests.get(f'https://api-takumi-record.mihoyo.com/event/game_record_zzz/api/zzz/avatar/info?id_list[]={角色id}&need_wiki=true&server=prod_gf_cn&role_id=14177799',cookies=cookies,headers=headers,verify=False)
    json = response.json()
    return json

def 读取字典(字典名):
    with open(f"./json/{字典名}.txt", 'r', encoding='utf-8') as file:
        读取的库 = json.load(file)
    return 读取的库

def 保存字典(字典, 字典名):
    # 将字典转换为字符串并保存到文本文件
    with open(f"./save/{字典名}.txt", "w", encoding="utf-8") as file:
        json.dump(字典, file, ensure_ascii=False, indent=4)

def 转浮点数(值):
    try:
        if '%' in 值:
            数 = float(值.replace('%', '')) / 100
            数 = round(数, 3)
            return 数
        else:
            return round(float(值), 3)
    except ValueError:
        print(f"无法将字符串转换为浮点数: {值}")
        return 值

def 取驱动盘主属性返回字典(号, json):
    驱动盘主属性字典 = {}
    try:
        驱动盘主属性字典['驱动盘名'] = json['data']['avatar_list'][0]['equip'][号 - 1]['equip_suit']['name']
    except:
        驱动盘主属性字典['驱动盘名'] = '未佩戴驱动盘'
    驱动盘主属性字典['驱动盘号'] = 号
    if 号 == 1:
        驱动盘主属性 = '小生命值'
    elif 号 == 2:
        驱动盘主属性 = '小攻击力'
    elif 号 == 3:
        驱动盘主属性 = '小防御力'
    else:
        try:
            驱动盘主属性 = json['data']['avatar_list'][0]['equip'][号 - 1]['main_properties'][0]['property_name']
        except:
            驱动盘主属性 = '无'
    try:
        驱动盘主属性值 = 转浮点数(json['data']['avatar_list'][0]['equip'][号 - 1]['main_properties'][0]['base'])
    except:
        驱动盘主属性值 = 0
    驱动盘主属性字典[驱动盘主属性] = 驱动盘主属性值
    return 驱动盘主属性字典

def 取驱动盘随机属性返回字典(号, json):
    驱动盘随机属性字典 = {}
    for i in [0,1,2,3]:
        try:
            驱动盘随机属性 = json['data']['avatar_list'][0]['equip'][号 - 1]['properties'][i]['property_name']
            驱动盘随机属性值 = 转浮点数(json['data']['avatar_list'][0]['equip'][号 - 1]['properties'][i]['base'])
            if 驱动盘随机属性 == '生命值':
                if 驱动盘随机属性值 > 1:
                    驱动盘随机属性 = '小生命值'
            if 驱动盘随机属性 == '攻击力':
                if 驱动盘随机属性值 > 1:
                    驱动盘随机属性 = '小攻击力'
            if 驱动盘随机属性 == '防御力':
                if 驱动盘随机属性值 > 1:
                    驱动盘随机属性 = '小防御力'
            驱动盘随机属性字典[驱动盘随机属性] = 驱动盘随机属性值
        except:
            驱动盘随机属性字典[f'{i + 1}无'] = 0
    return 驱动盘随机属性字典

def 识别驱动盘两件套(字典1, 字典2, 字典3, 字典4, 字典5, 字典6):
    strings = [字典1['驱动盘名'], 字典2['驱动盘名'], 字典3['驱动盘名'], 字典4['驱动盘名'], 字典5['驱动盘名'], 字典6['驱动盘名']]
    套装 = Counter(strings)
    驱动盘两件套 = []
    索引 = 0
    for 键,值 in 套装.items():
        if 值 > 1:
            if 索引 >= len(驱动盘两件套):
                驱动盘两件套.extend([None] * (索引 + 1 - len(驱动盘两件套)))

            驱动盘两件套[索引] = 键  # 然后进行赋值
            索引 += 1
    while '未佩戴驱动盘' in 驱动盘两件套:
        驱动盘两件套.remove('未佩戴驱动盘')
    return 驱动盘两件套

def 加载两件套属性库(两件套列表):
    两件套装数据 = 读取字典("驱动盘套装库")
    两件套属性 = {}
    for i in 两件套列表:
        两件套属性.update(两件套装数据[i])
    return 两件套属性

def main():
    角色列表 = 读取字典("角色库")
    音擎列表 = 读取字典("音擎库")
    cookies = 取角色cookies()
    uid = 取角色uid(cookies)
    角色id字典 = 取角色列表id(uid, cookies)
    for 键, 值 in 角色id字典.items():
        角色整体属性 = {}
        角色整体属性.clear()

        json = 取角色装备(cookies, 值)
        角色属性 = 角色列表[键]
        try:
            音擎名 = json['data']['avatar_list'][0]['weapon']['name']
            音擎属性 = 音擎列表[音擎名]
        except:
            音擎属性 = {"音擎名": "未佩戴音擎","基础攻击力": 0,"无": 0}


        驱动盘主属性字典1 = 取驱动盘主属性返回字典(1, json)
        驱动盘主属性字典2 = 取驱动盘主属性返回字典(2, json)
        驱动盘主属性字典3 = 取驱动盘主属性返回字典(3, json)
        驱动盘主属性字典4 = 取驱动盘主属性返回字典(4, json)
        驱动盘主属性字典5 = 取驱动盘主属性返回字典(5, json)
        驱动盘主属性字典6 = 取驱动盘主属性返回字典(6, json)

        驱动盘两件套 = 识别驱动盘两件套(驱动盘主属性字典1, 驱动盘主属性字典2, 驱动盘主属性字典3, 驱动盘主属性字典4, 驱动盘主属性字典5, 驱动盘主属性字典6)
        两件套属性 = 加载两件套属性库(驱动盘两件套)

        驱动盘随机属性字典1 = 取驱动盘随机属性返回字典(1, json)
        驱动盘随机属性字典2 = 取驱动盘随机属性返回字典(2, json)
        驱动盘随机属性字典3 = 取驱动盘随机属性返回字典(3, json)
        驱动盘随机属性字典4 = 取驱动盘随机属性返回字典(4, json)
        驱动盘随机属性字典5 = 取驱动盘随机属性返回字典(5, json)
        驱动盘随机属性字典6 = 取驱动盘随机属性返回字典(6, json)

        print(驱动盘主属性字典1)
        print(驱动盘主属性字典2)
        print(驱动盘主属性字典3)
        print(驱动盘主属性字典4)
        print(驱动盘主属性字典5)
        print(驱动盘主属性字典6)
        print(驱动盘随机属性字典1)
        print(驱动盘随机属性字典2)
        print(驱动盘随机属性字典3)
        print(驱动盘随机属性字典4)
        print(驱动盘随机属性字典5)
        print(驱动盘随机属性字典6)

        角色整体属性["角色属性"] = 角色属性
        角色整体属性["音擎属性"] = 音擎属性
        角色整体属性["两件套属性"] = 两件套属性
        角色整体属性["驱动盘主属性1"] = 驱动盘主属性字典1
        角色整体属性["驱动盘主属性2"] = 驱动盘主属性字典2
        角色整体属性["驱动盘主属性3"] = 驱动盘主属性字典3
        角色整体属性["驱动盘主属性4"] = 驱动盘主属性字典4
        角色整体属性["驱动盘主属性5"] = 驱动盘主属性字典5
        角色整体属性["驱动盘主属性6"] = 驱动盘主属性字典6
        角色整体属性["驱动盘随机属性1"] = 驱动盘随机属性字典1
        角色整体属性["驱动盘随机属性2"] = 驱动盘随机属性字典2
        角色整体属性["驱动盘随机属性3"] = 驱动盘随机属性字典3
        角色整体属性["驱动盘随机属性4"] = 驱动盘随机属性字典4
        角色整体属性["驱动盘随机属性5"] = 驱动盘随机属性字典5
        角色整体属性["驱动盘随机属性6"] = 驱动盘随机属性字典6
        角色整体属性["核心技属性"] = {'无' : 0}

        保存字典(角色整体属性, 键)
        print(键)


if __name__ == "__main__":
    main()