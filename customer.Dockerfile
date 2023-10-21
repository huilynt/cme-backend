FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./customer.py .
CMD [ "python", "./customer.py" ]