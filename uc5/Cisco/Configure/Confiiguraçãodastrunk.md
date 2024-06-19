Autor: Thiago Sanches
Instagram: https://www.instagram.com/espetacular_sanches
LinkedIn Thiago Sanches: https://www.linkedin.com/in/thiagosanches07/
Github: https://github.com/sanchessky
Data de criação: 19/06/2024
Data de atualização: 19/06/2024








## Primeira Etapa (Configuração nas portas dos switch 2960)
    
    
    sw-03>enable 
    sw-03#
    configure terminal# 
    sw-03 config#    interface range 0/1
        0/23 - 24
        sw-03(config-if-range)#
            switchport mode trunk
            switchport nonegotiate
            do write
    end
    write

<br>


Observação: verificação as alterações do switch. (listar apenas a FastEthernet e GIgabitEthernet) <br>


     show running-config
    
    interface FastEthernet0/23
     switchport mode trunk
     switchport nonegotiate
    !
    interface FastEthernet0/24
     switchport mode trunk
     switchport nonegotiate
    !
    interface GigabitEthernet0/1
     switchport mode trunk
     switchport nonegotiate
    !
    interface GigabitEthernet0/2
     switchport mode trunk
     switchport nonegotiate


     
## Segunda Etapa (Configuração nas portas dos switch multiplayer)



    (config)#interface range GigabitEthernet 1/0/1 - 4
    (config-if-range)#description interface de trunk
    (config-if-range)#switchport mode trunk
    (config-if-range)#switchport nonegotiate
    end
    write

    show running-config


 Etapa 


sw-04#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
sw-04(config)#interface range Fast
sw-04(config)#interface range FastEthernet 0/1
sw-04(config-if-range)#description vlan 40 estoque
sw-04(config-if-range)#switch mode access
sw-04(config-if-range)#switchport access vlan 40
switchport nonegotiate
