import concurrent
from concurrent.futures import ThreadPoolExecutor

import requests
import tls_client
import uuid
import json
import random
import time
import string


time2 = int(time.time() * 1000)
session = tls_client.Session(client_identifier="chrome110", random_tls_extension_order=True)
skus = ["H085945CKAS", "H056289CK0W", "H073444CC18", "H085956CC8Q", "H073428CC10", "H056277CK89", "H075180CC18", "H073428CK8L", "H056289CK10", "H079086CKI2", "H085945CKAB", "H075180CKM8", "H069426CKAD", "H085956CC67", "H079086CK09", "H073428CKS2", "H075180CC0M", "H060991CK18", "H079086CC10", "H075180CC0L", "H056289CK8Q", "H056289CCI2", "H069426CKBF", "H073428CK10", "H073428CKI2", "H079086CK2Z", "H073444CK18", "H073428CK18", "H073444CK89", "H085956CC37", "H073444CCT0", "H082027CK18", "H082027CC18", "H056289CK0L", "H079086CK3Y", "H082027CC37", "H073428CC4B", "H079086CKX9", "H056289CCM4", "H073428CKQ1", "H069426CCAV", "H075180CK80", "H073597CC37", "H079086CKQ1", "H079086CCD2", "H069426CCCR", "H073428CCQ1", "H079086CC4B", "H085945CCAH", "H085956CK89", "H056289CC89", "H085956CKI8", "H073428CC18", "H075180CC8F", "H086418CKAC", "H085956CC18", "H073444CKI2", "H079086CCS2", "H056289CC08", "H085956CK09", "H056277CC18", "H085956CK37", "H079086CK6O", "H079086CK37", "H073428CK89", "H073428CC08", "H079086CC6O", "H085956CC89", "H079086CC37", "H056289CC10", "H056289CK09", "H073428CCD2", "H073428CC89", "H056289CK08", "H079086CCQ1", "H060991CC18", "H079086CK10", "H056277CK18", "H077913CK34", "H085945CCAD", "H073444CC89", "H060991CC89", "H079086CC0L", "H073428CK08", "H056289CKX9", "H073444CK0S", "H069426CKCR", "H056289CC0W", "H079086CC2Z", "H075180CK37", "H079086CC89", "H069426CKAV", "H079086CKD2", "H079086CCI2", "H079086CC18", "H056289CCQ1", "H079086CK18", "H073444CCI2", "H060991CC37", "H056289CK8L", "H079086CK0L", "H085945CKAD", "H069426CCCI", "H056289CC37", "H056289CKI2", "H056289CK89", "H056289CC18", "H075180CC80", "H056289CK3Q", "H079086CC08", "H079086CK4B", "H073428CK37", "H075180CK8L", "H069426CCEE", "H075180CC37", "H073428CK0L", "H085956CK8Q", "H069426CKCI", "H069426CCBF", "H069426CKDW", "H073428KC18", "H056289CC8Q", "H073444CKB4", "H060991CK89", "H073428CK09", "H079086CK8L", "H073428CCI2", "H079086CK08", "H073428CC8L", "H056289CK18", "H079086CC8L", "H075180CC8L", "H079086CK89", "H085956CKO0", "H079086CKS2", "H056289CC0M", "H085945CCAC", "H075180CK18", "H085956CK18", "H056289CK37", "H085945CCAB", "H073428CCS2", "H079086CC3Y", "H056289CC0L", "H073428CC37", "H073428CC0L"]

def monitor(xsrf_token, correlation_id, ECOM_SESS, datadome, proxy=None):
    headers = {
        'Host': 'bck.hermes.com',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr-FR,fr;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'x-xsrf-token': xsrf_token,
        'x-hermes-locale': 'de_de',
        'Origin': 'https://www.hermes.com',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.hermes.com/',
        'Cookie': f'x-xsrf-token={xsrf_token}; ECOM_SESS={ECOM_SESS}; correlation_id={correlation_id}; _cs_mk=0.9533126918465247_{(time.time() * 1000)}; rskxRunCookie=0; rCookie=c9w46qn1lfjmndn11n54xalmf46csu; _ga=GA1.2.48296570.1694450631; _cs_c=1; datadome={datadome}; lastRskxRun={(time.time() * 1000)}; _gat_UA-64545050-1=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
    }
    sku = random.choice(skus)
    url = f'https://bck.hermes.com/product?locale=de_de&productsku={sku}'
    sess = tls_client.Session(client_identifier="chrome110", random_tls_extension_order=True)
    r = sess.get(url, headers=headers, proxy=proxy)
    print(f'sku: {sku}, status: {r.status_code}')

def get_datadome(locale):
    ok = False
    i = 0
    while not ok:
        if i > 5:
            return
        i += 1
        xx = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        ip = f"user-mountain123-region-{locale}-sessid-{xx}-sesstime-185-keep-true:132465acb@pr-eu-vip.roxlabs.cn:4600"
        data = {
            'locale': locale,
            'ip': ip
        }
        headers = {'Content-Type': 'application/json'}
        url = "http://43.134.55.229:13468/monitor"
        r = requests.post(url, headers=headers, data=json.dumps(data, separators=(',', ':')))
        if r.status_code == 200 and "ip" not in r.json():
            ok = True
        print(f"response: {r.text}, ip: {ip}")
    return r, ip


def main():
    region = "de"
    response, ip = get_datadome(region)
    data = json.loads(response.text)
    xsrf_token = str(uuid.uuid4())
    datadome = data['datadome']
    correlation_id = str(uuid.uuid4())
    ECOM_SESS = str(uuid.uuid4())
    new_proxy = f"http://{ip}"
    futures = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        # 将下载任务分配给线程池
        for _ in range(10):
            future = executor.submit(monitor, xsrf_token, correlation_id, ECOM_SESS, datadome, new_proxy)
            futures.append(future)
        # 等待所有监测任务完成
        for future in concurrent.futures.as_completed(futures):
            pass

if __name__ == '__main__':
    main()