import os
import sys
import time
import json
import shutil
import argparse
import logging
import tempfile
import subprocess
import getpass
from Params import tdDbUrl
from Params import tdLogonMech
from Params import tptKafkaMsgLmt
from Params import tptKafkaOffsetDirectory
from Params import kafkaToDbLoadPrgmExtFlgFileName
from Params import kafkaTopic
from Params import kafkaServers
from Params import tdUName
from Params import tdPwd
from Params import tdDbName

class TPTJobExecutor:

    exeutionNumber = 0
    tptAccessModuleName = "libkafkaaxsmod.so"

    def __init__(self, scriptLocation='load_sensor_data.tpt'):
        self.tdUName = tdUName
        self.tdPass = tdPwd
        self.tdDefaultDB = tdDbName
        self.command = ["tbuild", "-f", scriptLocation]
        if os.name == "nt":
            self.tptAccessModuleName = "libkafkaaxsmod.so"
        logging.info("TPT access module name - "+self.tptAccessModuleName)
        global tptKafkaOffsetDirectory
        if tptKafkaOffsetDirectory is None:
            tptKafkaOffsetDirectory = os.getcwd()
            logging.info(
                "Setting tpt kafka offset directory as the working directory. "+str(tptKafkaOffsetDirectory))

    def execute(self):
        self.exeutionNumber += 1
        logging.info("Executing TPT - " + str(self.exeutionNumber))
        dirObj = tempfile.TemporaryDirectory()
        dirpath = dirObj.name
        logging.info("Temp directory path - "+dirpath)
        pathLocations = ["-L", dirpath, "-r", dirpath, "-u", "tdDbUrl='{tdDbUrl}',tdUName='{tdUName}',tdPass='{tdPass}',tdDefaultDB='{tdDefaultDB}',tdLogonMech='{tdLogonMech}',tptAccessModuleName='{tptAccessModuleName}',tptKafkaMsgLmt='{tptKafkaMsgLmt}',tptKafkaOffsetDirectory='{tptKafkaOffsetDirectory}',kafkaTopic='{kafkaTopic}',kafkaServers='{kafkaServers}'".format(
            tdDbUrl=tdDbUrl, tdUName=self.tdUName, tdPass=self.tdPass, tdDefaultDB=self.tdDefaultDB, tdLogonMech=tdLogonMech, tptAccessModuleName=self.tptAccessModuleName, tptKafkaMsgLmt=tptKafkaMsgLmt, tptKafkaOffsetDirectory=tptKafkaOffsetDirectory, kafkaTopic=kafkaTopic, kafkaServers=",".join(kafkaServers)), "-d"]
        process = subprocess.Popen(self.command + pathLocations, stdout=sys.stdout,
                                   stderr=sys.stdout)
        retCode = process.wait()
        logging.info("Process Code - "+str(retCode))
        return retCode


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    scriptLocation = None
    exitLoc = os.path.join(os.getcwd(), kafkaToDbLoadPrgmExtFlgFileName)

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tpt_location', required=True,
                        help="Location of the sensor data tpt script. The tpt script is available in the script folder.")

    logging.info("Exit file location - "+exitLoc)

    try:
        args = parser.parse_args()
        scriptLocation = args.tpt_location
        if os.path.isfile(exitLoc):
            logging.info("Exit file found on start. Removing it")
            os.remove(exitLoc)

    except:
        sys.exit(1)

    logging.info("Script location passed - "+str(scriptLocation))

    tpt = TPTJobExecutor(scriptLocation)

    while True:
        if os.path.isfile(exitLoc):
            logging.info("Exiting program. Flag file found")
            sys.exit(0)
        tpt.execute()
        logging.info("Sleeping 10 seconds")
        time.sleep(10)
