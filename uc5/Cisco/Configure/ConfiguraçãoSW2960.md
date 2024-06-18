Autor: Thiago Sanches<br>
Instagram: https://www.instagram.com/espetacular_sanches<br>
LinkedIn Thiago Sanches: https://www.linkedin.com/in/thiagosanches07/<br>
Github: https://github.com/sanchessky<br>
Data de criação: 17/06/2024<br>
Data de atualização: 17/06/2024<br>

## Configuração do Switch 2960

1) Modo Privilegiado

          Switch> enable
	     Switch#


2) *Configurando Data e Hora*


        clock set 15:15:00 22 May 2024


3) *Configuração Global*

          configure terminal#
          Switch# configure terminal   
          Switch(configure terminal)#



 4) Configuração Hostname (continuar no modo de configuração global)

          hostname sw-01
            
Habilitando o serviço de criptografia de senha
   
     service password-encryption
     service timestamps log datetime msec
        
Desativando o serviço de resolução de nomes de domínio
   
    no ip domain-lookup
        
Configuração do banner da mensagem do dia no Cisco IOS

     banner motd #AVISO: acesso autorizado somente a funcionarios

Habilitando o uso de senha
     
     enable secret 123@senac

 
Criação dos usuários locais
            
     username senac secret 123@senac
     username thiago password 123@senac 
     username admin privilege 15 secret 123@senac
Configuração da Linha Console
    
    line console 0

Forçando fazer login local;
                    
     login local
Habilitando a senha de acesso;
                
     password 123@senac
                
Habilitando o sincronismo das mensagens de Logs;
                
     logging synchronous
Habilitando o tempo de inatividade de uso;

     exec-timeout 5 30
Sair 
               
     end

Salvando da RAM para NVRAM

     copy running-config startup-config
