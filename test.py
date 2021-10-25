"""
作者:DiQi
日期:2021年10月25日
说明：测试
"""
import requests

url = 'https://www.baidu.com'
resp = requests.get(url)
resp.encoding = resp.apparent_encoding
print(resp.text)
