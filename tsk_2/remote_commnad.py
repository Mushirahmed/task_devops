import os
import sys
import paramiko
from pssh.pssh_client import ParallelSSHClient

def remote_command():
    """
    This function will print the output for remotely executed
    command output for given hostid
    
    """
    host_list = sys.argv[1].split(',')
    #we will be adding it automatically to the list of known hosts
    for each_host_id in host_list:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    #connecting and executing the command remotely
    client = ParallelSSHClient(host_list, user="ubuntu")
    cmd = input('Please enter the command to be executed on the remote host ')
    output = client.run_command(cmd, stop_on_errors=False)
    #printing the output of command
    for host_name, host_output in output.items():
        for line in host_output.stdout:
            print "Host [%s] - %s" % (host_name, line)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please enter comma separated HostIds for SSH."
    else:
        remote_command()