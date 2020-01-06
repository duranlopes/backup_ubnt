import paramiko
import os
from scp import SCPClient
from config import ips, user, password, localfile

path = os.getcwd()

def bar():
    if os.name == 'nt':
        bar = '\\'
        return bar
    else:
        bar = '/'
        return bar

backup_folder = path + bar() +'backup'

def backup_radio(ip_radio, directory):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_radio, username=user, password=password)
        try:
            print ('Efetuando backup do radio: '+ip_radio)
            if not os.path.exists(backup_folder):
                os.mkdir(backup_folder)
            scp = SCPClient(ssh.get_transport())
            scp.get(localfile, directory)
        except:
            print('Falha ao fazer download do arquivo em %s' % ip_radio)
        ssh.close()

    except paramiko.AuthenticationException:
        print("Falha na autenticacao em %s" %ip_radio)

    except:
        print("Nao foi possivel conectar em %s" % ip_radio)

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
    except WindowsError:
        os.remove(new_name)
        os.rename(old_name, new_name)

def main():
    for key, value in ips.items():
        newname = backup_folder + bar()+ key +'.cfg'
        backup_file = backup_folder + bar() + 'system.cfg'
        backup_radio(value, backup_folder)
        if os.path.exists(backup_file):
            rename_file(backup_file, newname)
        print('Backup efetuado com sucesso')

if __name__ == '__main__':
    main()