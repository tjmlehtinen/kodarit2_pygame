# ladataan tarvittavat kirjastot
import pygame
import sys
import random

# alustetaan pygame
pygame.init()

# määritellään pelikentän muodostavien ruutujen koko ja niiden avulla näytön koko
RUUTU = 20
LEVEYS = 20
KORKEUS = 15
NAYTON_KOKO = (LEVEYS * RUUTU, KORKEUS * RUUTU)
NAYTTO = pygame.display.set_mode(NAYTON_KOKO)
pygame.display.set_caption("MATOPELI 2026")

# määritellään värejä
taustavari = pygame.Color(33, 33, 0)
ruutuvari = pygame.Color(133, 133, 0)
matovari = pygame.Color(33, 233, 33)
ruokavari = pygame.Color(233, 33, 33)

# pelikenttä koostuu ruuduista, joita piirretään seuraavalla metodilla
def piirra_ruutu(x, y, vari):
    sijainti = (x * RUUTU + 1, y * RUUTU + 1)
    koko = (RUUTU - 2, RUUTU - 2)
    pygame.draw.rect(NAYTTO, vari, (sijainti, koko))

# piirtää kaikki taustan ruudut
def piirra_tausta():
    NAYTTO.fill(taustavari)
    for x in range(LEVEYS):
        for y in range(KORKEUS):
            piirra_ruutu(x, y, ruutuvari)

# funktio, joka kertoo onko sijainti peliruudukon sisällä
def on_peliruudukossa(sijainti):
    x, y = sijainti
    return 0 <= x and x < LEVEYS and 0 <= y and y < KORKEUS

# eri suunnat lukupareina
OIKEA = (1, 0)
VASEN = (-1, 0)
ALAS = (0, 1)
YLOS = (0, -1)

suunta = OIKEA

# määritellään mato
mato = [(0, 0), (1, 0), (2, 0), (3, 0)]

# ruokaan liittyvät
def sijainti_ruoalle():
    x = random.randrange(LEVEYS)
    y = random.randrange(KORKEUS)
    sijainti = (x, y)
    if not sijainti in mato:
        return sijainti
    else:
        return sijainti_ruoalle()

ruoka = sijainti_ruoalle()

def piirra_ruoka():
    x, y = ruoka
    piirra_ruutu(x, y, ruokavari)

def piirra_mato():
    for sijainti in mato:
        x, y = sijainti
        piirra_ruutu(x, y, matovari)

def liikuta_matoa():
    global ruoka
    paa_x, paa_y = mato[-1]
    suunta_x, suunta_y = suunta
    uusi_paa = (paa_x + suunta_x, paa_y + suunta_y)
    if uusi_paa in mato:
        print("Mato törmäsi itseensä :(")
        game_over()
    if not on_peliruudukossa(uusi_paa):
        print("Mato meni yli reunan :(")
        game_over()
    mato.append(uusi_paa)
    if uusi_paa == ruoka:
        ruoka = sijainti_ruoalle()
    else:
        mato.pop(0)

# määritellään fontit game over -ruutua varten
game_over_fontti = pygame.font.SysFont("cambria", 60)
game_over_teksti = game_over_fontti.render("GAME OVER", True, (255, 0, 0))

def game_over():
    print("Madon pituus: " + str(len(mato)))
    while True:
        # käydään läpi tapahtumat
        for tapahtuma in pygame.event.get():
            # onko tapahtuma ikkunan sulkeminen
            if tapahtuma.type == pygame.QUIT:
                # suljetaan pygame ja lopetetaan ohjelma
                pygame.quit()
                sys.exit()
        NAYTTO.blit(game_over_teksti, (50,100))
        pygame.display.update()

kello = pygame.time.Clock()

# peliluuppi
while True:
    # ruudun päivitysnopeus
    kello.tick(5)
    # käydään läpi tapahtumat
    for tapahtuma in pygame.event.get():
        # onko tapahtuma ikkunan sulkeminen
        if tapahtuma.type == pygame.QUIT:
            # suljetaan pygame ja lopetetaan ohjelma
            pygame.quit()
            sys.exit()
        # onko tapahtuma näppäimen painaminen
        if tapahtuma.type == pygame.KEYDOWN:
            # onko näppäin nuoli alas
            if tapahtuma.key == pygame.K_DOWN:
                suunta = ALAS
            # onko näppäin nuoli ylös
            if tapahtuma.key == pygame.K_UP:
                suunta = YLOS
            # onko näppäin nuoli oikealle
            if tapahtuma.key == pygame.K_RIGHT:
                suunta = OIKEA
            # onko näppäin nuoli vasemmalle
            if tapahtuma.key == pygame.K_LEFT:
                suunta = VASEN
    piirra_tausta()
    piirra_mato()
    piirra_ruoka()
    # päivitetään näyttö
    pygame.display.update()
    # pelin päivitys
    liikuta_matoa()

# tiedoston loppuun pygamen sulkeminen
pygame.quit()