## Overview

This repository contains files required to build docker images for Sensor data streaming usecase with TPT. There are 5 docker images as part of this project. 2 of them are pulled from the docker hub where as the other 3 are build locally.

## Pre-requisites

1. Docker and Docker compose installed.

2. Download the [Teradata Tools and Utilities - Linux Installation Package](http://downloads.teradata.com/download/tools/teradata-tools-and-utilities-linux-installation-package-0) (make sure to download the linux package and not ubuntu, you will also need to register and accept the licence terms). And place the tar.gz file inside the Consumer directory.

3. Execute the SQL in DDL.sql to create the target table inside Teradata database.

4. Provide Teradata connection details in the docker-compose.yaml file for the following environment variables:
    - 'host' - Teradata host url
    - 'uname' - Teradata login name
    - 'tdDbName' - Teradata Database (schema) Name
    - 'logonmech' - Logon Mechanism to be used. For eg. LDAP, TDNEGO etc.

5. Create '.env' file in the base project directory and provide the Teradata login password as show below:

        DB_PASSWORD=Replace_this_with_DB_Password

## Execution

From the base directory execute the below command to start building the docker containers and execute them.

      docker compose up
