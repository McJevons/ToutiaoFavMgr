import requests
import json
import pandas as pd


def main():
    url = "https://www.toutiao.com/c/user/favourite/"
    # request所需参数保存在info中
    with open('doc/info.json', 'r') as f:
        info = json.load(f)
    headers, querystring = info['headers'], info['querystring']

    # tags为需要读取的列
    # tags = [
    #     'title', 'chinese_tag', 'display_url', 'source', 'source_url',
    #     'abstract'
    # ]
    tags = ['title', 'chinese_tag', 'display_url', 'source']

    fav_list, err = get_fav_list(url, headers, querystring, tags)
    if err == '':
        make_table(fav_list, tags)
        # print(fav_list)
    else:
        print(err)
        make_table(fav_list, tags)


def make_table(fav_list, tags):
    table = pd.DataFrame(fav_list, columns=tags)
    table.to_excel('doc/myFav.xlsx')
    # print(table)


def get_fav_list(url, headers, querystring, tags):
    '''发送request请求，获取返回数据，并返回收藏列表'''
    fav_list = []
    err = ''
    # for i in range(2):
    while True:
        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        if response.status_code == 200:
            fav_list, err = make_fav_list(response.json(), querystring, tags,
                                          fav_list)
            if err == 'failed':
                break
        else:
            err = 'wrong request'
            break
    return fav_list, err


def make_fav_list(json_data, querystring, tags, fav_list):
    '''将查询结果组装成列表并返回'''
    err = ''
    if json_data['message'] == 'success':
        querystring['max_repin_time'] = json_data['max_repin_time']
        for data in json_data['data']:
            fav_list.append(
                [data[tag] if tag in data.keys() else '--' for tag in tags])
    else:
        err = 'failed'
    return fav_list, err


if __name__ == '__main__':
    main()
