# shellcheck disable=SC2046
if [ "$(whoami)" != 'root' ]; then
  echo "Setup requires root privileges to instal packages.
run with sudo."
  exit 1;
fi

bash ./venv/bin/activate;

pythonVersion=$(python --version);

if [ "$pythonVersion" = 'Python 3.7.5' ]; then
  echo "Python is loaded correctly"
else
  echo "Python is not loaded correctly.
  Delete the 'venv' environment folder and create a new environment with name 'venv' and python version == 3.7.5"
fi

pip install -r requirements.txt;

wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
codeName=$(lsb_release -c | cut -f 2)
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu $codeName/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

apt-get update
apt-get install -y mongodb-org
systemctl start mongod