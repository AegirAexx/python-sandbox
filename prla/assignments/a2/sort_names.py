from pprint import pprint


def sort_names(s):
    # Alphabet list and indices
    alphabet = ' aábcdðeéfghiíjklmnoópqrstuúvwxyýzþæö'
    alph_lis = []
    for i, d in enumerate(alphabet):
        alph_lis.append(tuple((d, i + 10)))
    alph_idx = {k: v for (k, v) in alph_lis}
    # print(alph_idx)

    # Just first name and last name.
    sans_lis = []
    for i in s:
        x = i.split()
        if len(x) > 2:
            xcv = x[-1]
            x.insert(1, xcv)
            del x[-1]
        sans_lis.append(' '.join(x))
    # print(sans_lis)

    # Lower case name with no middle and orginal name.
    lis_idx = []
    for i, x in enumerate(s):
        lis_idx.append(tuple((sans_lis[i].lower(), x)))
        # print(lis_idx[i][0])
    nam_idx = {k: v for (k, v) in lis_idx}
    # print(lis_idx)
    # pprint(nam_idx)

    # Numeric value of name and orginal.
    num_lis = []
    for s in lis_idx:
        asd = [str(alph_idx.get(d)) for d in s[0]]
        num_lis.append(tuple((''.join(asd), nam_idx.get(s[0]))))
    # qwer = {k: v for (k, v) in num_lis}
    # pprint(qwer)

    result = []
    for x in sorted(num_lis):
        result.append(x[1])
        # print(x[1])

    return result


print(sort_names(['Þórir Jakob Olgeirsson',
                  'Arnar Björn Pálsson',
                  'drengur Haraldsson',
                  'Eyþór Snær Tryggvason',
                  'Arnar Jóhannsson',
                  'Eyþór Traustason',
                  'Arnar Bjarni Arnarson',
                  'Þórhildur Þorleiksdóttir']))
# ['Arnar Bjarni Arnarson',
#  'Arnar Jóhannsson',
#  'Arnar Björn Pálsson',
#  'Eyþór Traustason',
#  'Eyþór Snær Tryggvason',
#  'Þórhildur Þorleiksdóttir',
#  'Þórir Jakob Olgeirsson']
# print(sort_names(['Markus Böhm',
#                   'María Bergþórsdóttir',
#                   'Shirley Lavy',
#                   'Hildur Guðnadóttir',
#                   'Nguyen Trinh',
#                   'Lára Sabido',
#                   'Mauro Pizzaia',
#                   'Sigríður Halldórsdóttir',
#                   'Artur Hemmerling',
#                   'Hjördís Rafnsdóttir',
#                   'Gunnar Björnsson',
#                   'Víkingur Hauksson',
#                   'Diego Gerevini',
#                   'Karen Hannesdóttir',
#                   'Harpa Hafliðadóttir',
#                   'Ragnar Stefánsson',
#                   'Marika Sagner',
#                   'Eugeniusz Madej',
#                   'Alina Jansone',
#                   'Guðrún Eiðsdóttir',
#                   'Andrzej Kulakowski',
#                   'Domantas Drungilas',
#                   'Einar Engelsen',
#                   'Gunnhildur Ómarsdóttir',
#                   'Herdís Gunnarsdóttir',
#                   'Birta Flókadóttir',
#                   'Halldór Ólafsson',
#                   'Jóhann Sigurbjörnsson',
#                   'Kai Johansen',
#                   'Agnar Sigurðarson',
#                   'Jóhanna Valdimarsdóttir',
#                   'Rut Ólafsdóttir',
#                   'Daníela Grétarsdóttir',
#                   'Alexandre Serheyuk',
#                   'Guðbjörn Haraldsson',
#                   'Ísabella Árnadóttir',
#                   'Magnús Norðdahl',
#                   'Kolbrún Gunnarsdóttir',
#                   'Helga Róbertsdóttir',
#                   'Örn Erlendsson',
#                   'Sandra Mieczkowska',
#                   'Brynja Ingólfsdóttir',
#                   'Kirsten Ertmann',
#                   'Berglind Gunnarsdóttir',
#                   'Arnas Mirauskas',
#                   'Roman Wasiewicz',
#                   'Rósar Snorrason',
#                   'Katla Bjarnadóttir',
#                   'Marcin Wójcik',
#                   'Guðmundur Hjaltalín',
#                   'Antonios Alexandridis',
#                   'Inga Karlsdóttir',
#                   'Peter Kovácik',
#                   'Sandra Bauze',
#                   'Ævar Austfjörð',
#                   'Steindór Bragason',
#                   'Atli Jósefsson',
#                   'Brynja Þórarinsdóttir',
#                   'Freyja Steindórsdóttir',
#                   'Kirsten Elborg',
#                   'Ásta Björnsdóttir',
#                   'Herborg Jóhannesdóttir',
#                   'Frida Callaghan',
#                   'Guðrún Gísladóttir',
#                   'Guðni Arason',
#                   'Heiðbjört Arnardóttir',
#                   'Giedre Rudzionyte',
#                   'Sverrir Magnússon',
#                   'Hörður Þorsteinsson',
#                   'Linda Stokkeland',
#                   'Kinga Dementiuk',
#                   'Jóhann Sörensson',
#                   'Linda Ingólfsdóttir',
#                   'Berglind Möller',
#                   'Brynja Þórarinsdóttir',
#                   'Orri Martinez',
#                   'Ariandra Punane',
#                   'Magnús Jóhannsson',
#                   'Bjarki Hreinsson',
#                   'Ingibjörg Árnadóttir',
#                   'Sigríður Árnadóttir',
#                   'Ögmundur Ólafsson',
#                   'Baldur Þorleifsson',
#                   'Margrét Adolfsdóttir',
#                   'Friðgeir Hjaltason',
#                   'Risto Laur',
#                   'Elísabet Guðmundsdóttir',
#                   'Ómar Ármannsson',
#                   'Sif Karlsdóttir',
#                   'Adele Spieser',
#                   'Ion Gavriloi',
#                   'Ögmundur Kristjánsson',
#                   'Ævar Árnason',
#                   'Kjartan Gunnsteinsson',
#                   'Sandra Kucyte',
#                   'Aníta Lórenzdóttir',
#                   'Rakel Guðmundsdóttir',
#                   'Rebekka Roberts',
#                   'Guðmundur Þórðarson',
#                   'Bryndís Arnarsdóttir',
#                   'Petrea Tómasdóttir',
#                   'Guðmundur Stefánsson',
#                   'Skúli Baldursson',
#                   'Anna Breiðfjörð',
#                   'Kristín Þórðardóttir',
#                   'Flóki Baldvinsson',
#                   'Egill Gylfason',
#                   'Arnar Jóhannsson',
#                   'Hafdís Einarsdóttir',
#                   'Daníel Richter',
#                   'Gísli Sigurjónsson',
#                   'Erla Ágústsdóttir',
#                   'Hrönn Sveinbjörnsdóttir',
#                   'Gunnhildur Einarsdóttir',
#                   'Ingvar Sigurpálsson',
#                   'Pavel Erokhin',
#                   'Örn Erlendsson',
#                   'Jóhanna Pálsdóttir',
#                   'Pawel Sawon',
#                   'Davíð Helgason',
#                   'Ævar Ármannsson',
#                   'Annette Bauder',
#                   'Guðmundur Óskarsson',
#                   'Rúnar Sverrisson',
#                   'Ingibjörg Valtýsdóttir',
#                   'Agnieszka Kosakowska',
#                   'Örlygur Sævarsson',
#                   'Marsibil Sigurðardóttir',
#                   'Hulda Arnórsdóttir',
#                   'Freyja Gunnarsdóttir',
#                   'Anna Magnúsdóttir',
#                   'Íris Stefánsdóttir',
#                   'Irina Petrovica',
#                   'Guðmundur Sigfússon',
#                   'Snorri Ómarsson',
#                   'Halldóra Jónsdóttir',
#                   'Linas Indriulis',
#                   'Sigurður Bjarnason',
#                   'Andri Harðarson',
#                   'Hreinn Halldórsson',
#                   'Björg Gunnarsdóttir',
#                   'Sif Egilsdóttir',
#                   'Aðalsteinn Sigurðsson',
#                   'Berglind Guðmundsdóttir',
#                   'Árni Grétarsson',
#                   'Þórhildur Þorleiksdóttir',
#                   'Ólafur Rögnvaldsson',
#                   'Regína Geirsdóttir',
#                   'Klara Hreggviðsdóttir',
#                   'Darri Valgarðsson',
#                   'Aleksejs Vasilenko',
#                   'Guðbrandur Sigurðsson',
#                   'Fabiola Prince',
#                   'Andrea Magnúsdóttir',
#                   'Friðrika Sigurðardóttir',
#                   'Malene Stilling',
#                   'Óðinn Arason',
#                   'Sophia Tadesse',
#                   'Sigurrós Júlíusdóttir',
#                   'Friðrik Guðmundsson',
#                   'Magdalina Erdoglija',
#                   'Ólöf Arnardóttir',
#                   'Móeiður Gunnlaugsdóttir',
#                   'Birgir Sigurðsson',
#                   'Ólafur Þórarinsson',
#                   'Erla Sigurmundsdóttir',
#                   'Atli Egilsson',
#                   'Bjarni Kjartansson',
#                   'Hafdís Daníelsdóttir',
#                   'Snorri Ragnarsson',
#                   'Sigríður Bergþórsdóttir',
#                   'Hlynur Stefánsson',
#                   'Ásbjörn Einarsson',
#                   'Ævar Bóasson',
#                   'Hanna Ragnarsdóttir',
#                   'Iaroslava Kutsai',
#                   'Hreiðar Geirsson',
#                   'Ólafur Bjarnason',
#                   'Erla Víglundsdóttir',
#                   'Jonas Jakutavicius',
#                   'Edda Pétursdóttir',
#                   'Malwina Luczaj',
#                   'Ævar Ákason',
#                   'Ævar Aðalsteinsson',
#                   'Kristinn Magnússon',
#                   'Sigurlaug Indriðadóttir',
#                   'Gísli Guðmundsson',
#                   'Auður Friðriksdóttir',
#                   'Piotr Bielawa',
#                   'Kjartan Sveinsson',
#                   'Ívar Markússon',
#                   'Anna Guðmundsdóttir',
#                   'Guðjón Þorkelsson',
#                   'Klemenz Sæmundsson',
#                   'Lárus Felixson',
#                   'Sarloté Sirvyté',
#                   'Brynjar Vilmundarson',
#                   'Christian Christensen',
#                   'Gunnar Andrésson',
#                   'Ágúst Guðmundsson',
#                   'Sigrún Gunnarsdóttir',
#                   'Konráð Beck',
#                   'Marek Durski',
#                   'Christine Weiss',
#                   'Guðmundur Pétursson',
#                   'Dóra Sigurðardóttir',
#                   'Ingibjörg Hauksdóttir',
#                   'Kristina Guobyte',
#                   'Sigríður Björnsdóttir',
#                   'Sigríður Gústafsdóttir',
#                   'Gréta Jóakimsdóttir',
#                   'Marian Slowik',
#                   'Þorleifur Finnsson',
#                   'Roberta Brambilla',
#                   'Þóra Kjartansdóttir',
#                   'Hildur Stefánsdóttir',
#                   'Haukur Þórðarson',
#                   'María Árnadóttir',
#                   'Hinrik Pálsson',
#                   'Kaan Bjarkarson',
#                   'Daði Guðvarðarson',
#                   'Sigurður Sigurðsson',
#                   'Margrét Pálsdóttir',
#                   'Guðrún Vilmundsdóttir',
#                   'Ingibjörg Guðmundsdóttir',
#                   'Hörður Torfason',
#                   'Hrund Hauksdóttir',
#                   'Ástrós Guðmundsdóttir',
#                   'Ævar Björnsson',
#                   'Ragnheiður Birgisdóttir',
#                   'Lára Indriðadóttir',
#                   'Helena Ólafsdóttir',
#                   'Arnór Ragnarsson',
#                   'Sigmar Sigurðsson',
#                   'Stefán Ríkharðsson',
#                   'Guðlaug Kristmundsdóttir',
#                   'Jónína Sigurðardóttir',
#                   'Ingvar Friðleifsson',
#                   'Guðbjörn Ragnarsson',
#                   'Sverrir Pálsson',
#                   'Henrik Jochumsen',
#                   'Rafal Botte',
#                   'Matthildur Steinbergsdóttir',
#                   'Ágústa Friðriksdóttir',
#                   'Kristjana Larsen',
#                   'Kristján Guðjónsson',
#                   'Alexander Kost',
#                   'Árdís Árnadóttir',
#                   'Snorri Henrysson',
#                   'Haukur Þórðarson',
#                   'Juste Cimermanaite',
#                   'Hildur Finnsdóttir',
#                   'Marinó Pálmason',
#                   'Radoslaw Zalewski',
#                   'Ólína Jónsdóttir',
#                   'Hlynur Haraldsson',
#                   'Harry Kjærnested',
#                   'Einar Gunnarsson',
#                   'Skjöldur Magnússon',
#                   'Örlygur Sveinsson',
#                   'Ögmundur Kristinsson',
#                   'Elín Hirst',
#                   'Eymundur Magnússon',
#                   'Guðmundur Guðmundsson',
#                   'Siriphrapa Ponkumthanadee',
#                   'Sigurbjörg Níelsdóttir',
#                   'Ástrós Elísdóttir',
#                   'Helga Ingibergsdóttir',
#                   'Rakel Einarsdóttir',
#                   'Nebojsa Schally',
#                   'Reynir Magnússon',
#                   'Andrius Kidykas',
#                   'Elfa Vilhjálmsdóttir',
#                   'Björgvin Gíslason',
#                   'Ragnheiður Hannesdóttir',
#                   'Elvar Laxdal',
#                   'Guðrún Þorsteinsdóttir',
#                   'Bryndís Bragadóttir',
#                   'Pétur Wiencke',
#                   'Aðalheiður Ólafsdóttir',
#                   'Axel Jóhannsson',
#                   'Eva Antonsdóttir',
#                   'Elín Ragnarsdóttir',
#                   'Orri Axelsson',
#                   'Vignir Sveinsson',
#                   'Elín Jakobsdóttir',
#                   'Hermann Árnason',
#                   'Fróði Rosatti',
#                   'Egle Skersyte',
#                   'Hagen Freund',
#                   'Sigþór Árnason',
#                   'Steinþór Torfason',
#                   'Artur Maszkiewicz',
#                   'Óðinn Benónýsson',
#                   'Magnús Gunnarsson',
#                   'Elísabet Grétarsdóttir',
#                   'Sigríður Sigurðardóttir',
#                   'Ragnar Ólafsson',
#                   'Sigtryggur Georgsson',
#                   'Stefán Jónasson',
#                   'Anton Birgisson',
#                   'Arinbjörn Israelsson',
#                   'Kári Örvarsson',
#                   'Hjalti Guðmundsson',
#                   'Einar Jónsson',
#                   'Hlynur Haraldsson',
#                   'Kristjana Sigurgeirsdóttir',
#                   'Rakel Sigurjónsdóttir',
#                   'Einar Hafliðason',
#                   'Ævar Aðalsteinsson',
#                   'Jeanette Midgley',
#                   'Gunnar Rúnarsson',
#                   'Bjarki Ólafsson',
#                   'Melani Vranjes',
#                   'Tumi Guðmundsson',
#                   'Kirsten Krause',
#                   'Elzbieta Szczepanska',
#                   'Jacek Krol',
#                   'Edda Ásgeirsdóttir',
#                   'Anton Pisano',
#                   'Bartosz Buksik',
#                   'Soffía Árnadóttir',
#                   'Þórey Önundardóttir',
#                   'Gestur Halldórsson',
#                   'Lena Mikaelsson',
#                   'Jostein Tveit',
#                   'Grzegorz Karczmarczyk',
#                   'Drífa Örvarsdóttir',
#                   'Kristinn Jóhannsson',
#                   'Ásdís Gunnarsdóttir',
#                   'Jóhanna Árnadóttir',
#                   'Sesselja Jónsdóttir',
#                   'Björg Ingadóttir',
#                   'Saga Steingrímsdóttir',
#                   'Katrín Ólafsdóttir',
#                   'Sigurbjörg Guðlaugsdóttir',
#                   'Hanna Ólafsdóttir',
#                   'Ingileif Arngrímsdóttir',
#                   'Dröfn Traustadóttir',
#                   'Skúli Einarsson',
#                   'Leonard Gaidukevic',
#                   'Leszek Dytman',
#                   'Sigurlína Helgadóttir',
#                   'Ómar Hannesson',
#                   'Ewelina Dziondziakowska',
#                   'Aníta Arnórsdóttir',
#                   'Juhui He',
#                   'Ögmundur Runólfsson',
#                   'Halldóra Guðmundsdóttir',
#                   'Jón Blöndal',
#                   'Hákon Sverrisson',
#                   'Jón Sigurðsson',
#                   'Karl Jónsson',
#                   'Ómar Daoud',
#                   'Lilja Cardew',
#                   'Guðmundur Árnason',
#                   'Orri Arnfinnsson',
#                   'Margrét Magnúsdóttir',
#                   'Darko Horvat',
#                   'Rakel Grímsdóttir',
#                   'Hálfdán Þórhallsson',
#                   'Sigríður Halldórsdóttir',
#                   'Eyjólfur Halldórsson',
#                   'Sigurður Guðmundsson',
#                   'Daði Ófeigsson',
#                   'Svava Svavarsdóttir',
#                   'Alessandra Lionello',
#                   'Stefán Bjarnason',
#                   'Bessi Grétarsson',
#                   'Guðjón Guðlaugsson',
#                   'Einir Einisson',
#                   'Oliwer Wasiulewski',
#                   'Karólína Gunnarsdóttir',
#                   'Hörður Adolphsson',
#                   'Ævar Adolfsson',
#                   'Hrönn Helgadóttir',
#                   'Julia Cuber',
#                   'Sigurbjörg Sigurðardóttir',
#                   'Eyþór Karlsson',
#                   'Sigurður Björnsson',
#                   'Danuté Varskeviciené',
#                   'Lisa Bueschelberger',
#                   'Ólafur Jónsson',
#                   'María Tómasdóttir',
#                   'Eyrún Magnúsdóttir',
#                   'Jóhann Guðjónsson',
#                   'Alexander Ágústsson',
#                   'Sigurður Jónsson',
#                   'drengur Haraldsson',
#                   'Júlía Aradóttir',
#                   'Ólafur Gíslason',
#                   'Dailis Valters',
#                   'Stefán Guðjónsson',
#                   'Ævar Ágústsson',
#                   'Hrund Kristinsdóttir',
#                   'Gabríela Andradóttir',
#                   'Atli Elvarsson',
#                   'Garðar Þorsteinsson',
#                   'Njörður Sigurðsson',
#                   'Ingibjörg Sigurvinsdóttir',
#                   'Petrína Konráðsdóttir',
#                   'Ingunn Lúðvíksdóttir',
#                   'Sigríður Sigurðardóttir',
#                   'Ragnar Kazunin',
#                   'Nanna Sigmarsdóttir',
#                   'Andries Bosma',
#                   'Erna Friðriksdóttir',
#                   'Ögmundur Magnússon',
#                   'Ögmundur Sigfússon',
#                   'Skúli Magnússon',
#                   'Friðþjófur Blöndal',
#                   'Sigrún Ólafsdóttir',
#                   'Páll Sveinsson',
#                   'Kristófer Andrason',
#                   'Axel Björnsson',
#                   'Ævar Arngrímsson',
#                   'Edvin Kristinsson',
#                   'Elvar Ásgeirsson',
#                   'Andri Guðmundsson',
#                   'Ögmundur Kristgeirsson',
#                   'Yu Qian',
#                   'Ingólfur Rúnarsson',
#                   'Barbara Paciejewska',
#                   'Kristín Ingvarsdóttir',
#                   'Hugi Karlsson',
#                   'Helgi Runólfsson',
#                   'Óli Ólafsson',
#                   'Stefán Jóhannsson',
#                   'Malene Erkmann',
#                   'Sigríður Jónsdóttir',
#                   'Marcos Ramirez',
#                   'Bjartur Hafþórsson',
#                   'Brynjar Bragason',
#                   'Guðný Óskarsdóttir',
#                   'Kristín Þórhallsdóttir',
#                   'Svanur Jóhannesson',
#                   'Einar Jónsson',
#                   'Davide Nasci',
#                   'Símon Símonarson',
#                   'Daníel Þórarinsson',
#                   'Eydís Kristinsdóttir',
#                   'Arnþór Hjaltason',
#                   'Jóhann Birgisson',
#                   'Krisana Phaithai',
#                   'Guðbjörg Ólafsdóttir',
#                   'Ágústa Þorbjörnsdóttir',
#                   'Ósk Guðmundsdóttir',
#                   'Donatas Andruska',
#                   'Skúli Arnarsson',
#                   'Páll Siggeirsson',
#                   'Daníel Ólafsson',
#                   'Guðrún Bjarnadóttir',
#                   'Sigrún Einarsdóttir',
#                   'Jacek Tulibacki',
#                   'Ingibjörg Óskarsdóttir',
#                   'Caroline Einarsson',
#                   'Kolbrún Einarsdóttir',
#                   'Eva Björnsdóttir',
#                   'Ragnheiður Haraldsdóttir',
#                   'Freyja Sveinsdóttir',
#                   'Arnheiður Ragnarsdóttir',
#                   'Gunnar Gunnarsson',
#                   'María Magnúsdóttir',
#                   'Margrét Harðardóttir',
#                   'Björg Ólafsdóttir',
#                   'Kristinn Halldórsson',
#                   'Elín Sæmundsdóttir',
#                   'Marta Birgisdóttir',
#                   'Laura Laakkonen',
#                   'Ævar Bjarnason',
#                   'Ragna Eiríksdóttir',
#                   'Bergþóra Helgadóttir',
#                   'Krystyna Tuttas',
#                   'Jófríður Tobíasdóttir',
#                   'Sigurbjörg Guðmundsdóttir',
#                   'Catarína Eriksson',
#                   'Kristel Harðardóttir',
#                   'Ingólfur Lúðvíksson',
#                   'Edda Hreinsdóttir',
#                   'Rimvydas Peciulis',
#                   'Ewa Czyzynska',
#                   'Pawel Milewski',
#                   'Sabina Lopuszynska',
#                   'Sigrún Þorsteinsdóttir',
#                   'Michal Zambrzycki',
#                   'Villy Adolfsson',
#                   'Embla Einarsdóttir',
#                   'Þorvaldur Hreinsson',
#                   'Arna Ingólfsdóttir',
#                   'Gerður Guðmundsdóttir',
#                   'Sigurdís Sveinbjörnsdóttir',
#                   'Ottó Schopka',
#                   'Júlíus Samúelsson',
#                   'Krystian Kulak',
#                   'Ævar Baldvinsson',
#                   'Igor Guzek',
#                   'Sigurdís Benónýsdóttir',
#                   'Ævar Breiðfjörð',
#                   'Erla Þorvaldsdóttir',
#                   'Raimondas Ruchanskis',
#                   'Halldór Jóhannsson',
#                   'Ævar Agnarsson',
#                   'Ragnhildur Sveinsdóttir',
#                   'Einar Ólafsson',
#                   'Viðar Einarsson',
#                   'Brjánn Birgisson',
#                   'Rebekka Víðisdóttir',
#                   'Örn Eriksen',
#                   'Davíð Björnsson',
#                   'Aneta Duk',
#                   'Ævar Buthmann',
#                   'Guðrún Eggertsdóttir',
#                   'Örlygur Viðarsson',
#                   'Aðalsteinn Vestmann',
#                   'Stefanía Guðbergsdóttir',
#                   'Kjartan Björnsson',
#                   'Hrafnhildur Hauksdóttir',
#                   'Ólöf Þorsteinsdóttir',
#                   'Halina Kravtchouk',
#                   'Orri Arnarsson',
#                   'Krzysztof Wrobel',
#                   'Ingólfur Björnsson',
#                   'Björn Þórðarson',
#                   'Hildur Aðalsteinsdóttir',
#                   'Ingvar Sigurðsson',
#                   'Kristinn Guðmundsson',
#                   'Katrín Sigmundsdóttir',
#                   'Elva Gunnlaugsdóttir',
#                   'Ásgeir Magnússon',
#                   'Magnea Sigurbergsdóttir',
#                   'Haraldur Haraldsson',
#                   'Brynja Skúladóttir',
#                   'Stefanía Ómarsdóttir',
#                   'Katrín Bjarnadóttir',
#                   'Tristan Alexandersson',
#                   'Valtýr Pálsson',
#                   'Guðrún Zoega',
#                   'Áslaug Traustadóttir',
#                   'Sigurberg Guðbrandsson',
#                   'Hallgrímur Hinriksson',
#                   'Maríus Sævarsson',
#                   'Gerald Mueller',
#                   'Ögmundur Kristinsson',
#                   'Eyþór Traustason',
#                   'Jakub Malesa',
#                   'Marianne Ellingsen',
#                   'Edda Eðvaldsdóttir',
#                   'Flosi Ómarsson',
#                   'Aðalheiður Bjarnadóttir',
#                   'Marcel Janejka',
#                   'Kristján Gunnarsson',
#                   'Stefán Kristjánsson',
#                   'Patrick Arguin',
#                   'Kolbrún Aradóttir',
#                   'Kári Eiríksson',
#                   'Arnheiður Pálsdóttir',
#                   'Ingrid Karlsdóttir',
#                   'Erla Jónatansdóttir',
#                   'Sigurbirna Guðjónsdóttir',
#                   'Ingvar Kristinsson',
#                   'Dzintars Suhanovs']))
