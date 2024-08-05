
#01Primeira etapa: Criação da Máquina Virtual no Oracle VirtualBOX

```
Oracle VirtualBOX Gerenciado (versão 7.x ou superior).

01) Ferramentas;	
<Novo>

02) Nome da Máquina Virtual e Sistema Operacional:
	Nome: UbuntuWebserver (altere conforme a sua necessidade)
	Pasta (F): #PATH_PADRÃO\UbuntuWebserver (altere conforme a sua necessidade)
	Imagem ISO: <não selecionar>
	Edição: (sem informação)
	Tipo: Linux
	Versão: Ubuntu (64-bit)
<Próximo>

03) Hardware:
	Memória Base: 4096MB (altere conforme a sua necessidade, mínimo 2048MB)
	Processadores: 02 CPU (altere conforme a sua necessidade, mínimo 2 CPU)
	Habilitar EFI (SOs especiais apenas): OFF (Desligado)
<Próximo>

04) Disco Rígido Virtual:
	Criar um novo disco rígido virtual agora: ON (Selecionar)
		Tamanho do Disco: 50,00GB (alterar conforme a sua necessidade, mínimo 50GB)
	Pré-alocar Tamanho Total (F): OFF (Desativado) 
<Próximo>

05) Sumário
<Finalizar>

```

#02Segunda Etapa: Configurações da Máquina Virtual UbuntuWebserver

```
Oracle VirtualBOX Gerenciado (versão 7.x ou superior).

01) Selecionar a Máquina Virtual: UbuntuWebserver
<Configurações>

02) Sistema
	Placa-Mãe
		Recurso Estendidos
			Relógio da máquina retorno hora UTC: OFF (Desabilitar)
	Processador
        Recursos Estendidos: Habilitar PAE/NX
                             Habilitar VT-x/AMD-v Aninhado 

03) Monitor
	Tela (S)
		Memória de Vídeo: 128MB
		Recursos Estendidos: Habilitar Aceleração 3D: ON (Habilitar)

04) Áudio
	Habilitar Áudio: OFF (Desabilitar)

05) Rede
	Adaptador 1 (LAN)
		Habilitar Placa de Rede: ON (Habilitar)
		Conectado a: Placa em modo Bridge
		Nome: Intel(R) Ethernet Connection (Placa de Rede On-Board)
		#OBSERVAÇÃO: VERIFIQUE QUAL PLACA DE REDE VOCÊ ESTÁ USANDO NO SEU EQUIPAMENTO
		#QUE ESTÁ CONECTADO NA SUA REDE LOCAL, PODE SER PLACA DE REDE CABEADA OU PLACA
		#SEM-FIO (RECOMENDO SEMPRE PLACA DE REDE CABEADA, MELHOR DESEMPENHO).
<OK>
```


#04_ Quarta Etapa: Iniciando a Instalação do Ubuntu Server 22.04.x LTS (localizar a ISO)
```bash
Oracle VirtualBOX Gerenciado (versão 7.x ou superior).

01. Selecionar a Máquina Virtual: UbuntuWebserver: 
<Iniciar>

02. VirtualBOX VM	
	DVD: <Outro>
	LOCALIZAR A IMAGEM DA ISO DO UBUNTU SERVER 22.04.x LTS
<Montar e Tentar Novo Boot>



#05 Quinta Etapa: Instalação e Configuração do Ubuntu Server 22.04.x LTS<br>
```bash
A) Instalação do Ubuntu Server: https://ubuntu.com/server/docs/installation

01) *Try or Install Ubuntu Server
<Enter>

02) Use UP, DOWN and ENTER keys to select your language
	English (recomendado utilizar sempre a opção em Inglês)
<Enter>

03) Keyboard configuration
	Layout: [English (US)] ou [Portuguese (Brazil)] (altere conforme a sua necessidade)
	Variant: [English (US)] ou [Portuguese (Brazil)] (altere conforme a sua necessidade)
<Done>

04) Choose type of install
	(X) Ubuntu Server (DEFAULT - Selecionado)
	( ) Ubuntu Server (minimized)
	Additional options
		[ ] Search for third-party drivers
<Done>

05) Network connections
	enp0s3 eth (o nome lógico da placa de rede muda de equipamento para equipamento)
	DHCPv4 172.16.1.XXX/24 (altere conforme a sua necessidade)
	#OBSERVAÇÃO IMPORTANTE: VERIFICAR O ENDEREÇO IPv4 QUE VOCÊ ESTÁ USANDO NA SUA REDE 
	#INTERNA PARA ADAPTAR NO SEU CENÁRIO.
<Done>

06) Configure proxy
	Proxy address: (Default)
<Done>

07) Configure Ubuntu archive mirror
	Mirror: http://br.archive.ubuntu.com/ubuntu
	#OBSERVAÇÃO IMPORTANTE: CASO QUEIRA TROCAR O MIRROR DO UBUNTU DO BRASIL PARA O
	#OFICIAL NO US, SUBSTITUA A URL DE: http://br.archive.ubuntu.com/ubuntu PARA A
	#URL: http://us.archive.ubuntu.com/ubuntu
<Done>

08) 

09) Guided storage configuration
	(X) Use an entire disk (Default)
		[VBOX_HARDISK local disk 50.000G]
		(X) Set up this disk as an LVM group (Default)
<Done>

10) Storage configuration
	USED DEVICES
		ubuntu-lv	new, to be formatted as ext4, mounted at /	24G <Enter>
			Edit <Enter>
				Name: ubuntu-lv
				Size (max 47.996G): 47.996G
				Format: ext4
				Mount: /
			<Save>
<Done>
	Confirm destructive action
<Continue>

11) Profile setup
	OBSERVAÇÃO: ALTERAR OS DADOS DO NOME DO SERVIDOR, USUÁRIO E SENHA PARA O SEU CENÁRIO.
	Your name: Seu Nome e Sobrenome <Tab>
	Your servers name: wsthiago <Tab>
	Pick a username: senac <Tab>
	Choose a passwords: 123@senac <Tab>
	Confirm your passwords: 123senac
<Done>

12) Upgrade to Ubuntu Pro
	(X) Skip Ubuntu Pro setup for now
<Continue>

13) SSH Setup
	Install OpenSSH server: ON (Habilitar) <Space>
	Import SSH identity: No (Default)
<Done>

14) Featured Server Snaps
<Done>

15) Install complete!
<Reboot Now>

16) Please remove the installation medium, then press ENTER:
<Enter>
```

#06_ Sexta Etapa: Acessando o Ubuntu Server pela primeira vez<br>
```bash
#AGUARDAR A INICIALIZAÇÃO TOTAL DO UBUNTU SERVER, NO FINAL SERÁ GERADO VÁRIAS CHAVES 
#DE AUTENTICAÇÃO DO SSH SERVER, PRESSIONE <ENTER> PARA APARECER A TELA DE LOGIN.

01) Tela de Login do Ubuntu Server
	wsvaamonde login: vaamonde <Enter> (altere para o seu usuário)
	Password: pti@2018 <Enter> (altere para o seu usuário)
```
