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
