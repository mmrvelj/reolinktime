# Configure current time on Reolink camera which does not support NTP 

Some Reolink cameras (such as E330) do not have web gui or NTP support, so 
they cannot get correct time after they are started until either you connect with mobile phone app or NVR. 
This simple python program fixes this by periodically connecting to camera and setting the correct time.

## Installation
To instal copy  `config.ini.default` to `config.ini`, and set configuration details. Then you can start python program.

## Systemd
For convenience there is also systemd service file and timer to start it every hour.
These files assume you installed all files under `/opt/reolinktime`. 
If you installed it somewhere else, you need to **adjust** `reolinktime.service` file.

Copy .service and .timer file under /etc/systemd/system folder and install timer.

```
cp systemd/* /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable --now reolinktime.timer
```

,then check that the timer is functional
```
systemctl list-timers --all
```
