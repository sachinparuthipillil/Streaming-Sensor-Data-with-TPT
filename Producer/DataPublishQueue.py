import os
import sys
import time
import json
import logging
import argparse
import datetime
from Params import kafkaTopic
from Params import kafkaServers
from Params import kafkaEventsPerDay
from kafka import KafkaProducer
from DataGenerator import DataGenerator


class DataPublishQueue:

    def __init__(self, incr=1):
        self.dg = DataGenerator(incr)
        self.producer = KafkaProducer(bootstrap_servers=kafkaServers)

    def postDataToQueue(self):
        days, retData = self.dg.generateData()
        for i in retData:
            future = self.producer.send(
                kafkaTopic, value=json.dumps(i).encode('utf-8'))
            result = future.get(timeout=60)
            logging.debug(str(result))
        return days

    def closeKafkaQueue(self):
        self.producer.close()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--days', required=True,
                        help='How many days data to generate')
    parser.add_argument('-s', '--start_date', required=False,
                        help="Custom date to start the data generation process from. Date Format - %Y-%m-%d")
    parser.add_argument('-p', '--prod', required=False,  default=False, action="store_true",
                        help="If this flag is set, 30 sec sleep will be implemented after each iteration")
    try:
        args = parser.parse_args()
    except:
        sys.exit(1)
    dpq = DataPublishQueue()
    logging.info("Days - " + str(args.days))
    cutOff = int(args.days)
    if args.start_date is not None:
        logging.info("Start date - "+args.start_date)
        dpq.dg.setDateObjStart(args.start_date)
    logging.info("Prod - " + str(args.prod))
    while True:
        days = dpq.postDataToQueue()
        sys.stdout.flush()
        if days >= cutOff:
            logging.info("Exiting program")
            dpq.closeKafkaQueue()
            break
        if args.prod:
            logging.info("Sleeping 30 seconds")
            time.sleep(30)
