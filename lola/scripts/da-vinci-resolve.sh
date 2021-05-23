
sudo apt update
sudo apt upgrade
sudo apt install xorriso libssl1.0.0 ocl-icd-opencl-dev fakeroot
ping https://www.danieltufvesson.com/makeresolvedeb
ping https://www.blackmagicdesign.com/products/davinciresolve/
cd ~/Downloads
unzip DaVinci_Resolve_16.1.1_Linux.zip
./makeresolvedeb_16.1.1-3.sh lite
sudo dpkg -i davinci-resolve_16.1.1-3_amd64.deb