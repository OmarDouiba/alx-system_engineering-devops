# set up your client SSH configuration file using Puppet

file_line {'ssh_config_1':
    ensure => present,
    path   => '/etc/ssh/ssh_config,
    line   => 'IdentifyFile ~/.ssh/school',
}

file_line {'ssh_config_2':
    ensure => present,
    path   => 'etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}