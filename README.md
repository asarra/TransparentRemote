# TransparentRemote

TransparentRemote switches HDMI input of the Samsung TV by sending base64 encoded commands to the web API of the TV. It also communicates with the qemu script via another web API to read the VM's state and keyboard state.

I use these scripts to have an automated KVM switch. I just run my Windows 10 (Gaming) VM and that's basically it. It does all the automation.

Note:Use both ALT keys simultanously to change HDMI inputs on the TV! If you are using evdev, make sure to let it assign the keyboard to the host os (both CTRLs)!

I am using these scripts on my following setup: 
Arch Linux -> Kubuntu 20 LTS
           |_ Windows 10 Pro

They work with my Samsung TV from the year 2010.

You have to put the qemu script into the /etc/libvirt/hooks directory and the other scripts can be placed somewhere else, if you want to, but these have to stay together wherever they go.



#Installation

0. Make sure that you read what everything above, make sure that your win10 or whatever operating system you want to use, is ready to be started and make sure that your vm is called "win10". If it is not called win10, the software will not run as intended.
1. Make the ./run_win10.sh file executable by writing "chmod +x ./run_win10.sh" in the CLI.
2. Enter "./run_win10.sh" and hit enter.
