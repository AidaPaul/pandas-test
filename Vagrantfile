# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|

  config.vm.box = "hashicorp/trusty64"

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = "2"
    vb.memory = "2048"
    config.vm.synced_folder ".", "/opt/pandas-test"
  end

  config.vm.provider "hyperv" do |hv|
    hv.memory = "2048"
    hv.cpus = "2"
    config.vm.box = "ericmann/trusty64"
    config.vm.synced_folder ".", "/opt/pandas-test", type: "smb"
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y curl unzip
    sudo apt-get install -y python3-dev
    sudo apt-get install -y python3-pip
    sudo apt-get install -y python3-pandas
    sudo apt-get install -y redis-server
    sudo pip3 install -r /opt/pandas-test/requirements.txt

    curl -s https://sdm.lbl.gov/fastbit/data/star2000.csv.gz -o /tmp/star200.csv.gz
    gzip -d /tmp/star200.csv.gz --to-stdout > /opt/pandas-test/star200.csv

    python3 /opt/pandas-test/runme.py
  SHELL
end
