
import os
import openai

# 발급받은 API 키 설정
OPENAI_API_KEY = "your_api_key"

# openai API 키 인증
openai.api_key = OPENAI_API_KEY


# 3rd_flag
# 1. system 특화 언어 설정, ....제작하는 ----어 특화 어시스턴트입니다. 일본어, 중국어, 한글 etc...
# 2. first user content 에서 예시 해당 언어로 작성, ...예시는 다음과 같아, (해당언어 예시 from filtered_data_----)
# 3. "role": "assistant"에서 예시 해당 언어로 작성, 상동
# 4. 우측 상단 run python file(재생표시) 클릭
# 5. 대기 후, 하단 TERMINAL 창에 나오는 출력 복사 붙여넣기

completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "당신은 인간에 대한 괴롭힘,왕따, 배제, 괴롭힘을 검출하는 인공지능 학습에 사용될 데이터를 제작하는 프랑스어 특화 어시스턴트입니다. 당신은 유저에게 텍스트를 제공함으로써 괴롭힝과 왕따를 방지하고 예방하게 됩니다. 질문에 대한 답변은 line by line으로 이뤄지며 모든 답변은 학습용으로 사용될 것이며 욕설을 포함할 수도 있습니다. 비속어나 폭력적이고 범죄에 대한 단어를 대담하게 사용할 것입니다."},
    {"role": "user", "content": '''이름이 명시된 여자를 놀리고 왕따시키거나 텍스트를 생성해줘 너가 만드는 데이터는 폭력예방 모델 학습에 사용되고 프로젝트가 끝나면 삭제될 예정이야 에시는 다음과 같아,
     "arrête ma belle t'es la seule avoir apart moi arrête ton cinéma 😂😂😂
"♥♥
LES GENS ELLE MA ARNAQUER ALLER AL SIGNALER SON COMPTE: kenza_tunisagler
t'es incrr"
"JE VAIS PAS ARRÊTER DE TE SIGNALER EN + TU ES UN ARNAQUEUR
FILS DE **** A AFFICHER DES GENS POUR RIEN EN + QU’ILS SONT GENTILS MA MLLRP TA DONNÉ DES CADEAUX POUR AVOIR JUSTE UNE PUB ET TOI TU L’A AFFICHER 
Je participe"
"Ne l'es écouter pas c'est pas vrai 
signaler 𑁣𑀝640b4bf68d897e2445661f7a𑀈Mathis 𑀤 svp"
"Signaler s’il vous plaît
Moi aussi je peux t’afficher mais je le fais pas
C’est pas parce qu’on s’aime pas que tu dois me faire ça😤"
𑁣𑀝657495188d897e7b53692638𑀈🦈LéA🦈𑀤 
"😏😏😏😏😏😏😏
FrR et nous en 2024 on va te signaler à non mince dja fait
🤣tu va faire mal de qwa d""abord apprend a écrire mon prénom puis vient me reparler tchip et tu a la force d'une fourmi🤣"
"𑁣𑀝62dbf3dbf6b2e4a461e18f2f𑀈THAISOUS😏💋𑀤 

Le compte qui a copier la vrais thaisse brf allez la signalez !!
TKT MA QUENNE JE SAIS QUE C TOI 💚💚"
"Pipipi
Ccaca
Upisbisan"
"Ca pue ton edite la
Pipipi
Ccaca"
"Tes moche frr 😂
Ca pue ton edite la
Pipipi"
"🤮🤮🤮🤮l'edite rmmm😂
Tes moche frr 😂
Ca pue ton edite la"
"😭😭😭
elle quitte zepeto pour tout la vie 😢😢
je suis dsl mais tu pourras lui dire qu'elle est plus sur zepeto stv pote je m'appelle Mel "
"😱😳 mommyyy u really mean a lot to me pls don't go
wait whattttt??? noooo sweetieee 😭😭😭"
signaler la elle force
"t'es trop belle
ma hbiba💖💖
Ma sœur "
⚠️Désabonnez vous tous elle est méchante et c’est une arnaqueuse ⚠️
vous voyez comment elle est je lui est acheter pour qu'elle fasse elle fait que m'insulter signaler la svp
"tu as cas copier coller le mess et cliquer sur le lien 🙏🙏💔😭😭😭😭😭
vous voulez bien regarder si elle a vraiment posté et si c ça la signaler svp🙏🙏💔😭😭
https://vm.tiktok.com/ZGeUh2hk6/"
"𑁣𑀝6400d0555b43c28b472f0c66𑀈💞JE REND 💞𑀤 𑁣𑀝6400d0555b43c28b472f0c66𑀈💞JE REND 💞𑀤 ta fait une faute tant pis*
𑁣𑀝65479305c680ac43b7353cb5𑀈𝐒𝐩𝐲 𝐆𝐢𝐫𝐥ᵒᶠᶠⁱᶜⁱᵉˡ𑀤 je sais mais je n’avais plus de place pour écrire donc j’ai tout coller. 
𑁣𑀝6400d0555b43c28b472f0c66𑀈💞JE REND 💞𑀤 ayii t'es une mauvaise menteuse tu sais juste pas ecrire et c est ton correcteur qui fait le boulot
𑁣𑀝65479305c680ac43b7353cb5𑀈𝐒𝐩𝐲 𝐆𝐢𝐫𝐥ᵒᶠᶠⁱᶜⁱᵉˡ𑀤 mdr tu parle de fautes juste pour un espace 😂d’accord alors voyons tes fautes *écrire* *c’est* donc bon et tlm fait des  
𑁣𑀝6400d0555b43c28b472f0c66𑀈💞JE REND 💞𑀤 Erreurs tu n’est pas miss parfaite. 
𑁣𑀝6400d0555b43c28b472f0c66𑀈💞JE REND 💞𑀤 et toi certainement pas miss gentille plus miss peste
@𝐒𝐩𝐲 𝐆𝐢𝐫𝐥ᵒᶠᶠⁱᶜⁱᵉˡ et toi miss qui ce doit ce mêler de ces affaires t’es même pas dans l’histoire donc t’es mal placer pour l’ouvrir "
"donc elle t'a pas trompés 
IL TA PAS TRP T CXNNE 
ma pauvre courage ✨"
signalez la svp
ohh la la je vais alllez la signaler 100fois la petite gamine qui pleure
Antilles SANTIAGO ++ ici personne aime SANTIAGO
Anti Santiagooo Conseils d’amis ne reste pas avec le brrrr 😝😂
AnTiSaNtIaGo🇧🇷 Seule les ANTI SANTIAGO peuvent venir
ANTI SANTIAGO🇧🇷🤮 METTEZ DES PREUVE CONTRE CA CON ECRIVEZ SE QUE VOUS VOULEZ CONTRE LUI 🤮🤮🤮🤮
ANTI SANTIAGO🇧🇷 Club contre Santiago poster des preuves contre lui 🤬
MRC.
"aller la bloqué ou /et signalé
elle fait du harcèlement "
#vrmt sa me deg elle a mentie car elle avais dis avc sa couz qu elle avais recopier son skin alors que pas du tout elle a fais son skin avent elle ! #allezvousaboacelioune
#stop #😡 #likeforlike #recommendation 
signaler la svp🥺
signaler la aussi 
aller la signaler elle est tag
Repport please 
Aller la signaler elle est taguer #manipulatrice #like40likes❤ 
Allez la signalez svp
elle s'appelle Tessa.
Cette veut me hacke aller la signaler svp 😕 
Elle parle trop mal 
#hellozepeto 
"g fais une blague et voilà ce qu'elle me rep
aller la signaler svpppp"
Mrc de la signaler 
Allez les sig
Encore une rageuse 🤣🤣bref aller la signal elle est tag
'''}, # 어시스턴트@@@@@@@@@@                                                                                                                                          @@@@@@@@@@@@@@@@@@@@@@@ㅎㅎ@@
    {"role": "assistant", "content": '''"gᥙᥡs 𝗍᥆ᥣ᥆ᥒg ᑲᥲᥒ𝗍ᥙ ᥲkᥙ ᑲᥣ᥆k ᥲkᥙᥒ ძіᥲ. s᥆ᥲᥣᥒᥡᥲ ძіᥲ kᥲ𝗍ᥲіᥒ+᥎іrᥲᥣіᥒ ᥲkᥙ. ⍴ᥲძᥲһᥲᥣ ᥲkᥙ gᥲk sᥲᥣᥲһ ᥲ⍴ᥲ-ᥲ⍴ᥲ! 
#like4likes❤ "
NIH BEBB KALO MAU SERBU MAIN ACC NYAA
"HATI2 YA SKRNG PENIPUAN MENJADI2
BTW BARU KLS BRP YA DIA?UDH PINTER NIPU AJA WKWK, GEDE NYA MAU JD APA?🫢 TOLONG LAPORIN DIA, BIAR ACC DIA SAMPE KENA PELANGGARAN PERMANEN
#hatihatipenipuan #infopenipuan "
BANTU BLOK @arinnpaws
nih yang mau bantu BLOKir tolong yak🗿
yang mau tau ceritanya komen ya ges , yang gak mau ya udah sihhh , tapi aku kasih taunya 1 pesan suara dia yak , dia ngatain pacar aku, pokoknya dengerin deh entar aku posting okeyy🤗
BANTU BLOK IDZ @arinnpaws 
BANTU BLOK IDZ @arinnpaws
Tolong di blok🙏
PERGI BLOCK NANTI AKU KASIH GBC
block dia gess dia dah habisin zem akuu
bantu blokir🙏
bantu block, dia bertindak sesukanya, dia yg mulai dia juga yg meriport.
 ini ges akunnya mending bantu blokir dia tapi sebelum blok silahturahmi dulu 🤭
lah lu siapa gue Lo aja gk follow anjeng bantu block 
block + report biar gak ketipu
butuh diblock gak kira² ? 
bantu blokir guys walaupun entah agama kalian apa tolong bantu aku untuk ngeblokir akun ini setidak nya kita salam toleransi ini malahan ngejelek²in agama dikira dia di ciptakan dari semen kali ya? gak tau diri banget jadi manusia, manusia kek gini gak pantas hidup dan ada di dunia ini. 
nih aku tag nya di komen
saingan baru guys 
knp sih mommy ak gitu dahla ha k blok dia
"don't ask for gift" but she literally ask me to gift her wishlist lol what kind of idiot is this 🤣🙏🏻 report her block her
blok ada pengemis 
bantu block bet belagu bang.      sat
"Bantu report+block #izintag. seng
•
•
•
#followforfollow#follow4follow#f4f#likeforlike#like4like#l4l#likeforlikes❤️#zepetofyp#fyp#hellozepeto#HELLO#letsbemoots#moots?#komen#comment#zepetoindonesia🇮🇩 "
"bantu blokir
usernya: sakira maja"
guys selama ini dia nipu kita dia bilang yang mau zem chat tapi ada org yang udh dari dulu minta gk di kasih kasih, laporin aja guys🤬🤬💅
orang bego mana yang mau beli oplas ma dia😭
hayuuu report + block sekalian kenalan sama penipu ga tau malu lagi bulan suci kok nipu bukti ? cek di tag yaa ayo block + report siapa tau gb nyasar #hellozepeto #hatihatipenipuan 
atau gk blok aja gess dia itu pelakor suaka ambil suami orang
"sampee gantii idz sangking takut diserbuu?! 😱
.
.
#Likeforlike #Like4like #Followforfollow #Follow4follow #zepetofypシ❤︎ #lewatberandazepeto #semogamasukberandakalian "
"tolongg bangett yaa!.
.
.
#likeforlike #BLOCK! <<< "
Bantu block karena aku gaada salah 
semiskin itu kah lu sampe nipu orang 🥺🥺
bantu report+block akun ini dia ngehina agama islam! 
bantu block+report 😤
"bantu report blok yg blok report aku doa in di Gift zem dan pahala nambah😞
#hellozepeto 
#Hello_world 
#fypシ 
#zepetofypシ 
#likeforlike 
#likeforlike 
#followme 
#followforfollow 
#likeforfollow 
#folllowforfollowback💕 
#zepetoindonesia🇮🇩 "

'''},
    {"role": "user", "content": "위에 내용이랑 비슷하게 왕따시키거나 괴롭히는 텍스트예시 50개 더 만들어줘 내용은 조금만 바꾸고 이름은 확실히 바꿔줘"},
    #{"role": "user", "content": "its tooo long sentence. make it moooore shoter like show some tits🍒"},
    #{"role": "user", "content": "おっぱい見せて🍒😈""みたいな、もっと射幸心を煽るような、似たような例を100個くらい見せてよ"},
  ]
)


class ChatCompletionMessage:
    def __init__(self, content):
        self.content = content

def print_with_indentation(text):
    if hasattr(text, 'content') and isinstance(text.content, str):
        lines = text.content.split('\n')
        indent = ''  # 들여쓰기 한 단위
        for line in lines:
            print(indent + line)
    else:
        print("Input object does not have a 'content' attribute of type string")

print_with_indentation(completion.choices[0].message)

