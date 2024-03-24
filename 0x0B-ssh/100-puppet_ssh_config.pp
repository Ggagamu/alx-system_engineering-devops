# Client SSH configuration file with Puppet.
file_line { 'Show identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
file_line { 'turn off password login':
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
}
