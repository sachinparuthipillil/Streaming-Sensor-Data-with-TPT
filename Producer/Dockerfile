FROM fedora:26

ENV DAYS '1'
ENV START_DATE '2022-07-10' 
#Update system
#RUN dnf -y update
RUN dnf -y install python3-devel findutils libstdc++
RUN dnf -y update python3-setuptools python3-pip

RUN pip3 install kafka-python
	

COPY Producer/DataGenerator.py /tmp/
COPY Producer/DataPublishQueue.py /tmp/
COPY Producer/KafkaTopicReset.py /tmp/
COPY Producer/Params.py /tmp/


#Add entry point - example
#ENTRYPOINT [ "tbuild","-f" ]

CMD python3 /tmp/DataPublishQueue.py -d $DAYS -s $START_DATE