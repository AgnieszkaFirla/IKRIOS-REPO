label start:

    #$config.rollback_enabled = False
    #$quick_menu = False
    #$enviroment_SM = SpriteManager(event = enviromentEvents)
    #$inventory_SM = SpriteManager(update= inventoryUpdate, event= inventoryEvents)
    #$enviroment_sprites = []
    #$inventory_sprites = []
    #$enviroment_items = []
    #$inventory_items = []
    #$enviroment_items_names = []
    #$inventory_items_names = ["flowers"]
    #$current_scene = "bg forest"

    scene bg forest
    show screen gameUI
    play music "audio/Land of Wolves/WAV_01_Land_of_Wolves_Main_Theme_loop.wav" loop fadein 1.0

    show Korst neutral

    k @ happy "Sprzedałeś cały towar ojca zaskakująco szybko, panie."
    k @ happy "Lord Hegar będzie zachwycony... i dumny. Widać, że pieniądze zainwestowane w pańską edukację przynoszą owoce."

    window auto hide
    show Korst neutral:
        subpixel True
        xpos 0.5
        linear 0.18 xpos 0.22
    with Pause(0.28)
    show Korst neutral:
        xpos 0.22
    window auto show

    k "Teraz wystarczy wrócić do portu i popłynąś spowrotem na Wyspy Mell. Oby morze nam sprzyjało."

    
    hide Korst neutral

    window auto hide
    show Draenog neutral2:
        subpixel True
        xpos 1.0
        ypos 100
        linear 0.2 xpos 0.5
    with Pause(0.3)
    show Draenog neutral2:
        xpos 0.5
        ypos 100
    window auto show

    menu:
        "Mam nadzieję, że to wystarczy żeby zadowolić ojca.":
            $ k_affection = +1
            call Option1
        "Zrobiłem, co do mnie należało.":
            $ k_affection = -1
            call Option2

    "{i}Z głębi lasu słychać rozdzierający ciszę krzyk kobiet..."
    "{i}... i śmiech wielu mężczyzn."

    show Korst neutral at left
    k "Zaczekaj tu, panie. Sprawdzę co się dzieje."
    hide Korst neutral


    "{i}Korst przykucnął przed gęstymi zaroślami, które przysłaniały dalszą część traktu. Odsłonił ostrożnie gałęzie, zaglądając przez liście."
    "{i}Zamarł przypatrując się temu, co ich czekało na drodzę do portu."

    show Korst neutral at left with moveinleft
    k "Widziałem sześciu bandytów, panie. Napadli karocę, która wyglądała na kosztowną."
    d "Słyszałem krzyk kobiet, widziałeś je?"

    "{i}Korst przytakuje wolno."

    k @ angry "Jedną... Drugą próbowali wywlec z wozu."

    "{i}Draenog chwycił za rękojeść miecza. W jego oczach iskrzyła determinacja."

    k @ sad "Panie, jest ich sześciu, a my nie umiemy walczyć. Nie zdołamy nic uczynić. Jeśli spróbujemy okradną nas z tego, co zarobiłeś dla ojca."

    menu:
        "Masz rację, nie damy rady. Musimy się przekraść bokiem.":
            $ k_affection = +2
            call Option3
        "Tak, nie jestem dobrym wojownikiem, ale one nie mają nikogo lepszego.":
            $ k_affection = +1
            call Option4
        "Nie będę stał bezczynnie, bogowie są po mojej stronie! {i}(Walka)":
            $ k_affection = -2
            call Option5

    return

label Option1:

    d "Czasem mam wrażenie jakby wymagał ode mnie zbyt wiele."

    k "Jest wymagający, to prawda, ale zawsze docenia twoje starania."
    return

label Option2:
    d @ angry2 "Udowodnię mu ile jestem wart i jak wiele umiem. Nie będzie żałował wydanej na mnie fortuny."
    hide Draenog d
    window auto hide
    show Korst neutral:
        subpixel True
        xpos 0.5
        linear 0.18 xpos 0.22
    with Pause(0.28)
    show Korst neutral:
        xpos 0.22
    window auto show
    k "Nie mam co do tego wątpliwości, panie."
    return

label Option3:
    "{i}Draenog puszcza rękojeść miecza."
    d @ sad2 "Przejdźmy niepostrzeżenie, byle do portu..."
    "{i}Syn kupca odwrócił wzrok, zaciskając mocno powieki. Ciszę Płomiennego Lasu rozdzierały krzyki nieznajomych. Ich głosy długo odbijały się w głowie mężczyzny."
    "{i}Ich głosy błagały go po nocach o ratunek, którego nie potrafił im dać."

    jump E_die
    return

label Option4:
    show Korst neutral
    show Draenog neutral2
    k @ sad "Panie Draenog, zginiemy... W najlepszym przypadku okradną nas i wrócimy z niczym."
    d @ angry2 "Nie będę odwracał oczu, Korst. Wiem, że mam przy sobie wiele pieniędzy, które nie należą do mnie, ale nie mogę odejść, udając, że nic nie słyszałem."
    k "Co zamierzasz? W walce nie mamy szans, jest ich zbyt wielu. Gdyby było ich dwóch... ale nie sześciu."
    d @ happy2 "Nie każdą walkę trzeba wygrywać siłą. Największą bronią jest światły umysł."

    "{i}Draenog odwiązał sakiewkę pełną złotych mirsili. Monety zabrzęczały kusząco w skórzanym woreczku."

    jump E_rescew
    return

label Option5:
    jump D_die
    return

label E_die:
    "{i}Mężczyźni weszli między drzewa żeby obejść bandytów na trakcie. Podróż trwała dłużej, ale przynajmniej."
    "{i}Po jakimś czasie krzyki kobiet ucichły."
    "{i}Cisza była gorsza od wszasku pełnego przerażenia i bólu."
    show Korst neutral at left
    k "Nie mogliśmy nic zrobić"
    show Draenog sad2 at right
    d "Myślę, że zawsze można coś zrobić, ale teraz... Jest już za późno."
    return

label E_rescew:
    "{i}Syn kupieckiego Lorda z Wysp Mell pociągnął za rzemyk. Skórzany woreczek upadł z brzękiem monet na dłoń Draenoga."
    "{i}Ruszył traktem w stronę, z której dobiegały ich krzyki przestraszonych kobiet."
    "{i}Wkrótce zobaczył scenę, której widok ścisnął jego rzołądek w ciasny supeł. Trzech rosłych mężczyzn przeglądało zawartość licznych skrzyń i kufrów."
    "{i}Wśród bandytów była wśród nich też kobieta, która przykładała lśniący w słońcu sztylet do gardła ognistej elfki. Przerażona kobieta klęczała przywiązana do koła powozu."
    "{i}Dwóch innych mocowało się przed drzwiami karocy, próbując wywlec stamtąd kolejną kobietę. Na trakcie leżały ciała rozpłatanych na dzwonka mężczyzn."
    d "Hej! To jest dużo więcej warte!"
    "{i}Draenog zawołał pokazując sakiewkę pełną złota. Jeden z bandytów podszedł nieco bliżej, wyglądał na przywódcę."

    return

label D_die:
    "{i}Dranog chwycił energicznie za rękojeść miecza i wyciągnął go z pochwy. Ruszył dziarsko w stronę, z której dobiegały ich krzyki."
    "{i}Stanął przed Trzema rosłymi mężczyznami, którzy przeglądali zawrartość licznych skrzyń i kufrów."
    "{i}Wśród bandytów była wśród nich też kobieta, która przykładała lśniący w słońcu sztylet do gardła ognistej elfki. Przerażona kobieta klęczała przywiązana do koła powozu."
    "{i}Dwóch innych mocowało się przed drzwiami karocy, próbując wywlec stamtąd kolejną kobietę. Na trakcie leżały ciała rozpłatanych na dzwonka mężczyzn."
    d "Zostawcie je!"
    b1 "Ani mi się śni, cud chłopcze."
    "{i}Rabusie chwycili za broń. Draenog spojrzał w oczy Korsta, w których jarzył się strach."
    "{i}Walka nie trwała długo, ale też nie była krótka. Bandyci bawili się z kupcami, chcąc ich upokorzyć."
    "{i}W końcu jeden z nich przebił rycerskie serce Draenoga. Jego ciało upadło bezwładnie na trakt tuż obok zwłok woźnicy."
    return

    label Deathscreen:
    stop music
    play sound "audio/Land of Wolves/WAV_11_You're_Dead_1.wav"
    return
