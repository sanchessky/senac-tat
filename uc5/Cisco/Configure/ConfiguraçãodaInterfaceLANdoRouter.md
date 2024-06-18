Autor: Thiago Sanches<br>
Instagram: https://www.instagram.com/espetacular_sanches<br>
LinkedIn Thiago Sanches: https://www.linkedin.com/in/thiagosanches07/<br>
Github: https://github.com/sanchessky<br>
Data de criação: 17/06/2024<br>
Data de atualização: 17/06/2024<br>


```python
!ConfiguraçãodaInterfaceLANdoRouter
Enable
        !Acessando a Interface GigabitEthernet
            interface gigabitEthernet 0/0

            !Configuração da Descrição da Interface
                 description Interface de Gateway da Rede LAN
            !Configuração do Endereçamento IPv4
                ip address 192.168.1.254 255.255.255.0
            !inicializando a Interface
                no shutdown

             end
    copy running-config startup-config ou write

    !Visualizando as Configurações
    show running-config
    !Fazendo um Filtro
    show running-config | section include interface gigabitEthernet 0/0
    !Visualizando informações detalhadas
    show interface gigabitEthernet 0/0
    !Visualizando as configurações
    show ip interface brief
    !Visualizando informações
    show ip route
```
