import sys
import time
import logging
from kafka import KafkaAdminClient
from kafka import KafkaConsumer
from kafka.admin import NewTopic


class KafkaTopicReset:
    def __init__(self):
        self.adminClient = KafkaAdminClient(bootstrap_servers=["localhost:9092"])
        self.kafkaConsumer = KafkaConsumer(bootstrap_servers=["localhost:9092"])

    def deleteTopic(self):
        return self.adminClient.delete_topics(["MasksMfgSensorDataQueue"], timeout_ms=60000)

    def createTopic(self):
        return self.adminClient.create_topics([NewTopic(name="MasksMfgSensorDataQueue", num_partitions=1, replication_factor=1)], timeout_ms=60000)

    def checkTopicExist(self):
        if "MasksMfgSensorDataQueue" in self.kafkaConsumer.topics():
            return True
        else:
            return False

    def closeKafkaQueue(self):
        self.adminClient.close()
        self.kafkaConsumer.close()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    kaf = KafkaTopicReset()
    try:
        if kaf.checkTopicExist():
            logging.info("Deleting kafka topic - "+"MasksMfgSensorDataQueue")
            logging.info(str(kaf.deleteTopic()))
            time.sleep(7)
        logging.info("Creating kafka topic - "+"MasksMfgSensorDataQueue")
        logging.info(str(kaf.createTopic()))
        logging.info("Kafka reset topic completed successfully")
    except Exception as e:
        logging.error('Topic reset failed ' + str(e))
    finally:
        kaf.closeKafkaQueue()
