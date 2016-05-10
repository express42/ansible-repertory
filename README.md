[![Build Status](https://travis-ci.org/vitkhab/ansible-repertory.svg?branch=master)](https://travis-ci.org/vitkhab/ansible-repertory)

# Install prerequisites
```sh
ansible-galaxy install -r requirements.yml
pip install -r requirements.txt
touch vault.key
```
# Testing
## Using Travis-CI
- Fork git repository
- Add repository into Travis-CI
- Add 'DO_TOKEN' in repository's 'Environment Variables' with token for Digital Ocean
- Clone repository
- Inside repository's working dir run commands
```sh
ssh-keygen -b 4096 -N '' -f deploy_key
gem install travis
travis login
travis encrypt-file deploy_key --add
git commit -a -m 'Updated Travis CI info'
git push
```

## Using Digital Ocean
- Inside repository's working dir run commands
```sh
export DO_TOKEN=%dotoken%
export SSH_KEY_NAME='Some_name'
molecule test --provider=digital_ocean
```

# ToDo
- Make serverspec tests
- Update default packages playbook
- Add more playbooks

# Known issues
- 'zabbix_url' variable used in playbooks dj-wasabi.zabbix-agent and dj-wasabi.zabbix-server for different purposes
  - Workaround: redefine 'zabbix_url' in play_vars
- API calls in playbook dj-wasabi.zabbix-agent made from several servers can interfere with each other
  - Workaround: make API calls serial
- While using VirtualBox for testing you should change all mentions of interface 'eth0' to 'eth1'
