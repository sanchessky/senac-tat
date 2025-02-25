import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
    QHBoxLayout, QVBoxLayout, QListWidget
)
from PyQt5.QtGui import QPixmap

class Janela(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.setGeometry(10, 30, 1000, 700)
        self.setWindowTitle("Janela Gestão")

        # Barra azul no topo
        self.label_azul = QLabel("Restante:")
        self.label_azul.setStyleSheet("QLabel{background-color:blue}")
        self.label_azul.setFixedHeight(50)

        # Seção branca principal
        self.label_branca = QLabel()
        self.label_branca.setStyleSheet("QLabel{background-color:white}")

        # Layout horizontal interno na seção branca
        self.h_lay_dentro_branca = QHBoxLayout()


        # Layout principal (horizontal)
        layout_principal = QHBoxLayout()

        # Coluna esquerda
        layout_esquerda = QVBoxLayout()
        layout_principal.addLayout(layout_esquerda)

        lista_pagamento = QListWidget()
        formas_pagamento = [
            "DINHEIRO", "PRAZO (NOTA)", "CHEQUE-PRE", "CRÉDITO", "DÉBITO",
            "TEF ALIMENTAÇÃO", "WEB CARD ALIMENTAÇÃO", "VENDA ATACADO A VISTA",
            "TEF-CRÉDITO", "TEF-DÉBITO", "ALIMENTAÇÃO"
        ]
        lista_pagamento.addItems(formas_pagamento)
        layout_esquerda.addWidget(lista_pagamento)

        # Coluna direita
        layout_direita = QVBoxLayout()
        layout_principal.addLayout(layout_direita)

        # Seção de totais e operações na coluna direita
        restante_label = QLabel("Restante:")
        restante_label.setStyleSheet("font-size: 16pt; font-weight: bold; color: black;")
        restante_valor = QLabel("0,00")
        restante_valor.setStyleSheet("font-size: 24pt; font-weight: bold; color: blue;")

        layout_direita.addWidget(restante_label)
        layout_direita.addWidget(restante_valor)

        desconto_label = QLabel("Desconto: 0,00")
        desconto_label.setStyleSheet("font-size: 14pt;")
        acrescimo_label = QLabel("Acréscimo: 0,00")
        acrescimo_label.setStyleSheet("font-size: 14pt;")

        layout_direita.addWidget(desconto_label)
        layout_direita.addWidget(acrescimo_label)

        subtotal_label = QLabel("Sub-Total: 10,00")
        subtotal_label.setStyleSheet("font-size: 16pt; font-weight: bold; color: black;")
        layout_direita.addWidget(subtotal_label)

        mensagem = QLabel("Aguardando formas de pagamento")
        mensagem.setStyleSheet("font-style: italic; color: gray;")
        layout_direita.addWidget(mensagem)

        # Botões de ação
        layout_botoes = QHBoxLayout()
        cancelar_button = QPushButton("[F7] - Cancela forma de pagamento")
        finalizar_button = QPushButton("[F5] - Finalizar")
        finalizar_button.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        layout_botoes.addWidget(cancelar_button)
        layout_botoes.addWidget(finalizar_button)
        layout_direita.addLayout(layout_botoes)

        # Layout global (vertical)
        self.v_lay_global = QVBoxLayout()
        self.v_lay_global.addWidget(self.label_azul)  # Barra azul no topo
        self.v_lay_global.addWidget(self.label_branca)  # Seção branca com as colunas
        self.v_lay_global.addLayout(layout_principal)  # Layout com as colunas esquerda e direita

        # Define o layout principal da janela
        self.setLayout(self.v_lay_global)

# Criação e execução da aplicação
app = QApplication(sys.argv)
tela = Janela()
tela.show()
app.exec_()
