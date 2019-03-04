[![Galaxy](https://img.shields.io/badge/galaxy-dockpack.base__grid-blue.svg?style=flat)](https://galaxy.ansible.com/dockpack/base_grid)[![Build Status](https://api.travis-ci.org/dockpack/base_grid.svg)](https://travis-ci.org/dockpack/base_grid)

Base Grid
=========

A *Selenium Grid* running with docker-compose and others.

![Selenium Grid screenshot](https://raw.githubusercontent.com/bbaassssiiee/base_grid/master/meta/grid.png)

The goal is to help web developers make web sites work for the public at large.

`dockpack.base_grid` is an Ansible role that deploys a Selenium grid, and it adds
some extra's so you can use it in local mode to simulate the optimal variety of
web browsers.

Quite common in corporate life, people have Virtual Desktops
(Citrix or VMWare Horizon) for Windows, and  on-premise servers running Red Hat
Enterprise 7, where they could only run a Docker version which is supported by
RedHat, docker-latest 1.13.

Running containers would need to work with an internal docker registry like
Sonatype Nexus, and also all internet traffic should be proxied.

When you want to automate cross browser testing you would need a Selenium Grid
that you can connect to from the Virtual Desktops and from an in-house buildserver
(Jenkins). The docker-compose grid runs old and new versions of Firefox and
Chrome. These older versions are not present on modern corporate IT systems,
but some folks still use them. Microsoft publishes VM images with various older
versions of Internet Explorer, using Vagrant we can add these to the local grid.

Centos 7.5
----------

This Ansible role is tested with my redesign/centos7 Vagrant box. The Packer
source is available at
[https://github.com/bbaassssiiee/redesign](https://github.com/bbaassssiiee/redesign)

```
vagrant init redesign/centos7
```

Role Variables
--------------

The `defaults/main.yml` file has variables that can be changed for different
versions mostly. Refer to this page for browser versions supported:
[https://github.com/SeleniumHQ/docker-selenium/releases](https://github.com/SeleniumHQ/docker-selenium/releases)
This role assumes the presence of Docker and a (local) registry like Sonatype
Nexus holding images mentioned in the vars and defaults. This registry can be
set as `selenium_registry` in your group_vars if needed.

Testing
-------

You can imagine that maintaining such test infrastructure is and intricate job,
therefore this repo has tools to simulate various things that we need to deal
with in the near future (2019) We can address these issues:

1. Python 2.7 to Python 3
1. Ansible 2.6 to 2.7, and others

Requirements
------------

Python pip needs to be available to test multiple versions of Ansible with Tox
and Molecule.

```
pip install requirements.txt
```

On-Premise Docker Registry
--------------------------

You can download these originals, tag them and push them to your local
registry.

```
docker pull selenium/node-firefox:3.141.59-iron
docker pull  selenium/node-firefox:3.12.0-cobalt
docker pull  selenium/node-chrome:3.141.59-iron
docker pull  selenium/node-chrome:3.8.1-erbium"
docker pull  selenium/hub:3.141.59-iron
```

```
docker images
docker tag ...
docker push ...
```

Vagrant testing
---------------

You can use 7 versions of Internet Explorer by downloading Microsoft's VMs.
This script does the download unzip and `vagrant box add` so you can use the
`Vagrantfile`.

```
cd vagrant
./windows_boxes.py
```

```
vagrant up IE8Win7
vagrant up IE9Win7
vagrant up IE10Win7
vagrant up IE11Win7
vagrant up IE11Win81
vagrant up MSEdgeWin10
```

Mac Tools
---------

I test this on a Mac with Vagrant and Virtualbox. I install all Mac tools
included in th `Brewfile` with:

```
brew bundle
```

Roles that go well with this role
---------------------------------

dockpack.base_goss
dockpack.base.docker

Tox Testing
-------

Tox is used, so the full thing is tested with:

```
tox
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - name: provision selenium
      hosts: testsystem
      become: yes
      roles:
        - { role: dockpack.base_grid, tags: 'selenium'}

License
-------

MIT

Author Information
------------------

Bas Meijer
@bbaassssiiee
