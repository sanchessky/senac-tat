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


     
## Segunda Etapa (Configuração nas portas dos switch central )
