apt update -y
apt install -y curl
apt install -y git
apt install -y python3
apt install -y python3-pip
pip3 install virtualenv
virtualenv vvv
source vvv/bin/activate
echo "tzdata tzdata/Areas select America" | debconf-set-selections
echo "tzdata tzdata/Zones/America select Denver" | debconf-set-selections
apt install -y python3-tk
curl -sSfL https://raw.githubusercontent.com/AshGw/AES-256/main/important/setup.sh | bash
