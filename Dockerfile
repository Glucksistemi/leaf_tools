FROM python:3.10.6
WORKDIR /app
USER root
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
EXPOSE 7860
CMD ["python", "-u", "acf_app.py"]