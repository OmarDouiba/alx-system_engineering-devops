# the file create file name school in tmp
# and give him mode and owner and group

file { '/tmp/school':
    ensure  => present,
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}