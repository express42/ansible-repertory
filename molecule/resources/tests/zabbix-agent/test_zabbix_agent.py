import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_zabbix_agent_is_installed_and_running(host):
    assert host.package("zabbix-agent").is_installed
    assert host.service("zabbix-agent").is_enabled
    assert host.service("zabbix-agent").is_running
    assert host.socket("tcp://0.0.0.0:10050").is_listening
