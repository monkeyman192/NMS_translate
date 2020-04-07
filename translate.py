from itertools import accumulate
import json


CONST = 0x5A76F899
TINYVAL = 2.3283064370807974e-10

# Gek: 'traders'
# Vy'keen: 'warriors'
# Korvax: 'explorers'
RACES = {'traders': 0, 'warriors': 1, 'explorers': 2, 'robots': 3,
         'atlas': 4, 'diplomats': 5, 'exotics': 6, 'none': 7}
LANG_MAPPING = [2, 4, 3, 0, 0, 7, 0, 0]  # dword_141AAF408
VOWELS = ('a', 'e', 'i', 'o', 'u')

STRINGS = {
    0: ('aabaacaadaahaaiaakaalaanaapaaraasaauaavaayabaabbabcabdabeabhabiabjabk'
        'ablabnaboabrabsabtabuabwabyacaaccacdaceacgachaciackaclacmacnacoacpacq'
        'acractacuacvaczadaadbadcaddadeadfadgadhadiadjadkadladmadnadoadradsadu'
        'advadwadyadzaeaaebaecaedaegaehaelaemaenaeoaepaeqaeraesaetaeuaevaexaez'
        'afaafdafeaffafiafkaflafnafoafqafrafsaftafuafyagaagcagdageaggaghagiagk'
        'aglagmagnagoagpagragsaguagwagyahaahcahdaheahgahiahkahlahmahnahoahpahr'
        'ahtahuaiaaibaicaidaifaigaihaijaikailaimainaioaipairaisaitaiuaivaiwaiy'
        'aizajaajbajdajeajgajhajiajjajnajoajrajsajuakaakbakeakhakiakkaklakmakn'
        'akoakpakraksaktakuakvakwakyalaalbalcaldalealfalgalhalialjalkallalmaln'
        'aloalpalralsaltalualvalwalyalzamaambamcameamfamgamhamiamjamkammamnamo'
        'ampamqamramsamtamuamwamyamzanaanbancandaneanfanganhanianjankanlanmann'
        'anoanpanqanransantanuanvanwanyanzaoaaobaocaodaofaogaohaoiaokaolaonaop'
        'aoraosaotaouaovaowaoxapaapeapgaphapiaplapmapoappaprapsaptapuaqcaqiaqu'
        'araarbarcardarearfargarhariarjarkarlarmarnaroarparqarrarsartaruarvarw'
        'arxaryarzasaasbascasdaseasgashasiaskaslasmasoaspasqasrassastasuasvasw'
        'asyaszataatcateatfathatiatjatkatlatmatnatoatratsattatuatvatwatyatzaua'
        'aubaucaudaueaufaugauhauiaujaukaulaumaunauoaupaurausautauvauwauxauzava'
        'avdaveavgaviavlavnavoavravsavuavyawaawcaweawfawhawiawkawlawnawoawraws'
        'awuawyaxaaxbaxeaxiaxoaxtaxwayaaybaycaydayeaygayhayiaykaylaymaynayoayr'
        'aysaytayuaywayyazaazdazeazhaziazkaznazoazqazraztazuazyazzbaababbacbad'
        'baebafbagbahbaibajbakbalbambanbapbaqbarbasbatbaubavbawbaxbaybazbbabbe'
        'bbibblbbobbybcabcobdebdibdjbdubeabecbedbeebefbegbehbeibejbekbelbemben'
        'beobepberbesbetbeubevbeybezbgebhabhibhnbhobhrbhubiabibbicbidbiebifbig'
        'bihbijbikbilbinbiobipbirbisbitbiubivbiwbixbiybizbjabjibjobkabkebkhbko'
        'blableblibloblublybmcbmibnebnibnoboabobbocbodboebofbogbohboibojbokbol'
        'bombonboobopboqborbosbotboubovbowboybozbrabrebribrobrubrybrzbscbshbsi'
        'bsobstbtabtebthbtrbuabubbucbudbuebufbugbuhbuibujbukbulbumbunbuoburbus'
        'butbuwbuybuzbwabwebwgbwibyabybbydbyebyfbygbykbylbyobyrbysbytbyubywbzh'
        'cabcaccadcaecafcagcahcaicajcakcalcamcancapcarcascatcaucavcawcaycbrcca'
        'ccecchccicclccoccrccucdacdecdicdoceacebceccedceecegcehceicelcemcenceo'
        'cepcercescetceucevcewceycezcgicgrchachbchcchechhchichkchlchmchnchochr'
        'chschtchuchvchwchyciacibciccidciecifcigcihcijcikcilcimcinciocipcircis'
        'citciucivcixcizcjackackcckeckfckhckickjcklckmckockpckrckscktckvckwcky'
        'clacleclicllcloclucmacmicmocmucnacnecnicnocoacobcoccodcoecofcogcohcok'
        'colcomconcoocopcoqcorcoscotcoucovcowcoxcoycozcphcqucracrecricrocrucry'
        'csacsecshcslcsocssctactecthctictlctoctrctucuacubcuccudcuecufcugcuicul'
        'cumcuncupcurcuscutcuvcuycuzcvacvicyacybcyccydcygcylcyncyocyrcytczacze'
        'czkczydaadabdacdaddaedafdagdahdaidajdakdaldamdandaodapdaqdardasdatdau'
        'davdawdaydazdbadbedbhdbidbldbodbrdbudcadcedcldcoddaddeddhddiddodduddy'
        'deadebdecdeddeedefdegdehdeidejdekdeldemdendeodepderdesdetdeudevdewdex'
        'deydezdfidfodfrdgadgcdgedgkdgldgodgrdgsdgudhadhbdhedhidhjdhmdhndhodhr'
        'dhudhydiadibdicdiddiedifdigdihdiidijdikdildimdindiodipdirdisditdiudiv'
        'diwdixdiydizdjadjedjidjodjudkedkidkudladledlidlodludmadmedmidmodmudmy'
        'dnedngdnidnodnydoadobdocdoddoedogdohdoidokdoldomdondoodopdoqdordosdot'
        'doudovdowdoxdoydozdpadpedpodqudradredridrldrodrudrydrzdsadscdsedshdsk'
        'dsldsodspdssdstdtedtiduadubducduddufdugduidukduldumdundupduqdurdusdut'
        'duuduvduwduxdvadvedvidvodwadwedwidwodwrdwydxudyadybdycdyedygdyidyldym'
        'dyndyodypdyrdysdytdywdzadzedzhdzidzldzodzueabeaceadeaeeafeageajeakeal'
        'eameaneapeareaseateaueaveawebaebbebdebeebiebkebleboebrebsebtebuebyeca'
        'ecceceechecieckeclecoecqecrectecuecvecyedaedbeddedeedfedgedhediedjedk'
        'edledmednedoedpedqedredseduedvedwedyedzeebeeceedeefeegeeheekeeleemeen'
        'eepeereeseeteeueeveeyefaefeeffefiefjeflefnefoefrefsefuegaegbegeegfegg'
        'eghegieglegmegnegoegreguehaehbehdeheehiehlehnehoehpehrehsehtehuehweia'
        'eibeiceideieeigeijeikeileimeineioeipeireiseiteiveiweizejaejbejeejiejj'
        'ejkejlejoejtekaekcekdekeekfekhekiekkeklekmekoekpekreksektekuekwelaelb'
        'elceldeleelfelgelhelieljelkellelmelneloelpelrelselteluelvelwelyelzema'
        'embemcemeemgemhemiemkemlemmemnemoempemsemtemuemwemyenaenbencendeneenf'
        'engenhenienjenkenlenmennenoenpenqenrensentenuenvenwenyenzeobeoceodeof'
        'eogeoieokeoleomeoneopeoreoseoteoweozepaepcepeephepiepkeplepoeppepreps'
        'eptepyeqcequeraerbercerdereerfergerherierjerkerlermerneroerperqerrers'
        'erteruerverwerxeryerzesaesbescesdeseesgeshesieskeslesmesnesoespesqesr'
        'essestesuesvesweszetaetceteetfethetietjetketletmetnetoetretsettetuety'
        'etzeubeuceudeufeugeuheujeukeuleumeuneupeureuseuteuveuweuxevaevcevdeve'
        'evievlevnevoevrevsewaewbewcewdeweewfewgewhewiewkewlewmewnewoewpewsewt'
        'ewuewwewyexaexbexcexeexgexhexiexkexlexoexpexrextexveyaeybeyceydeyeeyf'
        'eyheykeyleymeyneyreyueyweyzezaezcezdezeezgezheziezkezmeznezoeztezuezv'
        'fabfacfadfaefaffagfaifajfalfamfanfarfasfatfaufavfawfaxfayfbefbofdefdi'
        'feafedfehfeifelfemfenfeoferfesfetfeufeyffaffeffifflffmffnffoffrfftffu'
        'fgrfhafhefhlfiafibficfidfiefiffigfilfimfinfiofirfisfitfiufjafjofkafla'
        'fleflhfliflofluflyfmafmefnafnefnhfnifnofoafodfoefogfokfolfomfonfoofor'
        'fosfotfoufowfozfqufrafrefrifrofryfscfskfssfstftefthftoftrfuafucfuefug'
        'fujfukfulfunfupfurfusfutfvefydgaagabgacgadgaegafgaggahgaigajgakgalgam'
        'gangaogapgargasgatgaugavgawgaygazgbagbegbigbogchgcigcogcrgcugdagdegdh'
        'gdigdogdrgdugeagebgecgedgeegefgehgeigekgelgemgengeogergesgetgeugevgew'
        'geygezgfegfogfrggaggdggeggigglggoggsgguggvghaghbgheghighlghmghnghoghr'
        'ghsghtghughvgiagibgicgidgiegiggihgikgilgimgingiogipgirgisgitgiugiygja'
        'gjegkagkhgkigkogkuglaglegligloglugmagmegmignagnegnggnignognugnygoagob'
        'gocgodgoegofgoggohgoigokgolgomgongoogopgorgosgotgougovgowgoygpagpegph'
        'gpugqigqugqvgragrbgregrigrlgrogrugrygrzgsagsbgscgsdgshgskgsmgsogstgsu'
        'gswgtegthgtigtoguagubgucgudguegugguigulgumgunguogupgurgusgutguuguvguy'
        'gvagvigwagwegwigwrgwugwygxigyagybgyegyhgylgyngypgyrgytgyvgzhhaahabhac'
        'hadhaehafhaghahhaihajhakhalhamhanhaohaphaqharhashathauhavhawhaxhayhaz'
        'hbahbehbihbohbrhbuhcahchhcrhdahdehdihdoheahebhechedheehefheghehheihek'
        'helhemhenheohepherheshetheuhevhewheyhezhfuhgehgnhgrhgwhhahhohiahibhic'
        'hidhiehifhighihhiihijhikhilhimhinhiohiphiqhirhishithiuhivhiwhixhiyhiz'
        'hjahjehkahkihklhkohkwhkyhlahldhlehlfhlghlihlohlqhlshlthluhlyhmahmehmi'
        'hmohmshmuhnahnehnhhnihnkhnohnphnshnuhoahobhochodhoehofhoghohhojhokhol'
        'homhonhoohophorhoshothouhovhowhoxhoyhozhpahpehpohpuhrahrdhrehrihrlhrm'
        'hrohrshruhryhsahsehsfhshhsihsuhtahtehthhtihtlhtohtrhtuhuahubhuchudhue'
        'hughuhhuihujhukhulhumhunhuohuphuqhurhushuthuuhuvhuxhuyhuzhvahvehvihwa'
        'hwehwihwohyahybhydhyehyghyihylhymhynhyphyrhyuiabiaciadiaeiagiahiajiak'
        'ialiamianiaoiapiariasiatiauiaviawiayiazibaibbibeibhibiiblibniboibribs'
        'ibtibuibwibyicaicciceichiciicjickiclicnicoicricsicticuiczidaiddideidg'
        'idhidiidjidkidlidmidnidoidpidridsiduidwidziebieciediegiehiekieliemien'
        'ieoieriesietieviewifaifeiffifiifjiflifnifoifriftifuigaigbigdigeiggigh'
        'igiigligmignigoigpigrigsiguigwigyihaiheihiihlihoihtihuiigiijiiniitiiw'
        'ijaijbijcijeijfijiijkijlijoijrijsijuikaikbikdikeikgikhikiikkiklikmikn'
        'ikoikpiksiktikuikwilailbilcildileilfilgilhiliiljilkillilmilniloilpilr'
        'ilsiltiluilvilwilyimaimbimdimeimfimhimiimlimmimnimoimpimrimsimtimuimv'
        'imwimyinainbincindineinfinginhiniinjinkinlinminninoinqinrinsintinuinv'
        'inyinziobiociodiogiohiojioliomioniopioriosiotiouioviowipaipcipeipgiph'
        'ipiiplipnipoippipsiptipuipyiqbiqiiquirairbircirdireirfirgirhiriirjirk'
        'irlirmirniroirpirrirsirtiruirvirwiryirzisaisbiscisdiseisgishisiiskisl'
        'ismisnisoispisqisrissistisuiswisyiszitaitbitcitditeitfithitiitjitkitl'
        'itnitoitritsittituitvitwitxityitziubiuciudiugiuhiukiumiuniuoiuriusiut'
        'iuxiuyiuzivaiveivgiviivjivkivoivrivsivuivyiwaiweiwniwoiwuixbixcixeixi'
        'ixkixoixtiyaiyeiyoiyuiyyizaizcizdizeizgizhiziizmizoizrizsizuizvizyizz'
        'jaajabjacjadjaejafjagjahjaijajjakjaljamjanjaojapjaqjarjasjatjaujavjaw'
        'jayjazjbajbujchjckjdajdejdujeajedjefjeijekjeljemjenjepjerjesjetjeujev'
        'jewjeyjgojhajhijhwjiajibjicjidjiejigjihjikjiljimjinjipjirjisjitjiujiv'
        'jiwjjajjujkbjkijkmjksjlajlejmajmijoajobjodjoejofjogjohjoijojjokjoljon'
        'jopjorjosjotjoujovjowjrajscjsejsijstjtojuajubjucjudjuejugjuhjuijukjul'
        'jumjunjupjurjusjutjuvjuwjyvkaakabkackadkaekafkagkahkaikajkakkalkamkan'
        'kaokapkaqkarkaskatkaukavkawkaxkaykazkbakbekbrkbukcakchkdekeakebkedkee'
        'kefkegkehkeikekkelkemkenkepkerkesketkevkewkeykezkfokfukgakhakhbkhekhi'
        'khmkhnkhokhrkhukhvkhwkiakibkickidkiekifkigkihkijkikkilkimkinkiokipkir'
        'kiskitkiukivkiykizkjakjekkakkekkikkjkklkkokkuklakleklhkliklokluklykma'
        'kmbkmekmikmokmukmyknaknekngkniknoknuknykoakobkockodkoekofkogkohkoikoj'
        'kokkolkomkonkookopkorkoskotkoukovkowkoykozkpakpekplkpokrakrekrikrokru'
        'krykrzksakscksekshksiksmksnksokstksvksyktaktekthktiktoktrktsktzkuakub'
        'kuckudkuekufkugkuhkuikujkukkulkumkunkuokupkurkuskutkuukuwkuxkuykvakve'
        'kvikvokwakwekwikwokwrkwukyakyckyekyhkylkyokypkyrkytkyulaalablacladlae'
        'laflaglahlailajlaklallamlanlaolaplarlaslatlaulavlawlaylazlbalbelbilbo'
        'lbrlbulcalcelchlcilcolculcylczldaldbldcldeldhldildlldmldoldrldslduldw'
        'ldylealeblecledleelefleglehleilejleklellemlenleoleplerlesletleulevlew'
        'lexleylezlfalfblfelfflfhlfilfnlfolfrlfslftlfulfvlgalgelghlgilgolgrlgu'
        'lhalhelhilholhulhylialibliclidlielifliglihliilijliklillimlinliolipliq'
        'lirlislitliulivliwlixliylizljaljeljiljulkalkelkhlkilkllkmlknlkolkulky'
        'llallcllellfllhllillkllmllnllollpllrllullvllwllylmalmelmhlmilmolmqlmu'
        'lnalnelnglnilnjlnolnyloalobloclodloelofloglohloiloklollomlonlooloploq'
        'lorloslotloulovlowloxloylozlpalpblpelphlpilpolprlptlpulqvlralrilrolru'
        'lsalsblsclselshlsilsklsllsolsplsrlstlsulswlszltaltbltdlteltglthltiltj'
        'ltmltoltrltsltultyltzlualublucludlueluflugluhluiluklullumlunluplurlus'
        'lutluuluvluwluyluzlvalvelvilvmlvrlvslwalwelwhlwilwolwulwylyalyblyclyd'
        'lyelyglyhlyilyklyllymlynlyolyplyrlyslytlyulyxlzalzblzelzolzumaamabmac'
        'madmaemafmagmahmaimajmakmalmammanmaomapmaqmarmasmatmaumavmawmaxmaymaz'
        'mbambdmbembhmbimbkmblmbombrmbumbwmcamcbmccmcdmcemchmcimckmclmcmmcnmco'
        'mcqmdameamebmecmedmeemegmehmeimejmelmemmenmeomepmeqmermesmetmeumexmey'
        'mezmfamfimfomgamglmgrmhemhimhomiamibmicmidmiemifmigmihmijmikmilmimmin'
        'miomipmiqmirmismitmiumiwmiymizmjemjomkhmkimkymlemlimllmlymmammemmimmo'
        'mmsmnamncmnemnimnomnumoamobmocmodmoemofmogmohmoimojmokmolmommonmoomop'
        'mormosmotmoumovmowmoxmoymozmpampbmpdmpempfmphmpimpkmplmpomppmprmpsmpt'
        'mpumpzmqumramrimrkmsamsbmsdmsemshmsimskmsomstmsumsvmtamtimtsmtumuamuc'
        'mudmuemufmugmuhmukmulmummunmuomurmusmutmuxmuymuzmvamvemvumwamwemwomya'
        'mycmydmyemyhmylmymmyomypmyrmysmytmyvmyxmzamzenaanabnacnadnaenafnagnah'
        'nainajnaknalnamnannapnaqnarnasnatnaunavnawnaxnaynbanbenbinblnbonbrnbu'
        'ncancenchncincknclnconcrnctncunczndandbndcndendgndhndindjndlndmndnndo'
        'ndpndqndrndsndtndundvndwndyndzneanebnecnedneenefnegnehneinejneknelnem'
        'nennepneqnernesnetneunevnewnexneyneznfanfenfinfonfrnfungangbngcngdnge'
        'ngfnggnghngingjngknglngmngnngongpngqngrngsngtngungvngwngxngyngznhanhe'
        'nhinhonhunianibnicnidnienifnignihniinijniknilnimninnionipniqnirnisnit'
        'niunivniwnixniyniznjanjenjhnjinjmnjonjunkankenkhnkinkknklnkonksnktnku'
        'nkwnlanlenlinlonltnlunmanmenminmunmynnannbnncnndnnenngnnhnninnlnnonns'
        'nnunnwnnynoanobnocnodnoenofnognohnoinojnoknolnomnonnoonopnoqnornosnot'
        'nounovnownoznpanpenphnponqanqonqunranrenrinronrunsansbnscnsdnsensfnsh'
        'nsinsknslnsmnsonsrnssnstnsunsvnsynszntantentgnthntintjntlntmntontpntr'
        'ntsntuntwntxntyntznuanubnucnuenufnugnuinujnuknulnumnunnupnurnusnutnuv'
        'nuwnuxnvanvenvinvonwanwenwinyanybnycnydnyenyinyknylnymnyonysnytnyunza'
        'nzenzhnzinzonzyoaboahoakoaloamoanoaroasoatoavobaobbobeobgobhobiobjobk'
        'oblobmoboobrobsobuobzocaoccoceochociockoclocmocnocoocrocsoctocuocyocz'
        'odaoddodeodfodgodhodiodmodnodoodroduodvodwodyodzoeboecoedoefoegoehoei'
        'oeloemoenoepoeroesoetoevoewofaofeoffofgofhofiofnofoofrofsoftogaogdoge'
        'oggoghogioglogmognogoogrogsogtoguogyohaoheohiohjohkohlohmohnohoohroht'
        'ohuoiaoiboicoidoikoiloimoinoiroisoitoiwojaojeojiojoojuokaokeokhokiokk'
        'okloknokookpokroksoktokuokwokyolaolbolcoldoleolfolgolholioljolkollolm'
        'olnoloolpolsoltoluolvolwolyolzomaombomcomeomfomgomiommomoompomsomtomu'
        'omyonaonboncondoneongonhonionjonkonlonmonnonoonponronsontonuonvonwony'
        'onzooboocoodoogoohooioojookooloomoonoopooroosootoovooyopaopdopeopfoph'
        'opiopkoplopmopooppoproptopuopwoqooquoraorborcordoreorforgoriorjorkorl'
        'ormornoroorporrorsortoruorvorworyorzosaosboscoseosgoshosioskoslosmosn'
        'osoosposrossostosuoswosyoszotaotbotcoteothotiotjotkotlotnotootrotsott'
        'otuotwotyotzouaouboucoudoueougouhouioujoukouloumounoupourousoutouvouw'
        'ouxouyouzovaoveovgoviovlovnovoovsovyowaowdoweowfowiowlownowpowrowsowt'
        'owvoxaoxeoxioxloxooxtoxuoyaoydoyeoyioyloynoyooysoyuozaozeozhoziozlozm'
        'ozooztpaapacpadpaepafpagpahpaipajpakpalpampanpaopapparpaspatpaupavpaw'
        'paxpaypazpbapbepchpdepdopeapecpedpeepegpehpeipejpekpelpempenpeppeqper'
        'pespetpewpeypezpfepfipgapgephaphephiphmphnphophrphtphuphypiapibpicpid'
        'piepigpihpijpikpilpimpinpiopippirpispitpiupivpiypkapkepkiplaplepliplo'
        'plupmapnepnipoapobpocpodpoepofpogpohpoipokpolpomponpoopoppoqporpospot'
        'poupovpowpoypozppappepphppipplppoppspraprepriproprtprupryprzpsapscpsh'
        'psipsopstpsupswpsyptaptepthptiptoptrpuapucpudpuepugpuipukpulpumpunpup'
        'purpusputpwipwypyapyepylpyrpytpyxpziqahqamqanqarqawqbaqchqeqqerqetqia'
        'qibqinqioqolqomquaqubqucqudquequiquoquqqurqusqutquuquvquyqviraarabrac'
        'radraerafragrahrairajrakralramranraoraprarrasratrauravrawraxrayrazrba'
        'rberbirborbrrburbyrcarcerchrcirckrclrcorctrcurcyrdarderdgrdhrdirdlrdm'
        'rdnrdordrrdsrdtrdurdwrdzrearebrecredreerefregreirejrekrelremrenreorep'
        'reqrerresretreurevrewrexreyrezrfarferffrfirfjrforfsrgargerghrgirgnrgo'
        'rgrrgsrgurgyrharherhirhorhurhyriaribricridrierifrigrihrijrikrilrimrin'
        'rioripriqrisritriurivriwrixriyrizrjarjorjurkarkerkhrkirklrkorkprkrrks'
        'rktrkurkvrkwrlarldrlerlirlmrlorlsrltrlurlyrmarmbrmermgrmirmormsrmurmy'
        'rnarnbrndrnernfrngrnhrnirnjrnkrnornsrntrnurnwrnyroarobrocrodroerofrog'
        'rohroirojrokrolromronrooroprorrosrotrourovrowroxroyrozrparperphrpirpo'
        'rpsrpurqurrarrerrfrrhrrirrorrurryrsarscrsdrsersfrshrsirskrsmrsorssrst'
        'rsursyrszrtartbrtcrtdrtertfrthrtirtjrtlrtmrtnrtortrrtsrturtvrtwrtyrtz'
        'ruarubrucrudruerugruhruirujrukrulrumrunruoruprurrusrutruvruwruxruyruz'
        'rvarvervirvorwarwerwirworxirxvryarybrycrydryeryfrygryhryirykrylrymryn'
        'ryorypryrrysrytryurywrzarzerzfrzhrzirzorzsrzusaasabsacsadsaesafsagsah'
        'saisaksalsamsansaosapsarsassatsausavsawsaxsaysazsbasbesbosbrsbuscasce'
        'schscisclscoscrscsscuscysdasdesdisdoseasebsecsedseesefsegsehseisejsek'
        'selsemsenseosepseqsersessetseusevsewseysfesfisfosgasgrsgushashbshcshd'
        'sheshishjshkshmshnshoshpshrshsshtshushvshwsiasibsicsidsiesifsigsiksil'
        'simsinsiosipsirsissitsiusivsiwsiysizskaskeskhskiskjsklskoskrskuskvsky'
        'slasleslislosluslysmasmesmismjsmosmusmysnasnesnisnjsnosnysoasobsocsod'
        'soesofsogsohsoksolsomsonsoosopsorsossotsousovsowsoyspaspesphspisplspo'
        'sprspusqusrasrbsresrisrnsrosrussassbsscssessfsshssissksslssmssossussw'
        'ssysszstastcstesthstistjstkstlstmstnstostpstrstsstustvstwstysuasubsuc'
        'sudsuesufsugsuhsuisuksulsumsunsuosupsursussutsuvsuysuzsvasvesvisvoswa'
        'sweswhswiswoswrsyasycsydsyesylsymsynsyosypsyrsytsyuszaszcszesziszkszm'
        'sznszoszpszrsztszuszvtaatabtactadtaetaftagtahtaitajtaktaltamtantaotap'
        'tartastattautavtawtaxtaytaztbetbutcatchtcltcotcutdatdoteatebtectedtee'
        'teftegtehteitejtekteltemtenteoteptertestetteutevtewtexteyteztfetfitfo'
        'tgatgethathbthethfthgthhthithkthlthmthnthothpthrthsthuthwthytiatibtic'
        'tidtietiftigtihtiitijtiktiltimtintiotiptiqtirtistittiutivtiwtixtiytja'
        'tjetjitjmtjotjutketkhtkitkotkutkwtlatletlhtlitlotlytmatmetmitmutnatne'
        'tnitnotnytoatobtoctodtoftogtohtojtoktoltomtontootoptortostottoutovtow'
        'toxtoytpatphtpotputratretritrotrutrytrztsatsbtsctsdtsetsftshtsitsktsl'
        'tsotsutswtsyttattettgtthttittkttlttmttnttottrttsttuttvtuatubtuctudtue'
        'tuftugtuitujtuktultumtuntuotupturtustuttuvtvatvetvitwatwetwhtwitwotwr'
        'txatxstyatyctyetyktyltyntyptyrtystyutzatzetzitzktzmtzntzotzstzutzwtzy'
        'uaauacuaduaeuaguahuaiuajuakualuamuanuaouapuaquaruasuatuavuayubaubbubc'
        'ubeubhubiubluboubrubuubyucauccuceuchuciuckuclucoucpucrucuuczudauddude'
        'udgudhudiudjudmudnudoudrudsudtuduudwudyudzuebuecuedueeuefueguekueluem'
        'uenuepueruesuetuevuewueyufaufeuffufmufoufrufuugaugbugdugeuggughugiugl'
        'ugnugougpugrugtuguuhauhcuheuhjuhluhmuhnuhouhruhtuhyuiauibuicuiduijuik'
        'uiluimuinuipuiquiruisuituivuiwuixuiyujaujeujiujjujmujoujuukaukbukcuke'
        'ukhukiukkuklukmuknukoukpukruksuktukuukyulaulbulculduleulfulgulhuliulk'
        'ullulmulnuloulpulrulsultuluulvulwulyumaumbumcumeumiumkumlummumnumoump'
        'umtumuumvunaunbuncunduneunfungunhuniunjunkunlunmunnunounrunsuntunuunw'
        'unyunzuoauoduoiuojuokuoluomuonuopuorupaupeuphupiupkupouppuprupsuptupu'
        'uquuraurburcurdureurgurhuriurkurlurmurnurourpurrursurturuurvuryurzusa'
        'usbuscusduseusgushusiuskuslusmusnusouspusrussustusuusvuszutautcuteutg'
        'uthutiutjutkutlutmutnutoutputrutsuttutuutyutzuuauuguujuukuuluunuuruut'
        'uvauveuviuvuuwauweuwiuwouwuuxauxeuxfuxiuxluyauyduyeuyguyluynuyouyruyt'
        'uyuuzauzbuzcuzeuzguzhuzouzuuzwvaavabvacvadvaevafvagvahvaivajvakvalvam'
        'vanvapvarvasvatvauvavvaxvayvazvchvdevdoveavebvedveevegveivejvelvemven'
        'veqvervesvetvevveyvezvgavgovguviavibvicvidvievigvihvijvikvilvimvinvio'
        'virvisvitviuvivvizvlavlevlivlovltvlyvmovnivocvodvogvoivolvonvoovorvos'
        'votvouvravrevrivrovryvsjvskvstvszvubvucvuivukvulvumvunvyavyevyovyrvys'
        'waawabwacwadwaewafwagwahwaiwakwalwamwanwaowapwarwaswatwauwavwawwaxway'
        'wazwbewbuwcewchwcowdawdrweawebwecwedweewegweiwekwelwemwenwepwerweswet'
        'weywezwfewfowgcwguwhawhewhiwhowhuwhywiawibwicwidwiewifwigwiiwijwikwil'
        'winwiowirwiswitwixwiywkewkiwlawlewliwlowmawmewmownbwncwnewngwnownswob'
        'wodwoewogwohwoiwolwomwonwooworwoswotwouwoywpewrawrewriwruwshwskwsowto'
        'wuawudwuiwulwunwuowurwutwvewwewyawydwyewylwynwyrxacxagxakxalxamxanxav'
        'xawxbaxbexblxcaxcexchxcrxedxejxelxenxepxerxesxetxevxeyxfoxgixgrxhoxhu'
        'xiaxibxicxidxigxihxilximxinxioxirxisxixxkaxkexkoxlaxlexmuxolxosxovxpa'
        'xphxpixraxroxsaxtaxtextoxtrxuaxucxuexuixvexweyaayacyadyaeyagyahyaiyaj'
        'yakyalyamyanyapyaqyaryasyatyauyavyawyaxyayyazybaybdybeybiyblyboybrybu'
        'ycayceychyciycnycoycrycuydayddydeydiydoydpydryduyeayebyecyegyehyeiyek'
        'yelyemyenyeoyeqyeryesyetyeuyevyfeyfiyfoygaygeyggygiygnygoygryguyhayhe'
        'yhlyhuyhyyicyieyijyikyilyimyinyizykeykiyklykoykrykuykyylayldyleylgyli'
        'ylkyllyloylsyluylvylyymaymbymeymiymnymoympymrymuymyynayncyndyneyngynh'
        'yniynkynlynmynnynoynsyntynuynyyoeyoiyokyolyomyonyooyopyoqyoryosyotyou'
        'yovypaypeyphypiypoyprypsyptypuyrayrbyreyrfyrhyriyrjyrmyrnyroyrryrsyru'
        'ysayseyshysiyskysnysoyssystysuyszytayteythytiytoytrytuyuayucyudyueyug'
        'yuiyujyukyulyumyunyupyuqyuryusyutyuwyuyyuzyvayveyviyvoywayweywiywoywr'
        'yxeyxiyyayzhzaazabzaczadzaezagzahzajzakzalzamzanzaozapzarzaszatzauzav'
        'zawzbezcazczzdazdizdozeazebzeczeezefzegzeizelzemzenzepzerzeszetzeuzew'
        'zexzeyzezzfezgazhazhbzhdzhezhizhkzhnzhozhuziazibzicziezigzihzikzilzim'
        'zinzioziszitziuzivziyzkozlazlozmazmezmizmyznaznezniznyzoazoczoezoizol'
        'zomzonzoozoqzorzoszotzouzovzoyzpizquzrazrozsazsczspztaztiztlztozubzuc'
        'zudzugzuhzukzulzumzunzupzurzutzuyzvazvezvizvozwazwezwizyazybzylzynzys'
        'zzazzi'),
    1: ('aadaafaakaaraataauabaabdabeabhabiaboabrabsabuabwabyabzacaaccacdaceacf'
        'achaciackaclacmacoacpacqacractacuacyaczadaaddadeadgadhadiadkadladmadn'
        'adoadradsadtadyadzaegaekaenaeraesaevafaafeaffafgafnafoafrafsaftafwaga'
        'ageaggaghagiagnagoagragsaguagyahaahcaheahiahlahnahoahpahyaibaidaihaik'
        'ailainaioaipairaisaitaiwaizajaajdajiajoajuakaakdakeakhakiakkakoakraks'
        'aktalaalbalcaldalealfalgalialkallalmalnaloalpalqalsaltalualvalyalzama'
        'ambamcamdameamfamiammamoampamramsamuanaanbancandaneanfanganhanianjank'
        'anlanmannanoanpanransantanuanvanyanzaohaolaoyapaapbapeapgaphapiapjapk'
        'aplapmapoappaprapsapuaqaaqiaquaraarbarcardarearfargarhariarkarlarmarn'
        'aroarparrarsartaruarvarwaryarzasaasbascaseashasiaskaslasmasoaspasrass'
        'astasuasvaswasyataatcateathatiatkatlatmatoatratsattatuatyaubaucaudaue'
        'aufaugaujaukaulaumaunaupauqaurausautauyavaaveaviavkavlavoavravsavyawa'
        'awbawcawfawlawrawsawtaxiaxwayaaycaydayeaylayraysazaazeazgazhaziazlazo'
        'azuazyazzbabbacbadbaebafbagbahbaibakbalbambanbaobapbarbasbatbaubavbay'
        'bazbbibdebdobeabecbedbefbehbeibelbembenberbetbeubeybezbfebhabhubiabic'
        'bidbiebigbijbikbilbimbinbiobipbirbisbitbivbixbjabjobkibkoblablebliblo'
        'blybneboabobbocboebofbogbohbojbokbolbombonbopborbosbotboubowboybrabre'
        'bribrobrubscbsqbssbswbtabtrbucbudbuebukbulbunburbusbutbuybyabyebyrbys'
        'bytbyzbzocabcaccadcafcagcahcaicalcamcancaocapcarcascatcavcawcaycbicca'
        'cchcciccocdocebceccedceicejcelcemcencercescetcevcewcfacgecguchachbche'
        'chhchichkchlchmchnchochrchschtchuchvchwchychzciacibcimcinciocipcircis'
        'ciuckackbckeckhckicklckmckscktclaclecliclocmocoacobcoccodcoecofcohcoi'
        'colcomconcoocopcoqcorcoscotcoucovcoxcphcqucracrecricrocrucrycssctecti'
        'ctocuacubcumcupcurcuscutcyacyccymcyrczedacdaddaedahdaldamdandaodaqdar'
        'dasdatdaudavdawdbrdbudcrddeddiddlddodeadebdeedefdeldemdendepderdesdev'
        'dewdfedfidgadgidgkdgodgrdhadhedhidhodiadicdiddiedigdildimdindiodirdis'
        'diudixdjedjidjudkedkrdladledlidlldlodmadmedmidmodmudnedoadobdocdohdoj'
        'doldomdondopdordosdotdovdowdoydozdpidqudqvdradredridrodrudsbdsldsodsp'
        'dstdtedtkdtsdufdugdukduldumdundurdusdutdwadwedwidwodymdypdyrdysdzheac'
        'eadeakealeameaneareateaueaveazebaebeebhebieblebneboebrebuecaecheckecl'
        'ecoecqecrectedaeddedeedgedhediedledmednedoedredseduedwedyeebeedeekeel'
        'eeneepeerefeeffefiefjefpefreftegaegeeghegieglegoegregseheehiehlehoehr'
        'ehyeibeiceideieeifeigeikeileimeineioeireiseiteivejeejiejkekaekeekhekl'
        'ekoektelaelbeldeleelfelhelielkellelmeloelpelrelseltelvelyelzemaembeme'
        'emiemlemmemoempemsemuenaenbencendeneenfengenhenienjenkenmennenoenpenr'
        'ensentenuenwenyenzeobeoceogeoleoneopeoreosephepiepkeplepmepoeppepreps'
        'epteraerbercerdereerfergerherierkerlermerneroerperrerserteruerverwery'
        'erzesaescesdeseeshesieskeslesmesnesoespesqessestesueszetaetceteetgeth'
        'etietjetoetpetretsettetuetzeuceudeugeuleuneureuseuxevaeveevievkevoevs'
        'evyewaewbeweewiewoewsexaeyeeyieyneyrezcezeeziezuezzfabfaifalfamfanfar'
        'fasfaufayfedfehfelfenferfesfetffeffifflffoffrfghfiafibficfiefilfinfis'
        'fitfizfjeflafleflifloflufmafnofobfogfoifonfooforfosfoufowfpafrafrefri'
        'frofsbfsofteftiftofuefukfulfurfvefwigaagabgacgadgaggahgaigakgalgamgan'
        'gargasgatgaugawgaygbagbegbogbugchgcrgdagdigeagebgecgedgeegehgeigelgem'
        'gengeogergesgetgevgezgfeggaggeggigglghaghbghdgheghighrghtghugiagibgie'
        'gilgingiogirgisgitgiugjegkiglaglegligmagmegnagnegnignognugobgocgodgoe'
        'golgomgongoogorgotgowgoygpegragregrigrogrugscgsegshgslgstgtagtogtugua'
        'gucgudguegugguigumgungupgusguyguzgwigwogyagypgyrgyshabhachadhaehafhag'
        'hahhaihajhakhalhamhanhapharhashathauhavhawhayhazhbehbohbuhchhcohcrhda'
        'heahechedheehefhegheihekhelhemhenheohepherheshetheuhevhewhexheyhezhhe'
        'hhohiahibhidhiehighilhimhinhiohirhishithiuhivhkahkihkohlehlfhlihlohly'
        'hmahmihnbhnehnghnihnohnshnthoahochodhoehofhoghohhoiholhomhonhoohophor'
        'hoshouhovhowhrahrehrihrlhrohryhsihsohsthtehthhtihtmhtohtshuahubhuchud'
        'huehughuihukhulhumhunhurhuthvihwahwehyahydhyhhylhyphythzeiabiaciadial'
        'iamianiaoiapiariasiauiavibaibbibeibiibkiboibribsibtibuicaicciceicgich'
        'iciickiclicoicricsicuidaidciddideidgidiidlidoidpidwidyidziebiediefieg'
        'iehieliemienieriesietifeiffifoigaigcigeiggighigiigligmignigoigriguiha'
        'iheihoihuihyiimiitijvikaikhikiiklikoikriksikuilailcildileilgilhiliilk'
        'illilmiloilpilsilvilyimaimbimeimfimgimhimiimkimmimoimpimrimsimtimuimz'
        'inainbincindineinfinginhiniinjinkinminninoinrinsintinuinyinzioaiobioc'
        'iodiofiogiohiojiokioliomiooiopioriosiotiowipeiphiplippipripsiptipuipy'
        'iraircireirfirgiriirkirniroirsirvisaisciseishisiiskismisoissistisvisw'
        'itaitcithitiitlitmitnitoitritsittituitvitziuliusivaiveiviivkivoivriwa'
        'iweiwhixbixeixiixuiyaizaizeizgiziizoizwizzjacjadjafjagjahjaijakjaljam'
        'janjarjasjdajeajeljenjepjerjiajibjiljimjinjkojoajoejogjohjokjoljonjoo'
        'jorjosjoujuajuejuljunjurjvokaakabkaekafkagkahkaikalkamkankaokapkarkas'
        'katkawkaykazkbrkcokdakdikebkeckedkefkeikelkenkerkesketkeukevkhakhckhe'
        'khikhmkhokhrkhtkidkiekilkimkinkiokipkirkiskitkkoklakleklikloklykmakmi'
        'knaknokobkockoekogkokkolkomkonkopkorkoskotkoukovkozkrakrekrikrokrukry'
        'ksekshksokspkssksuktaktekthktuktzkuakuckudkuekukkulkumkunkupkurkuskut'
        'kuzkvakvikyalablacladlaelaflaglailaklallamlanlaplarlaslatlaulavlawlay'
        'lazlbalbelbilbolbrlbulcalchlcilcllcolculdaldeldfldhldildmldoldqldrlds'
        'ldylealeblecledleelegleilellemlenleoleplerlesletleulevlewlfelfilfllfo'
        'lfplfrlfslfulgalgilgolhalhelhilialibliclidlielifligliklillimlinliolip'
        'lirlislitliulivlizlkalkelkhlkilkmlkollallbllcllellillmllollsllullwlma'
        'lmelmilmklmolmqlmslmulnalnoloalobloclodloflogloilollomlonloplorloslot'
        'loulovlowloylpalpelphlpilpllpnlpulqulrilrolsalsblsclsdlselshlsilsklso'
        'lstltalteltflthltiltkltlltnltoltpltslttltwlualublucludlueluklullumlun'
        'luolurlusluzlvalvelvilvolwelwilyalyblyclydlyelyglyhlyklyllymlynlyolyp'
        'lyslytlyulzalzblzilznmacmaemagmahmajmakmalmammanmapmarmasmatmaumavmaw'
        'maxmaymazmbambembimblmbombrmbumcamcbmcgmchmckmcomdomdrmedmeemegmeimej'
        'melmenmermesmetmeumeymfemfomgrmhamhomiamicmidmiemigmihmikmilmimminmio'
        'mipmirmismitmiumizmklmkomlamlemmammemmimmlmmomocmodmoemogmohmoimokmol'
        'monmoomopmormosmotmoumoymozmpempfmphmpimplmprmpsmqumramromsbmscmsdmse'
        'msomssmstmthmtymucmuemuimulmunmurmusmutmyamytmzenabnacnadnaenafnagnah'
        'najnaknalnamnannapnarnasnatnaunavnawnaxnaznbanbenblnbonbrnbuncancench'
        'ncincknconcrncuncyndandcndendgndhndindondqndrndsndundwndyneanebnecnee'
        'nefnegnehneineknelnemnennepnernesnetneunevnewneznfenfinflnfungangbngc'
        'ngdngengfnggnghnginglngongpngrngsngtngungwnhanhenhsnhunhynianicnidnie'
        'nifnigniknilninnionisnitniunivniznjanjinjonjunkankdnkenkhnkinklnkonkv'
        'nlanlenlinlonmanmenminnannenninnonnrnnsnnwnoanobnocnoenofnognohnoinoj'
        'noknolnomnonnoonopnoqnornosnotnounovnownoynoznpenpinponprnpynrinronrr'
        'nrynsdnsensfnshnsinsknslnsonstnswntantbntentgnthntintlntmntontrntsntu'
        'ntznufnuknunnusnvenwanwonyanybnyenyhnyunzanzenzhnzinzooaeoaloanoapoaq'
        'oaroasoatoauoaxobaobbobdobeobfobiobjobkobloboobrobsobtobuobyocaoccoce'
        'ochociockoclocoocroctocuocyodaoddodeodgodhodiodlodoodrodtoduoeboecoed'
        'oehoeloenoeroesoetoeuoewofeoffoflofooftogaogbogdogeoggogioglogoogrogt'
        'oguohaohbohdoheohiohlohmohnohoohuohyoiboigoihoinoiroisojaojiojoojuoka'
        'okeokiokkoklokookroksokuolaolboldoleolfoliolkollolmolnoloolqolsoltolu'
        'olyomaombomcomdomeomiomkommomoompomsomuomyonaonboncondoneongonhonionj'
        'onkonnonoonponsontonyoodooeooiookooloonoopooroosootopaopeophopioplopo'
        'oppopsoptopuopyoquoraorborcordoreorforgorhoriorkorlormornoroorporrors'
        'ortoruorvorzosaosboscoseosgoshosioskoslosmosnosoosposrossostosuotaote'
        'othotiotlotootpotrotsottotuotyotzouaouboudougouloumounourousoutouvoux'
        'ouzovaovdoveovgoviovoovsovyowaoweowiowlownowoowsowuowyoxaoxboxeoxfoxi'
        'oxmoxyoyaoyloyuozaozeoziozoozupaapabpacpadpagpahpaipakpalpanpapparpas'
        'patpaupavpbapcipeapecpedpeipekpelpenpepperpespetpeypezpgaphaphephiphl'
        'phophrphtphuphypiapicpidpiepigpilpimpinpiopirpispitpiypizpjopkhplaple'
        'pliploplupmapmepnopodpokpolponpopporpospotpoupovpowpoyppappepphppippk'
        'ppopraprepripropscpsepsipsopstpsuptaptiptoptupuapucpuhpujpumpunpurpus'
        'putpyapyrqanqaqqarqilqinqitquaquequiquoqusqviraarabracradraerafragrah'
        'rairakralramranraprarrasratrauravrawrazrbarberbirblrborbrrburbyrcarce'
        'rchrcirclrcorctrcyrdardbrderdgrdirdordsrdyrearebrecredreeregrehreirel'
        'remrenreoreprerresretreurevrewreyrezrfirfmrforfurfvrgargbrgergirgnrgo'
        'rgsrgurgyrharherhoriaribricridrierigrihrikrilrimrinrioriprisritriuriv'
        'riwriyrizrkarkcrkerkhrkirkorksrlarlbrlerlfrlgrlhrlirlorlsrmarmbrmermi'
        'rmlrmormsrnarnbrndrnernirnornsrnurnwroarobrocrodroerofrogrohroirojrok'
        'rolromronrooroproqrorrosrotrourovrowroxroyrozrparphrpirplrpurqurrarre'
        'rrhrrirrmrrorrurryrsarscrsdrsershrsirsmrsorssrstrsurtartdrterthrtirtl'
        'rtmrtnrtortrrtsrturtvrtzruarubrucrudrufrugruirumrunruprusrutrvarvervi'
        'rvorwerwirworyarygryirylrymrynryoryprysrytryzrzarzerzisabsadsafsagsah'
        'saisaksalsamsansapsarsassatsavsaysazsbasbesboscaschscisclscoscrsdasde'
        'sdisdoseasecsedseesegseisejsekselsemsensepsersetseusevsewsfisfosgesha'
        'shbshcsheshishkshlshmshnshoshtshushysiasibsicsidsiesigsilsimsinsiosit'
        'siusizsjoskaskeskisklskoskrskuskvslasleslosmasmismosmusmysnasnjsnosoa'
        'sobsocsodsofsogsohsolsomsonsopsorsotsousovspaspesphspisposprspusqusra'
        'sresrisrussassbsscssessisslssmssosstssustastbstesthstistlstmstnstostr'
        'stustysuasubsudsuesugsuksulsumsuosursussutsuvsvasvesvusvyswasweswiswu'
        'sylsymsynszaszeszmszoszytaatabtactadtaetaftagtahtaitaktaltamtantaptar'
        'tastattautavtaytaztbrtbutchtdateatebtedteeteftehteitekteltemtentepter'
        'testetteutevtewteztfotgetgothathethithmthothrthsthuthwtiatibtictietif'
        'tigtiktiltimtintiotiptirtistittiutivtjetkitkotlatletlitlotmatmotnatne'
        'tnitnotoatobtoctodtoetoftogtohtoitojtoktoltomtontootoptortostottovtow'
        'tpatpetratretritrotrutrytsatsbtsctsetsitsjtsmtsotsptsttsuttattettgtth'
        'ttittlttnttottrttsttutuctudtugtuhtuktultumtuntupturtustuttuvtuztvatve'
        'tvitwetwitwotyctyltyrtyutzatzetzitzkuacuaduaguaiualuanuaruatuauuawuaz'
        'ubaubeubiubnubrucauccuchuckuclucoucrudaudbuddudeudiudjudludmudoudrudw'
        'uebueduehueiueluemuenueruesuetuffuflufrugaugeuggughugiugmugsugtuhuuid'
        'uiluimuinuiruisujaujoukaukeukhukiuklukouksukuulaulculeulfulguliulkull'
        'ulmuloulpulrulsultulvulyulzumaumbumcumeumhumiummumoumpumsumtunaunbund'
        'uneunguniunkunnunounsuntuobuocuoiuoluonuorupaupcupeupiupkuplupruquura'
        'urburcurdureurguriurkurlurmurnurourpurqurrursurturuurvusauscuseushusi'
        'uskuslusmusouspussustutautcuteuthutiutlutnutoutsuttutuutwuvauviuxeuya'
        'uyeuynuytuzauzeuzluzmuznuzovaavacvadvaevaivajvalvanvapvarvasvatvauvav'
        'vayvdavdoveavedvegveivelvenveovervesvetvgoviavicvidvigvihviivikvilvim'
        'vinviovirvisvitvivvkivkovlavlovlyvoevogvoivolvonvorvosvovvowvozvrbvre'
        'vrivruvshvskvuavulvuovurvyavycvynvyrvysvyuwacwadwagwaiwakwalwanwarwas'
        'watwavwaywazwbewcrwebwedweewegweiwelwenwerweswetwfowhewhiwicwiewigwih'
        'wilwinwiswitwlewnewnlwnmwodwohwolwonwooworwrewrowsowstwthwuewulwurwya'
        'wycwyhwylxacxahxalxamxanxenxfexifxilximxioxipxitxmaxonxwexyhxykxyvyac'
        'yaeyafyagyakyalyamyanyaryasyatyavyazybaybdychyclycoycrydeydrydyyeayed'
        'yeeyegyelyeryftygiygoyhayheyhoyhyyivyixykiykoylayldyleyliyllyluylvyma'
        'ymeymkympynayncyneyngynoynsyodyogyolyonyosypeyphypsyptyrayreyriyroyrr'
        'yryyscyshysiysoystyteythytiytoyttyuayubyucyudyugyukyunyusyvayvoyzayzh'
        'zabzaczaizakzalzanzarzavzawzbuzcuzdezekzelzemzenzeozerzeuzgazgrzhazhe'
        'zhizhoziaziezigzilzimzinzipzirzlazlezmezmiznezoizokzolzomzonzotzugzun'
        'zuozuszvyzwizykzymzzazzezzo'),
    2: ('aabaadaaiaajaakaalaamaanaaraasaataauaavabaabbabeabiabjablaboabsabuaby'
        'accaceachackadaaddadeadfadgadiadjadkadladmadsaduaebaefaegaeiaelaemaen'
        'aeyafaafeaffafhafiafjafkaflafnafoafrafsaftafvafzagaagbagdageagfaggagi'
        'aglagnagragsaguahaaheahiahjahkahlahoahtahuahvahyaijaikailainaisaitaiv'
        'ajaajoajsakaakeakiakjakkaklakmaknakoakraksaktakualaalbaldalealfalialj'
        'alkallalmalnaloalpalsaltalualvalyamaambameamfamhamiamkamlammamnampamr'
        'amsamuamyanaandaneanganianjankanlanmannanoansantanuanvaoaaoiaoraosapa'
        'apeapiapjapoappaprapsapuapyaraarbarcardarearfargarhariarjarkarlarmarn'
        'aroarrarsartaruarvasaasbaseasgasiasjaskasmasoaspassastasuasyataateatf'
        'athatiatkatlatnatoatpatratsattatuatvatyaudaufaugauhaukaulaumaunauoaup'
        'aurausautavaavdaveavfavgavhaviavlavnavoavsavtavuavvavyaybaydaykaynayr'
        'aytazobaebagbajbakbambanbarbasbatbbabbebefbegbehbeibelbenberbesbetbev'
        'bifbihbilbinbiobirbisbitbjoblableblibloboebogbokbolbonbooborbotbrabre'
        'bribrobrubrybsjbskbspbssbucbudbuhbulbunbuoburbutbygbyrcarccecedcepcer'
        'cescetchacheciacipckeckncktclacolcomcrectictocuscykdaadabdaddagdahdak'
        'daldamdandapdardasdatdaudavdbadbedbidboddaddeddiddrddudeadefdegdeidek'
        'deldemdendepderdesdetdevdexdeydfadfedfodgadgedgldgrdgudhadhldhodiadic'
        'digdikdildimdindiodipdirdisditdiudjudkadkedkldkodladledlidludmadmidmy'
        'dnadnednidobdoddokdondopdordosdotdovdpldpudqudradredridrodsadsbdsedsf'
        'dshdsidskdsldsmdsodspdsrdssdsvdsydtadtedtydubducduddunduodupdurdusdut'
        'dvadvedvidykeadeageakeaneapeareatebbebeebleboebreckedbeddedeedgedhedi'
        'edkedledoedredseduedveeleeneereetefaefeefieflefnefoefreftefuegaegeegg'
        'egieglegnegoegreguehaehnehteideieeifeigeijeikeileimeineioeireiseitejn'
        'ekaekdekiekkeklekoekreksektekuekvelaelbeldeleelfelgelhelieljellelmeln'
        'eloelpelselteluelyemaembemeemgemiemlemmemnemoemuenaenbendeneengenheni'
        'enjenkenlennenoenrensentenuenveoaeoleoneorepaepeeplepoeppeprepteraerb'
        'ercerdereerfergerherierjerkerlermerneroerperqerrerserteruervesaesbese'
        'esiesjeskeslesnespessestesuesvetaetbeteetietjetletnetoetpetretsettetu'
        'etyeudeuleuneureuseutevaevbeveevievjevuevyexfexteydeyfeyjeykeymeyneyo'
        'eyreyseyteyvfabfacfadfaffakfalfamfanfarfasfatfbefbofekfelfenferfesfey'
        'ffeffiffufgefhafheficfiefikfilfimfinfiofirfisfjafjefjofklfkoflafleflj'
        'floflufnafnifnjfnsfntfnufoefolfonforfosfotfrafrefrifrofrsfrufryfsafsb'
        'fsdfsffsgfshfskfslfsofssfstfsvfsyftafteftiftrftsftufugfukfulfunfurfus'
        'fvefyrfysfyyfzegaagabgadgaegafgaggalgamgangargasgatgaugavgbagbegbigbo'
        'gdagdugebgefgeigelgemgengeogergesgetgeygfrggaggdggiggjggnggrggsggughe'
        'giegilgingiogisgitgiugjagjegjogkvglagligljglogluglygnagnegnignsgnugod'
        'goggolgorgprgragregrigrogrugsagsbgsdgsfgsggshgskgslgsmgsngsogspgssgst'
        'gsvgtngudgufguigulgumgunguogylhaahaehafhaghakhalhamhanhapharhathauhav'
        'hdiheahedhegheihelhemhenherheshetheuheyhiahilhinhirhishithjahjehjohju'
        'hkohlahlbhlehlghlihljhlmhlshnihnqhnuhofhoihojholhonhophorhoshovhrahre'
        'hrihrohruhtehtihtohughulhuohushuvhvahvehvohylhyphytiaaiafiagiakialian'
        'iapiariasiatiazibiibliboiceichicoictidaidbiddideidgidhidiidjidlidnido'
        'idpidsiduieaiebiedielienieriesietifiifjifrifsiftigaigeiggighigiiglign'
        'igoigsihiihnihoiihiikiimiiniiriisiitiivijaijoikaikeikiikkikmiknikoikr'
        'iksikuilailbildileilfilgilhiliiljilkillilmilrilsiltiluilvilyimaimbime'
        'imiimmimpimsimtimuinainbincindineinfinginiinkinlinminninoinpinsintinu'
        'invioaiogioiiojiokiolioniooioriosiouiovipeiplipoippiptipuirairbircird'
        'ireirfirgiriirjirkirlirmirnirpirrirsirtiruirvisaisbisciseisfisgishisi'
        'isjiskislismisnisoispisrissistisuisvisyitaiteitiitlitnitritsittituity'
        'itziugiuniusivaivbivdiveivfivgivhiviivkivlivmivnivoivpivrivsivtivuivv'
        'ixiizajaajacjafjahjaijakjaljanjaojapjarjasjatjaujavjeajeejekjeljemjen'
        'jepjerjesjnejodjofjogjohjoijojjokjoljonjorjosjotjoujtojubjudjufjuljun'
        'jupjurjusjuukaakabkadkaekafkagkaikajkakkalkamkankapkarkaskatkaukaykba'
        'kbekbikdakeakebkedkefkeikelkemkenkerkesketkeukeykhakhokiekifkijkilkim'
        'kinkiokipkirkiskitkivkjakjekjokjukkakkekkikkokkskkukkvklakleklikloklu'
        'kmakmekmokmyknakneknikobkodkoekogkohkoikokkolkomkonkookopkorkoskotkou'
        'krakrekrhkrikrokrukryksaksdkseksfkshksiksjkskksmkspkstksuktdktektiktl'
        'ktmktnktoktrktskttktukudkuekufkugkuikukkulkumkunkupkurkuskuvkvakvekvi'
        'kygkylkynkyrlaalablacladlaelaflaglahlailaklallamlanlaplarlaslatlaulav'
        'lbalbelboldaldbldeldfldildkldnldrldsldulealedleelefleglehleilejleklel'
        'lemlenleoleplerlesletlevleylfalfblfelfglfilfolfslftlfulgalgelgjlgrlhe'
        'lialiblielifligliiliklillimlinliolislitliulivljaljeljoljulkalkelkilkn'
        'lkolkslkulkyllallbllellfllgllillklllllmllnllollqllrllsllullvllylmalmd'
        'lmelmglmhlmilmklmnlmslmulnalnilnoloclodloeloflogloklomlonlooloplorlos'
        'lotloulovloylpalpjlpllpolptlqvlrelrilsalsblsdlselsflsglshlsilsklsllso'
        'lsrlsslstlsvlsyltalteltiltjltlltnltoltrltslualucludlueluflugluhluklul'
        'lunluoluplurluslutluylvalvelvflvilvolvulydlyelyhlyilyjlyklyllymlyslyt'
        'lyvmaamabmadmagmahmaimakmalmanmapmarmasmatmaumavmaymbimbrmbsmdamedmei'
        'mejmekmelmemmenmeomermetmfamfimfomgamgimgomgrmhemhimhumhvmidmigmiimik'
        'milminmiomirmismitmjomkomkvmlamlemlimmammemmimmsmmtmmumnamnemnimodmog'
        'mokmolmonmoomormosmotmpamplmpompsmpumqvmramremrimsbmsdmsemskmslmsnmst'
        'mtamtumubmuhmuimukmulmunmuomusmuumuvmvamynmyrmyynaanabnadnaenafnagnah'
        'nainaknalnamnannaonarnasnatnaunavnbanbenbinbrncencindandbnddndendfndg'
        'ndhndindkndlndmndnndqndrndsndtndundvnedneenefnegneineknelnemnenneoner'
        'nesnetneuneynfanfenfinflnfongangbngdngengingjnglngongpngrngsngunhanhe'
        'nhinhonhunicnienifnigniiniknimninnipnisnitnivnjanjonjunkankenkinkonks'
        'nktnlanlenlinmanmunnannbnnennfnngnninnknnonnrnnsnntnnunnvnnynoanofnoi'
        'noknolnomnonnoonornotnpanplnqunrinsansbnsensfnshnsinsknslnsmnsnnsonsp'
        'nsrnssnstnsunsvnsyntantenthntintlntontrntsnttntuntvntynudnumnunnupnus'
        'nutnvanvenvinvonycnyenyhnyknysoaaoadoaeoafoaioajoaloaroasoavobbobiobr'
        'obsoceochodaoddodeodfodiodlodmodnodoodrodsodtoduodvoekoeloenoerofaofb'
        'offofiofnofoofrofsoftogaogbogeoggogiognogrogsoguohaohiohjohlohoohtoid'
        'oikoiloimoinoisoitojaojeojtokaokbokeokhokiokkoklokmoknokookuolaolbold'
        'oleolfolgolholiolkollolmoloolsoltoluolvolyomaomeomfomgomiommomnomoomp'
        'omqomsomuomvomyonaonboncondoneonfonhonionkonlonmonnonoonsontonuonvony'
        'ooaoogooloomooooosootopaopbopeopiopnopooppopsoptopuoraorcordoreorforg'
        'orhoriorjorkorlormornoroorrorsortoruorvoryosaosbosfoshosioskosmosnoso'
        'osrossostosuosvosyotaoteotiotkotootsottotuoudoulounouroutovaoveoviovu'
        'oytpaapacpadpafpagpaipakpalpampanpapparpaspatpavpbepdrpeapeipekpelpen'
        'perpespetpiapibpidpiepihpiipikpilpimpinpiopippirpispivpjapjopkaplaple'
        'pliplopluplypnapofpohpoipokpolponpopporpospoyppappbppdppeppippjppkppl'
        'ppopprppspptpraprepripropruprypsapsepsjpskpsppstptaptiptupubpulpunpuo'
        'purpyrpysquiqviraarabradraerafragrahrairajrakralramranraprarrasratrau'
        'ravrayrbarberborbrrburchrcurdarddrderdirdlrdmrdnrdprdsrdurdvrearedree'
        'refregrehreirekrelremrenreoreprerresretreurevreyrfarferfirfjrflrforfr'
        'rgargergirgkrgnrgrrgurharherhorhrrhvriaridrierifrigrihriirikrilrimrin'
        'rioriprirrisritriurivrjarjerjorjurkarkerkirkjrkkrklrknrkorkrrksrkurla'
        'rlerlirlorlsrlurmarmermirmlrmormurmyrnarnbrndrnernirnsrnurnyroarobroc'
        'rodrofrogroirokrolromronrorrosrotrovrplrprrqurrarrerrhrrirrkrrorsarse'
        'rsfrshrsirsjrskrslrsmrsorsprssrstrsvrsyrtartertfrtirtortsrttrturtvrub'
        'rucrudrufrugrukrulrumrunruoruprusrutrvarvervirvnrvorycrygrykrymrynrys'
        'saasabsadsaesafsagsahsaisajsaksalsamsansapsarsassatsausavsaysbasbesbi'
        'sblsbosbrschscrscysdasdoseasedsefsegsehsekselsemsensepsersessetseusey'
        'sfasfesfisfjsflsfosfrsgasgesgisgnsgrshashishlshoshrshvsiasibsidsiesif'
        'sigsiisijsiksilsimsinsiosipsirsissitsiusivsjasjosjuskaskeskiskjsklskn'
        'skoskrsksskuskyslasleslisloslusmasmhsmismusmysnasnesnisnosnusodsofsog'
        'sohsoisoksolsomsonsopsorsotspaspespispjsplsposprspusrasresrisrosrussa'
        'ssbssessfssisskssosstssussystastbstesthstistjstlstmstnstostpstrstusty'
        'suasudsuesuhsuksulsumsunsuosupsuusvasvesvisvosvusyfsyksynsyosyrsyssyv'
        'taatabtadtaetaftagtahtaitajtaktaltamtantaotaptartastattautavtaytbatbe'
        'tbitbrtdotdrtecteetegtehteitekteltemtenteptertestetteutexteytfitfltfo'
        'tgatgethathethithothrthutidtietiftiitijtiktiltimtintiotirtistittiutiv'
        'tjatjetjotkatkitkotkutlatletlitlutmatmetnetnitnstoatodtoftogtohtoitoj'
        'toktoltomtontoptortostottovtpatpltputratretritrotrutrvtrytsatsbtsetsf'
        'tsgtshtsitsktsltsrtsststtsvtsyttattettftthttittmttnttottsttuttytudtue'
        'tugtuituktultumtuntuoturtustuttuutvatvetvitvotydtyityktymtyntyptyrtys'
        'tyytzeuaauafuakuasubaubbubluboubrubuuceuciudaudbuddudeudgudhudiudkudl'
        'udsudtuduudvueluetufaufiufjufrufsugaugeuggugiugrugsugtuguuheuhluhtuid'
        'uisuivujeukaukeukiukkuknukoukruksuktukuulaulbulduleulguliulkulluloult'
        'uluumaumeumgumhumiummumnumrumsumuunaunbunduneunguniunkunnunuuoauobuod'
        'uojuokuoluomuonuosuotuovupaupeupiupouppupsupuuraurburdureurfurhuriurk'
        'urmurnurourrursurturuurvusauseusfushusjuskuslusnusoussustusuusvutautb'
        'utduteutfutgutiutkutlutoutrutsuttutuutvuuduuluunuuruusuutuvauveuvuuyf'
        'uykvaavabvaevagvaivakvalvamvanvarvasvatvauvayvbevbivbovdavdevdoveaved'
        'vegveivejvekvelvenvervesvetvfivfovfrvfuvgavgrvguvhavhivhoviavicvidvig'
        'viivikvilvinviovirvisvitvivvixvjovkavkovlavlevlivmavndvnivnovofvogvoi'
        'vokvolvonvopvorvotvplvrevsavscvskvslvssvsyvtavtjvtrvudvujvunvuovupvur'
        'vutvuuvuvvvavvevykvyywahwalweswirxfixilybryckydaydeydiydnydoyeryesyfi'
        'yggygnyhdyheyhtyhyyilyinyisyjaykaykeykhykiykjykkyklykoyksylayldyleylk'
        'yllyluymfymiymmymsyndyneyngyniynjynlynnynsyntyoayoiyotypeyppyrayrdyre'
        'yriyrjyrkyrnyrsyruyryysaysbyseysiyskyslysmysoystysvysyytayteytoyttyty'
        'yviyvyyydyypyyszabzaczelzof'),
    3: ('abaabdabeabiablabrabuabyachadaadbadiadnadoadpadradsaduadyadzaetafiafo'
        'agaageagiagnagoagraibainaisaiuakaakhakiakoaksaktakuakzalaalcaldalealg'
        'aliallalmalnaloalsaltalualyalzamaambamcameamiamoamsamuamyanaandangani'
        'ankannanoanransantanuanzaozapaaplapoaprapsapuaraardareargariarkarmarn'
        'aroarparsartaruarvaryarzasaasbashasiaslasnasoaspassastasuataatcateati'
        'atkatnatoatsattatuatyavaavdaveavgaviavkavlavnavoavravsavyayaaybaycaye'
        'aygaykaylaymaysayvazaazdazeazhaziazlazmaznazoazrazybabbagbakbalbanbar'
        'basbatbavbaybazbchbdubedbekbelbenberbesbezbiabidbikbilbinbirbiybkhbki'
        'bkoblablebliblubnibnobnybobbodboebogbokbolborbovboybrabrobrsbrybshbts'
        'budbugbuibulburbusbutbuybuzbycbysbytchachechichkchnchochschtchuchydac'
        'dagdaldandardatdavdayddededdegdeldemdenderdesdetdevdeydgodiadigdikdim'
        'dindisditdivdlidmidnadnednidnodnydobdogdoldomdondopdordosdoudovdozdpi'
        'dpodredridrodrudskdstdubdudduidukduldurdusduzdvedvidvodyadygdykdymdyo'
        'dysdyudyzdzedzheapebaebeebneboebsechedeediedkednedoedredvedyefreftegd'
        'egeegiegkegoegregtegueinekaekhekiekoeksektekuelaelbeleelgelielneloels'
        'eltelyelzemaembemeemiemkemnemoemremsemvemyenbendeneengenienkennenoenp'
        'ensentenyenzeobeorepaepeepiepoeraerbercerdereergerierkerlermerneroerp'
        'erserterveryerzeseeshesieskeslesnesoessestesvesyetaeteetietletoetrets'
        'etuetyeudeureutevaevdeveevievkevoevrevsevuevyexaexeeyeeykeyneyseyueze'
        'ezheznezoezufakfalfatffifikfimfitflaflofokfomfonforfrefrofryftefurgac'
        'gadgaegaggalgangargatgavgdagdogelgeogepgesgeygezgidgilgingiogisgiygla'
        'gleglignigobgocgodgoggolgongopgorgosgotgovgoygozgragregrigrogrugrygty'
        'gubgucgudgukgulgurgusgutgvahabhachadhaehaghaihakhalhanhapharhashathay'
        'hchhdehdohduhebheghekhelhenhepherheshethevhezhgohiehighiihikhilhimhin'
        'hirhishithivhiyhizhkahkihkohlahlihlohnehnihnohnyhodhokholhonhophorhos'
        'hothovhoyhrohruhshhskhtahtihtohtuhtyhuchudhughukhulhumhunhurhushuvhuy'
        'hvahvihyehyoiaeiaiiakialiamiasiatiaviazibaibiiboichideidnidoidziesiga'
        'igligoigriguiiaiiniisikaikhikiikoiksikuilaileiliilkillilniloilsiluily'
        'imaimbimeimiimkimlimoimrimsinainbineinfinginiinkinninoinsintinuinyinz'
        'ioniozipaipeipkirairbireiriirkirniroirsiruiryirziseishisiiskislismiso'
        'ispissistitaiteitiitkitoitritsitviubiudiusiutivaivdiviivkivnivoiyeiys'
        'izaizbizdizeizhiziizkizlizokackadkaikakkalkamkankarkaskatkavkaykazked'
        'kemkeskevkhakhdkhgkhikhlkhmkhnkhokhrkhtkhukhvkhykimkinkirkiskitkiykiz'
        'klekliklykmiknykodkogkokkolkomkonkopkorkoskotkovkoykozkrakrekrokryksa'
        'kshksiksokspkstktiktoktrktykubkuckudkulkumkunkupkurkuskutkuvkuykuzkya'
        'kyskyzkzhlablacladlaglailaklamlanlaplaslatlavlaylazlbulchldaldoleblec'
        'legleklemlenleplerlesletleulevlexleylezlgalgolialibliclidligliklillim'
        'linliplislitliulivlizlkelkhlkilkolkullallellolmalmelmslmylnelnilnolny'
        'loalobloclodlogloklomlonlorloslotloulovloylozlpalpilshlskltaltiltsluc'
        'lugluklunlutluyluzlvylyalyglymlynlyolyslytlyulzalzhlzilzomadmaemagmai'
        'makmalmammanmarmasmatmavmaymazmbamblmbomchmecmedmegmeimelmenmermesmet'
        'meymezmglmiamicmidmikmilminmirmitmkamkhmlymmommumnimnomodmogmolmonmor'
        'mosmotmovmozmplmrymskmsomtsmukmunmurmutmuzmyamyomysmytmyznabnacnadnag'
        'nainaknalnamnannapnarnasnaunavnaynaznbunchndandendondrndyndznecnefneg'
        'neknelnemneonernesnetneunevneyneznfongangengingongrngunianicnienignii'
        'niknilnimninnirnisnitnivniyniznkonkunninnonnynoanocnodnognoknolnomnoo'
        'nornosnotnounovnoynoznponronsanshnsinsknstntantentintontsntunudnurnus'
        'nyanyenyknymnyonytnyunzenzhoaloanoarobaobeobiobkoblobnoboobrobsobuoby'
        'ochodaoddodeodgodiodkodnodoodpodsoduodvoemoenoetoevofiogaogdogioglogn'
        'ogoogroguoikoitokaokhokiokmokookroksoktokuolaolcoldoleolgoliolkolmoln'
        'oloolpolsoltoluolvolyolzomaomiomlommomnomoompomsomuomyonaoncondoneonk'
        'onnonoonsontonyoobooroozopaopeopiopkopoopropyoraorboreorgoriorkorlorm'
        'ornoroorsortoruoryorzosaoscoseoshosioskoslosnosoossostotdoteotiotkotl'
        'otmotnotootpotrotsotuotvoufougoukoulourousouzovaovdoveovgoviovkovnovo'
        'ovrovsovuovyoyaozaozdozeozhozlozmoznozoozyozzpadpalpampanparpaspatpav'
        'paypecpenperpespetpevpeypikpinpiopispitpiyplaplepliplypocpodpoepogpok'
        'polpompopporpospotpovpozpraprepriproprupshpskpucpudpugpukpusputpyapye'
        'pyopyspytrabracradraerafrakralramranraprasratravrayrazrbarberbirchrda'
        'rderdordsrdyrearecredregrekrelremrenrepresretreurevreyrezrgargirgorgu'
        'rigriirikrilrimrinriorisritrivriyrkarkerkhrkirkurlarlirlorlyrmarmermi'
        'rmornarnornurnyrobrocrodrogroirokrolromronroprorrosrotrourovrozrperpi'
        'rpursarsershrskrsmrtartirtkrtortsrtyrubrudrugruirukrunruprusruzrvorya'
        'rybryeryirykrylrymryoryprysryurzarzhrzysafsaksalsamsansarsassatsavsay'
        'sbescosdesebsegselsemsensepsersessevseyshashcsheshishkshlshmshnshosht'
        'shushvshysiasibsiisilsimsinsitsivsiyskaskiskoskrskuslaslosluslysmasmo'
        'snesnosobsocsogsoksolsomsoosorsossotsovsozspaspespisposressessissksso'
        'sspsstssussystastestistnstostrstustvstysudsufsuksulsumsuosursussutsuv'
        'suzsvasvesvisvosyasycsyesyksylsynsyssyztadtagtaktaltamtantartastattav'
        'taytchtdytebtegtekteltemtentertestetteyteztiatictietigtiitiktimtintio'
        'tirtistittivtiytiztkatkitkotkytlatlitlotlutnatnetnitnotobtogtoltomtop'
        'tortostottoutovtprtputratretritrotrutrytsetsitsktsotsvtsytuatubtuktul'
        'tupturtustuttuytvetvitvotvutyatyetyntyotyrtyutyvuapubaubcubeubiubkubn'
        'uboubtuchudaudeudiudnudouduudyudzufauffufiugaugiuglugouguuinuituiuuka'
        'ukhukoukruksuktulauleuliulkulmulouluulyumaumeumiumsunauneunguniunyuoy'
        'upaupiuppuraurburcureurguriurlurmuroursurturuuryurzuseushusiuskuslusm'
        'usoussustusuutauteutnutoutsutuuvauveuvouvsuyauybuyeuykuymuynuysuzauzd'
        'uzeuzhuziuzluznuzuvadvaivalvanvarvasvatvayvdevdivdovelvenvervesvetvez'
        'vgovgrviavicvidvigvikvilvinvirvisvitvkavkovlavlevlivlovmevnovnyvoavob'
        'vocvodvoevoivokvolvomvoovopvorvosvotvouvovvoyvozvrevrivrovsevshvskvst'
        'vuevuivukvurvusvyavybvycvykvylvypvysvytvyuvyzxanxeyyabyacyadyagyakyal'
        'yanyaryasyatyauyazybiybkybnyboybrybyychyefyegyekyelyemyenyeryesyevyey'
        'ygeygiyinykaykhykoyksyktylaylkyloylsymaymkymsynayndynkynoynsyokyolyom'
        'yonyoryosyovypoyrnysayseyshyskysoyssysvytayteytiytkytnytvyubyucyudyug'
        'yukyulyumyunyupyuryusyuyyuzyvayvkyvoyzhyzryzyzabzadzaizakzalzamzanzao'
        'zapzarzatzavzayzbezdazdezdnzdozdrzduzelzemzenzepzerzeyzhazhbzhczhdzhe'
        'zhgzhizhmzhnzhozhszhuzhyzilzimzinzkizlazlizlozlyzmezmoznaznezniznozny'
        'zobzorzovzrazrezubzulzuyzvazvezyazybzykzyozyvzzh'),
    4: ('aanaasaatabaabbabdabgabjabkablabnabqabsabuabyacaachacuadaadeadgadiado'
        'aebaecaegaejaesafaafeagaagbagcagdaggagiagjagkaglagmagnagoagqagragsagu'
        'agxagyagzahaahdahkahnahsaiaaibaicaidaifaigaihaijaikailaimainaipaiqair'
        'aisaitaiuaiwaixaiyaizajaajiajoakaakeakhakoaksaktakuakyalaalealgalhali'
        'aloalsaltaluamaambamcamdameamgamhamiamkamlamnamoampamqamramsamtamuamw'
        'amxamyamzanaanbancandanganhanianjankanlanmannanoanpanqansantanuanwanx'
        'anyanzaoaaobaocaodaogaohaojaolaomaonaopaoqaosaotaowaoxaoyaozapoapuaqa'
        'aqeaqiaqoaquaraarbarcardareargariarkarlarmarnaroarqarrarsartaruarvarx'
        'aryarzasaaseashasoasrastasuataatoatsatuausawaawoawsawuaxiaxoaxuayaayd'
        'ayeayiaykaylayoayuazaazhazibaabaebagbaibajbakbalbambanbaobaqbarbasbax'
        'baybazbdubeabebbeibenbeybgabgybiabiebijbilbinbirbiubixbjoblubnabodbog'
        'boibolbonboqborbosbotbozbqebribrobsabtabucbudbugbuibukbulbumbunbuqbur'
        'busbutbyabyebzhcaicakcalcamcancaocawcazcegcencerchachechichochuchwchy'
        'ciacixcoccodcogcokcomconcoqcorcoycozcuncuodaadabdaddaedafdagdaidajdak'
        'daldamdandaodapdaqdardasdatdawdaxdaydazdeadegdehdekdeldendeqderdewdex'
        'deydezdgadhidiadiedigdihdikdindiodiydizdobdogdoidoldomdondoqdordoudox'
        'druduaducdueduhduidujdukdunduodurdutduydzaeaneauebaebeebrecaechecuede'
        'ediedoedzeedeeieeleeoeereeyefeegaegeegnegyegzehhehueiaeibeiceideifeig'
        'eiheijeileineipeiseiteixeiyeizejeejiejoekaekoeleelhelielkeloeluemaemd'
        'emeenaencendeneengenhenjenkenlenmennenpenqenrensentenxenyenzeoceogeoj'
        'eomeoneoseouepiepuepzeqeeqieraerbercerdereergerierkerlermerneroerteru'
        'erweryeseeshesuetaeteetietseudeuieumeunewuexaexiexoexueyaeyieyteyuezh'
        'ezufacfahfanfeifenfosfuafudfujfukfulfuqfusfuxfuyfuzgaagacgadgaegaggai'
        'gakgalgamgangaogaqgargasgatgawgaxgazgbagbigbugcagchgcogdagdegdigdogdu'
        'gedgeegeggejgekgelgengeogeugfagfeggaggeggogguggwggyghaghoghugiagimgja'
        'gjegjigjogjugkagkogkuglaglhgligloglugmagmegmygnagnegnggnigocgohgoigol'
        'gomgongoqgorgougovgowgoxgoygozgpigpogpugqegqigqogqugragregrigsagsegsh'
        'gtagtigtogtsgtuguagueguigujgukgulgumgunguogurguuguxguygwagwegwigwogxa'
        'gxigxogxugyagyegyigyogyugzagzhgzuhaahabhachaehaghahhaihajhalhamhanhao'
        'haphaqharhashathawhaxhayhazhbahbehdzheahebhecheehefhegheihejhekhelhen'
        'heohepheqherheshetheuhexheyhezhgahhohiahibhichidhiehifhighihhiihijhil'
        'himhinhiohiphiqhirhishiuhiyhizhoehohhoihojholhomhonhoohorhothouhovhow'
        'hshhsihtohuahubhuchudhuehughuhhuihujhukhulhumhunhuohurhuxhuzhwahwehwo'
        'hwuhyahyrhyuiadiagiahiajiakialiamianiaoiaqiasiawiaxiayiazibaibeibiibm'
        'ibuibxicaichidaideidiidoiduieciefieliemiesiexieyiezifaifeigaigeiggign'
        'igoiguigwigxigyihaiheihsihuihwiibiihiijiinijaijeijiijyikaikhikiikoiks'
        'ikyilailhiliiloiluimaimcimdimeimhimjimpinainbincindineinfinginhiniinj'
        'inkinlinminninpinqinrinsintinwinxinyinzioniowipeipiipuiqiiquirairbirk'
        'irniroirtiryisaishisoisuitaitoituiuaiueiugiujiuliuniupiuqiutiuyiuziwa'
        'iweiwoiwuixaixiixoixuiyaiyeiyiiyoiyuizhizujagjahjaijamjanjeajecjedjeh'
        'jejjeljenjeojeyjiajiejigjiljimjinjiojisjiujixjiyjizjomjonjoojorjuajue'
        'jumjunjuojurjydjyijyukadkagkaikalkamkankaokarkaskatkazkchkeekenkeskha'
        'khbkhekhokiakiukonkorkosksaktskuakubkuekugkuikumkunkuokurkuykwakyakye'
        'kyulaaladlaelaglahlailaklamlanlaolaslazlealebleclegleilellenlepleslet'
        'lgalgilgolhalholhulialiclielihliilijlillinlioliplislitliuliylizlkalma'
        'lmulodloglonlooloploulsaltalualublucludlueluflugluklullumlunluoluqlur'
        'lusluxluzmaamabmacmadmagmaimalmammanmaomaqmarmasmatmaymbambrmcamchmdo'
        'mdumedmeemeimemmenmeymgymhamhemiamidmiemigmilminmiomiqmirmismlimndmny'
        'modmogmoimokmolmommonmoqmormotmpamqemqumrimsamsemtomudmugmukmulmunmus'
        'muxmwomxomxumyamyemynmzonaanacnagnahnainajnalnamnannaonapnaqnarnaynba'
        'nbenbonbuncancenchnconcundandendindondundznedneenehneinemnenneuneynfe'
        'ngangbngcngdngengfnggnghngingjngknglngmngnngongpngqngrngsngtngungwngx'
        'ngyngznhanhonhunianidnienihninnioniunjinkankhnkonkunkynlinlonlunmenmi'
        'nmonmunnanndnngnninnonnsnnunonnornpinponqanqenqinqjnqunqwnronsansensh'
        'nsonsuntantintontsntunuanuenujnumnuonurnuunwenxinxonyanyenyinyonyunza'
        'nzenzhnzonzuoanobaobeobgobiobjobqobzochodaodiodooduogaogbogdoggogkogl'
        'ogmognogoogqogtoguogwogxogyogzohaoheohhohsoiboicoidoigoijoiloimoinois'
        'oiyojiokaokcokpolaolgoliolmolooluomaombomcomdomeomiomnomoompomromuona'
        'ondongonionjonponsontonuonyooeoomoonooyopioqeoqioqooquorborcordorgori'
        'orkorlormoroorqorrortorxoryosaoshosoosuotaotiotooucoudougoukouloumour'
        'ousouyowaowdowlowsoxioxooxuoyaoyioyooyuozaozhozupadpagpaipajpanparpaz'
        'pelpenpexpiapiepikpinpixpizpocpohpoipomponporpotpshpubpuepugpulpunpuq'
        'purpusputpuypuzpyeqabqagqaiqajqamqanqarqayqemqenqeqqerqiaqidqigqihqil'
        'qinqioqiqqitqiuqixqizqjiqoiqomqonquaqudqufqugqujqukqulqumqunquoqusqux'
        'quzqwarabracragrairakramranrasrawrayrbirburcardarderdirdorehrenrgargo'
        'rgurgyrhoriaribridrigrikrilrimrinripriqrisritriwrixrizrkarkhrlerlirlu'
        'rmarmermyrnarnlrnurolronrparqerqurrerrirshrtarterturuarubrudruerugrui'
        'rumrunruoruprusrutruuruzrvarwarxarxirxuryaryerynryorzhsacsadsagsaisam'
        'sansapsarsatsebsejselsenseosersetseusewshasheshgshishoshtshushysiasib'
        'sicsihsimsinsipsiusogsoisoksonsotsrassistasuasucsuesuisuksumsunsuosuq'
        'sursuwsuztactaetagtaitaktaltamtantaotartaytebtemtenteqtertiatietintir'
        'tobtogtoitoltomtontostoutowtsatsetsotsutsytuatuetugtultumtuntuoturtus'
        'tyitzatzetzotzutzyuaduaiualuanuayuazubaubbubeubiubtubzuchudaudeudiudo'
        'uduuejueluenuepuequerueyufaufeugaugcugkuglugouguugyuhauhbuhsuiauibuic'
        'uiduifuiguihuijuiluinuipuisuituiwuixuiyuizujaujeujiukaukhukoukyulaule'
        'ulgulhuliuloulsuluumaumbumcumdumeumgumiumqumsumuumxumzunaunbuncundunf'
        'ungunhuniunjunkunlunmunnunpunqunsuntunuunxunyunzuobuoduohuoluomuoouop'
        'uoyuozupaupsuqauqiuquuraurcurdurgurmurourpurqurruruusaushusuutautiuto'
        'utzuuluunuweuwouxauxiuxouxuuyauyiuytuyuuzauzhvaivalwacwafwagwahwanwaq'
        'warwaswatwaxwdzweiwenwipwodwoiwojwolwomwonwoowoswshwsowuawucwudwugwuh'
        'wujwukwulwumwuswutwuwwuxwuywuzxabxagxaixalxanxarxaxxayxenxexxiaxicxie'
        'xifxigxijxikxilxinxioxipxisxizxoaxobxogxoixokxonxuaxucxudxumxunxuzyaa'
        'yabyacyadyagyahyaiyakyalyamyanyaryasyawyaxyazydayduyedyeeyemyenyeoyer'
        'yetyewyibyicyidyigyihyiiyilyimyinyioyipyiryisyityiwyixyiyyizyliyngynu'
        'yogyonyoryrhytuyuayubyucyudyueyugyuhyulyumyunyusyuxyuyyuzzabzadzaizak'
        'zalzamzanzaozapzaqzarzaxzayzebzeezemzenzeszetzezzhazhezhizhozhuzibzig'
        'zinzirzitzixziyzoczoizonzoozouzuazuezuizunzuozuszuuzux'),
    5: ('aakabaabiachadaadoaebaezagaageagoaguahaahiahoaibaicaidaifaijaikaimain'
        'aioairaisaitaiwaizajiakaakeakiakkakoakuakyamaambameamiamoamuanaandane'
        'anganianjankanmannanoantanuanyanzaokaomapparaareariaruasaaseashasoasu'
        'ataateatoatsattaurawaayaayoazaazubambanbarbasbatbaybeobepbetbibbihbik'
        'binbirbizbokborbosbukbunbusbuybuzchichochudabdacdaidakdamdandatdawdaz'
        'degderdogdomdorebaebeebiechedoefuegaeguehaeiyekiembemuenbendenienneno'
        'enrenteokepperiesaeseeshetaetoetsetteyaezafucfuefujfukfunfurfusfutgah'
        'gajgakgamgangaogargasgatgaugawgaygergifgingobgojgorgosgotgoygucgujgur'
        'gusgyohabhachadhaghakhamhanharhashathayhekhibhichidhighihhijhikhimhin'
        'hiohirhishithiuhiwhiyhizhobhofhoghokhonhoshunhyuiasiawibaibeiboibuich'
        'idaideidoiedigaiguihaihiihoiidiigiihiimiiyiizijoikaikeikiikkikoikuiky'
        'imaimeimiimoimuinainginjinoinsinuinziobiogiojiokiomiosiotirairiiroiru'
        'iryisaiseishisoissisuitaitoitsittiuriwaiyaiyoizaizeizujiejiijimjinjio'
        'jirjisjiyjoejonjosjoyjukkabkadkagkahkaikakkamkankaokarkaskatkawkaykaz'
        'kedkegkehkesketkihkikkimkinkirkiskitkiykizkkakobkockodkofkogkohkojkok'
        'komkonkorkoskotkubkuckudkugkuhkujkukkumkunkuokurkuskutkuwkuykuzkyokyu'
        'mabmacmadmaemagmaimakmammanmarmasmatmazmbomegmejmeomermeymiamibmicmid'
        'migmihmikmimminmiomirmismitmiumiymizmobmodmogmonmoomormotmukmunmurmus'
        'mutmyonabnagnahnaknamnannarnasnatnawnaynaznbendanemnerneynezngonicnih'
        'niinikninnirnisnitniwnjunkonkynmannannunobnodnognohnoinojnoknomnonnoo'
        'nosnownoynshntantsnuknumnuynzanzeoakobaobeobioboochodaodeoetofuogaogo'
        'ohaoicoigoisoitojiokaokeokiokkokookuokyomaomiomoomuonaonbondoneonjonm'
        'onoonuookoomoraorioroosaoseoshosuotaoteotootsottoucowaoyaoyoozaporppo'
        'rabradragrakranrasratrayrazresreyriaribridrigrihrikrimriorisritriyrob'
        'roirorrosrotrozrugrumrunruorutryusabsadsagsahsaisaksamsansaosapsarsas'
        'satsawsaysebsehseiseksemsensessetshishoshusodsojsoksomsonsossshsubsuc'
        'sudsugsuisujsuksumsunsursussuusuwsuysuztaatabtactagtahtaitajtaktamtan'
        'tartastattawtebtenteytobtoctodtogtoitoktomtontootortostottoutowtoytsu'
        'ttottsubaubuuchudaueduefuenugaugiuhauitujiukaukiukuumaumiumounaunguni'
        'unjunkunnunounzuokuonuozuraureuriurouruusauseushusoussusuutautsuttuur'
        'uwauyauzauzeuzuwacwadwagwajwakwamwanwarwaswatwazyabyacyagyaiyakyamyan'
        'yasyatyawyazyoayodyohyokyonyooyoryosyotyubyufyugyukyuryusyuzzaizakzam'
        'zawzenzugzuhzukzumzunzuozurzuszuw'),
    6: ('aabaagaamaanaarabaabbabcabdabeabgabhabiabjablaboabrabsabuabyacaaccace'
        'achaciaclacnacoacqacracsactacuadaadbadcaddadeadfadhadiadjadladmadnado'
        'adqadradsaduadvadyaebaecaedaeeaefaegaehaelaemaenaepaeqaeraesaetaeuaev'
        'afaaffafiafnafraftafuagaagdageaggaghagiagkaglagmagnagoagragtaguahaahe'
        'ahiahoahuahyaiaaibaicaidaieaigaikailaimainaioairaisaitaiuaivaixaizaja'
        'ajeajuakaakeakhakiakkaklaknakoakraksaktakuakyalaalbalcaldalealfalgalh'
        'alialkallalmalnaloalpalralsaltalualvalyamaambamcamdameamiamlammamnamo'
        'ampamqamsamtamuamvamyanaanbancandaneanfanganhaniankanlannanoanqanrans'
        'antanuanxanzaodaoeaolaonaouapaapeaphapiaplapoappaprapsaptapuaquaraarb'
        'arcardarearfargarhariarkarlarmarnaroarparqarrarsartaruarvaryasaascase'
        'asgasiaskaslasmasnasoaspassastasuasvasyaszataatcateatgathatiatlatmato'
        'atqatrattatuatyatzaubaucaudaufaugaukaulaumaunauoaupaurausautauvauwaux'
        'auzavaaveaviavlavoavravuawaawhaxaaxeaxiaxoaxuayaaycaydayeaygaylaymayn'
        'ayraysaytayuayvayzazaazeaziazobabbacbadbaebafbagbahbaibajbakbalbamban'
        'bapbarbasbatbaubavbaxbaybazbbabbebbobbrbbubcabcrbdebdibdobdubeabecbed'
        'befbeibelbenbeoberbesbetbeubevbeybezbfabgabgebgrbhabhrbiabibbicbidbie'
        'bifbigbiibikbilbinbiobipbirbisbitbiubivbizbjebjublableblibloblublybmo'
        'bnebnobobbocbodbogboibokbolbombonborbosbotboubovbozbpebplbpobprbrabre'
        'bribrobrubsabscbsebsibsobsqbstbsubtebtibtububbucbudbufbugbuhbuibujbuk'
        'bulbunburbusbutbuxbuybuzbvabvebvibybbycbydbylbytbyzcaacabcaccadcaecaf'
        'cagcahcaicalcamcancaocapcarcascatcaucavcawcaycboccaccecchccicclccoccr'
        'ccuccycduceacebceccedcegceicelcemcenceocepcercescetceuchachechgchichl'
        'chochrchschuchyciacibciccidciecifcigciicilcimcinciocipcirciscitciuciv'
        'cizckackickockuclacleclicloclucmacnacnecnicnocnucoacobcoccodcoecofcog'
        'cohcoicokcolcomconcoocopcoqcorcoscotcoucovcqucracrecricrocrucrycsecta'
        'ctectictoctrctuctycuacubcuccudcuecufcugcuiculcumcuncupcurcuscutcuucuv'
        'cybcyccygcylcymcyncyocyrcytcyudabdacdaddaedagdaidakdaldamdandapdaqdar'
        'dasdatdaudavdaydbedbrdcidcrddaddeddiddrddudeadebdecdeddefdegdeidekdel'
        'demdendeodepderdesdetdeudevdewdexdeydfadfedfidfldgedgwdhadhudiadibdic'
        'diddiedifdigdikdildimdindiodipdiqdirdisditdiudivdizdjadjedjodjudledli'
        'dmedmidmodnadnidnodnudoadobdocdoddoedogdokdoldomdondopdoqdordosdotdou'
        'dovdoxdqudradredridrodrudrydsedsidsodstdsudtuduadubducdudduedukduldum'
        'dunduodupdurdusdutduuduvdvadvedvidvodygdyldymdypdyteabeaceadeafeageal'
        'eameaneapeareaseateaueawebaebbebdebeebiebleboebrebuecaeccecdeceecheci'
        'eckeclecnecoecqecrectecuedaeddedeediedlednedoedredueebeemeetefaefeeff'
        'efiefkeflefoefrefuegaegeeggegiegnegoegreguegwegyehaeheehiehoeiaeibeic'
        'eideieeigeileimeineioeipeireiseiteiueiveiweizejeejuekaekeekhekiekkeko'
        'eksekuelaelbelceldeleelfelgelielkellelmelneloelpelselteluelvemaembemc'
        'emdemeemiemlemmemnemoempemuemyenaenbencendeneenfengenhenienkenlenneno'
        'enqenrensentenuenweoaeobeoceodeofeokeoleoneopeoreoseotepaepeephepiepl'
        'epoeppeprepseptepuepyequeraerbercerdereerfergerherierjerkerlermernero'
        'erperqerrerserteruerverweryerzesaesbescesdeseesfesgesieskeslesmesneso'
        'espessestesueswetaeteethetietletnetoetretsettetueubeuceudeueeugeuieuk'
        'eumeuneupeureuseutevaeveevievoevuewaeweewiexaexbexcexeexfexhexiexkexl'
        'exoexpexqexsextexueyaeyfeyleymeyneyreyseyteyuezeeziezoezuezzfabfacfad'
        'faefagfaifalfamfanfarfasfatfaufavfeafebfecfeffeifelfemfenfeoferfesfet'
        'feufeyffaffeffifflffmffoffrffufiafibficfidfiefigfilfimfinfiofirfisfit'
        'fiufixfkaflafleflifloflufmafnafnifoafocfodfoefogfolfonforfosfotfoufov'
        'foxfrafrefrifrofruftmftoftufuafugfulfumfunfurfusfutgabgacgadgafgaggai'
        'galgamgangaogargasgatgaugavgawgaygazgdagdogeagebgecgeigekgelgemgengeo'
        'gergesgetgeugevgewggeggiggrggughdgheghhghtgiagibgicgidgiegifgiggihgil'
        'gimgingiogipgirgisgitgiugivgkiglaglegligloglugmagmegnagnegnignognugob'
        'godgoegoggoigolgomgongopgorgosgotgougovgragregrigrogrugthgtoguagucgue'
        'guigulgumgungupgurgusgutguuguvguygwagwigyagydgylgymgypgyrgysgythabhac'
        'hadhaehafhaghaihajhakhalhamhanhaohapharhashathauhavhaxhayhbrhdaheaheb'
        'hechedhegheihekhelhemhenheohepherheshetheuhevhewhexheyhgahhehiahibhic'
        'hidhiehifhighikhilhimhinhiohiphirhishithiuhivhizhlahlehlihlohmahmihmo'
        'hnahnohoahobhochodhoehofhoghoihokholhomhonhophorhoshothouhrahrehrihro'
        'hruhryhsehtehthhtlhuahubhuchudhughuihukhulhumhunhuohurhushuthuzhyahyb'
        'hydhyehyghylhymhynhyphyrhyshytiabiaciadiaeiagiaiiakialiamianiapiarias'
        'iatiauiavibaibeibiibliboibribuibyicaicciceichiciiclicoicqicricsicticu'
        'icyidaidcideidgidiidlidmidnidoidridtiduidyiebieciediegieliemieniepier'
        'iesietieuievifaifeiffifiiflifoifriftifuigaigeighigiigligmignigoigrigu'
        'igyihaihiiiaiilikaikeikhikiikoikriksiktikuilailbildileilfilgilhiliilk'
        'illilniloiltiluilvilwimaimbimcimeimiimmimnimoimpimqimsimuimyinainbinc'
        'indineinfinginhiniinjinkinlinminninoinpinqinrinsintinuinvinwinyinzioa'
        'iobiociodioeiokioliomioniopioqioriosiotiouipaipeiphipiiplipoippiprips'
        'iptipuiquirairbircireirgiriirkirmirniroirpirqirrirsirtiruirvisaisbisc'
        'isdiseisfisgishisiisjiskislismisnisoispisqisrissistisuisvisyitaiteith'
        'itiitnitoitritsittituiubiuciudiugiuliumiuniupiuriusiutiuviuxivaiveivi'
        'ivoivuiwaiweixaixiixoixtixuizaizeiziizoizujacjahjamjanjarjaujavjeajec'
        'jerjesjetjocjoejonjopjorjovjubjudjugjuijuljumjunjupjurjusjutjuvkabkad'
        'kaekagkaikalkamkankaokapkarkaskatkaukaykazkdekeakebkedkeikelkemkenkeo'
        'kepkerkesketkeukevkhakhekhikhokhrkiakidkiekilkimkinkiokipkirkiskitkiu'
        'kivkkakkeklakleklokmaknekniknokoakobkoikokkolkomkonkopkorkoskotkoukoz'
        'kphkrakrekrikroksakseksiksokstktektiktoktrkudkukkulkumkunkuokupkurkut'
        'kuvkuzkydkynkyrkyvlablacladlaelaflaglailaklallamlanlaolaplaqlarlaslat'
        'laulavlawlaxlaylazlbalbelbilbllbolbrlbulcalcelchlcilcolcrlctlculcylda'
        'ldeldhldildrldulealeblecledleeleflegleileklemlenleoleplerlesletleulev'
        'lexleylezlfalfilfrlfulgalgelgilgllgolgulhalhelholialibliclidlieliflig'
        'liklillimlinliolipliqlirlislitliulivlixlizlkalkelkhlkilkolkullallelli'
        'llollulmalmelmilmolmulnalnelnilnolnuloalobloclodloeloflogloiloklollom'
        'lonloploqlorloslotloulovloxlpalpelphlpilpolrelrilsalselsflsilsolstlsu'
        'ltalteltiltoltrltulualublucludluelugluiluklullumlunluplurluslutluuluv'
        'luxlvalvelvilvulwelyblyclydlymlynlyplyrlyslyvmabmacmadmaemagmahmaimak'
        'malmammanmapmarmasmatmaumavmaxmaymazmbambembimblmbombrmbumbymchmcimco'
        'mcumdimeamecmedmegmeimekmelmemmenmeomepmeqmermesmetmeumexmeymfimfomfu'
        'mgrmhemiamicmidmiemifmigmihmikmilmimminmiomipmiqmirmismitmiumivmixmle'
        'mlimmammemmimmommumnamnimnomnumobmocmodmoemogmoimolmommonmoomopmormos'
        'motmoumovmpampemphmpimplmpnmpomprmpsmptmpumqumremsomtamtimtomuamucmue'
        'mufmugmuimukmulmummunmuomurmusmutmuzmvemvimycmydmyimylmynmyomyrmysmyt'
        'nabnacnadnagnainajnaknalnamnannaonapnarnasnatnaunavnaxnaynbanbenbinbl'
        'nbonbrnbuncancbncenchncinclnconcrnctncundandendfndindondrnduneanebnec'
        'nednefnegneinelnemnenneonepneqnernesnetneunevnewnexnfanfenfinflnfonfr'
        'nfungangenginglngnngongrngtngungwnhanhinhonhunianicnidnienifnignihnii'
        'niknilnimninnionipniqnirnisnitniunivniznjenjunkenkhnklnkonkpnktnkunla'
        'nlenlinlonmanmonnannenninnmnnonnunobnocnodnofnoinoknolnomnonnopnornos'
        'notnounovnoxnpenplnprnqunrenrinronrunsanscnsensfnsgnsinslnsmnsnnsonsp'
        'nstnsunsvnsyntantenthntintontrntunuanubnucnuenuinuknulnumnunnuonupnur'
        'nusnutnuunvanvenvinvonwanwrnycnymnynnysnzenzinzuoacoadoaeoagoaloanoar'
        'oasoatoauobaobbobdobeobgobioblobnoboobrobsobtobuobvocaoccoceochociock'
        'oclocmocnocoocroctocuocyodaoddodeodiodnodoodroduodyoecoedoegoeioeloem'
        'oenoepoeroesoetoezofaofeoffofiofnofoofroftofuogaogeoggogioglognogoogr'
        'oguohaoheohiohoohuohyoicoidoieoifoigoikoiloinoiooiroisoitoizokaokdoke'
        'okhokiokmokookroksokuolaolbolcoldoleolfolgolholiolkollolnoloolpolsolt'
        'oluolvolyomaombomeomiommomnomoompomtomuomyonaonboncondoneonfongonionj'
        'onmonnonoonqonronsontonuonvonyoodookoopootopaopeophopioplopooppoprops'
        'optopuopyoquoraorborcordoreorforgorhoriorjorkorlormornoroorporqorrors'
        'ortoruorvoryosaoscosdoseosioskosoospossostosuosyotaoteothotiotmotootr'
        'otsottotuotyouaouboudouioukouloumounoupourousoutouxovaoveoviovoovuowa'
        'oweownowuoxaoxioxooxuoxyoynozaozeozopaapacpadpaepagpaipakpalpampanpao'
        'papparpaspatpaupavpaxpaypecpedpegpeipelpenpeopepperpespetpeupevpeypez'
        'phaphephiphlphnphophrphtphuphypiapicpidpiepifpigpikpilpimpinpiopippir'
        'pispitpiupixpizplaplepliploplupnapnipnupoapobpocpodpoepoipokpolpompon'
        'popporpospotpoupowppappeppipplppopprppupraprepriproprupsapsepsipsopsu'
        'psyptapteptiptoptrptuptypubpucpudpuepugpulpumpunpuppurpusputpuupycpyd'
        'pygpylpyrpytpyupyxquaquequiquoqurquuquyraarabracradraerafragrahrairaj'
        'rakralramranraprarrasratrauravraxrayrazrbarberbirborburcarccrcerchrci'
        'rclrcnrcorctrcurcyrdarderdirdordrrdsrdurdyrearebrecredreerefregrehrei'
        'rejrekrelremrenreorepreqrerresretreurevrewrexreyrezrfarferfirflrforfr'
        'rfurgargerghrgirglrgorgrrgurgyrharherhirhorhurhyriaribricridrierifrig'
        'riirikrilrimrinrioripriqrirrisritriurivrixrizrjarjerjurkarkerkhrkirko'
        'rktrkurlarlerlirlorlurmarmbrmermirmormurnarnernirnornuroarobrocrodroe'
        'rofrogrohroirokrolromronroproqrorrosrotrourovrowroxroyrparperphrpirpl'
        'rporprrptrpurqurrarrerrhrrirrorrurryrsarscrsersirsorsprstrsurtartertg'
        'rthrtirtmrtortrrtsrturtyruarubrucrudruerufrugruhruirukrulrumrunruorup'
        'rurrusrutruuruvruxruyruzrvarvervirvorvurwiryirylrymrynryprysrytrzirzo'
        'sabsacsadsaesagsaisaksalsamsansapsarsatsausavsaxsaysbasbosbrsbusbysca'
        'sceschscisclscoscrscuscysdasdosdrsduseasebsecsedsefsegseisekselsemsen'
        'seosepseqsersessetseusevsewsexseysfasfesfosfrsgasgesgisgosgrshasheshi'
        'shoshrshusiasibsicsidsifsigsiksilsimsinsiosipsirsissitsiusivsizsjuska'
        'skeskhskisklskoskuskyslasleslismasmesmismosmusmysnasnesnisnosnysocsof'
        'soisoksolsomsonsoosopsorsossotsousovsozspaspesphspisplsposprspusqusra'
        'sresrossassesshssissossustastdstesthstistostpstqstrstsstustysuasubsuc'
        'sudsuesufsuisulsumsunsuosupsursussutsuusuvsvasveswasweswoswusybsycsyl'
        'synsypsyrsyuszetabtactadtaetaftagtaitajtaktaltamtantaotaptaqtartastat'
        'tautavtaxtaytchtditeatebtectedteftegteiteltemtenteotepteqtertestetteu'
        'tevtexteytgatgetgrthathbthethithlthmthnthothrthsthuthytiatibtictidtie'
        'tiftigtihtiktiltimtintiotiptiqtirtistittiutivtiztlatletlitlutmatmetmo'
        'tnitoatoctodtoftogtoltomtontoptortostottoutovtowtoxtpotqutratretritro'
        'trutrytsetsottattetthttittottrttutuatubtuctudtuetuftuituktultumtuntuo'
        'tupturtustuttuutuvtuxtwityltymtyntyptyrtyttyutzuuabuacuaduaeuagualuam'
        'uanuapuaquaruasuatuaxuazubaubbubcubdubeubfubhubiubjublubmubnuboubpubr'
        'ubsubtubuubvucauccuceuchuciuclucnucoucructucuudaudeudgudiudmudnudoudr'
        'udsuduudyueauebueduefueiueluemuenueoueruesuetueuuezufaufeuffufiufouft'
        'ufuugaugdugeuggugiugmugnuguuhtuhuuiauibuicuiduieuiguihuiiuiluimuinuio'
        'uipuiruisuituiuuivujeukaukeukhukiukkuklukoukruksuktulaulculduleulfulg'
        'uliulkullulmulnuloulpulrulsultuluulvumaumbumcumeumfumgumhumiummumnumo'
        'umpumqumrumtumuumvunauncunduneunfunguniunnunounqunsuntunuunxunzuoduom'
        'uonuopuoquoruosuotuouuovupaupeuphupiuplupouppupruptupuuraurburcurdure'
        'urfurguriurkurlurmurnurourpurqurrursurturuurvusausbuscusduseusgushusi'
        'uskuslusmusouspusqussustusuuswutauteuthutiutlutoutputruttutuuuauueuva'
        'uveuviuvouvuuwauxauxeuxiuxouxtuxuuyauyluysuzauzeuzivabvacvadvaevafvag'
        'vaivalvamvanvapvarvasvatvauvavveavecvehveivelvemvenvervesvetveuvexvia'
        'vibvicvidvievigvilvimvinviovipvirvisvitviuvivvixvlovoavobvocvokvolvom'
        'vonvorvosvotvouvovvravruvulwacwadwaewafwagwaiwalwamwanwapwarwaswatwau'
        'wavwaywdewdiweaweewegweiwelwenwerweswexweywhawhewhiwiawicwiewigwikwin'
        'wiswitwixwnswodwolwrdwrewudwulwykwymwynwytxacxaexalxamxanxarxatxbaxbr'
        'xcaxcexcixclxcoxcrxcuxelxemxenxeqxerxesxfrxhexhixhoxiaxibxicxidxifxig'
        'xilximxinxioxipxirxitxiuxkixlexodxogxoixonxorxosxouxpexpixplxpoxprxpu'
        'xquxsaxscxsexsixspxstxtextixtoxtrxtuxuaxulxupxurxusxybxylxysyaeyagyal'
        'yanyaryasybaybeybiyblycayceychyciyclycnycoyctycuydaydeydnydoydryelyem'
        'yepyerygeygiyglygmygnygoyiayinykeylayldyliyllyloyltyluylvymaymbymeymi'
        'ymnympymuynayncyndyngyniynoyntynuyonyotypaypeyphypiypoypryptypuyrayre'
        'yrgyrhyriyrmyrnyroyrtyruysayscysdysiysoystysuyteythytiytoytryttytuyul'
        'yuryveyviyvuyxiyzayzizabzaczaezakzalzamzanzarzatzeizelzenzepzeszetzeu'
        'zeyziazibzigzikzilzinziuzizzobzomzonzopzoszotzouzubzuczunzurzuszyg'),
    7: ('aacaagaalaamaanaaraasabaabdabeabhabiablabnaboabrabuabyacaaccaceachaci'
        'ackaclacoacqacractacuadaadcaddadeadfadhadiadladnadoadradsadtaduadyaeg'
        'aelaemaenaeoaeraesaetaeuaevafaaffafoaftafuagaagbageagfaggaghagiagjagn'
        'agoagraguagyahaaheahhahoahraiaaicaidaieaigaikailaimainaioaipairaisait'
        'aiuaizajaajeajjajoakaakeakhakkaklakoakraksakvakyalaalbalcaldalealfalg'
        'alhalialkallalmalnaloalpalsaltalualvalyamaambamdameamfamiamlammamnamo'
        'ampamsamtamuamwanaanbancandaneanfanganhanianjankanlanmannanoanransant'
        'anuanvanyanzaodaoeaomaotapaapeaphapiaplapoappaprapsapuapyaquaraarbarc'
        'ardareargarhariarjarkarlarmarnaroarparqarrarsartaruarvarwaryarzasaasb'
        'ascasdaseashasiaskaslasmasoaspassastasuasvataatcateatfathatiatlatoatr'
        'atsattatuatzaucaudaueaugaukaulaumaunaupaurausautavaaveaviavlavoavrawa'
        'awbaweawkawlawnawrawsawtaxaaxbaxeaxiaxmaxoaxtayeaygaylaymaynayoaytayw'
        'azaazeaziazoazuazzbaababbacbadbaebagbakbalbambanbapbarbasbatbaubawbbi'
        'bbobdebdibeabebbecbedbeebehbeibelbenberbesbetbeubevbewbexbezbhabhibho'
        'bhrbhubiabicbidbiebifbigbilbinbiobirbisbitbiublableblibloblybnobobboc'
        'bodboebogboibojbolbonbooborbosbotboubovbrabrebribrobrubrybucbudbuebuf'
        'bujbukbulbunbuqburbusbuxbybbydbylbymbyrbytbyzcaacadcaecagcaicalcamcan'
        'capcarcascatcaycclccrccuceacebceccedcehcelcencepcercescetchachcchdche'
        'chfchichlchmchochrchuchwchyciacidcifcilcimcincirciscitciuckbckeckfckh'
        'ckicklcknckpckrckscktckwclaclecliclocluclycnicoccodcogcolcomconcopcor'
        'coscotcoucowcqucracrecricrocrucrycsoctactictoctrctucubcucculcumcuncup'
        'curcuscutcuzcygcylcymcyncyocyrcytdacdaedagdahdaidajdakdaldamdandapdar'
        'dasdaudavdawdaydbadbedbrdbudcadcoddeddiddlddoddudeadebdecdefdeideldem'
        'dendepderdesdetdeudevdewdfodgadgedgndgwdhadhodhudiadicdiddiedigdihdik'
        'dildimdindiodisditdiudixdjidladledlidlodmadmidmodnadnednidocdoddohdol'
        'domdondordosdoudovdowdpadpodprdradredridrodrudsadsedsgdshdsodstdswdto'
        'duadubducdudduedukduldumdundurdusdwadwidwodymdysdzoeaceadeafeaheakeal'
        'eameaneapeareaseateauebaebbebdebeebhebiebleboebrebuecaecceceechecieck'
        'ecoectecuedaedbedceddedeedfedgedhediedledmednedoedreduedweedeeleeneep'
        'eeseetefaeffefiefkefoefregaegeeggeghegiegnegoegregyehaeheehiehoehreib'
        'eideieeigeijeileimeioeireiseiteiuejeekaekeekielaelbeldeleelfelgelielk'
        'ellelmeloelpelselteluelvelwelxelyelzemaembemeemfemiemmemoempemsemuemy'
        'enaenbencendeneenfengenhenienjenkenlennenoenpenrensentenuenvenwenzeob'
        'eodeoheoleomeoneopeoreoteoueovepaepeephepiepoeppeprepseptepuepweqoequ'
        'eraerbercerdereerfergerherierkerlermerneroerperqerrerserteruerverwery'
        'esaesbescesdeseesfesgeshesieslesmesnesoespesqessestesuesveswetaetbetc'
        'eteetfethetietoetretsettetuetweuaeubeuceugeukeuleuneupeureuseutevaeve'
        'evievuewaewbewcewdeweewhewiewjewkewlewmewoewpewqewsewtewyexaexbexhexi'
        'exlexmexteyaeybeyceykeymeyneyteywezbezeezhezifaefaifakfalfanfarfasfau'
        'favfayfazfeafelfenferffaffeffhffiffoffrfhafiefilfinfirfkaflaflefliflo'
        'fnafocfolfonforfowfrafrefrifrofteftoftufulfunfurfutgaagabgacgadgaegai'
        'gakgalgamgangapgargasgatgaygazgbegbogbrgdegdigdogefgeigelgemgengeogep'
        'gergesgetgewgfigfoggeggigglghaghbghdghlghoghtghughwgiagibgiegilgingio'
        'gipgirgitgiugjygkoglaglegligloglygnegnmgnogntgnugodgojgolgomgongoogor'
        'gosgotgougpogragregrigrogrugsbgsegstgtogtrguagueguigulgumgurgusgwagwe'
        'gwogyagydgypgyrgythaahabhachadhaehafhaghaihakhalhamhanhapharhashathau'
        'havhawhaxhayhazhbehbohbrhbuhcahchhcohdahdeheahebhechedhefhegheihelhem'
        'henheohepherheshetheuhexheyhfihflhfohgahhahiahibhichidhiehifhighilhim'
        'hinhiohiphirhishithiuhiyhkehlahlehlihlohluhmahmihmohnihnnhnohnuhobhoc'
        'hodhoeholhomhonhoohophorhoshouhowhpohrahrehrihrohryhsehtlhtohtrhuahud'
        'hughulhumhunhuphurhushuthvihwahwehwihwohyahybhydhyehyghylhymhyohyphyr'
        'hytiabiaciadiagiakialiamianiapiariasiatiauibaibeibiiboibribuicaiceich'
        'iciickicoicricticuicyidaidciddideidgidhidiidlidmidnidoidpidridsiduidw'
        'idyiegielienierietieuievifaifeiffifnifoifriftigaigeiggighigiignigoigt'
        'iguihaiheihuijiikaikiikoilailbildileilfiliilkillilmilnilsiltiluilvilw'
        'ilyimaimbimeimiimmimoimpimsimuinaincindineinfinginhiniinkinninoinsint'
        'inuiociogiolioniopioriosiotiouiowipaipeiphiplipoippipsiptiquiraircire'
        'irfirgiriirkirlirmiroirrirsirtiruirvisaisbiscishisiiskislismisoisriss'
        'istisvitaitbitciteitfithitiitnitoitrittituitwiuciuliuniurivaiveiviivy'
        'ixhixiixoixsiyaizaizeiziizojacjaijakjamjanjapjarjasjavjeajefjenjerjes'
        'jevjibjikjiljimjinjirjjajoajodjoejohjoljonjorjosjovjoyjuajubjudjukjul'
        'junjupjusjyokabkadkalkamkankarkaskatkavkaykbukbykeakeckegkehkeikekkel'
        'kemkenkepkerkesketkevkewkeykfakfikfokgrkhakhikhokhukidkiekilkimkinkio'
        'kipkirkivkjakkiklaklekliknaknekniknoknukobkokkolkomkonkopkorkoskotkou'
        'kpokrakrikrokryksbkshksoksvkswktaktokuakumkurkuskuwkvakwakydkylkynkyr'
        'laalablacladlaelaflaglahlailaklallamlanlaolaplarlaslatlaulavlawlaylaz'
        'lbalbelbilbolbrlbulcelchlcilcolculdbldeldfldhldildoldrldslealeblecled'
        'leelefleglehleilejlellemlenleoleplerlesletleulevlewlexleylfalfolfrlga'
        'lgilgrlhalialibliclielifliglihliklillimlinlioliplirlislitliulivlixliz'
        'lkelkglkllksllallellillollslltllullylmblmdlmelmilmllmolmslmulnelnilnw'
        'loclodloeloflogloilollomlonlooloplorloslotloulovlowloylpelphlptlsalsb'
        'lsclsdlselshlsilsolstlsulswltaltbltelthltiltlltoltrltwlublucludluiluk'
        'lullumlupluslutluxlvalvelvilwalwelwolwylxilyblyclydlyklymlynlyolyplyr'
        'lyslytlywlzemabmacmadmaemagmahmaimajmakmalmammanmapmarmasmatmaumaxmay'
        'mbambembhmbimblmbombrmbumcamchmckmdamdumecmedmegmeimejmekmelmemmenmep'
        'mermesmetmexmezmfomiamicmidmigmikmilmimminmiomipmirmismitmiumivmlemli'
        'mmammemmimmomnemnimnomnumobmocmodmogmolmonmoomormosmotmoumpampemphmpi'
        'mpompsmptmpumsbmsemsgmskmslmstmswmtamucmuemulmunmurmusmwomyamycmylmyn'
        'myomyrmysmytnaanabnacnadnaenafnagnahnainaknalnamnannaonapnarnasnatnau'
        'naxnbanbenbonbrnbuncancenchncincknclnconcundandbndendfndhndindlndondp'
        'ndrndsndundwndyneanebnecnedneenehneinelnemnenneonepnernesnetneunevnew'
        'nfinflnfonfrngangbngdngengfnggnghngingknglngpngrngsngtngungwngynhanhe'
        'nhonianicnidnienifnignilninnioniqnirnisnitniunjanjonjunkankenklnkonkr'
        'nlenmanmonnannenninnonnsnnynoanobnocnodnoinolnomnoonopnornosnotnovnox'
        'nponrinronrynsansbnscnsensfnshnsinslnsonstnsvnswnsyntantentfntgnthnti'
        'ntlntnntontpntrntsntuntwnuenumnunnurnusnutnuunuwnvenvinwinwonymnysnyu'
        'nyvnzanzooadoakoanoavobaobbobeobioboobuobyocaoceochociockoclocoocroct'
        'ocuodaodboddodeodiodlodmodnodoodsoduoeboedoemoenoeooezofioftogaogdoge'
        'oggogiognogooguohaohiohnoinoisoitojookaokeokiokkoklokyolaolbolcoldole'
        'olgoliolkollolmolnoloolsoltoluolvolyomaombomcomeomfomiomlommomnomoomp'
        'omsomuomyonaonboncondoneonfongonhonionjonkonnonoonronsontonvonyonzood'
        'oogookooloorootopaopeophopiopjopoopropsopuoraorborcordoreorforgoriork'
        'orlormornoroorporqorrorsortoruorvorworyosaosboscoseoshosioskoslosposs'
        'ostosuoswotaoteotfotgothotiotlotnotootrottougouioulounoupourousoutouv'
        'ouxoveoviowaowbowcowdoweowlowmownowsoxaoxeoxvoyaoycoydoynoyooysoznozo'
        'paapacpadpaepagpaipalpampanpapparpaspatpaupavpazpeapecpedpegpeipekpel'
        'pempenpeoperpespetpezphaphephiphlphnphophrphuphypiapicpidpiepilpimpin'
        'piopirpispitpiupixpizplaplepluplypocpoipolpomponpoopopporpospotpoyppe'
        'ppipplppopraprepriproprupsapsbpsepshpstpswpsyptepthptiptoptupucpudpue'
        'pulpunpuppurpusputpwopydpygpylpyopyrpyxqedqiaquaquequiquurabracradrae'
        'rafragrahrairajrakralramranrapraqrarrasratrauravrawraxrayrazrbarberbh'
        'rbirborbrrburcarcerchrcircorcurcyrdardbrderdirdordsrdurdwrearebrecred'
        'reeregrehreirekrelremrenreorepresretreurevrewreyrfirforfrrfurgargergi'
        'rgorgurgyrharherhirhorhurhyriaricridrierifrigrihrijrikrilrimrinriorip'
        'riqrisritriurivrixriyrizrjarjorkarkbrkerkhrkirksrlarlbrlerlirlorlsrlt'
        'rmarmermirmormsrmurnarnbrncrndrnernfrnhrnirnjrnlrnornsrntrnuroarobroc'
        'rodroerogroirokrolromronrooroprorrosrotrourovrowroxroyrozrparperphrpi'
        'rporprrpurqerqurrarrerrhrrirrorryrsarsdrsersfrshrsirslrsorstrsurtartc'
        'rtertfrthrtirtlrtmrtnrtortrrtsrturtwrtyrtzrubrucrudrufrugrunrurrusrut'
        'rvarvervirvorvurwarwerwirworyarydryerygryhrylrymrynryprysrytrzasaasab'
        'sacsadsafsagsaisaksalsamsansaosapsarsassatsausawsaxsbasbesbosbrsbusca'
        'sceschsciscoscrscuscysdasdesdosduseasebsedsefseiselsemsenseosepserses'
        'setseusevsexseysfisfosgasgrshashbshdsheshfshishkshlshmshnshoshrshtshu'
        'shvshysiasicsidsilsimsinsiosipsirsissitsiuskaskeskisklskoslasleslislo'
        'smasmesmismosmysnasnosofsogsohsoisolsomsonsopsorsotsousovsowsoysozspa'
        'spespisposprsqusrassassessisslssossussystastbstcstesthstistjstlstmsto'
        'stpstrstustvstwstysuasucsudsuhsuksumsunsursussutsuvsuzsvesviswasweswi'
        'swosyasybsycsylsyrsystaatabtactadtaetaftagtaitaktaltamtantaptartastat'
        'tautavtawtaytbotbutchtcitcoteatebteftegtehteiteltemtenteoteptertestet'
        'teutevtewtexteytfatfitfotgotgrthathbthcthdthethfthgthithlthmthothpthr'
        'thsthuthwthytiatibtictidtiftigtiltimtintiotiptirtistittiutivtjotlatle'
        'tlitlotmitmotnatnetnotoctodtoftoitoktoltomtontoptortottoutowtoxtoytpa'
        'tratretritrotrutsbtsdtsetsftsotsvtsyttattetthttittlttottsttutuctultum'
        'tunturtuwtvatvitwatwhtwitwotyltymtyntyrtzetzitzuuadualuanuaruayubbube'
        'ublubuucauccuceuchuciuckucrucsucuudaudbuddudeudgudhudiudludrudsuebuee'
        'uehueluenueruezuffuflugbugeughugluguuhmuieuiluinuisuitukaukeukhukiukk'
        'ukouktulaulculduleulguliullulmuloulpulsuluulvulwumaumbumeumiumoumpumu'
        'unauncunduneunguniunnunsuntunwupauphupiupouppupruptupuuquuraurburcure'
        'urfurgurhuriurjurmurnurourpurrursurturuuryusauscuseushusiusoussustuta'
        'uthutoutsuttutuuuluveuwauxbuxeuxfuxtuzauzevabvadvalvanvapvarvasvatved'
        'vegvelvenvepvervesvetviavicvidvievilvinviovirvisvitviuvivvizvlovokvol'
        'vonvrevrivrovulvybwadwafwaiwalwanwarwaswatwauwaywbiwbowbrwbuwcawcewde'
        'wdlwedwelwemwenweswetweywhawhiwicwidwigwilwimwinwirwiswitwivwjewkewki'
        'wlawlewliwlywmawmewnewnhwnswobwokwolwooworwotwpowquwrawrewsawsbwstwte'
        'wtowtrwymwyoxanxapxboxbrxemxenxetxezxfaxhaxhixiaxicxidximxinxiuxlexmi'
        'xmoxmuxouxstxtaxtextoxviyadyakyalyanyaryasyatyavybayblybrybuyceychyci'
        'ycoydeydiydnydoydryelyenyeoyeqyetygeygiygnyhiykjylayleyliyllyloylsylv'
        'ymeymiymnymoympymuyndyneyniynnynsyntyolyomyonyoryotypeypoypsyptyrayrc'
        'yreyrgyriyrmyrnyroyrryrtyruysiysnysoyspyssystytcythytiytoytryueyvayve'
        'yvoywaywoyxiyzayzozabzaczagzahzakzanzapzavzawzazzbezebzelzenzepzetzez'
        'zhezhozikzimzinzioziuzoazomzonzopzupzuzzza')}

with open('letter_map.json', 'r') as f:
    NEXT_CHAR_MAPPING = json.load(f)

# r8 / r14 are the registers containing the seed before this function is called


def hprint(x):
    print(hex(x))


def bittest(val, n):
    """ Return the n^th least significant bit of val. """
    return (val >> n) & 1


def split_seed(seed):
    """ Returns the low (last 4 bytes) and high (first 4 bytes) of the seed.
    """
    return LOBYTES(seed), HIBYTES(seed)


def join_seed(low, high):
    return (high << 0x20) + low


def update_seed(seed):
    low, high = split_seed(seed)
    return CONST * low + high


def HIBYTES(seed):
    return seed >> 0x20


def LOBYTES(seed):
    return seed & 0xFFFFFFFF


def flip_chunk(chunk):
    """ Reverse the byte order of a chunk and return the numeric representation
    of that number.
    Ie. abc -> cba -> 0x63 0x62 0x61 -> 0x636261
    """
    val = 0
    for i, char in enumerate(chunk):
        val += ord(char) << 8 * i
    return val


def compare_chunk(subject, comparand):
    """ Returns -1, 0, or 1 depending on whether the subject (our chunk) is
    smaller than, equal, or greater than (respectively) the comparand (the
    chunk we wish to compare to)
    """
    our_chunk = flip_chunk(subject)
    cmp_chunk = flip_chunk(comparand)
    if our_chunk > cmp_chunk:
        return 'ja'
    elif our_chunk == cmp_chunk:
        return 'jz'


def get_chunk(seed, n):
    rdx = update_seed(seed)
    rcx = LOBYTES(rdx)                  # get last 4 bytes of this
    rax = (len(STRINGS[n]) // 3) * rcx
    rax = HIBYTES(rax)                  # strip off lower 4 bytes
    rax *= 3
    chunk = STRINGS[n][rax:rax + 3]     # load the actual chunk
    # construct new seed from previous seed an calculation of chunk
    new_high = HIBYTES(rdx)
    new_seed = join_seed(rcx, new_high)

    return chunk, new_seed


def determine_letter_a(data, weight):
    # Mapped from function at 0x140816350
    keys = list(data.keys())
    if len(keys) == 1:
        return keys[0]
    else:
        possibilities = len(keys)
        # Technically the following has some funky logic involving getting the
        # sign of something, but I am pretty sure the weight is always
        # positive, so the value will always be 0, so we can just add a half to
        # it.
        new_weight = (possibilities - 1) * weight + 0.5
        # get the integer part
        idx = int(new_weight)
        # Then select this element from the list
        next_letter = keys[idx]
        return next_letter


def determine_letter_b(data, weight):
    # Mapped from function at 0x140816300
    letters = list(data.keys())
    acc_weights = list(accumulate(data.values()))
    for i in range(len(letters)):
        if acc_weights[i] >= weight:
            return letters[i]
    return letters[-1]


def parse_branch(data, chunk, weight, picker_func):
    """ Recursively parse a branch. """
    if isinstance(data, list):
        for (check_chunk, sub_data, jump_type) in data:
            if compare_chunk(chunk, check_chunk) == jump_type:
                return parse_branch(sub_data, chunk, weight, picker_func)
    elif isinstance(data, dict):
        # parse the weighted letter dictionary
        return picker_func(data, weight)


def gen_next_char(chunk, weight, choice, picker_func):
    first_char = chunk[0]
    branch = NEXT_CHAR_MAPPING[str(choice)]
    letter_branch = branch[first_char]
    return parse_branch(letter_branch, chunk, weight, picker_func)


def ROL_8(val, shift):
    # Left roll value by amount `shift` for a 64 bit (8 byte) value
    return ((val << shift % 64) & (2 ** 64 - 1)
            | ((val & (2 ** 64 - 1)) >> (64 - (shift % 64))))


def ROL_4(val, shift):
    # Left roll value by amount `shift` for a 64 bit (8 byte) value
    return ((val << shift % 32) & (2 ** 32 - 1)
            | ((val & (2 ** 32 - 1)) >> (32 - (shift % 32))))


def ROR_8(val, shift):
    # Right roll value by amount `shift` for a 64 bit (8 byte) value
    return (((val & (2 ** 64 - 1)) >> shift % 64) |
            (val << (64 - (shift % 64)) & (2 ** 64 - 1)))


def add64(a, b):
    """ Perform addition as if we are on a 64-bit register. """
    return (a + b) & 0xFFFFFFFFFFFFFFFF


def capitalize_if_required(func):
    def wrapper(*args, **kwargs):
        trans_word = func(*args, **kwargs)
        word = args[0]
        if word[0].lower() != word[0]:
            return trans_word.capitalize()
        return trans_word
    return wrapper


def insert_letter_at_idx(word, letter, idx):
    """ Returns word `word` with `letter` inserted at index `idx`. """
    return word[:idx] + letter + word[idx:]


def prepare(word):
    r11 = rbx = 0x72C085E2EE7C6F27
    # rdx = word[:4]
    length = len(word)
    # The following line is equivalent to length % 0x20
    mod_length = length & 0x1F  # If length <= 31 this does nothing
    r10 = rax = 0xDEADBEEFDEADBEEF
    if length > 0xF:
        # do somthing... Not yet mapped sorry...
        # This looks like is does some kind of squashing of the word down to
        # 16 characters
        pass
    r10 = (length << 0x38) + rax
    # We use mod length here because it may be modified in the above un-mapped
    # code.
    if mod_length <= 8:
        rax += flip_chunk(word)
    else:
        r10 += flip_chunk(word[8:])
        rax += flip_chunk(word[:8])
    r10 = r10 ^ rax
    rax = ROL_8(rax, 0xF)
    r10 = add64(r10, rax)
    rbx = rbx ^ r10
    r10 = ROR_8(r10, 0xC)
    rbx = add64(rbx, r10)
    r11 = r11 ^ rbx
    rbx = ROL_8(rbx, 0x1A)
    r11 = add64(r11, rbx)
    rax = rax ^ r11
    r11 = ROR_8(r11, 0xD)
    rax = add64(rax, r11)
    r10 = r10 ^ rax
    rax = ROL_8(rax, 0x1C)
    r10 = add64(r10, rax)
    rbx = rbx ^ r10
    r10 = ROL_8(r10, 0x9)
    rbx = add64(rbx, r10)
    r11 = r11 ^ rbx
    rbx = ROR_8(rbx, 0x11)
    r11 = add64(r11, rbx)
    rax = rax ^ r11
    r11 = ROR_8(r11, 0xA)
    rcx = rax = add64(rax, r11)
    # After here the symmetric repeating operation breaks
    r10 = r10 ^ rax
    rcx = ROL_8(rcx, 0x20)
    rcx = add64(rcx, r10)
    rax = rcx
    rcx = rcx ^ rbx
    rax = ROL_8(rax, 0x19)
    rax = add64(rax, rcx)
    r11 = r11 ^ rax
    rax = ROR_8(rax, 0x1)
    seed = rax      # I *think* this is the actual seed we want...
    # rax = add64(rax, r11)
    # rax register contains one seed value
    # rbx has some number
    # rcx has another seed
    # r9 points to a memory location which contains rax in 8 bytes, then the
    # capitalised version of the word in the next... 0x10.
    # r10 and r11 are probably just intermediate variables.
    return seed


def get_next_letter(seed, chunk, trans_idx, picker_func):
    seed = update_seed(seed)
    weight = LOBYTES(seed) * TINYVAL
    return gen_next_char(chunk, weight, trans_idx, picker_func), seed


@capitalize_if_required
def translate(word, race):
    """ main translation function. """

    rbx = prepare(word)
    rax = 0
    rcx = LOBYTES(rbx)
    rcx = ROL_4(rcx, 0x10)
    seed = rax = LOBYTES(rbx)  # bottom part of seed
    rax = rbx
    rax = rax >> 0x20
    rcx = rcx ^ rax
    rcx = LOBYTES(rcx ^ rbx)
    seed = seed + (rcx << 0x20)

    trans_idx = LANG_MAPPING[RACES[race]]
    chunk, seed = get_chunk(seed, trans_idx)

    translated_word = chunk

    seed = update_seed(seed)
    cl = seed & 0xFF
    if cl & 1:
        picker_func = determine_letter_a
    else:
        picker_func = determine_letter_b
    seed = update_seed(seed)
    rax = LOBYTES(seed) * 3  # check val is static?
    r8 = len(word) - 1
    rcx = r8 - 3
    rax = rax >> 0x20
    rax += rcx
    letters_required = ((LOBYTES(seed) * 3) >> 0x20) + len(word) - 4

    if letters_required <= 0:
        # dummy for now. Need to finalise too
        return chunk

    for _ in range(letters_required):
        next_char, seed = get_next_letter(seed, chunk, trans_idx, picker_func)
        if next_char:
            translated_word += next_char
            chunk = translated_word[-3:]
        else:
            extra_letter = finalize_no_last_letter(translated_word, seed,
                                                   letters_required, trans_idx,
                                                   picker_func)
            if extra_letter:
                translated_word += extra_letter
            # We are done in this case...
            break
    hprint(seed)
    translated_word = finalise(translated_word, seed)
    return translated_word
    # if cl & 1: sub_140816350, else: v8 = sub_140816300


def check_consecutive_consonants(word):
    """ Return the start location of where there are 3 consecutive consonants.
    """
    consecutive_consonants = 0
    for idx, letter in enumerate(word):
        if consecutive_consonants != 3:
            if letter not in VOWELS:
                consecutive_consonants += 1
            else:
                consecutive_consonants = 0
        else:
            if letter not in VOWELS + ('y',):
                return idx - 3
            else:
                consecutive_consonants = 0
    # If we don't have any then return None.
    return


def finalize_no_last_letter(word, seed, letters_added, trans_idx, picker_func):
    retries_left = 7  # this is technically 8, but by the time we get here we
    # need to decrement it by one anyway
    # r15 = letters_added - 1
    if letters_added == 0:
        # dummy
        return
    while retries_left:
        # TODO: there is a check here for r13 being less than letters_added
        # Need to figure out where r13 gets its value.

        # In this case another letter is needed to be added so the translation
        # index is incremented and we try and get a new letter...
        chunk = word[-3:]
        trans_idx = (trans_idx + 1) % 8
        next_char, _ = get_next_letter(seed, chunk, trans_idx, picker_func)
        if not next_char:
            retries_left -= 1
        else:
            return next_char
    return


def finalise(word, seed):
    """ This function may add a number of extra letters to make the final word
    more... reasonable...?"""
    first_letter = word[0]
    second_letter = word[1]
    compare_const = 0b100000100000100010001  # filter to pick out vowels
    first_letter_idx = ord(first_letter) - 0x61
    second_letter_idx = ord(second_letter) - 0x61

    if (first_letter not in VOWELS) and (second_letter not in VOWELS):
        # loc_140B5136E
        if first_letter != 's':
            if second_letter == 'h':
                # loc_140B5143B
                pass
            elif second_letter == 'l':
                # loc_140B51418
                pass
            elif second_letter == 'r':
                # loc_140B513F5
                pass
            elif second_letter == 'w':
                # loc_140B513DB
                pass
            elif second_letter == 'y':
                mod_char = ord(first_letter) - 0x68
                if mod_char <= 0xA:
                    if chr(mod_char) in ('a', 'f', 'k'):
                        # loc_140B51498
                        pass
                    else:
                        # default (def_140B51416)
                        seed = update_seed(seed)
                        rax = LOBYTES(seed)
                        rax = (5 * rax) >> 0x20
                        new_letter = VOWELS[rax]
                        word = insert_letter_at_idx(word, new_letter, 1)
                        # loc_140B51498
                        if len(word) < 2:
                            # def_140B514F2
                            pass
                        else:
                            last_letter = word[-1]
                            second_last_letter = word[-2]
                            print('hi')
                            if ((second_last_letter != 'g') or
                                    (((ord(last_letter) - 0x61) < 0x14) and
                                     last_letter in VOWELS)):
                                # loc_140B514DA
                                eax = LOBYTES(0xFFFFFF9E + ord(last_letter))
                                if eax <= 0x15:
                                    idx = check_consecutive_consonants(word)
                                    if idx is not None:
                                        seed = update_seed(seed)
                                        r8 = LOBYTES(seed)
                                        seed = update_seed(seed)
                                        rcx = (5 * LOBYTES(seed)) >> 0x20
                                        idx += ((3 * r8) >> 0x20) + 1
                                        new_letter = VOWELS[rcx]
                                        word = insert_letter_at_idx(
                                            word, new_letter, idx)
                                else:
                                    # default
                                    pass
                            else:
                                pass

                else:
                    # default (def_140B51416)
                    pass
            else:
                # default (def_140B51416)
                pass
    else:
        # loc_140B51498
        pass

    return word


if __name__ == "__main__":
    word = "Nanites"
    race = 'explorers'
    trans_word = translate(word, race)
    print(f'"{word}" translates to "{trans_word}"')
