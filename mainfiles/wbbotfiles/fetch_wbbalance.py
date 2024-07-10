import requests
import json

def load_cookies():
    with open('storage_state.json', 'r') as file:
        storage_state = json.load(file)
        cookies = storage_state['cookies']
        cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
        return cookie_dict

def fetch_balance():
    cookies = {
        '_wbauid': '5531026151718537185',
        '___wbu': 'e8349a57-c3d4-48ff-925f-16ff06edc4c6.1718537185',
        'wbx-validation-key': '1e40bf87-d815-46f5-87fb-646c5c359cf5',
        '___wbs': 'c6ae8dae-04a3-48e4-8339-acdc149e59b3.1719103864',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTkxMDM4NjUsInZlcnNpb24iOjIsInVzZXIiOiI1NTA5MTU0OSIsInNoYXJkX2tleSI6IjE2IiwiY2xpZW50X2lkIjoid2IiLCJzZXNzaW9uX2lkIjoiZDIxMzU5ZThjMDkzNGNkMGFlZjY4MTM0ZDM2MTY3NDUiLCJ1c2VyX3JlZ2lzdHJhdGlvbl9kdCI6MTY3NTkwODcyMywidmFsaWRhdGlvbl9rZXkiOiJhNGMxNDYzODk1ZDI4ODM1OGM3ODFkMjY0MTdlNzRlMDg1MjA5ZTVhN2M3NmFhNDlhOGI2MWI5MzQzMGJiZTI5IiwicGhvbmUiOiJ4ODZyNlMxYzRxVEg1V3k2dTEzb2p3PT0ifQ.htruuC3oSYzde_GyvZ9azd6xY5iq3PTEzhEFy11HGkWadm713GinQmEygVTX7EV62u85NeS7Nb5FqxM0f_RYbXklgSVnfjSKByryNjmQus6WLdgokbb2WDwNQ16BK8HiO8A6mGXYIqLqOzo-O4Hot2l5hD-vqjOr3-rC9phoD0i-hi4ZAbAQSn35UlyY9RwSwv-yYdBIzelrAllRbw_7CAiTLtJpPlvYSeISxsMbia6N91EsNncpME-jzISuBgxncompFw4dRfHJc3aAFDmn61hDxWoMe_7yJMunmSTDVicp0W6ueTjQLCL9OMTRRtqGeutiingS-bkylBoSPnBxWQ',
        # 'content-length': '0',
        # 'cookie': '_wbauid=5531026151718537185; ___wbu=e8349a57-c3d4-48ff-925f-16ff06edc4c6.1718537185; wbx-validation-key=1e40bf87-d815-46f5-87fb-646c5c359cf5; ___wbs=c6ae8dae-04a3-48e4-8339-acdc149e59b3.1719103864',
        'deviceid': 'site_3f28a3f323c64bd496fc9ffcf795b5eb',
        'origin': 'https://www.wildberries.ru',
        'priority': 'u=1, i',
        'referer': 'https://www.wildberries.ru/lk/mywallet/purchases',
        'sec-ch-ua': '"Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-spa-version': '10.0.18',
    }

    response = requests.post('https://www.wildberries.ru/webapi/account/getsignedbalance', cookies=cookies, headers=headers)
    if response.status_code == 200:
        return response.json()['value']['walletBalance']
    else:
        raise Exception('Failed to fetch balance')
    
fetch_balance()
