# global variables
import requests
error_class = 'alert alert-danger'
success_class = 'alert alert-success'
# checks if connected to the internal server : time out is 3 seconds
# def isInternalNetwork():
#     response =  os.system("ping -c 1 -W 3 " + "10.50.40.166")
#     return False if (response>0) else True



def getAccessToken(account):
    url = "https://oauth.brightcove.com/v4/access_token?grant_type=client_credentials"

    payload = {}
    if(account == 1):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic N2ZmNGEzZDAtZDRhMy00NjhlLWFjN2MtM2U3NDRjYjgzNDM2OjhRSHpkWjVkNGFVYU4yakxXLTlHVV83V3FtUENnakhyWU5oRmNaX3RiX3NUQS1vaXNyLVJHdlBndjUzOFAyY1hyMXc3cGhXQV9VUmhTUmxSa2c1Mll3',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, x-requested-with'
        }
    else:
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic YTkxMmQ5NmMtYjA5MC00YzAzLWIzOTctNjQ4Yjk5ZmJjNDVjOms2MEhneUwyYUhjM1Y1MGdlRFRqNEtvZThvakROVmFRXzV6bHhsMXljREI2MXlpeGJzbTNVU281RlM5SlplbENZX3g3SWV6SGRQVVV5RjdRQkU0UU1n',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, x-requested-with'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['access_token']


def get_videos(access_token):
    url = "https://cms.api.brightcove.com/v1/accounts/5121028909001/videos"
    payload = {}
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()
