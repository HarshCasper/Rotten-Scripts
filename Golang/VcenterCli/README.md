# GoVcenterRESTcli
    Test enviroment: 
    go version go1.17.2 darwin/amd64 # go 1.17 or higher should work
    VsphereVcenter Version:	7.0.3 ,Build:	19234570
    

Simple go client for using vcenter rest api.

Sample user/pass json file

    cat ~/.vmwarepass.json
    {
    "host":"host1.virtualdc.local",
    "username":"staff@virtualdc.com",
    "secret":"wli#Lol-2Gbv#"
    }


First clone the repo and run build

    cd into /path/to/repo
    go build

#Usage -help :
    

    ./vcenterapi -h   //display help
    2022/03/01 14:05:36 Connection successful vsph.virtualdc.com:443
    Usage of ./vcenterapi:
    -list
    Lists available virtual machines
    -start
    start vm700 vm701 #starts vms with vmid vm700 vm701
    -stop
    stop vm10 vm31 #stops vms with vmid vm10 vm31

        
        
List vm's & get the vmid eg. 
--------------------------------------------------------------------------

Output order - vmid , vmName,PoweredState  , Memory(MB) , Num of cpu

    ./vcenterapi -list | grep "192.45.9.19" 

    vm-236,Normal_Windows_192.45.9.191,POWERED_OFF,mem:32768,cpu:16

    vm-138,Normal_Windows_192.45.9.192,POWERED_OFF,POWERED_OFF,mem:32168,cpu:18

    vm-182,Normal_Windows_192.45.9.193,POWERED_OFF,POWERED_ON,mem:4096,cpu:8

--------------------------------------------------------------------------
Start vm's
--------------------------------------------------------------------------
    ./vcenterapi -start vm-24949 vm-51499 vm-51500 vm-51501 vm-51502 vm-51503 vm-5646 vm-69521
    2022/03/01 20:42:36 Connection was successful :vsph.virtualdc.com:443
    2022/03/01 20:42:36 [vm-24949 vm-51499 vm-51500 vm-51501 vm-51502 vm-51503 vm-5646 vm-69521]
    2022/03/01 20:42:39 &{0x1120700 {0xc000114ab0} 0x11d0ee0} 204
    2022/03/01 20:42:39 Machine/s started successfully.
    2022/03/01 20:42:39 &{0x1120700 {0xc000114ab0} 0x11d0ee0} 204
    2022/03/01 20:42:39 Machine/s started successfully.
    2022/03/01 20:42:39 &{0x1120700 {0xc000240f20} 0x11d0ee0} 400
    2022/03/01 20:42:39 Problem starting vm-5646, already in poweredOn state.
    2022/03/01 20:42:40 &{0x1120700 {0xc000114ab0} 0x11d0ee0} 204
    2022/03/01 20:42:40 Machine/s started successfully.
    2022/03/01 20:42:40 &{0x1120700 {0xc000114ab0} 0x11d0ee0} 204
    2022/03/01 20:42:40 Machine/s started successfully.
    2022/03/01 20:42:40 &{0x1120700 {0xc000114ab0} 0x11d0ee0} 204
    2022/03/01 20:42:40 Machine/s started successfully.
    2022/03/01 20:42:40 &{0x1120700 {0xc000114ab0} 0x11d0ee0} 204
    2022/03/01 20:42:40 Machine/s started successfully.
    2022/03/01 20:42:40 &{0x1120700 {0xc000114ab0} 0x11d0ee0} 204
    2022/03/01 20:42:40 Machine/s started successfully.


--------------------------------------------------------------------------
Shutting down one or more vm's
--------------------------------------------------------------------------

    ./vcenterapi -stop vm-51502 vm-5646 vm-69521
    2022/03/01 01:34:45 [vm-51502 vm-5646 vm-69521]
    2022/03/01 01:34:47 &{0x1120700 {0xc000100ab0} 0x11d0e00} 204
    2022/03/01 01:34:47 &{0x1120700 {0xc000100ab0} 0x11d0e00} 204
    2022/03/01 01:34:47 Machine/s stopped successfully.
    2022/03/01 01:34:47 Machine/s stopped successfully.
    2022/03/01 01:34:47 &{0x1120700 {0xc000100ab0} 0x11d0e00} 204
    2022/03/01 01:34:47 Machine/s stopped successfully.
if machines are already powered off the o/p is likely to be eg.:

    2022/03/01 01:36:46 &{0x1120700 {0xc0001f6c60} 0x11d0e00} 400
    2022/03/01 01:36:46 Problem stopping vm-5646, already in off state.

#### **Terms and its meaning**

    * ESXi is a product which provides virtualization.
    
    * Vsphere is the name givne to the bundle of all features in the new version (ESXi, vcenter and its features so on).So ESXi is one of the product in vsphere.
