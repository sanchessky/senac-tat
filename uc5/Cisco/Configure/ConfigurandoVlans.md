
Autor: Thiago Sanches<br>
Instagram: https://www.instagram.com/espetacular_sanches<br>
LinkedIn Thiago Sanches: https://www.linkedin.com/in/thiagosanches07/<br>
Github: https://github.com/sanchessky<br>
Data de criação: 17/06/2024<br>
Data de atualização: 20/06/2024<br>

## Configuração da Vlan

PRIMEIRA ETAPA: NOMEANDO AS VLANS
Acessando o modo Exec Privilegiado<br>
*enable*

    sw-05#show vlan brief

    VLAN Name                             Status    Ports
    ---- -------------------------------- --------- -------------------------------
    1    default                          active    Gig1/0/1, Gig1/0/2, Gig1/0/3, Gig1/0/4
                                                Gig1/0/5, Gig1/0/6, Gig1/0/7, Gig1/0/8
                                                Gig1/0/9, Gig1/0/10, Gig1/0/11, Gig1/0/12
                                                Gig1/0/13, Gig1/0/14, Gig1/0/15, Gig1/0/16
                                                Gig1/0/17, Gig1/0/18, Gig1/0/19, Gig1/0/20
                                                Gig1/0/21, Gig1/0/22, Gig1/0/23, Gig1/0/24
                                                Gig1/1/1, Gig1/1/2, Gig1/1/3, Gig1/1/4
    1002 fddi-default                     active    
    1003 token-ring-default               active    
    1004 fddinet-default                  active    
    1005 trnet-default                    active    


## Acessando o modo de Configuração Global de Comandos<br>
*configure terminal*

            sw-05(config)#
            sw-05(config)#vlan 10
            sw-05(config-vlan)#name servers
            sw-05(config-vlan)#exit
            sw-05(config)#end
            sw-05#show vlan brief
            sw-05# write
            

<br>

    sw-05#show vlan brief

    VLAN Name                             Status    Ports
    ---- -------------------------------- --------- -------------------------------
    1    default                          active    Gig1/0/1, Gig1/0/2, Gig1/0/3, Gig1/0/4
                                                Gig1/0/5, Gig1/0/6, Gig1/0/7, Gig1/0/8
                                                Gig1/0/9, Gig1/0/10, Gig1/0/11, Gig1/0/12
                                                Gig1/0/13, Gig1/0/14, Gig1/0/15, Gig1/0/16
                                                Gig1/0/17, Gig1/0/18, Gig1/0/19, Gig1/0/20
                                                Gig1/0/21, Gig1/0/22, Gig1/0/23, Gig1/0/24
                                                Gig1/1/1, Gig1/1/2, Gig1/1/3, Gig1/1/4
    10   switch                           active    
    20   server                           active    
    30   wireless                         active    
    40   estoque                          active    
    50   financeiro                       active    
    60   gerencia                         active    
    1002 fddi-default                     active    
    1003 token-ring-default               active    
    1004 fddinet-default                  active    
    1005 trnet-default                    active 
            





## Segunda Etapa: Configurando a Interface de Gerenciamento SVI do Switch Multilayer 3650

    sw-05(config)#interface vlan 10
    sw-05(config-if)#
    sw-05(config-if)#description interface SVI Switch 3650
    sw-05(config-if)#ip address 192.168.10.252 255.255.255.0
    sw-05(config-if)#no shutdown
    sw-05(config-if)#exit


## Terceira Etapa: Verificando as Configurações dos Switches.

    !Visualizando as Configurações do Running-Config (RAM)
    show running-config

    !Visualizando as configurações da memória RAM
    show running-config | section interface

    !Verificando as informações das Interfaces de Trunk
    show interface status
    show interface trunk
    show interfaces gigabitEthernet 0/1 status
    show interfaces gigabitEthernet 0/1 switchport
