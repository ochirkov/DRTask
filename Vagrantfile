# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 22, host: 2222
  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.provider "virtualbox" do |vb|
    vb.gui = true
    vb.memory = "2048"
    vb.name = "DataRobotInstance"
  end

  config.ssh.insert_key = false

#  config.vm.provision "ansible",

end