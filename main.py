#!/usr/bin/env python3
#coding:utf-8

import prometheus_client
from prometheus_client import Counter,Gauge
import logging,datetime
import tools
from flask import Response,Flask


app = Flask(__name__)
web_code = Gauge("web_code", "Web code of value",["project","env","service_name"])  # 数值可大可小

#eurake监控
@app.route("/metrics")
def eurake():
  urls=["http://tezign:tezign@172.17.217.146:10353/","http://tezign:tezign@172.17.217.146:10354/","http://tezign:tezign@172.17.217.146:10355/"]
  for index,url in enumerate(urls):
    code=tools.get_content(url)
    web_code.labels("sop","prod","eurake"+str(index)).set(code)
  return Response(prometheus_client.generate_latest(web_code),mimetype="text/plain")





if __name__ == '__main__':
  logging.info('server start：%s'% datetime.datetime.now())
  app.run(host='0.0.0.0',port=8080)
  logging.info('server close：%s'% datetime.datetime.now())

