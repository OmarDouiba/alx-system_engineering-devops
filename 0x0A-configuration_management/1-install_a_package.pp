#!/usr/bin/pup
# Install the flask package
package { 'python3':
  ensure => '3.8.10',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

package {'Werkzeug':
  ensure => '2.1.1'
}