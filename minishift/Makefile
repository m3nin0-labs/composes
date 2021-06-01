download:
	wget https://github.com/minishift/minishift/releases/download/v1.34.3/minishift-1.34.3-linux-amd64.tgz

unzip: download
	tar -xvzf minishift-1.34.3-linux-amd64.tgz

minishift: unzip
	chmod +x minishift-1.34.3-linux-amd64/minishift && sudo mv minishift-1.34.3-linux-amd64/minishift /usr/local/bin/minishift	

start:
	virsh net-start default
	minishift start
