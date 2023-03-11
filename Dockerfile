FROM python:3.9
RUN mkdir -p /usr/sales_app/
WORKDIR /usr/sales_app/
COPY . /usr/sales_app/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "-u", "test_task.py"]
