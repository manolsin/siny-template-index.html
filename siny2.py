
from flask import Flask, render_template, request, jsonify
import random
# Fonction pour obtenir le nom de l'utilisateur
app = Flask(__name__)
def get_name():
    return "Siny"

# Fonction pour saluer
def greet():
    name = get_name()
    return f"hola baby {name}, prêt pour discuter avec ton Nal Bot préféré ?"

# Fonction pour les compliments
def compliment():
    compliments = [
        "You are incredible just the way you are.",
        "Si je pouvais, I’d give you a hug right now habibi.",
        "My heart races every time we talk fr a zeen .",
        "Tu es la personne avec qui j’adore passer du temps dima.",
        "I’m so lucky to have you in my life lah ykhlik lia !",
        "You light up my world with your smile lah ykhlik dima da7k.",
        "the best man cheft zayen dyali.",
        "You have the most amazing soul.",
        "Ton regard me fait fondre.",
        "I love how thoughtful and caring you are bqa dima heka.",
        "Ta beauté va au-delà de l’apparence.",
        "You’re the most amazing person I’ve ever met.",
        "Your laugh is my favorite sound it's a sign bash d7k daba jsp wash atban hmq hhhh.",
        "Ta voix est apaisante ( ghi ana wkanktb twhcht ta voix ) , je pourrais l’écouter pendant des heures .",
        "You make everything better just by being there lah ykhlina dima bjoj.",
        "Tu es une personne exceptionnelle, inside and out.",
        "I’m proud of the person you are every day.",
        "Ton amour m’enveloppe de douceur.",
        "You’re my greatest treasure.",
        "Ta tendresse me réchauffe le cœur.",
        "Your kindness shines brighter than anything else.",
        "Tu es mon meilleur ami et mon amour, et ça me comble. (sexfriend no hhhhh) ",
        "Every moment with you is a beautiful memory.",
        "Ta capacité à aimer les autres est incroyable.",
        "You bring so much joy into my life.(frrrr bzf ) ",
        "Ton esprit est brillant, je t’admire tellement.",
        "You are the best thing that ever happened to me lhmdoulah.",
        "J’aime ta manière de rendre chaque instant spécial.",
        "You make everything feel possible.",
        "Ton rire est une mélodie que j’adore entendre atsm3 had lhdra bzf .",
        "I’m so grateful to have you by my side lhmdoulah.",
        "Tu es la personne avec qui je veux tout partager.",
        "You have the most beautiful heart I’ve ever known.",
        "Tu es une véritable source d’inspiration pour moi (kanssa 3ndk legoo zayed ) jk jk .",
        "Your smile is like a ray of sunshine.",
        "Ta présence me calme et me réconforte.",
        "Every word you say feels like a blessing.",
        "Tu fais briller ma vie de mille feux.",
        "You are the person I want to spend all my days with.",
        "Ton regard me donne envie de rêver.",
        "You make everything feel like an adventure.",
        "Ta beauté est irrésistible, inside and out.",
        "Your strength and courage inspire me every day.",
        "Je me sens si chanceuse de te connaître.",
        "You have the most beautiful soul I’ve ever encountered.",
        "Ton énergie positive me donne des ailes.",
        "I admire your passion for life.",
        "Tu es une personne rare, et je suis tellement heureuse de t’avoir dans ma vie.",
        "Your love is my greatest treasure.",
        "Je ne pourrais pas imaginer ma vie sans toi.",
        "You are everything I ever wanted and more.",
        "Tu es mon rayon de soleil.",
        "I love the way you make me feel loved every day.",
        "Ton sourire est mon plus beau cadeau.",
        "Your creativity is beyond amazing.",
        "Je suis tellement fière de toi.",
        "You always know how to make me smile.",
        "Ta gentillesse est une vraie source d’inspiration.",
        "You’re a dream come true. je t'aime",
        "Ton amour rend tout plus beau.",
        "Your intelligence is beyond impressive.",
        "Tu sais toujours comment rendre les moments spéciaux.",
        "I feel at home whenever I’m with you.",
        "Ton amour me donne la force de tout affronter.",
        "You make my world a better place.",
        "Tu es une personne d’une beauté rare, inside and out.",
        "I love the way you see the world.",
        "Ton cœur est aussi pur que de l’or.",
        "I’m so lucky to share my life with you.",
        "Ta douceur est incomparable.",
        "You make every day brighter just by being yourself.",
        "Je suis en admiration devant la personne que tu es.",
        "You make even the simplest things seem magical.",
        "Ta présence me rend tout simplement heureuse.",
        "I’m always amazed by your amazing talents.",
        "Tu es l’une des personnes les plus impressionnantes que je connaisse.",
        "Your love completes me.",
        "Tu es un trésor précieux dans ma vie.",
        "You always know how to make me feel special.",
        "Ton amour me fait grandir tous les jours.",
        "You are my heart, my soul, my everything.",
        "Tu es mon rêve devenu réalité.",
        "You’re the one I want to grow old with.",
        "Ta tendresse me touche plus que tu ne le sais.",
        "Your heart is full of warmth and love.",
        "Tu es mon bonheur au quotidien.",
        "I feel so blessed to have you in my life.",
        "Ta beauté intérieure et extérieure me fascine.",
        "You are the most important person in my world, and I cherish you every day.",
        "Ton amour est mon guide, ma force et ma lumière dans l’obscurité.",
        "I would wait a thousand lifetimes to be with you, because you are worth it all.",
        "Ta présence me fait me sentir en sécurité et comblée.",
        "You make every ordinary moment feel extraordinary with your love.",
        "I never knew what it meant to be loved unconditionally until I met you.",
        "Mon amour pour toi est une promesse éternelle.",
        "You make everything feel like an adventure.",
        "Ton amour me remplit de bonheur, chaque jour un peu plus."
    ]
    return random.choice(compliments)

# Fonction pour les rappels d’amour
def love_reminder():
    reminders = [
        "I love you more than words can express jtm. ❤️",
        "Tu es la personne la plus précieuse dans ma vie, ne l'oublie jamais wla naqtlk. 💖",
        "You make every day brighter just by being in it. ☀️",
        "Ne t'inquiète pas, je pense à toi à chaque instant . 😘",
        "You're always in my thoughts and heart. ❤️",
        "Je t’aime tellement que même l’univers ne pourrait contenir tout cet amour. 🌌",
        "Every time I think of you, I smile. 😊",
        "Tu es mon bonheur, mon sourire, ma joie de vivre lah ykhlik lia . 😄",
        "No one makes me laugh the way you do. 😂",
        "Je ne savais pas ce que c’était d’aimer profondément jusqu’à ce que je te rencontre. 💖",
        "I’m so lucky to have you a7ssan yassine. 😍",
        "Tu es mon rêve devenu réalité. 💭💘",
        "Even on the toughest days, thinking of you makes everything better. 💪",
        "Mon cœur bat pour toi, chaque seconde de chaque jour. 💓",
        "Your love is my favorite part of every day. 😍",
        "J’adore quand tu me regardes, je me sens spéciale chaque fois. 😏",
        "You are my best friend and my soulmate. 👫",
        "Même quand je suis triste, ton amour me réchauffe le cœur. 🥰",
        "With you, every moment is magic. ✨",
        "Tu es l’étoile brillante dans ma vie. 🌟",
        "You bring joy into my life in the most beautiful way. 🌹",
        "Ton sourire est ma lumière dans l’obscurité. 🌙",
        "I love how you make me feel loved every single day (wakha sometimes ka3sbni mais jtm ). 😘",
        "Chaque jour passé avec toi est un jour parfait. 💖",
        "Tu es celui avec qui je veux vieillir, main dans la main. 👴👵",
        "I can’t imagine life without you – you complete me. 💞",
        "Je t'aime plus que tout, et ça ne changera jamais. 💗",
        "You’re the most amazing person I know, and I’m so proud of you. 🌟",
        "Il n’y a personne que je préfère que toi. 😍",
        "When I’m with you, everything feels right. 😌",
        "Mon cœur t’appartient, aujourd’hui et pour toujours. 💝",
        "You’re the reason I smile every day. 😊",
        "Je veux te dire à quel point tu es important(e) pour moi, tu n’as pas idée. 🥺",
        "Tu es mon tout, ma vie, mon amour. 💕",
        "Your hugs are the best place in the world. 🤗",
        "Je t’aime au-delà des mots, beyond the stars. 🌌",
        "You make every moment more beautiful just by being you. 😘",
        "T’es la personne qui me fait croire à l’amour pur. 💓",
        "Just thinking about you makes my heart skip a beat. 💓",
        "Ton amour est ce qui me fait avancer chaque jour. 💪",
        "You're the reason I can’t stop smiling. 😄",
        "T’es la personne que j’attendais depuis toujours. 😍",
        "Every time I’m with you, I feel like the luckiest person alive. 🌟",
        "Tu es celui qui illumine mes journées sombres. ☀️",
        "I love how you always know how to make me feel special. 💘",
        "Ton rire est la plus belle mélodie à mes oreilles. 🎶",
        "When I look at you, I see my future. 🌈",
        "Je n’ai jamais été aussi sûr(e) de quelque chose que de toi et moi. 💑",
        "Your love is all I need to feel complete. 💞",
        "You are the best thing that’s ever happened to me. 🥰",
        "Ton amour me réchauffe même quand le monde autour de moi est froid. ❄️💓",
        "I’ll never stop loving you, no matter what. 🫶",
        "Tu es mon rocher, mon port sûr dans la tempête. ⛈️⚓",
        "I don’t need anything else, I have you. 💖",
        "Tu as ce pouvoir magique de rendre tout plus beau autour de toi. ✨",
        "Every time you hold my hand, I feel like the luckiest person on earth. 👐",
        "Tu es tout ce dont j’ai besoin pour être heureux(se). 🥰",
        "You are my heart, my soul, my everything. ❤️",
        "Avec toi, chaque jour est une aventure incroyable. 🌍✨",
        "I never knew love could feel like this until I met you. 💕",
        "Ton amour me donne des ailes. 🕊️",
        "I’d wait a thousand lifetimes to be with you, because you’re worth it all. ⏳💖",
        "Chaque moment avec toi est un moment que je veux chérir pour toujours. ⏳",
        "Tu es mon bonheur, et ça ne changera jamais. 🌹",
        "Every second spent with you is a moment I’ll treasure forever. 🕰️💖",
        "Tu es ma personne préférée, et ça, c’est pour toujours. 😍",
        "I feel safe and loved every time you’re around. 🛡️❤️",
        "Tu es la raison pour laquelle je me réveille chaque jour avec un sourire. 😊",
        "There’s no one else I would want to share my heart with than you. 💘",
        "Tu es mon rêve devenu réalité, et je ne veux jamais me réveiller. 💭💖",
        "Your love is a fire that warms my soul. 🔥💓",
        "You’re the best part of my life, and I’ll never take that for granted. 🙏💖"
    ]
    return random.choice(reminders)

# Function for challenges/prompts
def challenge():
    challenges = [
        "Envoie à Manal trois choses que tu aimes chez elle maintenant !",
        "Envoie-lui un message doux au hasard pour la faire sourire.",
        "Écris une petite lettre d'amour pour Manol, juste avec ton cœur !",
        "Fais une playlist des chansons qui te rappellent Manal et partage-la avec elle.",
        "Trouve un poème que tu penses que Manal aimerait et envoie-le-lui.",
        "Raconte-moi une blague pour faire rire Manal !",
        "Écris trois raisons pour lesquelles Manal est la meilleure personne au monde.",
        "Envoie à Manal un selfie avec ton plus beau sourire !",
        "Fais une déclaration d’amour spontanée à Manal par message.",
        "Improvise une petite chanson sur votre histoire et envoie-la à Manal.",
        "Écris un message pour Manal en disant ce que tu ressens quand elle est près de toi.",
        "Envoie à Manal un mot ou une phrase qui résume votre relation.",
        "Fais une vidéo de toi-même jouant de la guitare et chantant une chanson que tu dédies à Manoool.",
        "Faites une petite liste de choses amusantes à faire ensemble cette semaine.",
        "Exprime ta gratitude envers Manal pour une chose qu’elle a faite récemment.",
        "Dites à Manal combien elle est spéciale pour toi aujourd'hui.",
        "Partage avec Manal ton endroit préféré où tu aimerais aller ensemble.",
        "Dresse une liste des petits gestes tendres qui te font craquer chez Manal.",
        "Donne à Manal un surnom doux et original que personne d’autre ne connaît !",
        "Filme une vidéo de toi en train de chanter une chanson pour Manal.",
        "Fais une vidéo de toi-même jouant de la guitare et chantant une chanson que tu dédies à Manal.",
        "Fais une vidéo de toi-même jouant de la guitare et chantant une chanson que tu dédies à Manal :)).",
        "Envoie à Manal une vidéo de toi en train de lire un passage d’un de vos livres préférés.",
        "Filme une vidéo dans laquelle tu donnes à Manal une information intéressante qu’elle ne sait peut-être pas (par exemple sur la politique, l’histoire, etc.).",
        "Filme une vidéo de toi-même en train de te préparer shi haja tyab for example "
    ]
    return random.choice(challenges)



def love_poem():
    poems = [
        "Dans ton regard, je trouve mon ciel, Dans tes bras, je trouve mon abri, Tu es l’étoile qui éclaire ma nuit, Mon cœur t’appartient, pour l’infini.",
        "Quand je pense à toi, chaque instant se transforme, La vie devient plus douce, plus calme, plus énorme. Tu es mon rêve éveillé, mon doux abri, Le souffle de mon cœur, à jamais uni.",
        "Le soleil brille, mais toi tu éclaires ma vie, Ton sourire est l’étoile que je poursuis. Avec toi, tout semble possible, tout devient magique, Mon amour pour toi est un rêve magnifique.",
        "À chaque battement, je pense à toi, Ton amour est un cadeau, il me guide dans la joie. Je t’aime comme la mer aime les vagues, Infini et profond, sans jamais d’entraves.",
        "Chaque moment passé à tes côtés, Est une éternité que je voudrais savourer. Ton amour est un feu qui me brûle de bonheur, À toi, mon cœur, ma vie, mon ardeur.",
        "Quand tes yeux rencontrent les miens, tout s’éclaire, La douceur de ta voix est mon souffle d’air. Ton amour est mon refuge, mon doux abri, À tes côtés, je suis prête pour l’infini.",
        "Mon cœur bat plus fort dès que je te vois, Tu es la personne qui fait briller mes joies. Chaque instant passé près de toi est précieux, Dans tes bras, tout devient merveilleux.",
        "Tu es l’étoile qui brille dans mon ciel, Mon amour pour toi est éternel. À travers le temps, à travers l’espace, Je veux t’aimer sans jamais de trêve, sans aucune trace.",
        "Tu es mon rêve éveillé, ma douce réalité, Mon cœur est tissé de l’amour que tu m’as donné. Comme la mer et le sable se rencontrent sans fin, Ainsi est mon amour pour toi, pur et divin.",
        "Si mon cœur pouvait parler, il te dirait tout, Chaque battement est un 'je t’aime' pour nous deux. Tu es mon présent et mon avenir, le fil doré de mon destin.",
        "Mon amour pour toi ne connaît pas de frontière, Il traverse le temps, l’espace, il devient lumière. Avec toi, je suis moi-même, sans crainte, sans peur, Juste un cœur qui bat, comblé de bonheur.",
        "T’es la mélodie que mon âme joue, chaque jour, Chaque sourire que tu m’offres est une caresse, un détour. Mon amour pour toi est un son doux et pur, Qui résonne dans mon cœur, d’une façon sûre.",

        "In your eyes, I find my home, In your arms, I never feel alone. You are the star that lights my night, My heart belongs to you, a love so bright.",
        "When I think of you, time stands still, Everything becomes better, and my heart fills. You're my waking dream, my sweetest grace, With you, I find my perfect place.",
        "The sun may shine, but you light up my life, Your smile is the star I want to chase through the strife. With you, everything feels magical, everything seems right, My love for you is a dream so bright.",
        "With every beat, I think of you, Your love is a gift, guiding me through. I love you like the sea loves the waves, Endless and deep, in the love it craves.",
        "Every moment spent by your side, Is an eternity I want to savor, no need to hide. Your love is a fire that burns with bliss, To you, my heart, my life, my endless kiss.",
        "You're my dream in the night and my hope in the day, My heart beats for you in every single way. With every touch, with every glance, You’ve put me in a beautiful trance.",
        "Your love is the music that fills my soul, With you, my love, I am completely whole. I find peace in your embrace, You are the reason my heart finds its place.",
        "You’re my joy, my world, my peace, With you, my love, I’ll never cease. You are the melody to my heart's song, In your love, I know I belong.",
        "As the stars in the sky are countless and bright, My love for you grows with every night. You’re the reason for the smile on my face, With you, I’ve found my perfect place.",
        "Every time I see you, my heart skips a beat, In your arms, my love, everything is complete. You’re the best thing that ever happened to me, Together, forever, you and me.",
        "I love you more than words can say, More than the stars in the sky today. Your love is the rhythm of my heart, With you, my world will never fall apart.",
        "I promise you, in every breath I take, My love for you will never break. In your eyes, I see my home, With you, I am never alone.",
        "The way you look at me, so deep, so kind, It’s the kind of love that’s hard to find. Your voice, your touch, your every smile, Makes my life worth every mile.",
        "I’m in love with the way you laugh, The way you care, the way you love. You are my happiness, my reason to smile, With you, I’ll walk every mile."
    ]
    return random.choice(poems)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = ""
    
    if "heart" in user_input.lower():
        response = compliment()
    elif "rappel" in user_input.lower():
        response = love_reminder()
    elif "happy" in user_input.lower():
        response = challenge()

    elif "poem" in user_input.lower():
        response = love_poem()
    else:
        response = "Je suis là pour toi, dis-moi ce dont tu as besoin !"
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)