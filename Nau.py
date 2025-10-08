def menu():
    print("w- Moure amunt")
    print("a- Moure equerre")
    print("d- Moure amunt")
    print("s- Moure avall")    
    print("0- Sortir")

def main():

    menu()
    
    posX = 0
    posY = 0

    sortir=False
    while not sortir:
        op = input('Entra una opció: ')
        if op=='d':
            posX=posX+1
            #sumar 1 a la variable posX
        elif op=='a':
            posX=posX-1
            #restar 1 a la variable posX
        elif op=='w':
            posY=posY+1
            #sumar 1 a la variable posY
        elif op=='s':
            posY=posY-1
            #restar 1 a la variable posY
        elif op=='0':
            sortir=True
            print("Has sortit de la nau")
        
        print(f"La nau està a la posició ({posX},{posY})")
        
if __name__ == "__main__":
    main()
