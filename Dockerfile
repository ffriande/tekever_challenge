FROM python:3.9 

COPY challenge challenge
RUN cd challenge && pip3 install -e .

ENV LC_ALL=C.UTF-8 
ENV LANG=C.UTF-8
ENV FLASK_APP=challenge
CMD flask run -h 0.0.0.0