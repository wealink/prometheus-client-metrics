#!/usr/bin/env python3
#coding:utf-8

import prometheus_client
from prometheus_client import Counter,Gauge
import logging,datetime,logging.config
import tools
from os import path
from flask import Response,Flask
import configparser



app = Flask(__name__)

config = configparser.ConfigParser()
config.read(path.abspath(path.dirname(__file__))+"/config/app.ini")

name=config['default']['appname']
print(name)
logging.config.fileConfig(path.abspath(path.dirname(__file__))+"/config/log.conf")
logger = logging.getLogger("simple")

web_code = Gauge("web_code", "Web code of value",["project","env","service_name","host"])  # 数值可大可小

#eurake监控
@app.route("/metrics")
def eurake():
  urls=["http://tezign:tezign@172.17.217.146:10353/","http://tezign:tezign@172.17.217.146:10354/","http://tezign:tezign@172.17.217.146:10355/"]
  for index,url in enumerate(urls):
    code=tools.get_content(url)
    web_code.labels("sop","prod","eurake"+str(index),url).set(code)
  return Response(prometheus_client.generate_latest(web_code),mimetype="text/plain")





if __name__ == '__main__':
  logger.info('server start：%s'% datetime.datetime.now())
  app.run(host='0.0.0.0',port=8080)
  logger.info('server close：%s'% datetime.datetime.now())

