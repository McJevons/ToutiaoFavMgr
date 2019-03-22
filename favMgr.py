import requests


def main():
    n = 0
    for i in range(5):
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

    querystring = {
        "page_type": "2",
        "user_id": "4020899592",
        "max_behot_time": "0",
        "count": "20",
        "as": "A135AC79948868E",
        "cp": "5C946816480ECE1",
        "_signature": "BiQpGxAVWraOEdjDVf7z6gYkKQ",
        "max_repin_time": "0"
    }

    headers = {
        'accept':
        "application/json, text/javascript",
        'accept-encoding':
        "gzip, deflate, br",
        'accept-language':
        "zh-CN,zh;q=0.9",
        'content-type':
        "application/x-www-form-urlencoded",
        'cookie':
        "tt_webid=6669916608644924942; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16993afb74bca-0c23301f9374c-38395c0b-1fa400-16993afb74c10e; tt_webid=6669916608644924942; csrftoken=f01db60935dabddc0f00b7343ad55d88; sso_uid_tt=95ba842556aef37a71d129923f088b0d; toutiao_sso_user=ba55620de54f46b4a1997c99494c499c; login_flag=11c4601f9406844bf11c2b89df7312a5; __tea_sdk__ssid=23a82a89-bbda-4fc2-a1fa-6743b0310fe8; _ga=GA1.2.220163845.1552964138; ccid=ba55620de54f46b4a1997c99494c499c; sid_guard=ba55620de54f46b4a1997c99494c499c%7C1552964270%7C3021181%7CTue%2C+23-Apr-2019+02%3A10%3A51+GMT; uid_tt=95ba842556aef37a71d129923f088b0d; sid_tt=ba55620de54f46b4a1997c99494c499c; sessionid=ba55620de54f46b4a1997c99494c499c; _gid=GA1.2.1690204862.1553224921; __tasessionId=ofi3p61891553236365665; CNZZDATA1259612802=1556106449-1552958926-%7C1553234280; s_v_web_id=ef355e783897fb8d3e152e8a126c1ef9",
        'referer':
        "https://www.toutiao.com/c/user/4020899592/",
        'user-agent':
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        'x-requested-with':
        "XMLHttpRequest",
        'cache-control':
        "no-cache",
        'postman-token':
        "7aaa2344-4e76-c42b-862c-911d1b965922"
    }

    main()
