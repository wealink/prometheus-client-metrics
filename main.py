#!/usr/bin/env python3
#coding:utf-8

import prometheus_client
from prometheus_client import Counter,Gauge
import logging,datetime,logging.config
import tools
from os import path
from flask import Response,Flask
import configparser
from loguru import logger



app = Flask(__name__)
web_code = Gauge("web_code", "Web code of value",["project","env","service_name","host"])  # 数值可大可小

#metrics监控
@app.route("/metrics")
def metrics():
  #sop project
  sop_urls = ["http://tezign:tezign@10.80.82.203:30622/"]
  for index,url in enumerate(sop_urls):
    code=tools.get_content(url)
    web_code.labels("sop","prod","eurake"+str(index),url).set(code)
    logger.info(prometheus_client.generate_latest(web_code))

  #ai project
  ai_urls = {
    "ai-gpu-prod": "http://47.103.96.111:9081/health_check",
    "ai-video-prod": "http://47.103.96.111:9083/health_check",
    "ai-ocr-prod": "http://47.103.96.111:9086/health_check",
    "ai-cdmp-prod": "http://47.103.96.111:9089/health_check",
    "ai-forecast-prod": "http://47.103.96.111:9087/health_check",
    "ai-search-prod": "http://47.103.96.111:9085/health_check",
    "ai-picture-prod": "http://47.103.96.111:9092/health_check",
    "ai-dam-prod": "http://47.103.96.111:9096/health_check",
    "ai-saas-prod": "http://47.103.96.111:9084/health_check"
             }
  for project, url in ai_urls.items():
    code = tools.get_content(url)
    web_code.labels("ai", "prod", project, url).set(code)

  #vms project

  return Response(prometheus_client.generate_latest(web_code),mimetype="text/plain")






if __name__ == '__main__':
  config = configparser.ConfigParser()
  config.read(path.abspath(path.dirname(__file__)) + "/config/app.ini")
  appname = config['default']['appname']
  logging.config.fileConfig(path.abspath(path.dirname(__file__)) + "/config/log.conf")
  logger = logging.getLogger(appname)
  logger.info('server start：%s'% datetime.datetime.now())
  app.run(host='0.0.0.0',port=8080)
  logger.info('server close：%s'% datetime.datetime.now())

