
sudo apt-get update
sudo apt-get install -y xorriso libssl1.0.0 ocl-icd-opencl-dev fakeroot
cd ~/Downloads
echo 'Download the DaVinci_Resolve_16.1.1_Linux.zip file from https://www.blackmagicdesign.com/products/davinciresolve/#'
wget https://www.danieltufvesson.com/download/?file=makeresolvedeb/makeresolvedeb_1.5.0_multi.sh.tar.gz
unzip DaVinci_Resolve_16.1.1_Linux.zip
./makeresolvedeb_16.1.1-3.sh lite
sudo dpkg -i davinci-resolve_16.1.1-3_amd64.deb
