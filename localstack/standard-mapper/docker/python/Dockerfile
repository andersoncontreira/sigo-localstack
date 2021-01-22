FROM python:3.8

MAINTAINER Anderson Contreira <anderson.contreira@gmail.com>

ARG projectName=standard-mapper
ARG projectRoot=.

RUN echo ${projectName}


# copy all files
ADD . /${projectName}
# force the copy the config
COPY ./.chalice/config.json /${projectName}/.chalice/config.json

# RUN ls -a /${projectName}
# RUN ls /${projectName}/.chalice/

RUN pip install -r ./${projectName}/requirements.txt && \
    pip install -r ./${projectName}/requirements-vendor.txt

EXPOSE 8000

WORKDIR /${projectName}

# CMD
CMD [ "chalice", "local", "--host", "0.0.0.0"]

# Changing port
#CMD [ "chalice", "local", "--host", "0.0.0.0" ,"--port", "8000"]