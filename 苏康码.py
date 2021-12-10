import requests
s = requests.Session()
s.get('https://jsstm.jszwfw.gov.cn/jkmIndex.html?token=&uuid=YOUR_UUID')
headers1 = {
    'authority': 'jsstm.jszwfw.gov.cn',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://jsstm.jszwfw.gov.cn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://jsstm.jszwfw.gov.cn/jkmIndex.html?token=YOUR_TOKEN&uuid=YOUR_UUID',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = {
  'token': 'YOUR_TOKEN',
  'uuid': 'YOUR_UUID',
  'source': 'other'
}

AuthResponse = s.post('https://jsstm.jszwfw.gov.cn/jkm/userAuth', headers=headers1, data=data)

abc = (AuthResponse.json()['res']['userdetail']['abc'])

headers2 = {
    'authority': 'jsstm.jszwfw.gov.cn',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://jsstm.jszwfw.gov.cn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://jsstm.jszwfw.gov.cn/jkmIndex.html?token=YOUR_TOKEN&uuid=YOUR_UUID',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data2 = {
  'member_id': '身份证',
  'name': '姓名 ',
  'mobile': '手机',
  'idType': '1',
  'degree': '37.3',
  'realtimeLocation': '',
  'source': 'other',
  'degree_flag': '0',
  'r1data': '0',
  'r2data': '0',
  'r3data': '0',
  'travel': '0',
  'r5data': '',
  'travel_destination': '',
  'travel_time': '',
  'travel_duration': '',
  'travel_destination_code': '',
  'other': '',
  'abc':abc
}

response = s.post('https://jsstm.jszwfw.gov.cn/day/saveDailyAttendance', headers=headers2, data=data2)
print(response.text)
requests.get('https://sctapi.ftqq.com/推送key.send?title='+response.text)