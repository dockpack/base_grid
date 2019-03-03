# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # define provider preference in your environment with VAGRANT_DEFAULT_PROVIDER
  config.vbguest.auto_update = false
  config.ssh.forward_agent = false
  config.ssh.insert_key = false
  # Timeouts
  config.vm.graceful_halt_timeout=30

  config.vm.define :IE8Win7, autostart: false do |windows|
    windows.vm.box = "IE8.Win7"
    windows.vm.hostname = "IE8.Win7"
    windows.vm.guest = :windows
    windows.vm.communicator = "winrm"
    # Admin user name and password
    windows.winrm.username = "IEUser"
    windows.winrm.password = "Passw0rd!"
    config.vm.boot_timeout = 36000
    windows.vm.network "private_network", ip: "192.168.10.23", :netmask => "255.255.255.0",  auto_config: true
    # puts "Use RDP to connect to 192.168.33.147:3389 User: IEUser, Password: Passw0rd!"
    #windows.vm.network :forwarded_port, guest: 3389, host: 3389, id: "rdp", auto_correct: true
    #windows.vm.network "forwarded_port", id: 'selenium', guest: 4444, host: 4444, auto_correct: false
    windows.vm.provider "virtualbox" do |vb|
      vb.customize [
        "modifyvm", :id,
        "--memory", "4096",
        "--natdnshostresolver1", "on",
        "--cableconnected1", "on",
      ]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
      vb.gui = true
      vb.name = "IE8.Win7"
    end
  end

  config.vm.define :IE9Win7, autostart: false do |windows|
    windows.vm.box = "IE9.Win7"
    windows.vm.hostname = "IE9.Win7"
    windows.vm.guest = :windows
    windows.vm.communicator = "winrm"
    # Admin user name and password
    windows.winrm.username = "IEUser"
    windows.winrm.password = "Passw0rd!"
    config.vm.boot_timeout = 36000
    windows.vm.network "private_network", ip: "192.168.10.24", :netmask => "255.255.255.0",  auto_config: true
    # puts "Use RDP to connect to 192.168.33.147:3389 User: IEUser, Password: Passw0rd!"
    #windows.vm.network :forwarded_port, guest: 3389, host: 3389, id: "rdp", auto_correct: true
    #windows.vm.network "forwarded_port", id: 'selenium', guest: 4444, host: 4444, auto_correct: false
    windows.vm.provider "virtualbox" do |vb|
      vb.customize [
        "modifyvm", :id,
        "--memory", "4096",
        "--natdnshostresolver1", "on",
        "--cableconnected1", "on",
      ]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
      vb.gui = true
      vb.name = "IE9.Win7"
    end
  end

  config.vm.define :IE10Win7, autostart: false do |windows|
    windows.vm.box = "IE10.Win7"
    windows.vm.hostname = "IE10.Win7"
    windows.vm.guest = :windows
    windows.vm.communicator = "winrm"
    # Admin user name and password
    windows.winrm.username = "IEUser"
    windows.winrm.password = "Passw0rd!"
    config.vm.boot_timeout = 36000
    windows.vm.network "private_network", ip: "192.168.10.25", :netmask => "255.255.255.0",  auto_config: true
    # puts "Use RDP to connect to 192.168.33.147:3389 User: IEUser, Password: Passw0rd!"
    #windows.vm.network :forwarded_port, guest: 3389, host: 3389, id: "rdp", auto_correct: true
    #windows.vm.network "forwarded_port", id: 'selenium', guest: 4444, host: 4444, auto_correct: false
    windows.vm.provider "virtualbox" do |vb|
      vb.customize [
        "modifyvm", :id,
        "--memory", "4096",
        "--natdnshostresolver1", "on",
        "--cableconnected1", "on",
      ]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
      vb.gui = true
      vb.name = "IE10.Win7"
    end
  end

  config.vm.define :IE11Win7, autostart: false do |windows|
    windows.vm.box = "IE11.Win7"
    windows.vm.hostname = "IE11.Win7"
    windows.vm.guest = :windows
    windows.vm.communicator = "winrm"
    # Admin user name and password
    windows.winrm.username = "IEUser"
    windows.winrm.password = "Passw0rd!"
    config.vm.boot_timeout = 36000
    windows.vm.network "private_network", ip: "192.168.10.26", :netmask => "255.255.255.0",  auto_config: true
    # puts "Use RDP to connect to 192.168.33.147:3389 User: IEUser, Password: Passw0rd!"
    #windows.vm.network :forwarded_port, guest: 3389, host: 3389, id: "rdp", auto_correct: true
    #windows.vm.network "forwarded_port", id: 'selenium', guest: 4444, host: 4444, auto_correct: false
    windows.vm.provider "virtualbox" do |vb|
      vb.customize [
        "modifyvm", :id,
        "--memory", "4096",
        "--natdnshostresolver1", "on",
        "--cableconnected1", "on",
      ]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
      vb.gui = true
      vb.name = "IE11.Win7"
    end
  end

    config.vm.define :IE11Win81, autostart: false do |windows|
    windows.vm.box = "IE11.Win81"
    windows.vm.hostname = "IE11.Win81"
    windows.vm.guest = :windows
    windows.vm.communicator = "winrm"
    # Admin user name and password
    windows.winrm.username = "IEUser"
    windows.winrm.password = "Passw0rd!"
    config.vm.boot_timeout = 36000
    windows.vm.network "private_network", ip: "192.168.10.27", :netmask => "255.255.255.0",  auto_config: true
    # puts "Use RDP to connect to 192.168.33.147:3389 User: IEUser, Password: Passw0rd!"
    #windows.vm.network :forwarded_port, guest: 3389, host: 3389, id: "rdp", auto_correct: true
    #windows.vm.network "forwarded_port", id: 'selenium', guest: 4444, host: 4444, auto_correct: false
    windows.vm.provider "virtualbox" do |vb|
      vb.customize [
        "modifyvm", :id,
        "--memory", "4096",
        "--natdnshostresolver1", "on",
        "--cableconnected1", "on",
      ]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
      vb.gui = true
      vb.name = "IE11.Win81"
    end
  end

    config.vm.define :MSEdgeWin10, autostart: false do |windows|
    windows.vm.box = "MSEdge.Win10"
    windows.vm.hostname = "MSEdge.Win10"
    windows.vm.guest = :windows
    windows.vm.communicator = "winrm"
    # Admin user name and password
    windows.winrm.username = "IEUser"
    windows.winrm.password = "Passw0rd!"
    config.vm.boot_timeout = 36000
    windows.vm.network "private_network", ip: "192.168.10.28", :netmask => "255.255.255.0",  auto_config: true
    # puts "Use RDP to connect to 192.168.33.147:3389 User: IEUser, Password: Passw0rd!"
    #windows.vm.network :forwarded_port, guest: 3389, host: 3389, id: "rdp", auto_correct: true
    #windows.vm.network "forwarded_port", id: 'selenium', guest: 4444, host: 4444, auto_correct: false
    windows.vm.provider "virtualbox" do |vb|
      vb.customize [
        "modifyvm", :id,
        "--memory", "4096",
        "--natdnshostresolver1", "on",
        "--cableconnected1", "on",
      ]
      vb.customize ["setextradata", "global", "GUI/SuppressMessages", "all" ]
      vb.gui = true
      vb.name = "MSEdge.Win10"
    end
  end
end
