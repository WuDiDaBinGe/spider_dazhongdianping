# window.shop_config = {
#     userId: 70333952,
#     shopId: "k873Y8sTbMxpuqXr",
#     shopCityId: 22,
#     shopName: '西堤牛排',
#     address: '泉城路188号恒隆广场西翼3层372室',
#     publicTransit: '3路、K59路、151路、5路',
#     cityId: "22",
#     cityCnName: "济南",
#     cityName: "济南",
#     cityEnName: "jinan",
#     isOverseasCity: 0,
#     power: 5,
#     shopPower: 45,
#     voteTotal: 0,
#     district: 0,
#     shopType: 10,
#     mainRegionId: 66666,
#     categoryURLName: "food",
#     shopGroupId: "k873Y8sTbMxpuqXr",
#     loadUserDomain: "//www.dianping.com",
#     map: {
#         power: 5,
#         manaScore: "0"
#     },
#     mainCategoryId: 116,
#     defaultPic: "http://p0.meituan.net/biztone/714280094_1666078627391.jpeg%40300w_225h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20",
#     textCssVersion: "qo767wnn8n",
#     shopEvtId: "k873Y8sTbMxpuqXr"
# }

import requests

cookies = {
    '_lxsdk_cuid': '18e1e6b54dcc8-0e409e117e53ca-4c657b58-144000-18e1e6b54dcc8',
    '_lxsdk': '18e1e6b54dcc8-0e409e117e53ca-4c657b58-144000-18e1e6b54dcc8',
    '_hc.v': 'f9cf90d4-5478-f904-8bc9-38232123daf0.1709907336',
    'WEBDFPID': 'w6305110vu04586yyvz16u18uxuy4uxx81v8v3y4y3u9795826zyx309-2025267336381-1709907334556UWEASQWfd79fef3d01d5e9aadc18ccd4d0c95072918',
    'qruuid': '9caf3b3d-6c37-4a97-a67c-7c443f18dd39',
    'dper': '02021523de75c23e3f08fc06fe3e8fee3f5d52c1af202c10cd4d5aefd632254bf2b8d9d1c90e7fe5dcbad30e89e6ba97c1dc637393af850dae2d00000000a81e00009f05daa1b0327aa84e7549bc7aeeb50495e40495b761207c1e145f338d98b68a48e6f957aa302b3b4ffa4b0afea88d07',
    'll': '7fd06e815b796be3df069dec7836c3df',
    'Hm_lvt_602b80cf8079ae6591966cc70a3940e7': '1709733772,1709907307,1709907362',
    's_ViewType': '10',
    'fspop': 'test',
    'Hm_lpvt_602b80cf8079ae6591966cc70a3940e7': '1709972878',
    '_lxsdk_s': '18e2253714f-ae7-6bf-a57%7C%7C25',
}



params = {
    'shopId': 'G6TFMj83gG9mvjO4',
    'cityId': '22',
    'mainCategoryId': '116',
    '_token': 'eJxVT9tqg0AQ/Zd5Ft3VjTfIQ2hriWChuja1oQ/RXBRRV9fqNiX/3gnYh8LAucw5MPMDw/YIPiWEMKrBdBrAB6oT3QYNRokbh3ieY3qUeczRoPjnrRhFLx/eHsHf24RpDmWfdyNGvacry9ZcG52FWkhNhnPPbDEC5TgK6RvGPM/6sTq0omovetE1hiw7YdSuY2Wu5HmkxFf/PuBJgNWGYxWxXvCw4PinI/wBs7K6tMhOoeKJZLI/x5Hk6Xcqx5drpK68UiEv3GnT1dmz6EWwO9fB/PBhxnmjxNNOJUE4lWkgsjSO027jGnPCX9druP0C8SpZjQ==',
    'uuid': 'f9cf90d4-5478-f904-8bc9-38232123daf0.1709907336',
    'platform': '1',
    'partner': '150',
    'optimusCode': '10',
    'originUrl': 'https://www.dianping.com/shop/G6TFMj83gG9mvjO4',
    'yodaReady': 'h5',
    'csecplatform': '4',
    'csecversion': '2.4.0',
    'mtgsig': '{"a1":"1.1","a2":1709972915421,"a3":"w6305110vu04586yyvz16u18uxuy4uxx81v8v3y4y3u9795826zyx309","a5":"74CX8hLlHPF8T423mzo0","a6":"hs1.4aOG4x69iuIGtADfqn9IKcSWvNNojhjXhi1qBoZlULMO6XviGO1n+jFSZBY9qZRkrokzFlaE80IU9dUW6ZWoN8A==","x0":4,"d1":"29ea2fbe3eb0af2f0da7d12f175a8099"}',
}

response = requests.get(
    'https://www.dianping.com/ajax/json/shopDynamic/reviewAndStar',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.text)