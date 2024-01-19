# SSH

### Articles

(Config File) [Using the SSH Config File
](https://linuxize.com/post/using-the-ssh-config-file/)

### Videos

- [How Secure Shell Works (SSH) - Computerphile](https://www.youtube.com/watch?v=ORcvSkgdA58)

- [Creating and Using an ssh config file](https://www.youtube.com/watch?v=bO9eX5JIHdE)

- [What is a Server? (Deepdive)](https://www.youtube.com/watch?v=VXmvM2QtuMU)

- [SSH Crash Course | With Some DevOps](https://www.youtube.com/watch?v=hQWRp-FdTpc)

- []()

### General

- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using #!/usr/bin/env bash instead of /bin/bash

---

#### Specify the Key Explicitly:

If you have multiple SSH keys, you might need to specify the correct key explicitly when connecting. You can do this using the -i option:

    ssh -i /path/to/private/key.pem username@hostname

### Task 0

```
#!/bin/bash

# Variables
REMOTE_HOST="8.8.8.8"
REMOTE_USER="ubuntu"
PRIVATE_KEY_PATH="$HOME/.ssh/school"

# SSH connection
ssh -i "$PRIVATE_KEY_PATH" "$REMOTE_USER@$REMOTE_HOST"
```

The -i option in the SSH command is used to specify the identity file (private key) to use for public key authentication.

### Task 1

```
#!/bin/bash

# Variables
KEY_NAME="school"
BITS=4096
PASSPHRASE="betty"

# Create RSA key pair
ssh-keygen -t rsa -b "$BITS" -C "$KEY_NAME" -N "$PASSPHRASE" -f "$KEY_NAME"

echo "RSA key pair has been created:"
ls -l "$KEY_NAME" "$KEY_NAME.pub"

```

In the ssh-keygen command, the options -C, -N, and -f are used as follows:

- `C`: This option allows you to provide a comment or label to help identify the key. In the script, it's used to set the comment of the key to be the same as the key name, which is "school" in this case.

- `N`: This option allows you to specify a new passphrase for the key. In the script, it's used to set the passphrase for the private key to "betty."

- `f`: This option allows you to specify the filename of the key file. In the script, it's used to set the filename of the private key to "school" and, by extension, the public key to "school.pub."

(
`-C is for setting a comment, -N is for setting the passphrase, and -f is for specifying the filename of the key files`
)

### Task 4 (file_line)

- file_line Ensures that a given line is contained within a file. The implementation matches the full line, including whitespace at the beginning and end. If the line is not contained in the given file, Puppet will append the line to the end of the file to ensure the desired state. Multiple resources may be declared to manage multiple lines in the same file.

```
Example:

    file_line { 'sudo_rule':
      path => '/etc/sudoers',
      line => '%sudo ALL=(ALL) ALL',
    }

    file_line { 'sudo_rule_nopw':
      path => '/etc/sudoers',
      line => '%sudonopw ALL=(ALL) NOPASSWD: ALL',
    }

    In this example, Puppet will ensure both of the specified
    lines are contained in the file /etc/sudoers.
```
