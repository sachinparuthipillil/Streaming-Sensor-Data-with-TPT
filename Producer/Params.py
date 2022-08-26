import os

tptKafkaMsgLmt = 4800
tptKafkaOffsetDirectory = None # current working directory will be used if the value is none
kafkaServers = [os.getenv('kafkaServer')]
kafkaTopic = os.getenv('kafkaTopic')
kafkaEventsPerDay = 960