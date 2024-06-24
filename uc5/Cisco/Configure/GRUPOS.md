Autor: Thiago Sanches
Instagram: https://www.instagram.com/espetacular_sanches
LinkedIn Thiago Sanches: https://www.linkedin.com/in/thiagosanches07/
Github: https://github.com/sanchessky
Data de criação: 24/06/2024
Data de atualização: 24/06/2024




## CRIANDO-GRUPOS-NOS-SWITCH

Observação:Refazer nos outros switch(ficar atento com as redes)

    enable
    configure terminal
        interface range GigabitEthernet 1/0/1 - 2 
            channel-group 1 mode active
            exit
        interface port-channel 1
            description LACP Switch 3650 para 2960
            switchport mode trunk
            switchport trunk allowed vlan all

<br>

    configure terminal
            interface range gigabitEthernet 0/1 - 2
            channel-group 1 mode passive
            exit

        interface port-channel 1
            description LACP Switch 2960 para 3560
            switchport mode trunk
            switchport trunk allowed vlan all
 
 
