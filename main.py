def logo():
    print("     TEA     ")

def menu():
    print("1 - Realizar estudio")
    print("2 - Consultar estudio")
    print("3 - ABM Paciente")
    print("4 - ABM Medico")
    print("5 - ABM Gestos")
    sel = input("Seleccione una opcion: ")
    if(sel==1):
        #realiza estudio
        print(sel)
    if(sel==2):
        #consulta estudio
        print(sel)
    if(sel==3):
        #ABM paciente
        print(sel)
    if(sel==4):
        #ABM Medico
        print("Selecciono 4")
    if(sel==5):
        #ABM Gesto
        print(sel)



def main():
    logo()
    menu()


main()

