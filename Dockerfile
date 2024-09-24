FROM python

RUN git clone https://github.com/rutgervaneijden/Propaan.git

RUN pip install --no-cache-dir flask requests

EXPOSE 8000

CMD ["python", "./Propaan/app.py"]
