# syntax=docker/dockerfile:1

FROM public.ecr.aws/docker/library/python:3.11.6

WORKDIR ./
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]