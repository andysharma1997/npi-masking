FROM python:3.8-slim-buster
RUN python3.8 -m venv /venv
ENV PATH=/venv/bin:$PATH
RUN pip3 install --upgrade pip
RUN pip3 install wheel
LABEL org.opencontainers.image.authors="shubham@salesken.ai"
COPY . /opt
WORKDIR /opt
RUN  apt-get update
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install "uvicorn[standard]" gunicorn
EXPOSE 9999
CMD ["gunicorn", "app.main:app", "--workers", "1", "--timeout", "300", "--worker-class", "uvicorn.workers.UvicornH11Worker", "--bind", "0.0.0.0:9999"]