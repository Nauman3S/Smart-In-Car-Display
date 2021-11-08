sudo apt install whiptail -y

phases=( 
    '1) Creating directories, Downloading Firmware...'
    '2) Installing System Packages...'
    '3) Installing python packages...'
    '4) Downloading and Installing HyperPixel...'
    '5) Setting up Scripts...'
    '6) Configuring Startup Script...'
    '7) Finalizing Installation...'
    '8) Finalizing Installation...'
    
)   

for i in $(seq 1 100); do  
    sleep 0.01

    if [ $i -eq 100 ]; then
        echo -e "XXX\n100\nDone!\nXXX"
    elif [ $(($i % 15)) -eq 0 ]; then
        let "phase = $i / 25"
        echo -e "XXX\n$i\n${phases[phase]}\nXXX"
    else
        echo $i
    fi

    if [ $i -eq 5 ]; then
        if [ -d "$HOME/SmartInCarDisplay" ]
        then
            echo "Directory SmartInCarDisplay exists."
        else
            echo "Error: Directory SmartInCarDisplay does not exists."
            cd $HOME
            mkdir SmartInCarDisplay;
            mkdir SmartInCarDisplay/temp;
            # mkdir ~/RPiClient
            git clone https://github.com/Nauman3S/Smart-In-Car-Display.git >> $HOME/SmartInCarDisplay/temp/SICDRepo.text 2>&1;
            cd Smart-In-Car-Display;
            mv Firmware ../SmartInCarDisplay/Firmware;
            cd ..
            rm -rf Smart-In-Car-Display
            cd SmartInCarDisplay/Firmware
            sudo chmod a+rx starter.sh
            clear;
        fi
        if [ -d "$HOME/SmartInCarDisplay/logs" ]
        then
            echo "Directory SmartInCarDisplay/logs exists."
        else
            echo "Error: Directory SmartInCarDisplay/logs does not exists."
            mkdir ~/SmartInCarDisplay/logs
        fi
    elif [ $i -eq 10 ]; then
        sudo apt-get update >> $HOME/SmartInCarDisplay/temp/sysUpdate.text 2>&1
        clear
    elif [ $i -eq 15 ]; then
        sudo apt install python3-pip
    elif [ $i -eq 20 ]; then
        sudo apt-get install python3-pil python3-pil.imagetk
    elif [ $i -eq 25 ]; then
        sudo pip3 install pillow
    elif [ $i -eq 30 ]; then
        sudo pip3 install python3-dev &>/dev/null
        sudo apt install libpython3-dev
    elif [ $i -eq 35 ]; then
        sudo pip3 install hyperpixel2r
    elif [ $i -eq 40 ]; then
        sudo pip3 install Adafruit_DHT
    elif [ $i -eq 80 ]; then
        cd $HOME
        cd SmartInCarDisplay/temp
        git clone https://github.com/pimoroni/hyperpixel2r $HOME/SmartInCarDisplay/temp/hyperpixelRepo.text 2>&1;
        cd hyperpixel2r
        sudo ./install.sh
    elif [ $i -eq 90 ]; then
        File="/etc/rc.local"
        if [[ $(grep "(sleep 10; sh /home/pi/SmartInCarDisplay/Firmware/starter.sh)&" $File) ]] ; then
            echo "Found startup script. Doing nothing."
        else
            echo "Not Found. Adding startup script"
            sed -i -e '$i \(sleep 10; sh /home/pi/SmartInCarDisplay/Firmware/starter.sh)&\n' /etc/rc.local
        fi
    fi
done | whiptail --title 'Smart In-Car Display Installer' --gauge "${phases[0]}" 8 70 0

whiptail --title "Smart In-Car Display Installer" --msgbox "Installed!" 8 70

# curl -sSL https://raw.githubusercontent.com/Nauman3S/Smart-In-Car-Display/main/Firmware/installer.sh | bash