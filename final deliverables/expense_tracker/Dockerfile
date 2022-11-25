    FROM python:3.9.2
    LABEL maintainer="rameshrk210, rameshrk21012@gmail.com"
    RUN apt-get update
    RUN mkdir /expend
    WORKDIR /expend
    COPY . /expend
    RUN pip install -r requirements.txt
    EXPOSE 5000
    ENTRYPOINT [ "flask" ]
    CMD [ "run" ]
