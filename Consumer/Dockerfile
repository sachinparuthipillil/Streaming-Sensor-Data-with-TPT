FROM fedora:26

#Update system
#RUN dnf -y update
RUN dnf -y install python3-devel findutils libstdc++
RUN dnf -y update python3-setuptools python3-pip

#RUN pip3 install kafka-python
#Install Teradata python package
RUN pip3 install --no-cache-dir \
	teradatasql
	

#Install Teradata Tools & Utilities
ADD Consumer/TeradataToolsAndUtilitiesBase__linux_*.tar.gz tmp/
#ADD ttu.repo /etc/yum.repos.d/ttu.repo
COPY Consumer/load_sensor_data.tpt /tmp/
COPY Consumer/Params.py /tmp/
COPY Consumer/TPTJobExecutor.py /tmp/
COPY Consumer/libkafkaaxsmod.so /opt/teradata/client/17.20/lib64/
RUN cd tmp; find . -name '*.tar.gz' -exec tar zxvf {} --strip=1 \;
#RUN yum -y install bteq fastexp fastld mload

#Install TPT (manual, not in the above repo)
RUN rpm -ivh /tmp/TeradataToolsAndUtilitiesBase/Linux/x8664/signing/ttupublickey*.rpm
RUN rpm -ivh /tmp/TeradataToolsAndUtilitiesBase/Linux/x8664/tdicu*.rpm
RUN rpm -ivh /tmp/TeradataToolsAndUtilitiesBase/Linux/x8664/cliv2*.rpm
RUN rpm -ivh /tmp/TeradataToolsAndUtilitiesBase/Linux/x8664/tdodbc*.rpm
RUN rpm -ivh /tmp/TeradataToolsAndUtilitiesBase/Linux/x8664/tptbase*.rpm

#Add entry point - example
#ENTRYPOINT [ "tbuild","-f" ]
CMD ["python3","/tmp/TPTJobExecutor.py","-t","/tmp/load_sensor_data.tpt"]