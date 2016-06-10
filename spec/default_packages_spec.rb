require 'spec_helper'

describe package('gnupg2') do
  it { should be_installed }
end
