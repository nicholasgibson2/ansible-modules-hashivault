#!/usr/bin/env python
DOCUMENTATION = '''
---
author: Developed for AT&T by Nicholas Gibson, August 2017
module: hashivault_write_file
version_added: "3.7.0"
short_description: Hashicorp Vault write file module
description:
    - Writes a file encoded in base64 to Hashicorp Vault. Implementation in `/plugins/action/hashivault_write_file.py`.
options:
    url:
        description:
            - url for vault
        default: to environment variable VAULT_ADDR
    verify:
        description:
            - verify TLS certificate
        default: to environment variable VAULT_SKIP_VERIFY
    authtype:
        description:
            - "authentication type to use: token, userpass, github, ldap, approle"
        default: token
    token:
        description:
            - token for vault
        default: to environment variable VAULT_TOKEN
    username:
        description:
            - username to login to vault.
    password:
        description:
            - password to login to vault.
    secret:
        description:
            - vault secret to write.
    key:
        description:
            - secret key/name of file to write to vault.
    dest:
        description:
            - fully qualified path name of file to read from remote host.
    update:
        description:
            - Update secret rather than overwrite.
        default: True
'''
EXAMPLES = '''
---
- hosts: localhost
  tasks:
    - hashivault_write_file:
        secret: giant
        key: foo.dat
        path: /tmp/foo.dat
'''