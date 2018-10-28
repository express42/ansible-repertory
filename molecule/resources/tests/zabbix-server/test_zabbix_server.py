import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('zabbix_server')


def test_installed_packages(host):
    assert host.package("zabbix-server-pgsql").is_installed
