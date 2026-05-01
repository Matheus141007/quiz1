
def quiz ():
    print  ("""pergunta 1:  qual anime e conhecido como melhor anime da historia" \
    a) dragom ball
    b) one piece
    c) naruto
    d) fulmeetal"""
    
    
)

    print(""" pergunta 2: qual nome verdadeiro do goku" \
    a)joao 
    b)matheus 
    c)kakaroto 
    d)todas estao erradas""")
    
    print("""pergunta 3:  quem diz a frase: eu vou ser rei dos piratas" \
    a)shanks
    b)luffy
    c)zoro
    d)law """)
quiz()
    

    

    
# essas sao as variveis do if e else
resposta1 = "a" 
resposta2 = "c"
resposta3 = "b"
# ---------
resposta_1= "a"
resposta_2 = "c"
resposta_3 = "b"
# essas sao para vericar as respostas.


resposta1 = input(""" pergunta1:
 digite a sua resposta: """)
resposta2 = input(""" pergunta 2:
digite sua resposta: """)
resposta3 = input ("""pergunta 3:
 digite sua resposta: """)

pontuacao = 0



if resposta1 == "a":
    print("parabens vc acertou")
    pontuacao += 1
else:
    print("vc errou,a resposta correta e: ",resposta_1)
    
if resposta2 == "c":
    print("parabens vc acertou")
    pontuacao += 1
else:
    print("vc errou,a resposta correta e: ",resposta_2)
      
if resposta3 == "b":
    print("parabens vc acertou")
    pontuacao +=1
else:
 print("vc errou a,resposta correta e: ",resposta_3)
print("." *30)
if pontuacao == 0:
    print("aposentado")
elif pontuacao == 1:
    print("fraco")
elif pontuacao == 2:
    print("qause nerd")
elif pontuacao == 3:
    print("top,vc e nerd")
print(f"sua pontuaçao e:  {pontuacao}")




 
 

       
    
    
    

   
 
    




    

     







