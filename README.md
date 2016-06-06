[![Build Status](https://travis-ci.org/vitkhab/ansible-repertory.svg?branch=master)](https://travis-ci.org/vitkhab/ansible-repertory)

# Overview
This repository is used as a good start point for infrastructure development. It contains basic roles and describes workflow to create solid solution.

The mastery of the ensemble is determined by the quantity and quality of plays performed. Repertory is created to comprise everything needed for server infrastructure of any level and complexity.

## Basic principles
* Playbook per application
* All variables should be defined in environments' vars files

# Directory structure

* `environments/` - root directory for environments
  * `environment_dir/` - directory containing vars and hosts per environment
    * `group_vars/` - variables defined per group
    * `host_vars/` - variables defined per host
    * `play_vars/` - variables defined per play in playbooks
    * `inventory_file` - inventory file with hosts related to the environment
* `playbooks/` - directory for playbooks, playbook per application
* `roles/` - custom roles
* `ansible.cfg` - config for ansible
* `molecule.yml` - config for molecule
* `requirements.txt` - python requirements
* `requirements.yml` - ansible playbooks' requirements
* `site.yml` - playbook containing every app in infrastructure
* `vagrantfile.j2` - custom Vagrantfile template for molecule

# What goes where

## Variables
* All variables should be defined per environment
* The precedence order can be seen at http://docs.ansible.com/ansible/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable
* Try to use only next places to define a variable:
  * Environment host_vars
  * Environment group_vars
  * Environment play_vars
* Avoid setting variable in playbooks

## Tasks
* All tasks should be defined in roles

## Playbooks
* Playbooks contain only roles, groups of hosts and vars files
* Playbook should contain everything needed for application to start
* Avoid setting variables and tasks in playbooks

# Getting started

## Fast start
* Do not forget use Python 2.7 instead of 3.x. Molecule and Ansible doesn't support Python 3.x
* Clone git repo
```sh
git clone git@github.com:vitkhab/ansible-repertory.git
``` 
* Install [the latest release of Vagrant][Vagrant]
* Install Vagrant DigitalOcean provider
```sh
vagrant plugin install vagrant-digitalocean
```
* Install prerequisites
```sh
cd ansible-repertory
ansible-galaxy install -r requirements.yml
pip install -r requirements.txt
touch vault.key
```
* Create VMs using Digital Ocean
  * %DOTOKEN% - Digital Ocean token (if you haven't got one you can create it at https://cloud.digitalocean.com/settings/api/tokens)
  * %SOMENAME% - Name of SSH key at Digital Ocean, it should match your key at https://cloud.digitalocean.com/settings/security 
```sh
export DO_TOKEN=%DOTOKEN%
export SSH_KEY_NAME='%SOMENAME%'
molecule converge --provider=digital_ocean
```
* Destroy created VMs
```sh
molecule destroy --provider=digital_ocean
```

## Using with your infrastructure
* Remove excessive roles from requirements.yml, python modules from requirements.txt and playbooks
* Make changes to site.yml
* Make changes to vars files for molecule environment
* Test changes with command
```sh
molecule test --provider=digital_ocean
```
* Copy molecule environment to new environment
* Make changes to inventory and vars files
* Run command
```sh
ansible-playbook site.yml --inventory-file=./environments/new_environment/inventory
```
## Molecule

First install the [latest release of Vagrant][Vagrant].
```sh
molecule list
molecule converge
molecule status
molecule login common
molecule destroy
```

# Testing using Travis-CI
* Fork git repository
* Add repository into Travis-CI
* Add 'DO_TOKEN' in repository's 'Environment Variables' with token for Digital Ocean
* Clone repository
* Inside repository's working dir run commands
```sh
ssh-keygen -b 4096 -N '' -f deploy_key
gem install travis
travis login
travis encrypt-file deploy_key --add
rm deploy_key deploy_key.pub
git commit -a -m 'Updated Travis CI info'
git push
```

# ToDo
* Make serverspec tests
* Update default packages playbook
* Add more playbooks or list recommended ones
* Add base role (as it is in testo)

# Known issues
* 'zabbix_url' variable used in playbooks dj-wasabi.zabbix-agent and dj-wasabi.zabbix-server for different purposes
  * Workaround: redefine 'zabbix_url' in play_vars
* API calls in playbook dj-wasabi.zabbix-agent made from several servers can interfere with each other
  * Workaround: make API calls serial
* While using VirtualBox for testing you should change all mentions of interface 'eth0' to 'eth1'
* Travis check will fail if VMs are already exists in DO

# Links
* [Ansible documentation](https://docs.ansible.com/ansible/index.html "Ansible documentation")
* [Molecule documentation](https://molecule.readthedocs.io/en/master/ "Molecule documentation")
* [Vagrant documentation](https://www.vagrantup.com/docs/ "Vagrant documentation")

[Vagrant]: https://www.vagrantup.com/downloads.html "Vagrant"
