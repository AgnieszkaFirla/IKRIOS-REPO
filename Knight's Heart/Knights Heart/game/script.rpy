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

    show Korst neutral at left with moveinleft

    k @ happy "Sprzedałeś cały towar ojca zaskakująco szybko, panie."
    k @ happy "Lord Hegar będzie zachwycony... i dumny. Widać, że pieniądze zainwestowane w pańską edukację przynoszą owoce."
#animacja
    #window auto hide
    #show Korst neutral:
        #subpixel True
        #xpos 0.5
        #linear 0.18 xpos 0.22
    #with Pause(0.28)
    #show Korst neutral:
        #xpos 0.22
    #window auto show

    k "Teraz wystarczy wrócić do portu i popłynąś spowrotem na Wyspy Mell. Oby morze nam sprzyjało."


    hide Korst neutral with moveinleft
#animacja
    #window auto hide
    #show Draenog neutral2:
        #subpixel True
        #xpos 1.0
        #ypos 100
        #linear 0.2 xpos 0.5
    #with Pause(0.3)
    #show Draenog neutral2:
        #xpos 0.5
        #ypos 100
    #window auto show

    menu:
        "Mam nadzieję, że to wystarczy żeby zadowolić ojca.":
            $ k_affection = +1
            call Option1
        "Zrobiłem, co do mnie należało.":
            $ k_affection = -1
            call Option2

    play music "audio/Land of Wolves/WAV_09_Werewolf_Territory_loop.wav" loop fadein 1.0

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
    show Korst neutral at left
    show Draenog neutral at right
    d @ angry2 "Udowodnię mu ile jestem wart i jak wiele umiem. Nie będzie żałował wydanej na mnie fortuny."

    k "Nie mam co do tego wątpliwości, panie."
    return

label Option3:
    play music "audio/Land of Wolves/WAV_01_Land_of_Wolves_Main_Theme_loop.wav" loop fadein 1.0
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
    play music "audio/Land of Wolves/WAV_05_Dragon_Eye_Boss_Fight_loop.wav" loop fadein 1.0

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

    jump Port_E_Die
    return

label E_rescew:
    "{i}Syn kupieckiego Lorda z Wysp Mell pociągnął za rzemyk. Skórzany woreczek upadł z brzękiem monet na dłoń Draenoga."
    "{i}Ruszył traktem w stronę, z której dobiegały krzyki przestraszonych kobiet."
    "{i}Wkrótce zobaczył scenę, której widok ścisnął jego rzołądek w ciasny supeł. Trzech rosłych mężczyzn przeglądało zawartość licznych skrzyń i kufrów."
    "{i}Wśród bandytów była też kobieta, która przykładała lśniący w słońcu sztylet do gardła ognistej elfki. Przerażona kobieta klęczała przywiązana do koła powozu."
    "{i}Dwóch innych mocowało się przed drzwiami karocy, próbując wywlec stamtąd kolejną kobietę. Na trakcie leżały ciała rozpłatanych na dzwonka mężczyzn."
    d "Hej! To jest dużo więcej warte!"
    "{i}Draenog zawołał pokazując sakiewkę pełną złota. Jeden z bandytów podszedł nieco bliżej, wyglądał na przywódcę."
    show Bandyta1
    b1 "Życie ci nie miłe chłopcze? Zdar chętnie przyjmie twoją duszę do swojego królestwa, a ja z przyjemnością ją tam wyślę"
    show Bandyta2 at left
    b2 "Podrostek chce zostać bohaterem."
    b1 "A już myślałem, że są jeszcze na tym świecie altruiści. Nic bardziej mylnego."
    "{i} Bandytka ze złośliwym uśmiechem na twarzy podeszła do kobiety, wyglądającej na guwernantkę. Dobyła sztyletu i bez ogródek poderżnęła jej gardło."
    b1 "Jeden problem mniej."

    menu:
        "To na prawdę jest więcej warte {i}(Rozsyp monety)":
            $ k_affection = -1
        "Wy ścierwa! Zapłacicie za to życiem! {i}(Walka)":
            jump Deathscreen

    "{i} Bandyci widząc złoty deszcz monet rzucają się żeby je zebrać. Draenog wykorzystując sytuację uwalnia elfkę i umyka z nią w las."
    play music "audio/Land of Wolves/WAV_03_Wandering_Lone_Wolf_loop.wav" loop fadein 1.0
    "{i} Po jakimś czasie biegu głosy za ich plecami giną w ciszy i śpiewie ptaków. Elfka spogląda dużymi, płomiennymi oczami na larmianina."
    e "Gdyby nie ty...{i}Głos uwiązł jej w gardle, a oczy zaszły łzami."
    e "Estre zasłużyła na lepszy los."

    menu:
        "Przepraszam, że nie zdołałem jej uratować.":
            $ e_affection = +2
            call Hug
        "To prawda, jednak czasu nie możemy cofnąć.":
            $ e_affection = -1
            call NoHug

    d "Chodźmy, w Kalaman czeka na nas statek. Jeśli chcesz możesz płynąć z nami. Zaraz..."
    d "Gdzie jest Korst?"
    "{i} Z pomiędzy drzew wybiegł Korst."
    k "Tu jesteś panie, bandyci mogą niebawem ruszyć traktem z łupami. Pośpieszmy się."
    d "Racja, musimy dotrzeć do miasta przed nimi."
    "{i}Ruszyli, a Korst wyrwał się do przodu z pośpiechem. Draenog zastanawiał, się w którym momencie Korst uciekł."
    e "Nie zdążyłam ci podziękować panie, ani się przedstawić. Jestem Elanwe i dziękuję ci, na prawdę jestem wdzięczna za to poświęcenie."

    menu:
        "To mój obowiązek":
            $ e_affection = -1
            jump Town1
        "To dla mnie wiele znaczy.":
            $ e_affection = +1
            jump Town2

    return

label Town1:

    e "Wiem, że nie musiałeś tego robić, a mimo to naraziłeś swoje życie."

    return

label Town2:

    return

label D_die:
    "{i}Dranog chwycił energicznie za rękojeść miecza i wyciągnął go z pochwy. Ruszył dziarsko w stronę, z której dobiegały ich krzyki."
    "{i}Stanął przed Trzema rosłymi mężczyznami, którzy przeglądali zawrartość licznych skrzyń i kufrów."
    "{i}Wśród bandytów była też kobieta, która przykładała lśniący w słońcu sztylet do gardła ognistej elfki. Przerażona kobieta klęczała przywiązana do koła powozu."
    "{i}Dwóch innych mocowało się przed drzwiami karocy, próbując wywlec stamtąd kolejną kobietę. Na trakcie leżały ciała rozpłatanych na dzwonka mężczyzn."
    d "Zostawcie je!"
    show Bandyta1 at left
    b1 "Ani mi się śni, cud chłopcze."
    "{i}Rabusie chwycili za broń. Draenog spojrzał w oczy Korsta, w których jarzył się strach."
    "{i}Walka nie trwała długo, ale też nie była krótka. Bandyci bawili się z kupcami, chcąc ich upokorzyć."
    "{i}W końcu jeden z nich przebił rycerskie serce Draenoga. Jego ciało upadło bezwładnie na trakt tuż obok zwłok woźnicy."
    return

label Hug:
    #PUŚĆ INNĄ MUZYKĘ
    e "Nie przepraszaj... Gdyby nie ty, skonczyłabym tak, jak ona. {i}Żarliwe łzy zaczęły spływać po jej policzkach."
    "{i}Draenog zbliżył się o krok do elfki. Niepewnie położył jej rękę na ramieniu."
    d "Płacz, ja nikomu nie powiem o tych łzach. Ona na nie zasługuje, a ty ich potrzebujesz."
    "{i} Po tych słowach Elanwe po prostu przytuliła się do larmianina. Schowała twarz w jego ramiona i zaczęła szlochać."
    "{i} Draenog nie wiedział ile czasu stoją tak bez ruchu pośród drzew, niemych świadków serca pogrążonego w żałobie"
    "{i} W końcu szloch ucichł. Jej ramiona na powrót zaczęły zwolna unosić się i opadać z każdym oddechem. Odsunęła się od niego na krok."
    e "Miałeś rację. {i}Patrzyła na niego wielkimi, złotymi oczami."
    return

label NoHug:
    #PUŚĆ INNĄ MUZYKĘ
    e "To prawda, ale to nie znaczy, że jej śmierć mnie nie złamała."
    d "Widzę, że jesteś silna. Podniesiesz się."
    e "Jestem, a na rozpacz przyjdzie jeszcze czas. {i}Przełknęła łzy i spojrzała na niego hardo."
    return

label Port_E_Die:

    play music "audio/Land of Wolves/WAV_02_A_Tipsy_Tavern_loop"
    scene bg town

    show Korst neutral at left
    k @ sad "Zginęlibyśmy. Jeśli nawet udałoby się nam przeżyć, stracilibyśmy pieniądze pańskiego ojca."
    k "Podjął Pan właściwą decyzję"

    show Draenog neutral2 at right

    menu:
        "Żałuję, że nie postąpiłem inaczej.":
            $ k_affection = -1
            call Wyrzuty

        "Masz rację, nie mialiśmy na to wpływu":
            $ k_affection = +2

    k @happy "Wracajmy już do domu, Panie. Ojciec Pana oczekuje"

    scene To_Be_Continued

    return

label Deathscreen:
    stop music
    play sound "audio/Land of Wolves/WAV_11_You're_Dead_1.wav"
    return
