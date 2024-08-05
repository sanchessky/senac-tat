
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
