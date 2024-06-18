Autor: Thiago Sanches<br>
Instagram: https://www.instagram.com/espetacular_sanches<br>
LinkedIn Thiago Sanches: https://www.linkedin.com/in/thiagosanches07/<br>
Github: https://github.com/sanchessky<br>
Data de criação: 17/06/2024<br>
Data de atualização: 17/06/2024<br>

## Configuração da VTY

```python
!configuração da VTY
enable
    #configure terminal

    !Acessando as Linhas
    line vty 0 4   

    Habilitando a senha
    login local

    password 123@senac
    
    Habilitando o sincronismo das mensagens
    logging synchronous

    !Habilitando o tempo de inatividade
    exec-timeout 5 30
    !Configuração do tipo de Protocolo de Transporte
    transport input ssh

    !sair
    end
!salvar as configurações
copy running-config startup-config
ou
write
!Fazendo um Filtro na Visualização do Running-Config
show running-config | section include line vty
```
