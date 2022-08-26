import os

tdDbUrl = os.getenv('host')
tdLogonMech = os.getenv('logonmech')
tptKafkaMsgLmt = 4800
tptKafkaOffsetDirectory = os.getenv('offsetDir')
kafkaServers = [os.getenv('kafkaServer')]
kafkaTopic = os.getenv('kafkaTopic')
kafkaEventsPerDay = 960
kafkaToDbLoadPrgmExtFlgFileName = "tptflg.exit"
tdUName= os.getenv('uname')
tdPwd= os.getenv('tdPwd')
tdDbName= os.getenv('tdDbName')