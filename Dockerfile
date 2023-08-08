FROM python:3.11

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/Yay-yay-api

#ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./Yay-yay-api /opt/Yay-yay-api/
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas
RUN pip install convertdate
RUN pip install LunarCalendar
RUN pip install holidays
RUN pip install pystan
RUN pip install -r /opt/Yay-yay-api/requirements.txt

RUN chmod +x /opt/Yay-yay-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
