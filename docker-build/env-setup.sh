RUN apt-get update -y
apt-get install -y curl
apt-get install -y git
pip install --upgrade pip
pip install virtualenv
virtualenv vvv
source vvv/bin/activate
