# tempreport
Read the DHT temp on a Raspberry PI and report it to a graphite host

## Install

login in as pi on Raspberry PI

git clone https://github.com/hpepper/tempreport.git

## Configuration
You have to create the file etc/graphite_host_addr.dat
And write the ip or hostname of the graphite server, you want to send the data to

You have to create the file etc/adjust.dat
The first value in 'adjust.dat' is the temperature adjustment, the second is humidity.


To run every five minutes add to crontab:
crontab -e
0,5,10,15,20,25,30,35,40,45,50,55 * * * * /home/pi/tempreport/bin/senddata.py
