#!/usr/bin/env bash
set -e

mkdir -p /home/ubuntu/yn-build/package_v2/exefs
mkdir -p /home/ubuntu/yn-build/package_v2/control
mkdir -p /home/ubuntu/yn-build/package_v2/out
mkdir -p /home/ubuntu/yn-build/package_v2/nca

cp /home/ubuntu/yn-build/package/exefs/main /home/ubuntu/yn-build/package_v2/exefs/main
cp /home/ubuntu/yn-build/tools/modern_main.npdm /home/ubuntu/yn-build/package_v2/exefs/main.npdm

/opt/devkitpro/tools/bin/nacptool --create "梦日记" "YG" "1.0.0" /home/ubuntu/yn-build/package_v2/control/control.nacp --titleid=0100A1B2C3D40000
cp /home/ubuntu/yn-build/package/control/icon_AmericanEnglish.dat /home/ubuntu/yn-build/package_v2/control/icon_AmericanEnglish.dat

if [ ! -d /home/ubuntu/yn-build/package_v2/romfs ]; then
    ln -s /home/ubuntu/yn-build/package/romfs /home/ubuntu/yn-build/package_v2/romfs
fi

cd /home/ubuntu/yn-build/package_v2
/home/ubuntu/yn-build/tools/Nro2Nsp-master/Source/Control/Resources/hacbrewpack --nologo -k /mnt/d/Download/SwitchKeys/prod.keys --nspdir ./out --ncadir ./nca > ./hacbrewpack.log 2>&1
echo "hacbrewpack finished with exit code $?"
tail -n 25 ./hacbrewpack.log
ls -la ./out/
