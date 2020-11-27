import admin as adm

def main():
    print("\n1. Para logar como administrador\n2. Para cadastrar\n3. Ver catálago\n0. Para sair")
    op = int(input('Digite sua escolha: '))
    if op==1:
       adm.admin().login()
    elif op==2:
        adm.admin().cadastro()
    elif op==3:
        adm.aeronaves().listarAeronave()
    else:
        pass
if __name__ == '__main__':
    main()