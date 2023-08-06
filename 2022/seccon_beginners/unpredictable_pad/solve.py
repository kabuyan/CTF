import random
from Crypto.Util.number import *

oracle1 = -7254423520209206832320254898223319629760149898405282925618312218461459471094756618260349716919604057186947599256667397764683695284422637340310533871597876197947964121239240575240280432438180660572458214359557866837423686175078868057783832325089277410902770591604106387640236781218422212075501472418141226132372605742414695580201013352573017494849074628349207376167806264011895725566299040362818077681202143167444713449260572422305747223181939216003045655575410100014234175846522417051154741073837675627683148036487450140914676247421994917769407847070234019191798136176442497603553662676866998269965778426342095768015840650655540227403864968706088867929209480305342677396841768438185494372927832180444233089368570370458794524818665889074150936222786937130900949195956161690407369917799038795918480304641438498929530753259837926860065850917821935935032422806976151119025576455143690218171604603809731306570433261539876473222548847859157040142774470053198923763261105498094834157947085346978825183420727558734280141107869425954825773244078181450724509579377154131326594214468663921315332418650878566984276491647729240697883865025934075732262199760280686291574443262371765483288580280052984459326898268492024620309898679845501023921036071020527426157715936292369567350089542873800402752701359275364125901013844799868772220465274586232010897427775508005786404554833902003595382935123024022316254971067312791968578851487983563307149532768813516345840189785585070242823959569745236550343591466750937895917193985332392340870239461885420332233310679605215195515468011082077083581370563022842782862291852797792708873486542607354017061811952037931584626369989673471374469427202893817804554889736853577636718857769872489458606302442592371774846364650666570375159166313819279616086772476824188568404031330179554541581183045732993047423903865386219332252822020358737333602446554440737278670021624276625669172338970918395690323820050930481380873965619007658024011828964610396105723577093688074337234847750401389630598
oracle2 = -311428590899933115109019464886308046214015282056463660826002421170185829180762516028799135757345260517087519055794520061324170737492414425833785152471072686954232741910671903931131551046574171628055180515597411023078204815821372716383251025619397529689710076118946770117737530376700027310005601149345054988958161522288926660119822311859508027388512365995359125535795769042913716113746968272032980696864587000949068866376351028657342558039306353378374912723141251340933855309004011622838302780137641017427816859092241247104891770636614314649774279231449459440559197476884187064529428210462535829767769430759537523817510037741779354722529698998845629112647717184857025848422390133284129229129166618713995368875633809457484841019129917983374751248772095099603977249996055652032805773598405662740085109131421280279638544871548360275905635613125220463912714305090703859407051814887579480838881340525509486819404354636900069675901492782508760363165133493766462873618131786327387413362106935135214315267089100555287293531979797645058927127655283498616474647896544401038689172217351901794047036576108688668638588522785564466880812862800015792927757007650972979253400382357917746668738748047742951942945916366887784448473868308434985052881456261958680595666866978566297188161412785348102332997173185619801653182096722681080559031112178454731941904348515351674451066260871304964238788172809255360150851432687988899366660732063479941732863410348306372684220482866144496352978799672384999943721716184407224814947105716641059833340853494516183016988518937117605697697860820820740124619796790380827734853686010085674331119278256921053887872801595367898406384588941050957031553668450529079939129609539630007836930811959619748930654927612928046750591128988776439730101882477582560056239927910373460862657604025040518265142571123197246328170176318357162846608109343137611365822028473588925217071776382231297313622448190515514678460765723313274903691162335276544730889045217658690618310709166526564682934138801812181756422
oracle3 = -50323165696580143096107304097208447812870302603548633356600711484565016854261868571982922540440569692697077974186230699534819474919650311653201052732179552379035544370038752473285042823108169073020052049525368362620068356780228940637899668765389827146023667424798888944349663141455676265458598141686516639570301519968418322819035360092358733358104708508043078334277033883176775189427790624764034363826951415777207144313011187215682718667109683919382427136567669548295921322770534615343448193802644180292929807157147899479137687190837421780462754063714578021136055630058181173780796614763394565953373798599777337403277106596542693690353538125150505572298244623961840792378504151176574324413190696939677188934075915593902311951699708006874357175745814959030055706482676127792779648739517299131802650875896810019853953799974955874577893772165123765896925322043886845963704236814503899610017489335978967254659895763130837665399429954152816188437824860471346753188834014842426866743008675774697085933520345960456941309212027472127295317213502226567892710719798722321070451964510692923930193375619121347472267065654966741640462632755247870575027649456801227905449783132840021128951095428536999941245429557468755372842402515475687380889814610109465925902361489217989337661396406800412629206452133573844733014406590889076701205714060716522296940447014438520265430741982050707456829124268852683685018745646052964197840690307318880044435570275406972523802013512114762752253992611978884812867677626750781313237616773981707483611495546319419363332725176419136846998323254737933051377826467727990758712487662497707567328830518345677506158591473226844037785320957594891328270581240272848045945326290770268554788721011954549968831869338877209331870747058166252383308150136571371053776619834520009173130033274447971984165430546363041101787462533970922344179551714945154858163078167504988311892448574203393301592242082358881168104314956317737760252931612911916450153579277591997308054036951765635934550468690151384217115
inp = -(2**6656-1)  # 6656=32*624//3
enc = 310363849385076574991137514498377643144439964090238812333333700512633915

def left_unshift(x, shift, mask):
    i = shift
    y = x
    while i < 32:
        y = x ^ ((y << shift) & mask)
        i += shift
    return y 

def right_unshift(x, shift):
    i = shift 
    y = x
    while i < 32:
        y = x ^ (y >> shift)
        i += shift
    return y

rnd = random.Random()
numbers = []

for oracle in [oracle1, oracle2, oracle3]:
    x = oracle ^ inp
    for i in range(6656//32):
        numbers.append(x&0xffffffff)
        x >>= 32

for i in range(len(numbers)):
    num = numbers[i]
    num = right_unshift(num, 18)
    num = left_unshift(num, 15, 0xefc60000)
    num = left_unshift(num, 7, 0x9d2c5680)
    num = right_unshift(num, 11)
    numbers[i] = num

state = tuple(numbers + [624])
rnd.setstate((3, state, None))
x = rnd.getrandbits(enc.bit_length()+1)
print(long_to_bytes(x^enc))