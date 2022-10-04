#!/bin/bash

# change working dir to script directory
cd "$(dirname "$0")"

# validate arguments
if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Supply an integer value (1-59). This integer denotes the interval in mins between consecutive data uploads."
    exit 1
fi

while true; do
    read -p "Have you verified the config paramaters in src/config/amatsa-client.yml (y/n)?" yn
    case $yn in
        [Nn]* ) echo "Verify config values and begin setup again."; exit;;
        [Yy]* ) echo "Starting installation..."; break;;
        * ) echo "Please answer yes or no.";;
    esac    
done

# check python3
echo "Checking if python3 requisites are met..."
pyver=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
if [ $? -eq 0 ]
then
    split=(${pyver//./ })    
    if [ "${split[0]}" -eq "3" ] && [ "${split[1]}" -lt "10" ]
    then
        echo "Found python v${split[0]}.${split[1]}. Install Python v3.10+ and try again."
        exit 1
    fi
else
    echo "python3 not found. Install v3.10+ and begin setup again."
    exit 1
fi

echo "python3 [OK]"

# create venv
python3 -m venv .venv
if [ $? != "0" ]
then
    echo "Failed to create virtual env."
    exit 1
fi

echo "venv creation successful [OK]"

# activate venv
source .venv/bin/activate
if [ $? != "0" ]
then
    echo "Failed to activate virtual env."
    exit 1
fi

echo "venv activation successful [OK]"

# install python libs
if [ -f requirements.txt ]
then
    pip install -r requirements.txt;
    pip install -e .
    if [ $? != "0" ]
    then
        echo "Failed to install dependency libs."
        exit 1
    fi
fi

echo "dependency libs installed [OK]"

# setup scheduled job
pypath=$(whereis python | awk '{print $2}')
script=$(pwd)
script="${script}/src/driver.py"
crontab -l | { cat; echo "*/$1 * * * * $pypath $script"; } | crontab -
if [ $? != "0" ]
then
    echo "Failed to setup cron job."
    exit 1
fi

echo "cron-job setup [OK]"
echo "Installation completed successfully!"
