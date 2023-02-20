FROM python:3.9.6 as builder
COPY src/ /opt/src
WORKDIR /opt/src

# Install python3
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt


FROM builder as builder_ex
RUN rm /etc/apt/sources.list
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free" >> /etc/apt/sources.list

# Set timezone
# ERROR: It seems did not change anything.
# RUN apt-get install -y tzdata
# RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime
# RUN echo $TZ > /etc/timezone

# Install cron
RUN apt-get update 
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

