# Using strace, find out why Apache is returning a 500 error
exec {'fix-wordpress':
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp'
}
