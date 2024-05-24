"""Defina um usuário e senha, depois verifique se login do usúario é valido"""

Usuario = "Danilo"
Senha = "DD303"

while True:
  
  Usuario_login = input("Digite seu Login: ")
  Usuario_Senha = input("Digite sua Senha: ")
  
  if Usuario_login == Usuario and Usuario_Senha == Senha:
    print("Login Validado!!")
 
  else:
      print("Login invalido!! Tente novamente");