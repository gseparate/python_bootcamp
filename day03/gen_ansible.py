import subprocess
import yaml
import os
with open('config_files/host.ini') as f:
    hostname = f.read().split('\n')
    hostname.pop()
    hostname = hostname[0].replace('[', '').replace(']', '')

with open('config_files/todo.yml', 'r') as f:
    s = f.read()

load_file = yaml.load(s, Loader=yaml.SafeLoader)
todo_list = [
    {'name' : 'todo', 
     'hosts': hostname, 
     'tasks': [
        {
            'name' : 'install packages-' + i,
            'ansible.builtin.apt' : {'pkg' : i}
        } for i in load_file['server']['install_packages']
     ]+[
         {
            'name' : 'install packages-redis', 
            'ansible.builtin.pip' : {'name':'redis'}
         }
     ]+[
        {
            'name' : 'copy packages-' + i,
            'ansible.builtin.copy' :
            {
                'src': i,
                'dest': 'copy_'+i
            }
        } for i in load_file['server']['exploit_files']
     ]+[
        {
            'name': 'run exploit files-exploit.py',
            'ansible.builtin.command' : 'python3 exploit.py'
        },
        {
            'name': 'run exploit files-consumer.py',
            'ansible.builtin.command' : 'python3 consumer.py -e '+ ','.join(i for i in load_file['bad_guys'])
        }
     ]
    }]
r = yaml.safe_dump(todo_list, default_flow_style=False, sort_keys=False)

with open('deploy.yml', 'w+') as f:
    f.write(r)

test = subprocess.run(['sudo','ansible-playbook', '-i', 'config_files/host.ini', 'deploy.yml', '-c', 'local'])
