# Android link and automation
<br>  

Repo: https://github.com/Genymobile/scrcpy
  
Requires adb to be installed and the env var ADB to be set. 
```
echo $ADB
which adb
adb --version
```
If adb is available using Android Studio, then set as an alias  
`alias adb='/path/to/adb/'`  
  
Env var can be set in .bashrc   
`export ADB=/path/to/adb`  

  
<br>  

---  
### Connecting to device  

start clean  
`adb kill-server`

plug your device and check if the device is connected  
`adb devices`   
  
***OR***  
  
connect via TCP  
`adb connect _IP_:_PORT_`

export the path to currently used adb or use the same path to adb when you connected to the device, in the previous step  
`export ADB=$(which adb)`

run scrpy  
`scrcpy`

<br>  

---
  
How to get device ip address  
 `adb shell ip addr show wlan0`  

<br>  

---  
### Keys

`MOD + h` &emsp;&emsp;&emsp;&emsp;&emsp; Home  
`MOD + s` &emsp;&emsp;&emsp;&emsp;&emsp; App switcher  
`MOD + c` &emsp;&emsp;&emsp;&emsp;&emsp; copy  
`MOD + v` &emsp;&emsp;&emsp;&emsp;&emsp; paste: pc -> device  

`MOD + shift + h` &emsp; paste: device -> pc  
`MOD + r` &emsp;&emsp;&emsp;&emsp;&emsp; rotate screen  
`MOD + o` &emsp;&emsp;&emsp;&emsp;&emsp; Device screen off (mirroring does not stop)  
`MOD + shift + o` &emsp; Device screen on  
  
`MOD + n` &emsp;&emsp;&emsp;&emsp;&emsp; Open notification panel  
`MOD + shift + n` &emsp; Close notification panel  




<br><br><br>
