
print('Bienvenido a "Golpe de Estado". ')
print("Hola soldado... Saldras en el primer vuelo....")
print("Primero tendras que apuntar tu nombre y tu apellido, ¿sabes usar un arma verdad?.")
nombre = input("Introduce tu nombre → ")
apellido = input("Introduce tu apellido → ")
print(f"Buenas {nombre} - dice el coronel Girafales - Despierta soldado!, estamos a punto de llegar, ¿emocionado? eh?")
print("Bueno- la mision es esta, tendremos que entrar a la Capital de Guatemala para dar ese golpe de estado a Giamatei antes que sea demasiado tarde.")
respuesta = input("¿Qué opinas, has estado tan cerca de una batalla alguna vez? (Si/No) ")
respuesta.capitalize()
if(respuesta == "No"):
  print("Bueno, nunca es tarde para aprender algo nuevo.")
elif(respuesta == "Si"):
  print(f"Entonces vendras conmigo {nombre} a lo más intenso de la batalla.")

print("Estas en el punto de la batalla en el que no sabes si vas a morir a si vas a vivir. Cabo quico - Hey! el coronel dice que avances o te mueres.")
input("¿Continuar? ")
print("Por avanzar casi te mata una granada jajajajaj, pero estas bien")
print("Logras avanzar y logras darle 200 a un soldado.")
print(f"{nombre} avanza y entra a el fuerte, yo los distraigo - dijo el coronel Girafales.")
print("Entras y vez que Giamatei esta justo enfrente a ti, pero se acercan soldados y te empiezan a disparar.")
input("¿Continuar? ")
print("Por poco y te matan pero gracias a que jugaste Fortnite toda la vida, le sabias un poco al aim asist.")
print("Subes las gradas, tiras una granada por si acaso. Al subir te das cuenta que mataste a Arevalo, porque lo tenian de rehen.")
print("No sabes si continuar o no (pero si dices que no lo más probable es que te maten)")
input("¿Continuar? ")
print("------------------------------------------------------------------------------------")
print("Continuas porque tampoco querias que quedara Arevalo, tienes a Giamatei a un disparo (esta a 5 de vida) pero no sabes si al entrar al cuarto pueda haber una bomba.")
print(f"AVISO: Tus decisiones a partir de ahora decidirán el destino de {nombre}.")

FinalMalo1 = f"Al pasar giamatei se explota a si mismo y a toda Guatemala (que malo el giamate). "
Continuacion1 = "Tuviste suerte de decir que no al pasar al cuarto y matarlo de una sola vez."

respuesta1 = input("¿Entras o eliminarlo? (Elegir E/L) ")
respuesta1.upper()
if(respuesta1 == "E"):
  print(FinalMalo1)
  print(f"Por desgracia, has fallado, {nombre} ha muerto.")
  import  sys
  sys.exit(0)
elif(respuesta1 == "L"):
  print(Continuacion1)
print("Salvaste a Guate jijijija")