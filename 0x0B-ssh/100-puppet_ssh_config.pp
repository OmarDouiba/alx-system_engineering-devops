# 100-puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => "# This file is managed by Puppet\n\nPasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}
