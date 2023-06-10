apt-get update -y
apt-get install -y curl
apt-get install -y git
apt-get install -y python3
apt-get install -y python3-pip
pip3 install --upgrade pip
pip3 install virtualenv
virtualenv vvv
source vvv/bin/activatec
curl -sSfL https://raw.githubusercontent.com/AshGw/AES-256/main/important/setup.sh | bash
