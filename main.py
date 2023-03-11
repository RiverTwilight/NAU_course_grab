import requests
import time
import json
import datetime
import random

def grab():

   with open('config.json', 'r') as f:
    config_data = json.load(f)

    url = config_data['url']
    payload_data = json.dumps(config_data['data'])
    cookies = config_data['cookies']
    header = config_data['header']

    response = requests.post(url, data=payload_data, cookies=cookies, headers=header)

    res = response.text

    if "可以使用以下方式登录" in res:
        return "Cookie无效，请重新登录获取"

    if res and len(res) > 0 and res[0]['success'] == '0':
        print('抢课失败，原因：' + res[0]['msg'])
    else:
        print('抢课成功', + res[0]['msg'])

    return response.text


times = 1

while True:
    timestemp = str(datetime.datetime.now())
    print(f'第{times}次请求 ' + timestemp )
    res = grab()

    if times % 5 == 0:
        with open("log.md", "a", encoding="utf-8") as log_file:
            log_file.write(f'| {times} | {timestemp}  | {res} |\n')
            log_file.close()
            # clear the file content if it has more than 100 lines
            # if sum(1 for _ in open("log.md", encoding="utf-8")) > 100:
            #     log_file.truncate(0)
                
    times += 1
    sleep_seconds = random.randint(7, 13)
    time.sleep(sleep_seconds)
