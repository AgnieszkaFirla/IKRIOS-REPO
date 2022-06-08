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

    #początek rozdziału

    scene bg forest
    show screen gameUI
    play music "audio/Land of Wolves/WAV_01_Land_of_Wolves_Main_Theme_loop.wav" loop fadein 1.0
    show ember1
    show ember2
    #add Snow("gui/ember1.png")
    #add Snow("gui/ember2.png")


    show Korst happy at right with moveinright

    k "Sprzedałeś cały towar ojca zaskakująco szybko, panie."
    k "Lord Hegar będzie zachwycony... i dumny. Widać, że pieniądze zainwestowane w pańską edukację przynoszą owoce."
    show Korst neutral with dissolve
    k "Teraz wystarczy wrócić do portu i popłynąś spowrotem na Wyspy Mell. Oby morze nam sprzyjało."


    #hide Korst neutral with moveinright
    show Draenog neutral at left with moveinleft

    menu:
        "Mam nadzieję, że to wystarczy żeby zadowolić ojca.":
            $ k_affection = +1
            call Option1
        "Zrobiłem, co do mnie należało.":
            $ k_affection = -1
            call Option2

    play music "audio/Land of Wolves/WAV_09_Werewolf_Territory_loop.wav" loop fadein 1.0
    play sound "audio/scream.mp3"

    "{i}Z głębi lasu słychać rozdzierający ciszę krzyk kobiet..."
    "{i}... i śmiech wielu mężczyzn."

    #show Korst neutral at right
    k "Zaczekaj tu, panie. Sprawdzę co się dzieje."
    hide Korst neutral with moveoutright


    "{i}Korst przykucnął przed gęstymi zaroślami, które przysłaniały dalszą część traktu. Odsłonił ostrożnie gałęzie, zaglądając przez liście."
    "{i}Zamarł przypatrując się temu, co ich czekało na drodzę do portu."

    show Korst sad at right with moveinright
    k "Widziałem sześciu bandytów, panie. Napadli karocę, która wyglądała na kosztowną."
    d "Słyszałem krzyk kobiet, widziałeś je?"

    "{i}Korst przytakuje wolno."
    show Korst angry with dissolve
    k "Jedną... Drugą próbowali wywlec z wozu."
    show Draenog angry with dissolve
    "{i}Draenog chwycił za rękojeść miecza. W jego oczach iskrzyła determinacja."
    show Korst sad with dissolve
    k "Panie, jest ich sześciu, a my nie umiemy walczyć. Nie zdołamy nic uczynić. Jeśli spróbujemy okradną nas z tego, co zarobiłeś dla ojca."

    menu:
        "Masz rację, nie damy rady. Musimy się przekraść bokiem.":
            $ k_affection = +2
            call Option3
        "Tak, nie jestem dobrym wojownikiem, ale one nie mają nikogo lepszego.":
            $ k_affection = +1
            call Option4
        "Nie będę stał bezczynnie, bogowie są po mojej stronie! {i}(Walka)":
            $ k_affection = -2

            call D_die

    return

label Option1:

    show Draenog sad with dissolve
    d "Czasem mam wrażenie jakby wymagał ode mnie zbyt wiele."
    show Draenog neutral with dissolve
    show Korst happy with dissolve
    k "Jest wymagający, to prawda, ale zawsze docenia twoje starania."
    show Korst neutral with dissolve
    return

label Option2:
    #show Korst neutral at left
    #show Draenog neutral at right
    show Draenog angry with dissolve
    d "Udowodnię mu ile jestem wart i jak wiele umiem. Nie będzie żałował wydanej na mnie fortuny."
    show Draenog neutral with dissolve
    show Korst happy with dissolve
    k "Nie mam co do tego wątpliwości, panie."
    show Korst neutral with dissolve
    return

label Option3:
    play music "audio/Land of Wolves/WAV_06_Full_Moon_in_the_Highlands_loop.wav" loop fadein 1.0
    show Draenog sad with dissolve
    "{i}Draenog puszcza rękojeść miecza."
    d "Przejdźmy niepostrzeżenie, byle do portu..."
    play sound "audio/scream.mp3"
    "{i}Syn kupca odwrócił wzrok, zaciskając mocno powieki. Ciszę Płomiennego Lasu rozdzierały krzyki nieznajomych. Ich głosy długo odbijały się w głowie mężczyzny."
    "{i}Ich głosy będą go błagały po nocach o ratunek, którego nie potrafił im dać."

    jump E_die
    return

label Option4:
    show Korst sad with dissolve
    show Draenog neutral with dissolve
    k "Panie Draenog, zginiemy... W najlepszym przypadku okradną nas i wrócimy z niczym."
    show Draenog angry with dissolve
    d "Nie będę odwracał oczu, Korst. Wiem, że mam przy sobie wiele pieniędzy, które nie należą do mnie, ale nie mogę odejść, udając, że nic nie słyszałem."
    k "Co zamierzasz? W walce nie mamy szans, jest ich zbyt wielu. Gdyby było ich dwóch... ale nie sześciu."
    show Draenog happy with dissolve
    d "Nie każdą walkę trzeba wygrywać siłą. Największą bronią jest światły umysł."

    #"{i}Draenog odwiązał sakiewkę pełną złotych mirsili. Monety zabrzęczały kusząco w skórzanym woreczku."

    jump E_rescew
    return



label E_die:
    "{i}Mężczyźni weszli między drzewa żeby obejść bandytów na trakcie. Podróż trwała dłużej, ale przynajmniej uszli z życiem."
    show Draenog neutral with dissolve
    show Korst neutral with dissolve
    "{i}Po jakimś czasie krzyki kobiet ucichły."
    "{i}Cisza była gorsza od wszasku pełnego przerażenia i bólu."
    k "Nie mogliśmy nic zrobić"
    show Draenog angry with dissolve
    d "Myślę, że zawsze można coś zrobić, ale teraz... Jest już za późno."
    show Draenog neutral with dissolve
    jump Port_E_Die
    return

label E_rescew:
    play sound "audio/coins1.mp3"
    "{i}Syn kupieckiego Lorda z Wysp Mell pociągnął za rzemyk. Skórzany woreczek upadł z brzękiem monet na dłoń Draenoga."
    "{i}Ruszył traktem w stronę, z której dobiegały krzyki przestraszonych kobiet."
    show Draenog neutral with dissolve
    "{i}Wkrótce zobaczył scenę, której widok ścisnął jego żołądek w ciasny supeł. Trzech rosłych mężczyzn przeglądało zawartość licznych skrzyń i kufrów."
    "{i}Wśród bandytów była też kobieta, która przykładała lśniący w słońcu sztylet do gardła ognistej elfki. Przerażona kobieta klęczała przywiązana do koła powozu."
    "{i}Dwóch innych mocowało się przed drzwiami karocy, próbując wywlec stamtąd kolejną kobietę. Na trakcie leżały ciała rozpłatanych na dzwonka mężczyzn."
    d "Hej! To jest dużo więcej warte!"
    play sound "audio/coins1.mp3"
    "{i}Draenog zawołał pokazując sakiewkę pełną złota. Jeden z bandytów podszedł nieco bliżej, wyglądał na przywódcę."

    window auto hide
    show Korst sad:
        subpixel True
        xpos 1.0
        linear 0.26 xpos 0.75
    with Pause(0.36)
    show Korst sad:
        xpos 0.75
    window auto show


    show Bandyta at right with moveinright
    b1 "Życie ci nie miłe chłopcze? Zdar chętnie przyjmie twoją duszę do swojego królestwa, a ja z przyjemnością ją tam wyślę."
    hide Korst sad with moveoutleft

    window auto hide
    show Bandyta:
        subpixel True
        xpos 1.0
        linear 0.3 xpos 0.69
    with Pause(0.4)
    show Bandyta:
        xpos 0.69
    window auto show

    show Bandytka at right with moveinright
    b2 "Podrostek chce zostać bohaterem."
    b1 "A już myślałem, że są jeszcze na tym świecie altruiści. Nic bardziej mylnego."
    hide Bandytka at right with moveoutright
    "{i} Bandytka ze złośliwym uśmiechem na twarzy podeszła do kobiety, wyglądającej na guwernantkę. Dobyła sztyletu i bez ogródek poderżnęła jej gardło."
    b1 "Jeden problem mniej."

    menu:
        "To na prawdę jest więcej warte {i}(Rozsyp monety)":
            $ k_affection = -1
        "Wy ścierwa! Zapłacicie za to życiem! {i}(Walka)":
            jump D_die2
    show Draenog neutral2 with dissolve
    "{i} Bandyci widząc złoty deszcz monet rzucają się żeby je zebrać. Draenog wykorzystując sytuację uwalnia elfkę i umyka z nią w las."
    hide Bandyta at right with moveoutright
    play music "audio/Land of Wolves/WAV_03_Wandering_Lone_Wolf_loop.wav" loop fadein 1.0
    show Elanwe neutral at right with moveinright
    "{i} Po jakimś czasie biegu głosy za ich plecami giną w ciszy i śpiewie ptaków. Elfka spogląda dużymi, płomiennymi oczami na larmianina."
    show Elanwe sad with dissolve
    el "Gdyby nie ty...{i}Głos uwiązł jej w gardle, a oczy zaszły łzami."
    el "Estre zasłużyła na lepszy los."

    menu:
        "Przepraszam, że nie zdołałem jej uratować.":
            $ e_affection = +2
            call Hug
        "To prawda, jednak czasu nie możemy cofnąć.":
            $ e_affection = -1
            call NoHug

    d "Chodźmy, w Kalaman czeka na nas statek. Jeśli chcesz możesz płynąć z nami. Zaraz..."
    show Draenog neutral2 with dissolve
    d "Gdzie jest Korst?"
    show Korst neutral at right with moveinright
    "{i} Z pomiędzy drzew wybiegł Korst."
    show Korst happy with dissolve
    k "Tu jesteś panie, bandyci mogą niebawem ruszyć traktem z łupami. Pośpieszmy się."
    show Draenog happy2 with dissolve
    d "Racja, musimy dotrzeć do miasta przed nimi."
    hide Korst happy at right with moveoutright
    "{i}Ruszyli, a Korst wyrwał się do przodu z pośpiechem. Draenog zastanawiał, się w którym momencie Korst uciekł z pola walki."
    el "Nie zdążyłam ci podziękować panie, ani się przedstawić. Jestem Elanwe i dziękuję ci, na prawdę jestem wdzięczna za to poświęcenie."

    menu:
        "To mój obowiązek":
            $ e_affection = -1
            jump Town1
        "To dla mnie wiele znaczy.":
            $ e_affection = +1
            jump Town2

    return

label Town1:
    scene bg town with dissolve
    show ember1
    show ember2
    show Draenog neutral2 at left with moveinleft
    e "Wiem, że nie musiałeś tego robić, a mimo to naraziłeś swoje życie."
    d "Jestem pewien, że każdy postąpiłby tak samo."
    e "Zdradziłam ci swoje imię, ale ja wciąż nie znam twojego."
    d "Wybacz, pani, jak mogłem zapomnieć... Gdzie moje maniery? Jestem Draenog z rodu Jeża, a to Korst z rodu Hieny."
    d "Przybyliśmy do Dolhal sprzedać towar mego ojca, wielkiego kupca z Wysp Mell. Nasz statek czeka w porcie. Płyń z nami. Pokażę ci Wyspy, i ugoszczę w pałacyku na Szafirowym Wybrzeżu."
    "{i}Elanwe zastanawiała się dłuższą chwilę. Rozejrzała się po Kalaman. Larmianach i elfach kłębiących się na ulicach portowego miasta. Widać w tym spojrzeniu zapłakanych oczu była tęsknota."
    e "Popłynę z tobą, Draenogu. Zostanę na Wyspach, przynajmniej na jakiś czas."
    show Draenog happy2 with dissolve
    d "Zatem zapraszam. Statek czeka."
    "{i}Draenog wskazał uliczkę prowadzącą do portu zapraszającym gestem dłoni."
    jump Rozdzial1

    return

label Town2:
    scene bg town with dissolve
    show ember1
    show ember2
    show Draenog neutral2 at left with moveinleft
    "{i}Elanwe uśmiechnęła się lekko na słowa młodego kupca."
    e "Zdradziłam ci panie moje imię, a ja wciąż nie znam twego imienia."
    d "Wybacz, pani! Gdzie moje maniery? Jestem Draenog z rodu Jeża, a to Korst z rodu Hieny. Przybyliśmy do Dolhal sprzedać towar mego ojca, wielkiego kupca z Wysp Mell."
    d "Płyń znami na Wyspy. Pokażę ci Szafirowe Wybrzeże i Diamentowe Iglice. Moja rodzina przyjmnie cię w pałacyku jak córkę króla."
    "{i}Elanwe zastanawiała się dłuższą chwilę. Rozejrzała się po Kalaman. Larmianach i elfach kłębiących się na ulicach portowego miasta. Widać w tym spojrzeniu zapłakanych oczu była tęsknota."
    e "Popłynę z tobą, Draenogu. Chcę zobaczyć Szafirowe Wybrzeże i... chcę stąd uciec. Przynajmniej na jakiś czas."
    show Draenog happy2 with dissolve
    d "Zatem zapraszam. Statek czeka."
    "{i}Draenog wskazał uliczkę prowadzącą do portu zapraszającym gestem dłoni."
    jump Rozdzial1
    return

label D_die:
    play music "audio/Land of Wolves/WAV_05_Dragon_Eye_Boss_Fight_loop.wav" loop fadein 1.0
    "{i}Dranog chwycił energicznie za rękojeść miecza i wyciągnął go z pochwy. Ruszył dziarsko w stronę, z której dobiegały ich krzyki."

    window auto hide
    show Korst sad:
        subpixel True
        xpos 1.0
        linear 0.32 xpos 0.79
    with Pause(0.42)
    show Korst sad:
        xpos 0.79
    window auto show

    "{i}Stanął przed Trzema rosłymi mężczyznami, którzy przeglądali zawrartość licznych skrzyń i kufrów."
    "{i}Wśród bandytów była też kobieta, która przykładała lśniący w słońcu sztylet do gardła ognistej elfki. Przerażona kobieta klęczała przywiązana do koła powozu."
    "{i}Dwóch innych mocowało się przed drzwiami karocy, próbując wywlec stamtąd kolejną kobietę. Na trakcie leżały ciała rozpłatanych na dzwonka mężczyzn."
    d "Zostawcie je!"
    show Bandyta at right with moveinright
    b1 "Ani mi się śni, cud chłopcze."
    "{i}Rabusie chwycili za broń. Draenog spojrzał w oczy Korsta, w których jarzył się strach."
    hide Korst sad with moveoutleft
    "{i}Walka nie trwała długo, ale też nie była krótka. Bandyci bawili się z kupcami, chcąc ich upokorzyć."
    "{i}W końcu jeden z nich przebił rycerskie serce Draenoga. Jego ciało upadło bezwładnie na trakt tuż obok zwłok woźnicy."

    jump Deathscreen
    return

label D_die2:
    play music "audio/Land of Wolves/WAV_05_Dragon_Eye_Boss_Fight_loop.wav" loop fadein 1.0
    show Draenog angry with dissolve
    "{i}Dranog chwycił energicznie za rękojeść miecza i wyciągnął go z pochwy."
    "{i}Bandyci chwycili za broń."
    "{i}Walka nie trwała długo, ale też nie była krótka. Szubrawcy bawili się z kupcem, chcąc go upokorzyć."
    "{i}W końcu jeden z nich przebił rycerskie serce Draenoga. Jego ciało upadło bezwładnie na trakt tuż obok zwłok woźnicy."
    jump Deathscreen
    return

label Hug:
    play music "audio/Land of Wolves/WAV_04_Fields_of_Sun_loop.wav" loop fadein 1.0
    el "Nie przepraszaj... Gdyby nie ty, skonczyłabym tak, jak ona. {i}Żarliwe łzy zaczęły spływać po jej policzkach."

    window auto hide
    show Draenog neutral2:
        subpixel True
        xpos 0.0
        linear 0.23 xpos 0.29
    with Pause(0.33)
    show Draenog neutral2:
        xpos 0.29
    window auto show


    "{i}Draenog zbliżył się o krok do elfki. Niepewnie położył jej rękę na ramieniu."
    show Draenog happy2 with dissolve
    d "Płacz, ja nikomu nie powiem o tych łzach. Ona na nie zasługuje, a ty ich potrzebujesz."
    "{i} Po tych słowach elfka po prostu przytuliła się do larmianina. Schowała twarz w jego ramiona i zaczęła szlochać."
    "{i} Draenog nie wiedział ile czasu stoją tak bez ruchu pośród drzew, niemych świadków serca pogrążonego w żałobie"
    "{i} W końcu szloch ucichł. Jej ramiona na powrót zaczęły zwolna unosić się i opadać z każdym oddechem. Odsunęła się od niego na krok."
    el "Miałeś rację. {i}Patrzyła na niego wielkimi, złotymi oczami."
    return

label NoHug:
    play music "audio/Land of Wolves/WAV_03_Wandering_Lone_Wolf_loop.wav" loop fadein 1.0
    el "To prawda, ale to nie znaczy, że jej śmierć mnie nie złamała."
    show Draenog happy2 with dissolve
    d "Widzę, że jesteś silna. Podniesiesz się."
    el "Jestem, a na rozpacz przyjdzie jeszcze czas. {i}Przełknęła łzy i spojrzała na niego hardo."

    return


label Port_E_Die:

    scene bg town with dissolve
    play music "audio/Land of Wolves/WAV_02_A_Tipsy_Tavern_loop.wav"
    show ember1
    show ember2
    show Korst sad at right with moveinright
    k "Zginęlibyśmy. Jeśli nawet udałoby się nam przeżyć, stracilibyśmy pieniądze pańskiego ojca."
    show Korst neutral with dissolve
    k "Podjął Pan właściwą decyzję"

    show Draenog neutral at left with moveinleft

    menu:
        "Żałuję, że nie postąpiłem inaczej.":
            $ k_affection = -1
            call Wyrzuty

        "Masz rację, nie mialiśmy na to wpływu":
            $ k_affection = +2

    show Korst happy with dissolve
    k "Wracajmy już do domu, Panie. Ojciec Pana oczekuje"
    d "Czas wracać na statek."


    jump Rozdzial1

    return

label Wyrzuty:

    show Draenog angry with dissolve
    d "Mogłem je uratować. Miast tego egoistycznie odwróciłem wzrok od cierpienia."
    k "Z pewnością nie był to egoizm, gdyż myślał pan również o swojej rodzinie i nie swoich pieniądzach."
    show Korst happy with dissolve
    k "Pański ojciec na pewno pochwali taką decyzję."
    show Draenog neutral with dissolve
    d "Przekonajmy się zatem. Czas wracać na statek."

    jump Rozdzial1

    return

label Rozdzial1:
    stop music
    play sound "audio/WAV_10_Mission_Succesful.mp3"
    scene ship sea
    play music "audio/Land of Wolves/WAV_02_A_Tipsy_Tavern_loop.wav" fadein 7.0
    pause(2.0)
    call screen Rozdzial_1 with dissolve
    return

label Deathscreen:
    stop music
    play sound "audio/WAV_11_You're_Dead_1.mp3"
    play music "audio/Land of Wolves/WAV_03_Wandering_Lone_Wolf_loop.wav" loop fadein 1.0
    scene deathscreen
    pause(2.0)
    call screen Deathscreen with dissolve
    return
