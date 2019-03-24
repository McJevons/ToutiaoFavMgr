import requests
import json


def main():
    n = 0
    for i in range(2):
        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()
            if data['message'] == 'success':
                querystring['max_repin_time'] = data['max_repin_time']

                for x in data['data']:
                    n = n + 1
                    print('第%d条：%s' % (n, x['title']))
            else:
                print('no data')
                break
            print('第%d次请求' % i)
        else:
            print('wrong request')
            break


if __name__ == '__main__':
    url = "https://www.toutiao.com/c/user/favourite/"

    with open('doc/info.json', 'r') as f:
        j = json.load(f)

    headers, querystring = j['headers'], j['querystring']

    main()
