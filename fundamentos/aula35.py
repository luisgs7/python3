trabalho_terca = True
trabalho_quinta = False

"""
 - Confirmado os 2: TV 50' + sorvete
 - Confirmado apenas 1: TV 32' + Sorvete
 - Nenhum confirmado: Fica em casa
"""
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("Tv50={}, Tv32={}, Sorvete={}, Saudável={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))
