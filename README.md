# How to deploy this for yourself

I recommend a dedicated Debian vitrual machine.

## `apt-update` and install prerequesties

```sh
apt-get update
apt-get upgrade -y

apt-get install -y git curl python3-venv python3-pip
```


## Create a non-`root` user

```sh
adduser satoshi
usermod -aG sudo satoshi
```

## change `root` prompt to signal completion
```sh
echo 'export PS1="\n\[\e[1;35m\](\[\e[1;31m\]\u\[\e[1;35m\]@\[\e[1;34m\]\h\[\e[1;35m\]) [\w]\n\[\e[1;36m\]\$ \[\e[0m\]"' >> ~/.bashrc
```


Then, log out of `root` and log in as this user

```sh
# signal that we are non-root
echo 'export PS1="\n\[\e[1;35m\](\[\e[1;31m\]\u\[\e[1;35m\]@\[\e[1;34m\]\h\[\e[1;35m\]) [\w] \[\e[33;3m\]\A\[\e[0m\] \[\e[1;36m\]\$ \[\e[0m\]\n"' >> ~/.bashrc


# log out and in again...
```

## clone the repo

```sh
git clone https://github.com/PlebeiusGaragicus/plebtools.git
cd plebtools
```

## configure the Python virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```


Copy and paste in any API keys you have.

## setup a `systemd` service to launch the application

Note: This will need `root` access.  Log in as `root` for these next steps.


```sh
cat << EOF > /etc/systemd/system/plebtools.service
[Unit]
Description=PlebTools Service
After=network.target

[Service]
User=satoshi
WorkingDirectory=/home/satoshi/plebtools
ExecStart=/bin/bash -c "/home/satoshi/plebtools/production"
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
EOF

nano /etc/systemd/system/plebtools.service
```

Also, replace `satoshi` with the non-root Linux username that you created earlier.

## start the service and monitor for errors

```sh
systemctl start plebtools
systemctl status plebtools

# works..?  If so:
systemctl enable plebtools

# watch it run via:
journalctl -u plebtools -f # hitting 'q' will exit
```

## Visit the application

Open a browser and go to the IP address of the server at port 8501. To determine the ip address, run the `ip addr` command.

For example, if your ip address is `192.169.10.200`, then put `192.169.10.200:8501` in your browser and it should work.

If you're running this locally instead of on a dedicated server then visit [localhost:8501](http://localhost:8501)
