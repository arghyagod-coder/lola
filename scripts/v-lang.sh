cd ~;
wget https://github.com/vlang/v/releases/latest/download/v_linux.zip ;
unzip ~/v_linux.zip;
sudo echo "export PATH=$PATH:$HOME/v_linux" >> ~/."$0"rc