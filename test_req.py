import requests

URL = 'http://localhost:8000'

def get_Token():
    url = f'{URL}/crm/api/auth/'

    response = requests.post(url, data={'username': 'autoupdate', 'password': 'passwordtest'})
    return response.json()

# print(get_Token())

def get_data():
    url = f"{URL}/crm/api/ControlVersionList/"
    header = {'Authorization': f'Token {get_Token()}'}
    respones = requests.get(url, headers=header)
    return respones.json()

def create_new(hcode):
    url = f"{URL}/crm/api/ControlVersionList/"
    header = {'Authorization': f'Token {get_Token()}'}
    data = {
            "app_controlVersion": "4000",
            "hos_s_version": "4000",
            "hos_stock_version": "4000",
            "hos_ereferral_version": "4000",
            "hcode": f"{hcode}"
        }
    respones = requests.post(url, data=data, headers=header)
    # return respones.json()
    # print(respones.text)



def edit_data(hcode):
    url = f"{URL}/crm/api/ControlVersionDetail/{hcode}/"
    header = {'Authorization': f'Token {get_Token()}'}
    data = {
            "app_controlVersion": "8000",
            "hos_s_version": "8000",
            "hos_stock_version": "8000",
            "hos_ereferral_version": "8000",
        }
    respones = requests.put(url, data=data, headers=header)
    # return respones.json()
    print(respones.text, respones.status_code)



def delete_data(hcode):
    url = f"{URL}/crm/api/ControlVersionDetail/{hcode}/"
    header = {'Authorization': f'Token {get_Token()}'}
    respones = requests.delete(url, headers=header)
    # return respones.json()
    print(respones.status_code)

delete_data(12345)