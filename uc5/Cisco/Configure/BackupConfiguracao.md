```python
BackupConfiguracão
enable 
    !versão
    show version
	63488K bytes of flash-simulated non-volatile configuration memory.
		63488KB / 1000 = 64MB (64MB de Memória RAM)
	Configuration register is 0xF

    !Visualizando as informações da inicialização
    essas informações são importante para o processo de quebra de senha do Switch
     show boot
	BOOT path-list      : c2960-lanbasek9-mz.150-2.SE4.bin   (Binário do Cisco IOS)
	Config file         : flash:/config.text                 (Arquivo de Inicialização do Cisco IOS)
	Private Config file : flash:/private-config.text
    
    !informações do Flash Card
        show flash
        dir flash

        salvar
        write/ copy running-config startup-config
        
        !Salvando as configurações da memória NVRAM para a memória FLASH
        copy startup-config flash

        dir flash


        !Servidor TFTP
        ping 192.168.1.1

        !!Verificando o Arquivo Startup-Config da NVRAM
        dir nvram


!Verificando o Arquivo Startup-Config da NVRAM
sw-01# dir nvram:
	238  -rw-        1690          <no date>  startup-config

!Copiando o arquivo de configuração da NVRAM para o Servidor TFTP
sw-01# copy startup-config tftp:
	Address or name of remote host []? 192.168.1.1
	Destination filename [sw-01-confg]? thiago-sw-01-config

!Verificando o Binário do Cisco IOS do Switch
sw-01# dir flash:
	1  -rw-     4414921          <no date>  c2960-lanbase-mz.122-25.FX.bin

sw-01# copy flash: tftp:
	Source filename []? c2960-lanbase-mz.122-25.FX.bin
	Address or name of remote host []? thiago192.168.1.1
	Destination filename [c2960-lanbase-mz.122-25.FX.bin]?



etapa sw-01

!
version 15.0
service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
!
hostname sw-01
!
enable secret 5 $1$mERr$3O.pM7PScAETpkhlqaEiE.
!
!
!
ip ssh version 2
ip ssh authentication-retries 2
ip ssh time-out 60
no ip domain-lookup
ip domain-name senac.br
!
username admin secret 5 $1$mERr$3O.pM7PScAETpkhlqaEiE.
username senac secret 5 $1$mERr$3O.pM7PScAETpkhlqaEiE.
username thiago privilege 1 password 7 08701E1D290A00191308
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
interface FastEthernet0/1
!
interface FastEthernet0/2
!
interface FastEthernet0/3
!
interface FastEthernet0/4
!
interface FastEthernet0/5
!
interface FastEthernet0/6
!
interface FastEthernet0/7
!
interface FastEthernet0/8
!
interface FastEthernet0/9
!
interface FastEthernet0/10
!
interface FastEthernet0/11
!
interface FastEthernet0/12
!
interface FastEthernet0/13
!
interface FastEthernet0/14
!
interface FastEthernet0/15
!
interface FastEthernet0/16
!
interface FastEthernet0/17
!
interface FastEthernet0/18
!
interface FastEthernet0/19
!
interface FastEthernet0/20
!
interface FastEthernet0/21
!
interface FastEthernet0/22
!
interface FastEthernet0/23
!
interface FastEthernet0/24
!
interface GigabitEthernet0/1
!
interface GigabitEthernet0/2
!
interface Vlan1
 description interface svi do sw-01
 ip address 192.168.1.250 255.255.255.0
!
ip default-gateway 192.168.1.254
!
banner motd ^CAVISO: acesso autorizado somente a funcionarios^C
!
!
!
line con 0
 password 7 08701E1D290A00191308
 logging synchronous
 login local
 exec-timeout 5 30
!
line vty 0 4
 exec-timeout 5 30
 password 7 08701E1D290A00191308
 logging synchronous
 login local
 transport input ssh
line vty 5 15
 login
!
!
!
!
end















    etapa sw-02

    !
version 15.0
service timestamps log datetime msec
no service timestamps debug datetime msec
service password-encryption
!
hostname sw-02
!
enable secret 5 $1$mERr$3O.pM7PScAETpkhlqaEiE.
!
!
!
ip ssh version 2
ip ssh authentication-retries 2
ip ssh time-out 60
no ip domain-lookup
ip domain-name senac.br
!
username admin secret 5 $1$mERr$3O.pM7PScAETpkhlqaEiE.
username senac secret 5 $1$mERr$3O.pM7PScAETpkhlqaEiE.
username thiago privilege 1 password 7 08701E1D290A00191308
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
interface FastEthernet0/1
!
interface FastEthernet0/2
!
interface FastEthernet0/3
!
interface FastEthernet0/4
!
interface FastEthernet0/5
!
interface FastEthernet0/6
!
interface FastEthernet0/7
!
interface FastEthernet0/8
!
interface FastEthernet0/9
!
interface FastEthernet0/10
!
interface FastEthernet0/11
!
interface FastEthernet0/12
!
interface FastEthernet0/13
!
interface FastEthernet0/14
!
interface FastEthernet0/15
!
interface FastEthernet0/16
!
interface FastEthernet0/17
!
interface FastEthernet0/18
!
interface FastEthernet0/19
!
interface FastEthernet0/20
!
interface FastEthernet0/21
!
interface FastEthernet0/22
!
interface FastEthernet0/23
!
interface FastEthernet0/24
!
interface GigabitEthernet0/1
!
interface GigabitEthernet0/2
!
interface Vlan1
 description interface svi do sw-02
 ip address 192.168.1.251 255.255.255.0
!
ip default-gateway 192.168.1.254
!
banner motd ^CAVISO:   ___________    ____   ____ |  |__   ____   ______
 /  ___/\__  \  /    \_/ ___\|  |  \_/ __ \ /  ___/
 \___ \  / __ \|   |  \  \___|   Y  \  ___/ \___ \ 
/____  >(____  /___|  /\___  >___|  /\___  >____  >
     \/      \/     \/     \/     \/     \/     \/^C
!
!
!
line con 0
 password 7 08701E1D290A00191308
 logging synchronous
 login local
 exec-timeout 5 30
!
line vty 0 4
 exec-timeout 5 30
 password 7 08701E1D290A00191308
 logging synchronous
 login local
 transport input ssh
line vty 5 15
 login
!
!
!
!
end

```

