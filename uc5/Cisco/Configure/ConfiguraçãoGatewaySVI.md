Autor: Thiago Sanches<br>
Instagram: https://www.instagram.com/espetacular_sanches<br>
LinkedIn Thiago Sanches: https://www.linkedin.com/in/thiagosanches07/<br>
Github: https://github.com/sanchessky<br>
Data de criação: 17/06/2024<br>
Data de atualização: 17/06/2024<br>

## Configuração do Gateway SVI

```python
!Configuração GatewaySVI

enable
    #configure terminal
    
         !Configuração do Gateway padrão IPv4 no Switch
         ip default-gateway 192.168.1.254

         !Configuração da Interface Virtual do Switch SVI
         interface vlan 1
            !Configuração da Descrição da Interface Virtual VLAN-1
            description Interface SVI do SW-01
            !Configuração do Endereçamento IPv4 da Interface Virtual VLAN-1
            ip address 192.168.1.250 255.255.255.0
            !Inicializando a Interface Virtual da VLAN-1
            no shutdown

            end
write
show running-config | section include interface Vlan1
show ip interface brief
```
