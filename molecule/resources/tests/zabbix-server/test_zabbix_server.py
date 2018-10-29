import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('zabbix_server')


def test_zabbix_server_is_installed_and_running(host):
    assert host.package("zabbix-server-pgsql").is_installed
    assert host.service("zabbix-server").is_enabled
    assert host.service("zabbix-server").is_running
    assert host.socket("tcp://0.0.0.0:10051").is_listening


def test_zabbix_web_is_installed_and_running(host):
    assert host.package("zabbix-frontend-php").is_installed
    assert host.service("apache2").is_enabled
    assert host.service("apache2").is_running
    assert host.socket("tcp://0.0.0.0:80").is_listening
