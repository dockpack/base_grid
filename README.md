[![Galaxy](https://img.shields.io/badge/galaxy-dockpack.base__grid-blue.svg?style=flat)](https://galaxy.ansible.com/dockpack/base_grid)[![Build Status](https://api.travis-ci.org/dockpack/base_grid.svg)](https://travis-ci.org/dockpack/base_grid)


Base Grid
=========

A Selenium Grid running with docker-compose

Requirements
------------

Python pip needs to be available to test multiple versions of Ansible with Tox and Molecule.

```
pip install requirements.txt
```

Docker
------

This role assumes the presence of a (local) registry with docker images mentioned in the vars and defaults.

Vagrant
-------

I test this on a Mac with Vagrant and Virtualbox. Download my custom Centos 7:
`vagrant init redesign/centos7`


Role Variables
--------------

The defaults/main.yml file has variables that can be changed for different versions mostly.
Refer to this page for browser versions supported: [https://github.com/SeleniumHQ/docker-selenium/releases](https://github.com/SeleniumHQ/docker-selenium/releases)

Roles that go well with this role.
------------

dockpack.base_goss
dockpack.base.docker

Testing
-------
Tox is used, so the full thing is tested with:
```
tox
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

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
