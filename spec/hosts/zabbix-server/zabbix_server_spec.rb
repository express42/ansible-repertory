require_relative '../../spec_helper'

describe package('zabbix-server-pgsql') do
  it { should be_installed }
end
