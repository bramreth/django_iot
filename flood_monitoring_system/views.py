from django.shortcuts import render
from flood_monitoring_system.models import environmental_agency_flood_data, MqttWaterLevelData, Notifications
# Create your views here.
query = {}
query['api_data'] = environmental_agency_flood_data.get_newest("")
print(query['api_data'])
query['sensors'] = MqttWaterLevelData.get_newest("")
query['sensors_all'] = MqttWaterLevelData.get_all("")
query['notifications'] = Notifications.objects.all().order_by("-date")
query['flood_area'] = []

flood_area_coordinates = [
            [
              1.084671034348597,
              51.283542731778795
            ],
            [
              1.084644887425557,
              51.28356905404535
            ],
            [
              1.08451602945395,
              51.28357245144711
            ],
            [
              1.084608629408154,
              51.28349804999732
            ],
            [
              1.084596517240304,
              51.28348937770115
            ],
            [
              1.084621405294923,
              51.28321879267623
            ],
            [
              1.084257480699097,
              51.28313849764722
            ],
            [
              1.084231229038449,
              51.283175201544324
            ],
            [
              1.084147129984873,
              51.28320440246753
            ],
            [
              1.084145324428069,
              51.28317746617876
            ],
            [
              1.08407894116123,
              51.28317921614433
            ],
            [
              1.084055951975669,
              51.283125854393546
            ],
            [
              1.084098255381052,
              51.28311718170661
            ],
            [
              1.084101780442281,
              51.28311214033945
            ],
            [
              1.08409787337223,
              51.283111482584204
            ],
            [
              1.083966293375296,
              51.283074250084546
            ],
            [
              1.084005634660266,
              51.28301924525652
            ],
            [
              1.083871748178668,
              51.282947594873846
            ],
            [
              1.083910703290474,
              51.28288682824187
            ],
            [
              1.083674253298672,
              51.282812109140885
            ],
            [
              1.083583376403459,
              51.282814504427094
            ],
            [
              1.083492032723288,
              51.28284389582948
            ],
            [
              1.08340843834497,
              51.28281911515472
            ],
            [
              1.083328804210855,
              51.28285343071456
            ],
            [
              1.083395278532721,
              51.28290041363926
            ],
            [
              1.08327002631665,
              51.28295759247134
            ],
            [
              1.083304873123822,
              51.28283550653973
            ],
            [
              1.083145829161556,
              51.28277206831558
            ],
            [
              1.08320903029106,
              51.282689451087904
            ],
            [
              1.083188591557074,
              51.28266300584378
            ],
            [
              1.082972292430889,
              51.282695689816805
            ],
            [
              1.082908211607348,
              51.282724362331
            ],
            [
              1.08298788407644,
              51.28259979231754
            ],
            [
              1.082959719763553,
              51.28254201528572
            ],
            [
              1.082725731170563,
              51.28254028362647
            ],
            [
              1.082602289683917,
              51.28262448786042
            ],
            [
              1.08256309019088,
              51.28267948846992
            ],
            [
              1.08246291522878,
              51.28273609563291
            ],
            [
              1.082435895806815,
              51.28270982364569
            ],
            [
              1.082097693177761,
              51.28279968550743
            ],
            [
              1.082058349760196,
              51.2828546897309
            ],
            [
              1.081909435074117,
              51.28283162877256
            ],
            [
              1.081858984948214,
              51.282859941631884
            ],
            [
              1.081755880915678,
              51.28283567371077
            ],
            [
              1.081707659682323,
              51.28275599229413
            ],
            [
              1.081660956345178,
              51.28270325475053
            ],
            [
              1.081492756407042,
              51.28276165287209
            ],
            [
              1.081145532551081,
              51.28271683021061
            ],
            [
              1.081056021109942,
              51.28266521982823
            ],
            [
              1.081052413684675,
              51.28261134708881
            ],
            [
              1.081224221282164,
              51.28260682233048
            ],
            [
              1.081199863284895,
              51.28249952835321
            ],
            [
              1.081223986735665,
              51.28241794139896
            ],
            [
              1.081499300446983,
              51.28236673280365
            ],
            [
              1.081410434627205,
              51.28234732737757
            ],
            [
              1.081289575654885,
              51.28229770056146
            ],
            [
              1.081284871295594,
              51.28222745075281
            ],
            [
              1.081104046553633,
              51.28209729372381
            ],
            [
              1.080935848056656,
              51.28215569102417
            ],
            [
              1.080870575320854,
              51.28223836154963
            ],
            [
              1.080731872706511,
              51.28220998584272
            ],
            [
              1.080659837520923,
              51.28215014543242
            ],
            [
              1.080755220220833,
              51.2820263134808
            ],
            [
              1.080665514932461,
              51.28197392271604
            ],
            [
              1.080601348824152,
              51.281837502524816
            ],
            [
              1.080505011730489,
              51.28184322966697
            ],
            [
              1.080438249695447,
              51.28179059200513
            ],
            [
              1.080565179213592,
              51.28176060382524
            ],
            [
              1.08066184188758,
              51.281704180717604
            ],
            [
              1.081040402964344,
              51.28166722784456
            ],
            [
              1.081082387051288,
              51.281734699498045
            ],
            [
              1.081115832842842,
              51.28178844929647
            ],
            [
              1.081384176428125,
              51.281782809142506
            ],
            [
              1.081357665258905,
              51.281729270093976
            ],
            [
              1.081089890463988,
              51.281638940678704
            ],
            [
              1.081069017144964,
              51.281574160304835
            ],
            [
              1.08104178224615,
              51.28153227214695
            ],
            [
              1.081105512877978,
              51.281476625994905
            ],
            [
              1.081057151116261,
              51.28139694802153
            ],
            [
              1.080988981535972,
              51.28141015037222
            ],
            [
              1.080815316699309,
              51.28131108220841
            ],
            [
              1.08070389879993,
              51.281259778895496
            ],
            [
              1.080823492710677,
              51.28119525580252
            ],
            [
              1.080663060463284,
              51.281110503418496
            ],
            [
              1.08051829854547,
              51.28106034751558
            ],
            [
              1.080623638538757,
              51.28096358716208
            ],
            [
              1.080552232445862,
              51.28092453462009
            ],
            [
              1.080339283835873,
              51.28095712556046
            ],
            [
              1.080268798697839,
              51.280864455705384
            ],
            [
              1.080234286367418,
              51.2806741065201
            ],
            [
              1.080105817442586,
              51.28068319807864
            ],
            [
              1.080058285375322,
              51.28061373349038
            ],
            [
              1.08030682693583,
              51.28047227041212
            ],
            [
              1.080303220669382,
              51.28041839761445
            ],
            [
              1.080170764881765,
              51.280367917285844
            ],
            [
              1.080233186179254,
              51.28024018075616
            ],
            [
              1.079780610491037,
              51.280324221020294
            ],
            [
              1.079596080729418,
              51.280164235283024
            ],
            [
              1.079509292165077,
              51.280193638478615
            ],
            [
              1.079296390394637,
              51.279970874874806
            ],
            [
              1.079209569239844,
              51.27993176843759
            ],
            [
              1.079301440271791,
              51.27984228519695
            ],
            [
              1.079095421635929,
              51.27975636061237
            ],
            [
              1.079027077526572,
              51.27975530476625
            ],
            [
              1.078966059496043,
              51.27972503229185
            ],
            [
              1.078695748655278,
              51.27954325899268
            ],
            [
              1.078380689035184,
              51.2793356787112
            ],
            [
              1.078287583590963,
              51.27923019311278
            ],
            [
              1.078362669811013,
              51.27906631417586
            ],
            [
              1.078183931115369,
              51.2789648819569
            ],
            [
              1.078521850626477,
              51.278873238430954
            ],
            [
              1.078822490205532,
              51.278865326845164
            ],
            [
              1.078782619554564,
              51.278731319994165
            ],
            [
              1.078459601990827,
              51.27862812396514
            ],
            [
              1.078189309666371,
              51.278707799713914
            ],
            [
              1.078160387781196,
              51.27861291092478
            ],
            [
              1.078153180759449,
              51.27850516507703
            ],
            [
              1.078319307182573,
              51.27839446080767
            ],
            [
              1.078136977456804,
              51.27839765593244
            ],
            [
              1.078058126738554,
              51.278372656760595
            ],
            [
              1.078052727699436,
              51.27829193715211
            ],
            [
              1.078090270601193,
              51.27820999775898
            ],
            [
              1.078217312580913,
              51.27817967121766
            ],
            [
              1.078129758246682,
              51.278154991052915
            ],
            [
              1.078253053322538,
              51.27807079531513
            ],
            [
              1.078154866405448,
              51.277999473058905
            ],
            [
              1.078158149133291,
              51.27793837308258
            ],
            [
              1.078149140586594,
              51.27780369075652
            ],
            [
              1.077980953619083,
              51.277862083642425
            ],
            [
              1.077850309275203,
              51.27783853697048
            ],
            [
              1.077674916065757,
              51.27778918352551
            ],
            [
              1.077661721081596,
              51.277716651766916
            ],
            [
              1.077535265376278,
              51.27763095409761
            ],
            [
              1.077241680852522,
              51.277744255953955
            ],
            [
              1.077161346457391,
              51.277829677009784
            ],
            [
              1.077143257535857,
              51.27771892073237
            ],
            [
              1.076931950125302,
              51.277644907743756
            ],
            [
              1.076599419785957,
              51.27779039841218
            ],
            [
              1.076336481440539,
              51.27771645131443
            ],
            [
              1.076209296240694,
              51.277746779578536
            ],
            [
              1.076032247741081,
              51.27767048335248
            ],
            [
              1.076069650651498,
              51.2775885483123
            ],
            [
              1.075892459836675,
              51.27751225562281
            ],
            [
              1.076053988025424,
              51.277411129921745
            ],
            [
              1.075836910173387,
              51.277324829120445
            ],
            [
              1.075697404344886,
              51.2771665038044
            ],
            [
              1.075692009675302,
              51.27708578400028
            ],
            [
              1.075591442173105,
              51.2769606132419
            ],
            [
              1.075460930908241,
              51.27684900425936
            ],
            [
              1.075408553270916,
              51.27670900544707
            ],
            [
              1.07520049299894,
              51.2766152396259
            ],
            [
              1.07506001132264,
              51.27664367238873
            ],
            [
              1.074743188480939,
              51.276409145054224
            ],
            [
              1.074691238160408,
              51.27627550120613
            ],
            [
              1.074429967730244,
              51.27622848993314
            ],
            [
              1.074208590792144,
              51.27610946013923
            ],
            [
              1.074131137376272,
              51.27626323673879
            ],
            [
              1.074229631091693,
              51.276449625456756
            ],
            [
              1.074100791776187,
              51.276453011063815
            ],
            [
              1.073865818643043,
              51.276243314442176
            ],
            [
              1.073644342558355,
              51.27606024660273
            ],
            [
              1.072632685414969,
              51.275324457407784
            ],
            [
              1.071199617456531,
              51.27488319548251
            ],
            [
              1.071486327921995,
              51.27469222772389
            ],
            [
              1.071362122336818,
              51.27452732144613
            ],
            [
              1.071029559480214,
              51.274543526222665
            ],
            [
              1.070988296009725,
              51.27429509850845
            ],
            [
              1.070760993112185,
              51.27411217831389
            ],
            [
              1.070369102700156,
              51.27404151289399
            ],
            [
              1.070184884848233,
              51.27385737085337
            ],
            [
              1.069839397566871,
              51.2738395434841
            ],
            [
              1.069560183483131,
              51.2740595039053
            ],
            [
              1.068706684681422,
              51.27362640727834
            ],
            [
              1.067955110449349,
              51.27337189059702
            ],
            [
              1.067736780676929,
              51.27327407176335
            ],
            [
              1.06745082385936,
              51.27323228795159
            ],
            [
              1.065899050699231,
              51.27280955614436
            ],
            [
              1.065297549795102,
              51.272836546296624
            ],
            [
              1.064929288879695,
              51.27310480548737
            ],
            [
              1.064574978498988,
              51.272952184770126
            ],
            [
              1.06393062166022,
              51.272618273248376
            ],
            [
              1.06346194704526,
              51.27238769303439
            ],
            [
              1.063052156407017,
              51.27204763397778
            ],
            [
              1.062526583947912,
              51.2719332023481
            ],
            [
              1.062446831039142,
              51.272132557976384
            ],
            [
              1.061907610190723,
              51.27267159979396
            ],
            [
              1.060108920824734,
              51.27185874754543
            ],
            [
              1.059998985208232,
              51.2715261528985
            ],
            [
              1.059246317592342,
              51.27169819353025
            ],
            [
              1.059047724856096,
              51.27199051247317
            ],
            [
              1.058918896180786,
              51.27199388116701
            ],
            [
              1.059229709177165,
              51.27153793504189
            ],
            [
              1.058478728126016,
              51.27184348719039
            ],
            [
              1.054296353834292,
              51.27365224284644
            ],
            [
              1.062230821902879,
              51.27553556369486
            ],
            [
              1.067013372183303,
              51.27799888764762
            ],
            [
              1.068936911420752,
              51.27836952131935
            ],
            [
              1.070655035044461,
              51.2789720497246
            ],
            [
              1.071231770162132,
              51.279529878547486
            ],
            [
              1.071666233559878,
              51.2792962940585
            ],
            [
              1.072138884318062,
              51.279931495271924
            ],
            [
              1.072371760908833,
              51.2801952180967
            ],
            [
              1.072795950554918,
              51.28081915628985
            ],
            [
              1.072676082957324,
              51.28088880534671
            ],
            [
              1.072891740038341,
              51.281111899211446
            ],
            [
              1.072516491746568,
              51.28128371797225
            ],
            [
              1.07283292879971,
              51.28136604290813
            ],
            [
              1.073239719223093,
              51.281471872660276
            ],
            [
              1.073453453198105,
              51.28144704602498
            ],
            [
              1.073581199903218,
              51.28155648068396
            ],
            [
              1.073520656250832,
              51.28163516870015
            ],
            [
              1.073568839460175,
              51.28167486954575
            ],
            [
              1.07362856229374,
              51.28161924290517
            ],
            [
              1.073846780345535,
              51.28166756727478
            ],
            [
              1.074009627244966,
              51.28179820770898
            ],
            [
              1.074155371819266,
              51.281778398100705
            ],
            [
              1.074400938700534,
              51.28196468883767
            ],
            [
              1.074390992049093,
              51.28208500881427
            ],
            [
              1.074761394151842,
              51.282112266395934
            ],
            [
              1.075016591964207,
              51.28211555320546
            ],
            [
              1.075305578983087,
              51.28224985813289
            ],
            [
              1.075489347111427,
              51.28224018859006
            ],
            [
              1.075524606749019,
              51.282324925542206
            ],
            [
              1.075613443537485,
              51.282349700472494
            ],
            [
              1.075821725480461,
              51.28224715563282
            ],
            [
              1.076126769738437,
              51.28244413992711
            ],
            [
              1.076904078723361,
              51.28299036012714
            ],
            [
              1.076958909427782,
              51.283166853013945
            ],
            [
              1.078261130514396,
              51.28398004839741
            ],
            [
              1.078487861112895,
              51.284104649548055
            ],
            [
              1.078533412021956,
              51.28418875482932
            ],
            [
              1.079050295832677,
              51.28457310951977
            ],
            [
              1.079156536780973,
              51.28452314665477
            ],
            [
              1.079290519336474,
              51.284573588025204
            ],
            [
              1.079624415096269,
              51.28441911039361
            ],
            [
              1.080271859131713,
              51.28502405863177
            ],
            [
              1.080589201304438,
              51.28492404456876
            ],
            [
              1.080749477709463,
              51.28515580801141
            ],
            [
              1.080842601293799,
              51.28526129125952
            ],
            [
              1.080637874081405,
              51.2853677857692
            ],
            [
              1.080688957616007,
              51.28553508572988
            ],
            [
              1.08069617839286,
              51.28564292097859
            ],
            [
              1.080837374119044,
              51.28573252522944
            ],
            [
              1.081011286607159,
              51.285850404134244
            ],
            [
              1.081194271511913,
              51.28601406590458
            ],
            [
              1.082669219229304,
              51.28726389075784
            ],
            [
              1.086545181978292,
              51.28815998922585
            ],
            [
              1.087175252377897,
              51.28850101887306
            ],
            [
              1.087659084214656,
              51.28860696852469
            ],
            [
              1.087736339715402,
              51.28866980998674
            ],
            [
              1.088035389817728,
              51.28877259544135
            ],
            [
              1.088171675429612,
              51.288898758893566
            ],
            [
              1.088496751002241,
              51.28902594743979
            ],
            [
              1.088669098073927,
              51.28931730571175
            ],
            [
              1.088867536442967,
              51.28942091819232
            ],
            [
              1.089132518174978,
              51.2895218585888
            ],
            [
              1.088971537243844,
              51.289688010446866
            ],
            [
              1.088978771029507,
              51.28979575502842
            ],
            [
              1.089317004303365,
              51.28970578472632
            ],
            [
              1.089243896952687,
              51.28989669138347
            ],
            [
              1.089426438892865,
              51.290053775645305
            ],
            [
              1.089555457662778,
              51.290050369651674
            ],
            [
              1.089542796448333,
              51.289861816733435
            ],
            [
              1.089834175258874,
              51.2896921309686
            ],
            [
              1.090138783064184,
              51.289765129096175
            ],
            [
              1.09047451282052,
              51.28970229538818
            ],
            [
              1.090689202182919,
              51.28964445539397
            ],
            [
              1.090706285983563,
              51.28988506115166
            ],
            [
              1.090946181279053,
              51.290024641852085
            ],
            [
              1.091200243423163,
              51.29007436348651
            ],
            [
              1.091360063636886,
              51.28996533499674
            ],
            [
              1.091841157130995,
              51.29012491973154
            ],
            [
              1.091603317311095,
              51.290428025864756
            ],
            [
              1.091752104559333,
              51.29072091713446
            ],
            [
              1.091551789379099,
              51.290942079792856
            ],
            [
              1.09159160530946,
              51.291534581786436
            ],
            [
              1.091944161828566,
              51.29166043490954
            ],
            [
              1.092283629656315,
              51.292126456339254
            ],
            [
              1.092290321379845,
              51.2923257257482
            ],
            [
              1.092687008033228,
              51.292777030245475
            ],
            [
              1.092672327681328,
              51.29302108658673
            ],
            [
              1.093017370395166,
              51.29290031201699
            ],
            [
              1.092863794657928,
              51.29317405252996
            ],
            [
              1.093177195124239,
              51.29335456582754
            ],
            [
              1.093372077649908,
              51.29305259329032
            ],
            [
              1.093238213914668,
              51.2927673322932
            ],
            [
              1.093462987005517,
              51.2928734770272
            ],
            [
              1.094202980763497,
              51.293246587075146
            ],
            [
              1.094536348406976,
              51.29369305879221
            ],
            [
              1.095006945599339,
              51.293684051973585
            ],
            [
              1.095870178257272,
              51.29552547728518
            ],
            [
              1.097458019409192,
              51.29620965068122
            ],
            [
              1.099091235334907,
              51.296814023429995
            ],
            [
              1.102814169561976,
              51.29731341580826
            ],
            [
              1.105825236246089,
              51.29774174965372
            ],
            [
              1.107259459894895,
              51.29794662298414
            ],
            [
              1.107720049421305,
              51.29839311869478
            ],
            [
              1.112037403624923,
              51.29922282695448
            ],
            [
              1.11430079959985,
              51.29959442602636
            ],
            [
              1.11508331617202,
              51.29970836163781
            ],
            [
              1.11544971498118,
              51.29964721869694
            ],
            [
              1.115758020006087,
              51.29950160320273
            ],
            [
              1.116615517814857,
              51.299451786088355
            ],
            [
              1.116903502101074,
              51.29925522852398
            ],
            [
              1.11608932748215,
              51.29703117794096
            ],
            [
              1.116177012935224,
              51.296792282718044
            ],
            [
              1.118444573736949,
              51.29566694775837
            ],
            [
              1.119083239347416,
              51.294582925009564
            ],
            [
              1.118608686612807,
              51.29456850100481
            ],
            [
              1.118338139372429,
              51.29438691369267
            ],
            [
              1.116698528694988,
              51.29406559763177
            ],
            [
              1.115585950289567,
              51.2937856328675
            ],
            [
              1.114993247682624,
              51.29343730994785
            ],
            [
              1.11482154553963,
              51.29315513762231
            ],
            [
              1.114693897203885,
              51.293323671441144
            ],
            [
              1.112600308197136,
              51.2954571554222
            ],
            [
              1.110571192862986,
              51.29472858244112
            ],
            [
              1.108758768502173,
              51.294021201395886
            ],
            [
              1.107832916480256,
              51.293695006174936
            ],
            [
              1.107291905539201,
              51.29333159979338
            ],
            [
              1.10746711115716,
              51.29217469990205
            ],
            [
              1.105857847508832,
              51.29178970047242
            ],
            [
              1.103463014111782,
              51.29244610897266
            ],
            [
              1.101356752791839,
              51.29182398684922
            ],
            [
              1.100335446990533,
              51.292713928375015
            ],
            [
              1.096877598376162,
              51.291754864889185
            ],
            [
              1.09640290455261,
              51.291407509585724
            ],
            [
              1.095586126735884,
              51.290781508657616
            ],
            [
              1.095088210067543,
              51.29041699661775
            ],
            [
              1.094527935693704,
              51.29040483287503
            ],
            [
              1.094051766961178,
              51.29036345837273
            ],
            [
              1.093435666851428,
              51.289616214664946
            ],
            [
              1.09271948024218,
              51.289094198704554
            ],
            [
              1.091925886470835,
              51.28882760769769
            ],
            [
              1.090512776516924,
              51.28765066808028
            ],
            [
              1.090212082887672,
              51.287658610645714
            ],
            [
              1.08868465490161,
              51.286700540143315
            ],
            [
              1.087755236767033,
              51.28631778643463
            ],
            [
              1.087900682874586,
              51.285797189336094
            ],
            [
              1.087577097238585,
              51.285585996941954
            ],
            [
              1.087543189398027,
              51.285421325132624
            ],
            [
              1.087559720513235,
              51.28532707036394
            ],
            [
              1.087429015661362,
              51.285303017780535
            ],
            [
              1.087434236803712,
              51.28515444092376
            ],
            [
              1.087084330686781,
              51.285296413054574
            ],
            [
              1.086995893918833,
              51.285260997052966
            ],
            [
              1.087031618546827,
              51.28515211884066
            ],
            [
              1.086593864390564,
              51.28504102161655
            ],
            [
              1.086712287340076,
              51.28494453489686
            ],
            [
              1.086425169999325,
              51.28473574827559
            ],
            [
              1.086522378570514,
              51.2846147179878
            ],
            [
              1.086476415074984,
              51.284573121530165
            ],
            [
              1.086390508038423,
              51.284575387855526
            ],
            [
              1.086428040618976,
              51.284493446026836
            ],
            [
              1.086295560458963,
              51.28444288319024
            ],
            [
              1.086168513086176,
              51.284473308468634
            ],
            [
              1.085989472457991,
              51.284370095653365
            ],
            [
              1.085722450100146,
              51.28426920313119
            ],
            [
              1.085693505711917,
              51.28417699218724
            ],
            [
              1.085665984078164,
              51.284037842814804
            ],
            [
              1.085524147340501,
              51.284027310642266
            ],
            [
              1.085572182381989,
              51.28392237577314
            ],
            [
              1.085402176918545,
              51.28395384324687
            ],
            [
              1.085310995267736,
              51.28387529622146
            ],
            [
              1.085116880917187,
              51.2838596386668
            ],
            [
              1.084890666146602,
              51.28377844469073
            ],
            [
              1.084911633444189,
              51.28369694015425
            ],
            [
              1.084905307742245,
              51.283602594774116
            ],
            [
              1.084731744819145,
              51.28351279615124
            ],
            [
              1.084671034348597,
              51.283542731778795
            ]]

def clean_flood_area():
    for coord in flood_area_coordinates:
        rev = [coord[1], coord[0]]
        query['flood_area'].append(rev)
        print(rev)
clean_flood_area()

def index(request):
    return render(request, 'flood_monitoring_system/index.html', {"object_list":query})

def notifications(request):
    return render(request, 'flood_monitoring_system/notifications.html', {"object_list":query['notifications']})

def test(request):
    return render(request, 'flood_monitoring_system/test.html', {"object_list":query})


