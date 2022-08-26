FROM fedora:26

#Update system

RUN dnf -y install python3-devel findutils libstdc++
RUN dnf -y update python3-setuptools python3-pip
RUN pip3 install kafka-python


#Install Teradata Tools & Utilities
COPY Topic/KafkaTopicReset.py /tmp/
COPY Topic/Params.py /tmp/

CMD ["python3", "/tmp/KafkaTopicReset.py"]