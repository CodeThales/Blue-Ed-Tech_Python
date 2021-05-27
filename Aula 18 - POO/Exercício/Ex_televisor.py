class Televisor:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def trocar_canal(self, novo_canal=0):
        self.canal = novo_canal

    def aumentar(self, novo_volume=0):
        if novo_volume + self.volume <= 100:
            self.volume += novo_volume
        else:
            self.volume = 100

    def diminuir(self, novo_volume=0):
        if self.volume - novo_volume >=0:
            self.volume -= novo_volume
        else:
            self.volume = 0

    def mute(self):
        self.volume = 0

    def __str__(self):
        return f'Esse é o canal {self.canal} no volume {self.volume}'
