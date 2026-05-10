from pygame import *
import sys

init()

LARGURA, ALTURA = 1500, 1000
tela = display.set_mode((LARGURA, ALTURA))
display.set_caption("LOGIN")

clock = time.Clock()

fundo = image.load("fundo.png")
fundo = transform.scale(fundo, (LARGURA, ALTURA))

fundo_small = transform.smoothscale(fundo, (120, 80))
fundo_blur = transform.smoothscale(fundo_small, (LARGURA, ALTURA))

fonte = font.SysFont("Arial", 30)
fonte_peq = font.SysFont("Arial", 24)

def valida_email(email):
    return "@puc.com" in email

def valida_senha(senha):
    return len(senha) >= 8 and any(c.isupper() for c in senha) and any(c.islower() for c in senha) and any(c.isdigit() for c in senha)


email = ""
senha = ""
campo = "email"
msg = ""

cursor = True
cursor_time = 0

logado = False
tempo_login = 0
trocar = False

while True:

    clock.tick(60)

    tela.blit(fundo_blur, (0, 0))

    overlay = Surface((LARGURA, ALTURA))
    overlay.set_alpha(120)
    overlay.fill((0, 0, 0))
    tela.blit(overlay, (0, 0))

    cursor_time += clock.get_time()

    if cursor_time > 500:
        cursor = not cursor
        cursor_time = 0

    for event in event.get():

        if event.type == QUIT:
            quit()
            sys.exit()

        if event.type == KEYDOWN and not logado:

            if event.key == K_TAB:
                campo = "senha" if campo == "email" else "email"

            elif event.key == K_BACKSPACE:
                if campo == "email":
                    email = email[:-1]
                else:
                    senha = senha[:-1]

            elif event.key == K_RETURN:

                if not valida_email(email):
                    msg = "Email inválido!"

                elif not valida_senha(senha):
                    msg = "Senha inválida!"

                else:
                    msg = "BEM VINDO A CASINHA!"
                    logado = True
                    tempo_login = time.get_ticks()

            else:
                if campo == "email":
                    email += event.unicode
                else:
                    senha += event.unicode
    draw.rect(tela, (255, 255, 255), (120, 80, 460, 320), border_radius=15)

    tela.blit(fonte.render("LOGIN", True, (0, 0, 0)), (300, 110))

    cor_email = (0, 200, 0) if campo == "email" else (0, 0, 0)

    draw.rect(tela, (220, 220, 220), (170, 180, 360, 50), border_radius=10)

    txt_email = "Email: " + email
    if campo == "email" and cursor:
        txt_email += "|"

    tela.blit(fonte_peq.render(txt_email, True, cor_email), (185, 193))

    cor_senha = (0, 200, 0) if campo == "senha" else (0, 0, 0)

    draw.rect(tela, (220, 220, 220), (170, 260, 360, 50), border_radius=10)

    txt_senha = "Senha: " + ("*" * len(senha))
    if campo == "senha" and cursor:
        txt_senha += "|"

    tela.blit(fonte_peq.render(txt_senha, True, cor_senha), (185, 273))

    tela.blit(fonte_peq.render(msg, True, (0, 0, 0)), (170, 360))

    display.update()

    if logado:

        if tempo_login == 0:
            tempo_login = time.get_ticks()

        if time.get_ticks() - tempo_login > 2000:
        import casinha
