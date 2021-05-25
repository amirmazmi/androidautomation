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
#start clean  
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




<br><br>
