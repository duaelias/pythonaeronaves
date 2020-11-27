import pymysql.cursors
import main

class admin():
    def __int__(self):
        pass

    def conexao(self):
        try:
            self.banco = pymysql.connect(
                host='localhost',
                user='root',
                password='poder6645',
                db='projetoaeronave',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor

            )
            #print('Conectado')
        except:
            print('erro ao conectar com o bd')

    def login(self):
        global autenticado
        self.conexao()
        email = input('Email: ')
        senha = input('Senha: ')
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM admin')
                resultados = cursos.fetchall()
        except:
            print('erro ao fazer a consulta com o bd admin')
        for i in resultados:
            if email==i['email'] and senha==i['senha']:
                autenticado == True
                break
            else:
                autenticado = False
                pass
        if autenticado:
            self.menuAdmin()
        else:
            print("Dados errados ! tente novamente")
            self.login()



    def VerificaEmail(self, email):
        self.conexao()
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM admin')
                resultados = cursos.fetchall()
        except:
            print('erro ao fazer a consulta com o bd admin')
        for i in resultados:
            if email==i['email']:
                return 1
            else:
                pass
        return 0

    def cadastro(self):
        cod = '123'
        codigo = input('Digite o código verificador: ')
        if codigo==cod:
            nome = input('Nome: ')
            email = input('Email: ')
            senha = input('Senha: ')
            dados = [nome, email, senha, 1]
            self.conexao()
            n = self.VerificaEmail(email)
            if n==1:
                print('Email existe - Tente realizar o login')
                self.login()
            else:
                with self.banco.cursor() as cursos:
                    sql = "INSERT INTO admin (nome, email, senha, status) VALUES (%s, %s, %s, %s)"
                    cursos.execute(sql, dados)
                    self.banco.commit()
                    print("Cadastrado")
                    self.login()


    def menuAdmin(self):
        print("\n1. Cadastrar mova aeronave\n2. Alterar dados aeronaves\n3. Deletar aeronave\n4. Listar Aeronave\n0. Sair")
        op = int(input('Digite sua escolha: '))
        if op==0:
            return 0
        elif op ==1:
            modelo = input("Modelo: ")
            ano = int(input("Ano"))
            cor = input("Cor: ")
            tipo = int(input("Tipo(1.Avião|2.Helicóptero|3.Drone): "))
            dadosAeronaves = [modelo, ano, cor, tipo]
            aeronaves().cadastrarAeronave(dadosAeronaves)
        elif op==3:
            aeronaves().deletarAeronave()
        elif op==4:
            aeronaves().listarAeronaves()



class aeronaves(admin):
    def __init__(self, dadosAeronave):
        pass

    def cadastrarAeronave(self, dadosAeronave):
        self.conexao()
        with self.banco.cursor() as cursos:
            sql = "INSERT INTO aeronaves (modelo, ano, cor, tipo) VALUES (%s, %s, %s, %s)"
            cursos.execute(sql, dadosAeronave)
            self.banco.commit()
            print("Cadastrado")
            self.menuAdmin()

    def listarAeronave(self):
        self.conexao()
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM aeronaves')
                resultados = cursos.fetchall()
        except:
            print('erro ao fazer a consulta com o bd aeronaves')
        print("\n----------\n----Lista de aeronaves")
        for i in aeronaves:
            if i['tipo'] ==1:
                tipo = "Aviao"
            elif i['tipo']==2:
                tipo = "Helicoptero"
            else:
                tipo = "Drone"
            print("id: {} - Modelo: {} - Ano: {} - Cor: {}".format(i['idAeronave'], i['modelo'], i['modelo'], i['ano'], i['cor'], tipo))
        try:
            if autenticado:
                self.menuAdmin()
        except:
            main.main()

    def deletarAeronave(self):
        self.conexao()
        id = int(input('O id da aeronave qu quer deletar: '))
        with self.banco.cursor() as cursos:
            cursos.execute("DELETE FROM aeronaves WHERE idAeronave={}".format(id))
            self.banco.commit()
            print("\nDeletado")
            self.menuAdmin()

    def alterarAeronave(self):
        self.conexao()
        id = int(input('O id da aeronave que quer alterar: '))
        try:
            with self.banco.cursor() as cursos:
                cursos.execute('SELECT * FROM aeronaves WHERE idAeronave={}'.format(id))
                aeronaves = cursos.fetchall()
        except:
            print('erro ao fazer a consulta com o bd aeronaves')

        modelo = input("Modelo: ({}): ".format(aeronaves[0]['modelo']))
        ano = int (input("Ano: ({}): ".format(aeronaves[0]['ano'])))
        cor = input("Cor: ({}): ".format(aeronaves[0]['Cor']))
        tipo = int(input("Tipo: ({}): ".format(aeronaves[0]['tipo'])))
        with self.banco.cursor() as cursos:
            cursos.execute("UPDATE aeronaves SET modelo='{}', ano={}, cor='{}', tipo={} WHERE idAeronave={}".format(modelo, ano, cor, tipo, id))
            self.banco.commit()
            print("\nAlterado")
            self.menuAdmin()


