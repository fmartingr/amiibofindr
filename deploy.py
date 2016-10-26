# coding: utf-8

# 3rd party
import click
from fabric.api import local


@click.command()
@click.option('--branch', '-b', default='master',
              help='Branch to git clone from')
@click.option('--inventory', '-i', default='hosts',
              help='Inventory file for ansible to use')
@click.option('--host', '-h', default='web-01',
              help='Host to deploy to')
@click.option('--tag', '-t', default='deploy',
              help='Ansible tags to run')
@click.option('--tasks', count=True,
              help='List tasks instead of executing them')
@click.option('--hosts', count=True,
              help='List hosts instead of executing tasks')
@click.option('--verbose', count=True,
              help='Appends -vvvv to ansible')
def deploy(branch, inventory, host, tag, tasks, hosts, verbose):
    cmd = 'ansible-playbook -i provision/{}'.format(inventory)

    if host:
        cmd += ' -l {}'.format(host)

    cmd += ' -t {}'.format(tag)

    if tasks:
        cmd += ' --list-tasks'

    if hosts:
        cmd += ' --list-hosts'

    cmd += ' -e git_branch={}'.format(branch)

    cmd += ' provision/playbook.yml'

    if verbose:
        cmd += ' -vvvv'

    local(cmd)


# Let's do this
if __name__ == '__main__':
    deploy()
