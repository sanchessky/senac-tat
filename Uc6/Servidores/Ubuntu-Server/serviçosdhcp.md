



 Configuração do serviço DHCP (Servidor de IPs)

apt update
apt install isc-dhcp-server

ip link show (verificar as interfaces de rede)

1) Configurar a interface LAN para o DHCP
cd /etc/default
# fazer uma cópia do arquivo de configuração
cp isc-dhcp-server isc-dhcp-server.old

vim isc-dhcp-server
INTERFACES="enp0s8" (verificar antes a interface)




2) Configurar o script
cd /etc
# fazer uma cópia do arquivo de configuração
cp dhcpd.conf dhcpd.conf.bkp

vim dhcpd.conf
