import hashlib

def comprobar_hash(hash_terminal):
    fichero = open("ejemplo.txt") 
    linea = fichero.readlines() #crea una lista de cada elemento del fichero
    for palabra in linea:
        hash_creado = hashlib.new('sha512')
        hash_creado.update(b"palabra")
        #hash_creado.hexdigest()
        if hash_creado == hash_terminal:
            return palabra

if __name__=="__main__":
    hash_terminal = "99adc231b045331e514a516b4b7680f588e3823213abe901738bc3ad67b2f6fcb3c64efb93d18002588d3ccc1a49efbae1ce20cb43df36b38651f11fa75678e8"
    print(comprobar_hash(hash_terminal))