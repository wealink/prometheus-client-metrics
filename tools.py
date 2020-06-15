#!/usr/bin/env python3
#coding:utf-8
import requests

def get_content(url):
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
        return 0
    else:
        return response.status_code