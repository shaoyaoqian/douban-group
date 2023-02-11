# FROM python:3.9.6
FROM ubuntu:latest
COPY src/ /opt/src
WORKDIR /opt/src

# Install python3
RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r requirements.txt


# Install cron
RUN apt-get -y install cron 
# Copy hello-cron file to the cron.d directory
COPY src/cronfile /etc/cron.d/cron
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron
# Apply cron job
RUN crontab /etc/cron.d/cron
# Create the log file to be able to run tail
RUN touch /var/log/cron.log
# Run the command on container startup
CMD ["cron", "-f"]

