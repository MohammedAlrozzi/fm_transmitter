echo "Compiling project"
{
    sudo apt-get install make gcc g++ &&
    make
} &> /dev/null


echo "Install ffmpeg & other libraries in RaspberryPi"
{
    sudo apt-get install libmp3lame-dev &&
    cd /usr/src &&
    sudo git clone git://git.videolan.org/x264 &&
    cd x264 &&
    sudo ./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl &&
    sudo make &&
    sudo make install
} &> /dev/null



echo "Install libmp3lame and x264 libraries"
{
    cd /usr/src &&
    sudo git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg &&
    cd ffmpeg &&
    sudo ./configure --arch=armv7-a --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree --enable-libmp3lame --extra-cflags='-march=armv7-a -mfpu=neon-vfpv4 -mfloat-abi=hard' &&
    sudo make -j4 &&
    sudo make install
} &> /dev/null

echo "Completed"