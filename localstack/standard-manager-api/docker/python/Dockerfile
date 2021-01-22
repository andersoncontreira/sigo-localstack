FROM python:3.8

MAINTAINER Anderson Contreira <anderson.contreira@gmail.com>

ARG projectName=standard-manager-api

RUN echo ${projectName}

# copy all files
ADD . /${projectName}

#RUN pip install -r ./${projectName}/requirements.txt && \
#    pip install -r ./${projectName}/requirements-vendor.txt

RUN pip install -r ./${projectName}/requirements.txt && \
    pip install -r ./${projectName}/requirements-vendor.txt

EXPOSE 8000

WORKDIR /${projectName}

# CMD
# CMD [ "chalice", "local", "--host", "0.0.0.0" ]
CMD ["python",  "manage.py", "runserver", "0.0.0.0:8000"]