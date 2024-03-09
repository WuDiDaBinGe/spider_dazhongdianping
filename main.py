import time
import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from config import cookies, headers, restaurant_list_url, restaurant_score_url, restaurant_detail_url
import json
import re

COLSNAME = ['name', 'shopid', 'comment_num', 'avg_price', 'tag', 'address', 'score', 'city']

def get_one_restaurant_score(shop_id, city_code, headers):
    headers_new = dict()
    headers_new.update(headers)
    headers_new.update({
        'Referer': restaurant_detail_url.format(shop_id=shop_id)
    })
    params = {
        'shopId': shop_id,
        'cityId': f"{city_code}",
        'mainCategoryId': '116',
        '_token': 'eJxVT9tqg0AQ/Zd5Ft3VjTfIQ2hriWChuja1oQ/RXBRRV9fqNiX/3gnYh8LAucw5MPMDw/YIPiWEMKrBdBrAB6oT3QYNRokbh3ieY3qUeczRoPjnrRhFLx/eHsHf24RpDmWfdyNGvacry9ZcG52FWkhNhnPPbDEC5TgK6RvGPM/6sTq0omovetE1hiw7YdSuY2Wu5HmkxFf/PuBJgNWGYxWxXvCw4PinI/wBs7K6tMhOoeKJZLI/x5Hk6Xcqx5drpK68UiEv3GnT1dmz6EWwO9fB/PBhxnmjxNNOJUE4lWkgsjSO027jGnPCX9druP0C8SpZjQ==',
        'uuid': 'f9cf90d4-5478-f904-8bc9-38232123daf0.1709907336',
        'platform': '1',
        'partner': '150',
        'optimusCode': '10',
        'originUrl': restaurant_detail_url.format(shop_id=shop_id),
        'yodaReady': 'h5',
        'csecplatform': '4',
        'csecversion': '2.4.0',
        'mtgsig': '{"a1":"1.1","a2":1709972915421,"a3":"w6305110vu04586yyvz16u18uxuy4uxx81v8v3y4y3u9795826zyx309","a5":"74CX8hLlHPF8T423mzo0","a6":"hs1.4aOG4x69iuIGtADfqn9IKcSWvNNojhjXhi1qBoZlULMO6XviGO1n+jFSZBY9qZRkrokzFlaE80IU9dUW6ZWoN8A==","x0":4,"d1":"29ea2fbe3eb0af2f0da7d12f175a8099"}'
    }
    response = requests.get(
        url=restaurant_score_url,    
        params=params,
        cookies=cookies,
        headers=headers_new
    )
    if response.status_code == 200:
        data = json.loads(response.text)
        return data["fiveScore"]
    else:
        return ''
    



def get_restarurant_base(city, page):
    response = requests.get(restaurant_list_url.format(city=city, page=page), 
                            cookies=cookies, 
                            headers=headers)
    city_code = re.search(r"cityId: (.+),", response.text).group(1)

    def prase_one_item(div_element):
        # 解析name id
        title_info_a = div_element.find('div', class_='tit').find('a')
        name, shopid = title_info_a.get('title'),title_info_a.get('data-shopid')
        # 解析评价数目，平均价格
        comment_infos = div_element.find('div', class_='comment').find_all('a')
        comment_num = comment_infos[0].find('b').get_text()
        avg_price = comment_infos[1].find('b').get_text()
        # 解析标签， 地址
        comment_infos = div_element.find('div', class_='tag-addr').find_all('a')
        tag = comment_infos[0].find('span').get_text()
        address = comment_infos[1].find('span').get_text()
        score = get_one_restaurant_score(shop_id=shopid, city_code=city_code, headers=headers)
        return [name, shopid, comment_num, avg_price, tag, address, score]

    
    page = BeautifulSoup(response.text, 'lxml')

    main_list = page.find('div', class_='shop-list J_shop-list shop-all-list').find('ul')
    items = main_list.find_all('li')
    data = list()
    for item in tqdm(items):
        row = prase_one_item(item.find('div', class_='txt'))
        row = row + [city]
        data.append(row)
        time.sleep(5)
    return data 
    




def get_one_restaurant_info(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    assert response.status_code == 200, "Error fetching page"
    with open('./restaurant_info.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    return response.text


def main():
    all_data = list()
    for i in range(1, 11):
        print(f'fetching page {i}')
        data = get_restarurant_base(city='jinan', page=i)
        all_data.extend(data)
        print(f'page {i} done')
    pd.DataFrame(all_data, columns = COLSNAME).to_csv('./restaurant_info.csv', index=False)

if __name__ == '__main__':
    main()