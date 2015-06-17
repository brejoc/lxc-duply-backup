# lxc-duply-backup

With lxc-duply-backup you can generate Deb or RPM packages that automatically backup Linux Containers. It makes use of [duply](http://www.duply.net/) and cron jobs.

The origins of lxc-duply-backup can be found in my [blog post](http://brejoc.com/lxc_backup_with_duply/).

**Attention**:   
Containers are stopped before the backup and started right after the backup to make sure the backups are clean. Otherwise data might still be in memory and not on disk.


# Dependencies (for building packages)
* [invoke](https://github.com/pyinvoke/invoke)
* [fpm](https://github.com/jordansissel/fpm/wiki)
* [PyYAML](http://pyyaml.org/)
* [sh](https://github.com/amoffat/sh)

# Dependencies (for the package itself)
* [duply](http://duply.net/)
* [LXC](https://linuxcontainers.org/)

Debian/Ubuntu: `apt-get install lxc duply`

# Usage

1. Create your own [config](https://github.com/brejoc/lxc-duply-backup/blob/master/configs/invoices_example.yaml). Most likely you want to change the [package name](https://github.com/brejoc/lxc-duply-backup/blob/master/configs/invoices_example.yaml#L1), the paths to the [config files](https://github.com/brejoc/lxc-duply-backup/blob/master/configs/invoices_example.yaml#L7) (with the container name), the [config path](https://github.com/brejoc/lxc-duply-backup/blob/master/configs/invoices_example.yaml#L25) and [container name](https://github.com/brejoc/lxc-duply-backup/blob/master/configs/invoices_example.yaml#L26).
2. And build the package: `invoke build_deb --config configs/my_new_config.yaml`

# License

[Public Domain](https://github.com/brejoc/lxc-duply-backup/blob/master/LICENSE)
