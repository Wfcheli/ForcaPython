class Palavra:
    def __init__(self, arquivo):
        self.arquivo = open(arquivo, 'r', encoding ='utf-8')
        self.palavras = self.palavras_do_arquivo(self.arquivo)
        self.palavra = self.sortear(self.palavras)
        self.palavra = self.palavra.upper()
        self.esconder()

    def sortear(self, palavras):
        from random import choice
        return choice(palavras)
    
    def palavras_do_arquivo(self, arquivo):
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip().upper())
        return palavras

    def tem_letra(self, letra):
        if letra in self.palavra:
            return True
        else:
            return False
    
    def esconder(self):
        self.palavra_misterio = []
        for letra in self.palavra:
            self.palavra_misterio.append('__')

    def revelar(self, letra):
        for posicao, letra_palavra in enumerate(self.palavra):
            if letra == letra_palavra:
                self.palavra_misterio[posicao] = letra

    def esta_completa(self):
        if '__' in self.palavra_misterio:
            return False
        else:
            return True


class Jogo:
    def __init__(self, arquivo):
        self.vidas = 6
        self.chutes = 0
        self.palavra_escondida = Palavra(arquivo)
        self.historico_chutes = []

    def novo_jogo(self, arquivo):
        self.chutes = 0
        self.vidas = 6
        self.palavra_escondida = Palavra(arquivo)
        self.historico_chutes = []

    def chutar(self, letra):
        self.chutes += 1
        letra = letra.upper()
        if self.eh_valido(letra):
            if self.adiciona_historico(letra):
                if self.palavra_escondida.tem_letra(letra):
                    self.palavra_escondida.revelar(letra)
                else:
                    self.vidas -= 1    

    def adiciona_historico(self, letra):
        if letra in self.historico_chutes:
            return False
        else: 
            self.historico_chutes.append(letra)
            return True

    def eh_valido(self, letra):
        if len(letra) == 1 and letra.isalpha():
            return True
        else:
            return False        

    def ganhou(self):
        if self.palavra_escondida.esta_completa():
            return True
        else:
            return False
                
    def perdeu(self):
        if self.vidas <= 0:
            return True
        else:
            return False
      

if __name__ == "__main__":
    jogo = Jogo('palavras.txt')
    while not (jogo.ganhou() and jogo.perdeu()):
        print("------------------------------------------------")
        print(f"Vidas: {jogo.vidas}")
        print(jogo.palavra_escondida.palavra_misterio)
        print(f"Chutes: {jogo.historico_chutes}")
        print("------------------------------------------------")
        letra = input("Digite uma letra: ")
        jogo.chutar(letra)
        if jogo.ganhou():
            print("Você ficou vivo dessa vez")
            print("O personagem é: ", jogo.palavra_escondida.palavra_misterio)
            break
        elif jogo.perdeu():
            print("Chegou a sua hora! MuhHÁhahaHAHAhahá")
            break
            
    
