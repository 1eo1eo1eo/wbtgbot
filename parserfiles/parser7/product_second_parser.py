import aiohttp
import asyncio
from models import Product2
import logging

class ProductParser2:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    async def fetch_products(self, session, url, params):
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://www.wildberries.ru',
            'Referer': 'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bryuki-i-shorty?page=1&sort=newly&xsubject=11',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36',
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTgzNDAxMzIsInZlcnNpb24iOjIsInVzZXIiOiIxMTY0NDI5NzAiLCJzaGFyZF9rZXkiOiI1IiwiY2xpZW50X2lkIjoid2IiLCJzZXNzaW9uX2lkIjoiNWVmZDY3MDQ4Nzc1NDM0NThjZTI4NjkzMzg1NDliZDEiLCJ1c2VyX3JlZ2lzdHJhdGlvbl9kdCI6MTY4NjcwOTQ5MywidmFsaWRhdGlvbl9rZXkiOiIyNzQ2NTc1YzdjZjdiZmU3OTNkNzU1ZWFhYzljYjY0NDMxODhkNjgzNjU3YTdiM2JjYjU2NThkM2M1N2FlYjhiIiwicGhvbmUiOiJGcU9JaXNmN0djSm9zYnpMdXVQbEhnPT0ifQ.GCou8Wud_FGthhD2pxu_TZVX131Y56k7V1pCmZFIEbGkbBLJv5Hc1HKQUjcmQsKf3qK2GY8eOE9xWpxVAhSk5xbig04xUFs4WztR2iDzn88v9FELQ7EWJZcoF7bhqTkQGgj08cpmlrxCVZ4MtlJ-Wci0Ekp6BoeanYGQhuVdidw8OF9Uj3Pvi-mzcr55krBzSAlz68W8GFzGCwiQZ1z5o9fTzk9zSYcM8K14_gvs7ps03QweYYNgYBfqxsTFen3akb-09ig609hTb_z_SL2_3w49Qv3UtPA4AnmFPSJCpueTXMofXSqqSJRNpPlDszsFDLuaxbd6wlFeCjLRQ6lFDg',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "YaBrowser";v="24.4", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        try:
            async with session.get(url, headers=headers, params=params) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            logging.error(f"Network-related error occurred: {e}")
            raise
        except asyncio.TimeoutError:
            logging.error("Timeout error occurred when fetching products")
            raise

    async def parse_category(self, base_url):
        self.db_manager.clear_table(Product2)

        async with aiohttp.ClientSession() as session:
            params = {
                'appType': '1',
                'cat': '8127',
                'curr': 'rub',
                'dest': '123587791',
                'page': '1',
                'sort': 'newly',
                'spp': '30',
                'uclusters': '1',
                'xsubject': '11',
            }
            
            response_json = await self.fetch_products(session, base_url, params)
            products = response_json.get('data', {}).get('products', [])

            all_products = []
            for product in products:
                all_products.append(Product2(
                    name=product.get('name', ''),
                    brand_name=product.get('brand', ''),
                    product_id=product.get('id', ''),
                    price=next((info.get('price', {}).get('total', 0) / 100 for info in product.get('sizes', [])), 0),
                    url_name=f"https://www.wildberries.ru/catalog/{product.get('id', '')}/detail.aspx"
                ))

            if all_products:
                self.db_manager.add_products(all_products, Product2)
            else:
                logging.info("No products found on the page.")

            return True
