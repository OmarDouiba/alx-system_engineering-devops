# Install Python 3
# Install Flask using pip3
# Install Werkzeug using pip3

package { 'python3':
    ensure  => 3.8.10,
}
package { 'flask':
    ensure      => '2.1.0',
    provider    => 'pip3',
    require     => Package['python3']
}
package { 'Werkzeug':
    ensure      => '2.1.1',
    provider    => 'pip3',
    require     => Package['flask']
}