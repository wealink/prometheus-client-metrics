FROM python:3.6.4

WORKDIR /src

# add app
ADD . /src

# install requirements
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENTRYPOINT ["python","main.py"]