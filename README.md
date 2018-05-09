Base Grid
=========

A Selenium Grid running with docker-compose

Requirements
------------
Python pip needs to be available. (You could use dockpack.base_python for that.)
This role assumes the presence of a local registry for docker.

```
pip install requirements.txt
```

Role Variables
--------------

The defaults/main.yml file has variables that can be changed for different versions mostly.

Roles that go well with this role.
------------

dockpack.base_goss
dockpack.base.docker

Testing
-------

```
molecule test
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

		- name: provision selenium
			hosts: testsystem
			become: yes
			roles:
				- { role: dockepack.base_grid, tags: 'selenium'}

License
-------

MIT

Author Information
------------------

Bas Meijer
@bbaassssiiee
