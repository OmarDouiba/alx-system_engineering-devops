#!/usr/bin/pup
# Install the flask package
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
