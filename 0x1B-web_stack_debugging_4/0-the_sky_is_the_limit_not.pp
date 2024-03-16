# Increases the amount of traffic an Nginx server can handle.

exec { 'fix--for-nginx':
  command     => '/usr/sbin/nginx -s reload',
  path        => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
  refreshonly => true,
}
