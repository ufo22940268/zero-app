from fabric.api import *

# the user to use for the remote commands
env.user = 'root'
# the servers where the commands are executed
env.hosts = ['192.241.196.189']

def deploy():
    local('tar -cvf /tmp/k.tar ../zero-app')
    put('/tmp/k.tar', '/tmp/k.tar')
    run('tar -xvf /tmp/k.tar')
    with cd('zero-app'):
        with prefix('source /usr/bin/virtualenvwrapper.sh'):
            with prefix('workon zero-app'):
                run("bash kill.sh")
                run('gunicorn -w 4 -b 127.0.0.1:10000 run:app')

def kill_unicorn():
    with cd('zero-app'):
        run("bash kill.sh")
