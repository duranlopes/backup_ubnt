import paramiko
import os
from scp import SCPClient
from config import ips, user, password, localfile

path = os.getcwd()
backup_folder = path +'\\backup'

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

def new_name():
    if os.name == 'nt':
        newname = backup_folder +'\\'+ key+'.cfg'
    else:
        newname = backup_folder +'/'+ key+'.cfg'


def main():
    for key, value in ips.items():
        if os.name == 'nt':
            newname = backup_folder +'\\'+ key+'.cfg'
            backup_file = backup_folder + '\system.cfg'
        else:
            newname = backup_folder +'/'+ key+'.cfg'
            backup_file = backup_folder + '/system.cfg'
        backup_radio(value, backup_folder)
        if os.path.exists(backup_file):
            #print (newname)
            rename_file(backup_file, newname)
        print('Backup efetuado com sucesso')


if __name__ == '__main__':
    main()