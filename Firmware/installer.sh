sudo apt install whiptail -y

phases=( 
    'Creating directories...'
    'Installing System Packages...'
    'Installing python packages...'
    'Finalizing installation...'
)   

for i in $(seq 1 100); do  
    sleep 0.01

    if [ $i -eq 100 ]; then
        echo -e "XXX\n100\nDone!\nXXX"
    elif [ $(($i % 25)) -eq 0 ]; then
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
            # mkdir ~/RPiClient
            git clone \
            --depth 1  \
            --filter=blob:none  \
            --sparse \
            https://github.com/Nauman3S/Smart-In-Car-Display.git;
            cd Smart-In-Car-Display
            git sparse-checkout set Firmware
            mv Firmware ../
            cd ..
            rm -rf Smart-In-Car-Display
            mkdir SmartInCarDisplay
            mv Firmware SmartInCarDisplay
        fi
        if [ -d "$HOME/SmartInCarDisplay/logs" ]
        then
            echo "Directory SmartInCarDisplay/logs exists."
        else
            echo "Error: Directory SmartInCarDisplay/logs does not exists."
        mkdir ~/SmartInCarDisplay/logs
        fi
    elif [ $i -eq 10 ]; then
        sudo apt-get update
        clear
    elif [ $i -eq 15 ]; then
        sudo apt install python3-pip
    elif [ $i -eq 20 ]; then
        sudo apt-get install python3-pil python3-pil.imagetk
    elif [ $i -eq 25 ]; then
        sudo pip3 install pillow
    elif [ $i -eq 30 ]; then
        sudo pip3 install python3-dev
    elif [ $i -eq 35 ]; then
        sudo pip3 install hyperpixel2r
    elif [ $i -eq 40 ]; then
        sudo pip3 install Adafruit_DHT
    fi
done | whiptail --title 'Smart In-Car Display Installer' --gauge "${phases[0]}" 8 70 0

whiptail --title "Smart In-Car Display Installer" --msgbox "Installed!" 8 70

