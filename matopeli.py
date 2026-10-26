# ladataan tarvittavat kirjastot
import pygame
import sys

# alustetaan pygame
pygame.init()

# määritellään pelikentän muodostavien ruutujen koko ja niiden avulla näytön koko
RUUTU = 20
LEVEYS = 20
KORKEUS = 15
NAYTON_KOKO = (LEVEYS * RUUTU, KORKEUS * RUUTU)
NAYTTO = pygame.display.set_mode(NAYTON_KOKO)
pygame.display.set_caption("MATOPELI 2026")

# määritellään
taustavari = pygame.Color(133, 133, 0)
ruutuvari = pygame.Color(233, 233, 0)

def piirra_ruutu(x, y, vari):
    sijainti = (x * RUUTU + 1, y * RUUTU + 1)
    koko = (RUUTU - 2, RUUTU - 2)
    pygame.draw.rect(NAYTTO, vari, (sijainti, koko))

def piirra_tausta():
    NAYTTO.fill(taustavari)
    piirra_ruutu(3,3,ruutuvari)


# peliluuppi
while True:
    # käydään läpi tapahtumat
    for tapahtuma in pygame.event.get():
        # onko tapahtuma ikkunan sulkeminen
        if tapahtuma.type == pygame.QUIT:
            # suljetaan pygame ja lopetetaan ohjelma
            pygame.quit()
            sys.exit()
    piirra_tausta()
    # päivitetään näyttö
    pygame.display.update()

# tiedoston loppuun pygamen sulkeminen
pygame.quit()