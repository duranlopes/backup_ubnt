# Backup radios UBNT 
Script criado para fazer backup dos equipamentos UBNT.

# Configurações

Para iniciar o script é necessário editar o arquivo config.py e atualizar as informaçoes necessárias.

ips = {'station': '192.168.15.33','ap': '192.168.15.32'}

user = 'admin'		# Usuário do Rádio
password = 'yourpassword'			# Senha do Rádio
localfile = '/tmp/system.cfg' ### arquivo padrao dos radios ubnt
