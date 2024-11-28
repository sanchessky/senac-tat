import sys
#importar os componentes para a construção da janela
from PyQt5.QtWidgets import QApplication,  QWidget, QLabel, QLineEdit, QPushButton, QTableWidget , QHBoxLayout, QVBoxLayout
#construção da classe janela com o nome de caixa
class Caixa(QWidget):
    #criação do MÉTODO __init__ que inicia a janela e exibe ela em tela
    def __init__(self):
        super().__init__()
        #definir a posição da tela e definir o tamanho
        self.setGeometry(0,30,1500,800)



        #titudo da tela
        self.setWindowTitle("Caixa da Loja")

        #criando as labels que será a esquerda e direita

        #coluna esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color: #ac58aa}")


        #coluna direira
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color: #7e2d7e}")

        #-------criação do conteudo da coluna esquerda--------------
        self.v_layout_esquerda = QVBoxLayout()

        #-------criação da lebel e linesEdits que ficarão na coluna esquerda, dentro do layout vertical da esquerda-------------

        #coluna esquerda
        #-----------Código do Produto Label e LineEdit-------------
        self.codigo_produto_label = QLabel('Código do Produto')
        self.codigo_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.codigo_produto_label)
        self.v_layout_esquerda.addWidget(self.codigo_produto_edit)
        #-----------Nome do Produto Label e LineEdit-------------
        self.nome_produto_lebal = QLabel('Nome do Produto:')
        self.nome_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.nome_produto_lebal)
        self.v_layout_esquerda.addWidget(self.nome_produto_edit)
        #-----------Descrição do Produto Label e LineEdit ---------------
        self.descricao_produto_label = QLabel('Descrição do Produto:')
        self.descricao_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.descricao_produto_label)
        self.v_layout_esquerda.addWidget(self.descricao_produto_edit)
        #-----------Quantidade do Produto Label e LineEdit ---------------
        self.quantidade_produto_label = QLabel('Quantidade do Produto:')
        self.quantidade_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.quantidade_produto_label)
        self.v_layout_esquerda.addWidget(self.quantidade_produto_edit)
        #-----------Preço Unitário do Produto Label e LineEdit -------------
        self.preco_unitario_produto_label = QLabel('Preço Unitário do Produto:')
        self.preco_unitario_produto_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.preco_unitario_produto_label)
        self.v_layout_esquerda.addWidget(self.preco_unitario_produto_edit)
        #-----------Sub Total Label e LineEdit --------------------------
        self.sub_total_label = QLabel('Sub Total:')
        self.sub_total_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.sub_total_label)
        self.v_layout_esquerda.addWidget(self.sub_total_edit)
        #adiconar o layout vertical da esquerda com todos os controles:label e lineEdit dentro da coluna da esquerda (label_coluna_esquerda)
        self.label_coluna_esquerda.setLayout(self.v_layout_esquerda)
        #fim coluna esquerda

       #-------criação do conteudo da coluna direita--------------
        self.v_layout_direita = QVBoxLayout()

        #criar uma tabela e adiconar na coluna da direita, esta tabela terá os nomes dos campos que estão ao esquerdo
        #coluna direita
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setRowCount(10)
        self.v_layout_direita.addWidget(self.tabela)
        

        #-----------Total a pagar Label e LineEdit --------------------------
        self.total_pagar_label = QLabel('Total a Pagar')
        self.total_pagar_edit = QLineEdit('0,00')
        self.v_layout_direita.addWidget(self.total_pagar_label)
        self.v_layout_direita.addWidget(self.total_pagar_edit)
        self.label_coluna_direita.setLayout(self.v_layout_direita)






       
        
        #layout Horizontal para adicionar as colunas
        self.h_layout = QHBoxLayout()



        #-------------- Componentes das colunas --------
        # layout da coluna esquerda
        self.h_layout.addWidget(self.label_coluna_esquerda)
        # layout da coluna direita
        self.h_layout.addWidget(self.label_coluna_direita)


        #adicionar o layout na tela
        self.setLayout(self.h_layout)

        
app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()
