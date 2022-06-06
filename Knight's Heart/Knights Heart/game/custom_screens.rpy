screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "gui/uznaniebox_idle.png"
        action ShowMenu("UznanieUI")


screen UznanieUI:
    add "gui/main_menu.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Korst z rodu Hieny" size 40
                text "Elanwe Felariel" size 40

            vbox:
                spacing 10
                text "[k_affection]" size 40
                text "[e_affection]" size 40


    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "gui/backbox.png"
        action Return()

#koniec rozdziału 1

screen Rozdzial_1:
    add "gui/main_menu.png"
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        frame:
            xpadding 70
            ypadding 50
            xalign 0.5
            yalign 0.5


            vbox:
                spacing 10
                text "Rozdzał 1" size 60 xalign 0.7
                text "ukończony" size 40 xalign 0.5

        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton _("Main Menu") action MainMenu()

screen Deathscreen:
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        frame:
            xpadding 100
            ypadding 50
            xalign 0.5
            yalign 0.5


            vbox:
                spacing 10
                text "Poległeś" size 60 xalign 0.5
                text "Zdar przybył po twą duszę" size 40 xalign 0.5

        frame:
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            textbutton _("Main Menu") action MainMenu()
