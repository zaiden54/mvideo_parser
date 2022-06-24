from codecs import utf_8_encode
import requests
import json

def get_data():

    cookies = {
        '__lhash_': '1529f68e5bed38cfe37f8089e4f45df6',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MAIN_PAGE_VARIATION_1': '1',
        'MVID_2_exp_in_1': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20937975983',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '2',
        'MVID_MCLICK': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '3',
        'MVID_ENVCLOUD': 'primary',
        'SMSError': '',
        'authError': '',
        'advcake_track_id': 'e6962f3f-f9fc-3291-f326-e51fcd4b2628',
        'advcake_session_id': 'cf632d32-af43-cc5b-4d81-c535e9ada176',
        '_gid': 'GA1.2.1260359577.1656097499',
        'st_uid': '202f7f917ed4cf13ea0e0af33732d09c',
        'tmr_lvid': '96504a951fc27a2985081906498787d4',
        'tmr_lvidTS': '1656097498964',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'b296cf0b-9691-4bf7-9593-bd1b13e8483e',
        '_ym_uid': '1656097499533269909',
        '_ym_d': '1656097499',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '_ga': 'GA1.2.1874859828.1656097499',
        '_ym_isad': '2',
        'mindboxDeviceUUID': 'efb38cf1-f7b9-459b-8ee9-e47bead1b289',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22efb38cf1-f7b9-459b-8ee9-e47bead1b289%22%7D',
        'afUserId': '6efeda69-0875-445f-9d9f-38a6d0fc02ab-p',
        'flocktory-uuid': 'affa666b-30b0-4b58-a261-a876eade5090-8',
        'AF_SYNC': '1656097500150',
        'BIGipServeratg-ps-prod_tcp80': '1812257802.20480.0000',
        'bIPs': '434929338',
        'uxs_uid': '8d26beb0-f3f0-11ec-a95c-afbf76ebf8bf',
        'tmr_detect': '0%7C1656097502805',
        'adrdel': '1',
        'adrcid': 'ABhmwnPLtmYfGgXRDj0CrzA',
        'JSESSIONID': 'xPMkv2Lc1pc1PWyvf3Q9Wh1yyxjp3pWlyqRHtsSZr2QP790zsYV1!1917716930',
        'tmr_reqNum': '21',
        '_ga_CFMZTSS5FM': 'GS1.1.1656097498.1.1.1656097578.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1656097498.1.1.1656097578.60',
        'ADRUM_BT': 'R:98|g:f8a5261c-6470-4f51-8821-53b3123825082280003',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=1529f68e5bed38cfe37f8089e4f45df6; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MAIN_PAGE_VARIATION_1=1; MVID_2_exp_in_1=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20937975983; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=2; MVID_MCLICK=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=3; MVID_ENVCLOUD=primary; SMSError=; authError=; advcake_track_id=e6962f3f-f9fc-3291-f326-e51fcd4b2628; advcake_session_id=cf632d32-af43-cc5b-4d81-c535e9ada176; _gid=GA1.2.1260359577.1656097499; st_uid=202f7f917ed4cf13ea0e0af33732d09c; tmr_lvid=96504a951fc27a2985081906498787d4; tmr_lvidTS=1656097498964; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=b296cf0b-9691-4bf7-9593-bd1b13e8483e; _ym_uid=1656097499533269909; _ym_d=1656097499; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ga=GA1.2.1874859828.1656097499; _ym_isad=2; mindboxDeviceUUID=efb38cf1-f7b9-459b-8ee9-e47bead1b289; directCrm-session=%7B%22deviceGuid%22%3A%22efb38cf1-f7b9-459b-8ee9-e47bead1b289%22%7D; afUserId=6efeda69-0875-445f-9d9f-38a6d0fc02ab-p; flocktory-uuid=affa666b-30b0-4b58-a261-a876eade5090-8; AF_SYNC=1656097500150; BIGipServeratg-ps-prod_tcp80=1812257802.20480.0000; bIPs=434929338; uxs_uid=8d26beb0-f3f0-11ec-a95c-afbf76ebf8bf; tmr_detect=0%7C1656097502805; adrdel=1; adrcid=ABhmwnPLtmYfGgXRDj0CrzA; JSESSIONID=xPMkv2Lc1pc1PWyvf3Q9Wh1yyxjp3pWlyqRHtsSZr2QP790zsYV1!1917716930; tmr_reqNum=21; _ga_CFMZTSS5FM=GS1.1.1656097498.1.1.1656097578.0; _ga_BNX5WPP3YK=GS1.1.1656097498.1.1.1656097578.60; ADRUM_BT=R:98|g:f8a5261c-6470-4f51-8821-53b3123825082280003',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
        'x-set-application-id': 'fd0df218-5aef-422e-af3b-e4745d8c7a61',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    # print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    
    # print(products_ids)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    
    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }
    
    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)
    
    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')


        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()

if __name__ == '__main__':
    main()