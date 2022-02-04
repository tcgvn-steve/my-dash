FROM python:3.8-slim

WORKDIR /proj

COPY *.tar.gz ./

COPY requirements.txt /

RUN pip install -r /requirements.txt \
	&& rm -rf /root/.cache

COPY ./ ./

ENV ENVIRONMENT_FILE=".env"

EXPOSE 8061

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "main:server"]