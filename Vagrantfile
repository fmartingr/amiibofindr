# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define "globalwishlist-backend" do |web|
    web.vm.box = "ubuntu/trusty64"

    #web.vm.network "private_network", type: "dhcp"
    web.vm.network "forwarded_port", guest: 22, host: 2201
    web.vm.network "forwarded_port", guest: 8000, host: 8080

    web.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "512"]
    end

    web.vm.provision "ansible" do |ansible|
      ansible.limit = 'all'
      ansible.playbook = "provision/playbook.yml"
      ansible.inventory_path = "provision/hosts"
    end
  end
end
