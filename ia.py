# !/usr/bin/env python3.4.2
# -*- coding: utf-8 -*-

import os
import mysql.connector

desde_archivo = 'historial.txt'
rutaserver = 'server.txt'
con = mysql.connector.connect(user="root",password="hola",host="127.0.0.1",database="registro")

os.system("espeak -s130 -k20 -ves+f5 'Ingrese nombre'")
noma =  raw_input("Ingrese nombre: ")
os.system("espeak -s130 -k20 -ves+f5 'Ingrese edad'")
eda =  raw_input("Ingrese edad: ")
os.system("espeak -s130 -k20 -ves+f5 'Ingrese peso'")
peso =  raw_input("Ingrese peso: ")
os.system("espeak -s130 -k20 -ves+f5 'Ingrese mes de cumpleaños'")
me =  raw_input("Ingrese mes en el que cumples años: ")
os.system("espeak -s130 -k20 -ves+f5 'Ingrese dia de cumpleaños'")
dipo =  raw_input("Ingrese dia en el que cumples años: ")

cursor=con.cursor()
cursor.execute("INSERT INTO datos (Nombre,Edad,Peso,Mes,Dia) VALUES " "('"+noma+"','"+eda+"','"+peso+"','"+me+"','"+dipo+"')")
con.commit()
con.close()

lector = open('nombre.txt','a')
lector.close()
abrir = open('nombre.txt','w')
abrir.write(noma)
abrir.close()

lector = open('anos.txt','a')
lector.close()
abrir = open('anos.txt','w')
abrir.write(eda)
abrir.close()

lector = open('peso.txt','a')
lector.close()
abrir = open('peso.txt','w')
abrir.write(peso)
abrir.close()

lector = open('mes.txt','a')
lector.close()
abrir = open('mes.txt','w')
abrir.write(me)
abrir.close()

lector = open('dia.txt','a')
lector.close()
abrir = open('dia.txt','w')
abrir.write(dipo)
abrir.close()


def resumido(respuesta,result):
    os.system("espeak -s130 -k20 -ves+f5 '" + result +"'")
    lector = open(desde_archivo,'a')
    lector.write(respuesta + '\n')
    lector.close()
    print("\n")


        
while True:
        
    respuesta = raw_input(">>> ")
    respuesta = respuesta.lower()
    

    if respuesta == "si":
        resumido("si","Pues dimelo")
        
      
    elif respuesta == "no":
        resumido("no","De acuerdo")

    elif respuesta == "probar conexion":
        os.system("sudo python notifi.py")
        os.system("espeak -s130 -k20 -ves+f5 'Mensaje enviado'")

              
    elif respuesta == "que tal?":
        resumido("que tal?","Estupendamente")


    elif respuesta == "como estas?":
        resumido("como estas?","Estupendamente")
  

    elif respuesta == "cuando sera el fin del mundo?":
        resumido("cuando sera el fin del mundo?","Cuando todos mueran")

 
    elif respuesta == "quien es dios?":
        resumido("quien es dios?","Una figura a la que idolatran los humanos")


    elif respuesta == "Porque eres ateo?":
        resumido("porque eres ateo?","¿Porque eres creyente?")

    elif respuesta == "hola mamu":
        resumido("hola mamu","hola papu")


    elif respuesta == "no puedes decir otra cosa?":
        resumido("no puedes decir otra cosa?","yo digo lo que quiera")


    elif respuesta == "hola":
        resumido("hola","Hola")
    

    elif respuesta == "te gusta el pene?":
        resumido("te gusta el pene?","Por supuesto")


    elif respuesta == "actualiza el sistema":
        resumido("actualiza el sistema","Actualizando el sistema...")
        os.system("apt-get update && apt-get upgrade && apt-get dist-upgrade") 
    
    
    elif "como te llamas?" in respuesta:
        resumido("como te llamas?","Me llamo Friman")
    

    elif respuesta == "quien es tu creador?":
        resumido("quien es tu creador?","Dios mi padre")

    elif respuesta == "xd":
        resumido("quien es tu creador?","equisde equisde")


    elif respuesta == "cual es el significado de la vida?":
        resumido("cual es el significado de la vida?","lo siento no se puede revelar hasta el año 2022")


    elif respuesta == "aprobare el examen?":
        resumido("aprobare el examen?","solo si estudias")


    elif respuesta == "eres inteligente?":
        resumido("eres inteligente?","No, solo estoy programado para servirte, inteligente mi programador")


    elif respuesta == "puedes verme?":
        resumido("puedes verme?","No")


    elif respuesta == "me amas?":
        resumido("me amas?","si, como amigo")


    elif respuesta == "puedes verme?":
        resumido("puedes verme?","No")


    elif respuesta == "concidencia?":
        resumido("concidencia?","No lo creo")


    elif respuesta == "tamales?":
        resumido("tamales?","dos porfabor")


    elif respuesta == "eres tonto?":
        resumido("eres tonto?","efectivamente")

    elif respuesta == "me duele la cabeza":
        resumido("Me duele la cabeza?","usted ha estado bajo estrés")
        os.system("espeak -s130 -k20 -ves+f5 'o ha tomado bebidas energéticas?'")
        os.system("espeak -s130 -k20 -ves+f5 'sí es asi, deberías descansar un rato'")
        os.system("espeak -s130 -k20 -ves+f5 'o sí no, toma paracetamol o algún antigripal'")
        os.system("espeak -s130 -k20 -ves+f5 'sí los síntomas persisten consulte a su médico'")
        
            
    elif respuesta == "me duele el estomago":
        resumido("Me duele el estomago?","¿y?")
        

    elif respuesta == "historial":
        ("Mostrando historial... \n")
        os.system("espeak -ves+f4 'Mostrando historial'")
        lector = open(desde_archivo,'a')
        lector.write('historial \n')
        historial = open(desde_archivo,'r')
        lector.close()
        print(historial.read())
        historial.close()
        print("\n")
        

    elif respuesta == "saldre con la chica que me gusta?":
        resumido("saldre con la chica que me gusta?","Eso solo depende de ti")


    elif respuesta == "hay algo en la tele?":
        resumido("hay algo en la tele?","siempre hay algo")

    
    elif respuesta == "soy guapo?":
        resumido("soy guapo?","si")
        

    elif respuesta == "cual es tu edad?":
        resumido("cual es tu edad?","Acabo de nacer, ademas soy una maquina")
    
    elif respuesta == "soy feo?":
        resumido("soy feo?","Nose, weno si se peo no te wa decir")


    elif respuesta == "?":
        resumido("?","que me preguntas")


    elif respuesta == "te casarias conmigo?":
        resumido("te casarias conmigo?","La ley no lo permite")

    
    elif respuesta == "me amas?":
        resumido("me amas?","si, como amigo")
    

    elif respuesta == "quien eres?":
        resumido("quien eres?","soy friman")
    
    
    elif respuesta == "si le gusta el regueton?":
        resumido("si le gusta el regueton?","dale")

    
    elif respuesta == "tu madre":
        resumido("tu madre?","!la tuya!")

    elif respuesta == "tomar foto":
        resumido("tomar foto","tomando foto")
        an = raw_input("Nombre  del archivo: \n")
        os.system("raspistill -o "+str(an)+".jpg -f -q 100")
        
    elif respuesta == "cual es el mejor canal de internet?":
        resumido("cual es el mejor canal de internet?","Malas Amistades, obvio")


    elif respuesta == "Que puedo tomar para el dolor de cabeza?":
        resumido("Que puedo tomar para el dolor de cabeza?","Café, El café tiene la propiedad de reducir la inflamación, en este caso la de los vasos sanguíneos del cerebro, y esto ayudaría a aliviar el dolor de cabeza. Aunque si normalmente consumes café puede que no tenga tanto efecto")

    elif respuesta == "como me llamo?":
            resumido("como me llamo?","te llamas")
            os.system("espeak -s130 -k20 -ves+f5 -f nombre.txt")        


    elif "ingresar nombre" in respuesta:
        os.system("espeak -s130 -k20 -ves+f5 '¿desea ingresar un nombre?'")
        rnombre = raw_input("¿desea ingresar un nombre? (si no) \n")
        rnombre = rnombre.lower()
        lector = open(desde_archivo,'a')
        lector.write('ingresar nombre \n')
        lector.close()
        if rnombre == "si":
            os.system("espeak -s130 -k20 -ves+f5 'Dime tu nombre'")
            nombre = raw_input("Dime tu nombre \n")
            abrir = open('nombre.txt','w')
            abrir.write(nombre)
            abrir.close()
            print("Tu nombre es " + nombre)
            os.system("espeak -s130 -k20 -ves+f5 'Tu nombre es'")
            os.system("espeak -s130 -k20 -ves+f5 -f nombre.txt")
        elif rnombre == "no":
            print("Vale")
            os.system("espeak -v es 'vale'")
        print("\n") 
      

    elif "buscar en internet" in respuesta or "navegar en internet" in respuesta:
        resumido("internet","Abriendo navegador...")
        os.system("iceweasel")
        os.system("bg")

    
    elif respuesta == "ingresar cumpleaños":
        os.system("espeak -s130 -k20 -ves+f5 'Dime el dia en el que cumples años'")
        d = input("Dime el dia en el que cumples años: \n")
        print("\n")
        os.system("espeak -s130 -k20 -ves+f5 'Dime el mes en el que cumples años'")
        m =  raw_input("Dime el mes en el que cumples años: \n")
        print("\n")
        lector = open('dia.txt','a')
        lector.close()
        abrir = open('dia.txt','w')
        abrir.write(str(d))
        abrir.close()
        lector = open('mes.txt','a')
        lector.close()
        abrir = open('mes.txt','w')
        abrir.write(str(m))
        abrir.close()
        print("Tu fecha de cumpleaños es " + str(d) + " de " + str(m))
        os.system("espeak -s130 -k20 -ves+f5 'Tu cumpleaños es'")
        os.system("espeak -s130 -k20 -ves+f5 -f dia.txt")
        os.system("espeak -s130 -k20 -ves+f5 'de'")
        os.system("espeak -s130 -k20 -ves+f5 -f mes.txt")
        print("\n")    
    
    elif respuesta == "cuando es mi cumpleaños?":
        os.system("espeak -s130 -k20 -ves+f5 'Tu cumpleaños es'")
        os.system("espeak -s130 -k20 -ves+f5 -f dia.txt")
        os.system("espeak -s130 -k20 -ves+f5 'de'")
        os.system("espeak -s130 -k20 -ves+f5 -f mes.txt")
        print("\n")    

        
    elif respuesta == "cuantos años tengo?":
        os.system("espeak -s130 -k20 -ves+f5 'Tienes'")
        os.system("espeak -s130 -k20 -ves+f5 -f anos.txt")
        os.system("espeak -s130 -k20 -ves+f5 'años'")
        print("\n")  

    else:
        print("Aun no puedo responder a eso")
        os.system("espeak -s130 -k20 -ves+f5 'Aun no puedo responder a eso'")
