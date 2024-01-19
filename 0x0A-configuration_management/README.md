# 0x0A. Configuration management

#### Resources

- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file (check “Resource types” for all manifest types in the left menu)](https://www.puppet.com/docs/puppet/5.5/types/file.html)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Install puppet

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](https://www.puppet.com/docs/puppet/5.5/puppet_index.html)

### Install _puppet-lint_

```
$ gem install puppet-lint
```
