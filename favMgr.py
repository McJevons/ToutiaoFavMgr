import requests
import json
import pandas as pd


def main():

    # 读取必要信息，包括request参数，url，列信息等
    with open('doc/info.json', 'r', encoding='utf-8') as f:
        info = json.load(f)

    url = info['url']
    headers = info['headers']
    querystring = info['querystring']
    tags_keys = info['tags'].keys()
    tags_values = info['tags'].values()

    fav_list, err = get_fav_list(url, headers, querystring, tags_keys)

    if err == '':
        make_table(fav_list, tags_values)
        # make_html(fav_list, tags_values)
    else:
        print(err)


def make_table(fav_list, tags_values):
    """导出列表为excel文件"""
    table = pd.DataFrame(fav_list, columns=tags_values)
    table.to_excel('doc/myFav.xlsx', encoding='utf-8', index=False)
    print('成功')


def make_html(fav_list, tags_values):
    """导出列表为html"""
    table = pd.DataFrame(fav_list, columns=tags_values)
    h = table.to_html(render_links=True)
    with open('doc/myFav.html', 'w', encoding='utf-8') as f:
        f.write(h)
    print('成功')


def get_fav_list(url, headers, querystring, tags):
    """
    访问url，将返回数据组装成列表
        returns
        fav_list : 收藏列表
        err : 错误信息
    """
    fav_list = []
    n = 1

    while True:
        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        if response.status_code == 200:
            fav_list, err, has_more = make_fav_list(response.json(), querystring, tags,
                                                    fav_list)
            if err == 'failed':
                break
            elif not has_more:
                print('没有更多数据')
                break
            print('第%d页' % n)
            n = n+1
            # if n > 3:
            #     break
        else:
            err = 'wrong request'
            break
    return fav_list, err


def make_fav_list(json_data, querystring, tags, fav_list):
    """
    将json根据所需的列组装成列表，同时替换querystring中的'max_repin_time'
        returns
        fav_list:收藏列表
        err:错误信息
        has_more:是否还有数据
    """
    err = ''
    if json_data['message'] == 'success':
        querystring['max_repin_time'] = json_data['max_repin_time']
        for data in json_data['data']:
            fav_list.append(
                [data[tag] if tag in data.keys() else '--' for tag in tags])
    else:
        err = 'failed'
    return fav_list, err, json_data['has_more']


if __name__ == '__main__':
    main()
