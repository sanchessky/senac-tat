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
