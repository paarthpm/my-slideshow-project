### Setting up the application in raspberry pi
1. Clone the repo. 
2. Navigate to the project folder.
3. Run command in terminal: chmod +x setup.sh
4. Run command: ./setup.sh

#### Setting up for appliation when device starts up
5. Run command: nano run_slideshow.sh
6. Paste the following lines:
```
#!/bin/bash
source /home/parthapi/my-slideshow-project/venv/bin/activate
export DISPLAY=:0
python /home/pi/my-slideshow-project/slideshow.py >> /home/pi/my-slideshow-project/slideshow-error.log 2>&1

```
7. Save the file and run command: chmod +x run_slideshow.sh

#### Setting up for appliation autostart using lxde autostart
8. Run command. File location may vary depending devices and OS.: sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
9. Paste the following line at the bottom.

```
@bash /home/pi/my-slideshow-project/run_slideshow.sh
```
Additional lines can be added to disable screensaver or disable screen off of the device.

```
@xscreensaver -no-splash
@xset s off
@xset -dpms
@xset s noblank
@bash /home/parthapi/my-slideshow-project/run_slideshow.sh
```
10. Reboot the device: sudo reboot




