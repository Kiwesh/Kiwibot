import os
import random
import json
import requests
from dotenv import load_dotenv

class Kiwibot:
    def __init__(self):
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
        self.TWITCH_CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')
        self.TWITCH_USER_ID = os.getenv('TWITCH_USER_ID')
        self.TWITCH_TOKEN = ''
        self.blagues = [
        "Oui monsieur le commissaire, mon père est maire, ma tante est soeur. J'ai un cousin qui est frère et mon frère est masseur.",
        "A ma droite, il y avait un lion féroce, à ma gauche, un tigre prêt à bondir,  derrière des éléphants énormes,... - Alors ? Qu'as-tu fait pour t'en sortir ?   - J'ai souté au bas du manège !",
        "Allô Police ! Je viens d'écraser un poulet. Que dois-je faire ?  - Et bien , plumez-le et faites-le cuire à thermostat 6.  - Ah bon ! Et qu'est-ce que je fais de la moto ?",
        "Bonjour, je voudrais un livre ! - De quel auteur ? - Pas trop grand, je n'ai pas beaucoup de place.",
        "Chauffeur, soyez prudent, à chaque virage j'ai peur de tomber dans le ravin!  - Madame n'a qu'à faire comme moi, fermer les yeux!",
        "Chéri, dis-moi ce que tu préfères, une femme jolie, ou une femme intelligente?  - Ni l'un, ni l'autre, chérie, tu sais bien que je n'aime que toi.",
        "Docteur, je ne sais plus ce que je dis ! - Et vous avez ce problème depuis quand ? - Quel problème ?",
        "Ecoute, dit la maman à sa petite fille, si tu es sage, tu iras au ciel, et si tu n'es pas sage, tu iras en enfer. - Et qu'est-ce que je dois faire pour aller au cirque?",
        "Il faut être bon avec les animaux, explique le papa de Julien. - Oui papa, il ne faut pas les traiter comme des bêtes.",
        "J'ai battu un record. - Ah bon, lequel ? - J'ai reussi a faire en 15 jours un puzzle sur lequel il y avait écrit 'de 3 a 5 ans'.",
        "Je suis inquiet, je vois des points noirs. - Tu a vu l'oculiste ?  - Non, des points noirs !",
        "Je vais acheter cette toile dit le client au peintre.  - C'est une affaire, Monsieur. J'y ai passé dix ans de ma vie.  - Dix ans? Quel travail!  - Eh oui: deux jours pour la peindre et le reste pour réussir à la vendre!",
        "Les gens devraient tout le temps dormir la fenêtre ouverte. - Pourquoi, vous êtes médecin?  - Non, je suis cambrioleur.",
        "Moi j'ai toute l'année des ampoules dans les mains.  - Vous faites un travail difficile?  - Non, je suis vendeur au rayon électricité.",
        "Oh regarde un mouche ! - Non, pas un mouche, une mouche ! - Ben ça alors tu as de bons yeux.",
        "S'il te plait mon Papichou, tu veux bien me donner 5 F demande Julien à son grand-père ?  - D'accord, si tu me le demandes correctement.  - Sois cool, vieux, fille-moi 20 balles !",
        "T'as vu mon fer à repasser ? - T'inquiète il va repasser !",
        "Tu connais l'histoire de la feuille de papier ? - Non. - Elle déchire !",
        "Tu m'offres une bague ? - Pourquoi faire ? T'en as déjà plein les dents !",
        "Vous avez eu beau temps pendant vos vacances?  - Super! Il n'a plus que deux fois.  La première fois, pendant une demi-journée,  et la deuxième, pendant 29 jours.",
        "2 cosmonautes discutent : - Tu crois qu'on peut se cogner contre quelqu'un en apesanteur ? - Oui, mais ce sont toujours des accidents sans gravité !",
        "2 escarpins discutent à un défilé de mode : - Tu penses que je suis à la hauteur ? - Mais oui, tu as un talon fou !",
        "2 explosifs se rencontrent : Alors, ça boom ?",
        "2 icebergs discutent : - Alors il paraît que ta femme à accouché ? - Oui, on a eu un beau petit glaçon !",
        "2 vampires discutent : - Tu veux un peu d'hémoglobine ? - Non merci, je suis au régime - Tu peux y aller, c'est du zéro pour sang !",
        "A combien rouliez-vous? Demande le gendarme.  A deux seulement, mais si vous voulez monter, il reste de la place.",
        "A l'entrée d'un pont, il est inscrit sur une pancarte :  Ne pas passer à deux, sinon le pont casse.  Une homme lit la pancarte et traverse le pont.  Le pont casse car ... un homme averti en vaut deux.",
        "A la douane : - Qu'est ce que vous transportez ? - 6000 huîtres - Ouvrez les toutes.",
        "Alors mon cher, ces vacances? Où étiez-vous?  - Oh, la première semaine, j'étais dans les Alpes et les deux suivantes, j'étais dans le plâtre.",
        "Au cinéma, deux bavardes n'arrêtent pas de discuter. Excédé, leur voisin proteste :  - S'il vous plait, je n'entend rien du tout.  - Et alors, ça vous regarde, ce que nous disons.",
        "Au restaurant, Monsieur Dupont s'écrie:  - Garçon, il y a une mouche qui nage dans mon assiette.  - Oh, c'est encore le chef qui a mis trop de potage. D'habitude, elles ont pied!",
        "Au restaurant, le garçon demande au client:  - Comment avez-vous trouvé le beefsteak?  - Tout à fait par hasard, en soulevant une frite!",
        "C'est un habitant du village de Poil. On lui demande:  - Où êtes-vous né?  - A Poil!  - Et bien moi aussi figurez-vous!",
        "C'est une jolie petite antenne de T.V. qui est tombée amoureuse d'un paratonnerre. Elle murmure: 'dis, tu y crois toi, au coup de foudre?'",
        "Cela fait une semaine que je vous soigne pour une jaunisse,  dit le médecin à son client,  et c'est maintenant que vous me dites que vous êtes chinois!",
        "Charlotte demande à Nicolas :  - Tu sais pourquoi il y a des trous au fond des pots de fleurs ?  - Oui, c'est pour qu'on puisse prendre la température des plantes",
        "Charlotte part à la visite médicale avec son petit flacon d'urine. Elle demande :  - C'est pour quoi faire ?  - A ton avis ? répond sa maman  - C'est pour remercier le docteur ?",
        "Charlotte regarde un mille-feuilles qui coûte 4 euros. Elle entre et dit à la boulangère : - Je voudrais 500 feuilles, parce que je n'ai que 2 euros",
        "Charlotte va voir sa maman et demande :  - Est-ce que je pourrais avoir du chocolat ?  - On dit comment ? S'il... s'il ?  - S'il en reste encore ?",
        "Chez le coiffeur : - Tu veux du gel dans tes cheveux ? - Non merci j'ai déjà froid",
        "Chez le dentiste:  - Vous avez une dent morte. Je vous fais une couronne?  - Non merci, enterrez-la sans cérémonie.",
        "Dans la rue, un homme demande à une vieille dame : - Vous n'auriez pas vu un policier ? - Non. - Alors donnez-moi votre sac à main !",
        "Dans le grand océan, une petite vague est amoureuse du vent. Celui-ci lui demande tendrement:  - Tu veux que je te fasse une bourrasque ou un ouragan?  - Oh non, je veux juste une petite bise...",
        "Dans le train, le contrôleur dit à une vieille dame:  - Votre billet est pour Bordeaux. Or ce train va à Nantes.  - C'est ennuyeux, grommelle la voyageuse.  Et ça arrive souvent au chauffeur de se tromper comme ça?",
        "Dans un cocktail, une actrice rencontre une romancière qu'elle déteste. - J'ai beaucoup aimé votre dernier livre. Qui vous l'a écrit? - Je suis contente qu'il vous ait plu. Qui vous l'a lu?",
        "Dans un coin sombre, deux amoureux s'embrassent. Des gamins les regardent. L' un dit a l'autre : - Vise un peu, il essaye de lui piquer son chewing-gum !",
        "Dans un frigo, un oeuf aperçoit un kiwi à coté de lui. - Tiens, il est périmé celui-là !",
        "Dans un magasin : - Je peux essayer ce pantalon en vitrine ? - Vous ne préférez pas l'essayer en cabine ?",
        "Des frères et soeurs se disputent: - Quel âne! - Tête de cochon! - Espèce de dinde! Leur mère arrive et crie: 'Oh la ferme!' ",
        "Deux anges font la causette : - Quel temps fera-t-il demain ? - Nuageux.  -Ah tant mieux, on pourra s'asseoir !",
        "Deux bombes discutent : - Rendez-vous à 5 heures pétantes !",
        "Deux chasseurs parlent ensemble : - Tiens ! Tu as fait un noeud aux oreilles de ton chien ? - Oui, c'est pour penser à acheter du gibier en rentrant !",
        "Deux chaussettes se croisent : - Ça va ? - Et toi ? Comment tu te sens ?",
        "Deux coiffeurs discutent : - Tu veux bien m'aider pour une coupe ? - Tu peux te brosser !",
        "Deux enfants discutent : - Tu as quel âge ? - Attends je vais regarder l'étiquette de mon slip !",
        "Deux escargots arrivent sur une plage et aperçoivent une limace : - Demi-tour ! Nous sommes sur une plage nudiste !",
        "Deux gamins discutent : - Comment écris-tu 'Père Noël', avec un L ou deux ? - Avec deux sûrement, sinon, il ne pourrait pas voler !",
        "Deux gendarmes : - C'est quoi ton secret ? - Une crème qui fait la peau-lisse",
        "Deux grenouilles se parles. il y en a une qui dit : - Quoi quoi quoi. L'autre répond : - On ne dit pas 'quoi', on dit 'comment' ",
        "Deux microbes se rencontrent: - Tu es pâle, qu'est-ce que tu as? - Je suis malade, j'ai avalé une aspirine.",
        "Deux nuages discutent : - On va encore mal dormir, ils construisent de nouveaux gratte-ciel !",
        "Deux obus discutent : - T'as vu ma nouvelle fiancée ? - Ouais : c'est une vraie bombe !",
        "Deux orages discutent : - Tu t'es éclaté hier ? - C'était du tonnerre !",
        "Deux pantoufles se rencontrent : - Salut, savate ? - Ouais, c'est le pied !",
        "Deux passants se croisent dans la rue :  - Tiens, Jean, comme tu as changé : les cheveux, les yeux ...  - Mais monsieur, je ne m'appelle pas Jean.  - Ah bon ! Tu as même changé de nom !",
        "Deux petits garçons discutent : - Moi j'adore la barbe à papa ! - Le mien il se rase tous les matins. ",
        "Deux petits pois discutent : - T'étais où hier ? On t'a pas vu en boîte !",
        "Deux pianos se croisent : - Ça va, toi ? - Bof, j'ai mal au do.",
        "Deux tee-shirts discutent : - Ca caille ici on se croirait au pull nord !",
        "Deux téléphones portables sont à la plage. Soudain l'un d'eux se met à grelotter...  - Tu n'as quand même pas froid, il fait 30 degrés ! - Mais non, je reçois un texto !",
        "Deux vampires discutent : - Tu l'aimes ? - Je suis complètement mordu !",
        "Deux voyageurs de commerce discutent:  - Moi, fait l'un, je traite mes clients comme mes cigarettes.  - Comment cela?  - Je les roule toujours moi-même!",
        "Elle réfléchit avant de sortir avec moi - Et alors ? - Ça fait deux ans",
        "Julien demande 10 euros à son père. celui-ci questionne :  - C'est pour quoi faire ?   - Pour donner à une vieille dame.  - Bravo, c'est très bien de vouloir l'aider. Et où est-elle cette dame.  - Là-bas, elle vend des glaces !",
        "Julien rentre de l'école. Il a le genou écorché.  - Pauvre chou, tu as dû beaucoup pleurer, compâtit sa maman.  - C'est pas la peine, y'avait personne.",
        "La maman demande à Julien:  - Que fais-tu?  - Rien!  - Et ton frère?  - Il m'aide!",
        "La maman dit à Julien :  - Tu as encore mis tes doigts sales sur la porte !  - Même pas vrai ! Moi, je l'ouvre à coup de pied !",
        "La postière dit à Charlotte :  - Cette lettre est trop lourde. Il faut ajouter un timbre de 50ct.  - Oui, mais si j'ajoute un timbre, elle sera encore plus lourde !",
        "La vie d'une ampoule est fragile ... car elle ne tient qu'à un fil !",
        "Le coiffeur dit à son client:  - Cette mousse ferait pousser des cheuveux sur une boule de pétanque.  - Très bien. Mais est-ce que ça ne gênerait pas un peu le jeu?",
        "Le dentiste demande au patient:  - De quel côté mangez-vous?  - Du côté de la gare, mais je me demande bien ce que ça peut vous faire.",
        "Le papa dit à Emilie :  - Tu travailles lentement, tu comprends lentement, tu marches lentement. Y a-t-il quelque chose que tu fasses vite ? - Oui, je me fatigue vite.",
        "Le roi souffre des dents. Son dentiste lui dit :  - Sire, il faudrait changer votre couronne.  - Ah ça jamais ! répons le roi.",
        "Lors d'un sondage sur les après-rasages, on demande à un homme dans la rue:  - Monsieur, que mettez-vous après vous être rasé? - Mon pantalon!",
        "Lorsqu'une voiture de Formule 1 prend un virage à droite à 140 km/h,  quelle roue tourne le moins vite ?  Réponse : La  roue de secours.",
        "Madame Dupont achète des oeufs au marché.  - Ils sont pondus du jour au moins ? Elle s'inquiète :  - Bien sûr ! La nuit, elles dorment mes poules !",
        "Madame Dupont dit à son mari:  - Bouge un peu que je passe un coup de balai!  Il faut que tout soit propre pour la nouvelle femme de ménage!",
        "Madame dit à Monsieur :   - Tu te rases avec un rasoir électrique ?   - Non! répond Monsieur, j'ai peur des coupures de courant!",
        "Maman tu peux me faire une queue de cheval ? - Ils sont trop courts ! - Et bien fais-moi une queue de poney alors !",
        "Merlin rencontre Arthur pour la première fois. Arthur regarde le vieillard et lui dit : Enchanté !  L'autre répond : Non non, Enchanteur !",
        "Monsieur Dubois demande à sa femme :  - Quelle est la différence entre un accident et une catastrophe ?  - Heu, je ne sais pas...  - Ta mère tombe à l'eau, c'est un accident. Quelqu'un la repêche, c'est une catastrophe.",
        "Nicolas demande à sa maman :  - Elle faisait quoi, comme métier, la Sainte Vierge ?   - Elle était mère au foyer.  - Alors, pourquoi elle a mis le petit Jésus à la crèche",
        "On demande à un grand explorateur :  - Quelle est la peau de l'animal que vous avez eu le plus de mal à rapporter de vos chasses ?  - La mienne !",
        "Pourquoi faut-il aimer son prochain?  - Parce que les autres sont loin.",
        "Pourquoi faut-il se méfier des sirènes au volant ? Parce qu'elles font des queues de poisson !",
        "Pourquoi n'y a t il pas de corbeilles dans les piscines ? Parce que la corbeille a papier.",
        "Qu'est ce qu'une catapulte à salade ? Un lance roquette.",
        "Qu'est-ce qu'un squelette dans une armoire ? C'est quelqu'un qui a gagné à cache-cache.",
        "Que fait un sportif à qui on étire le nez ? Il prend son nez-long !",
        "Quel est le fruit le plus végétarien ? La 'pas steak'!",
        "Quel est le plus beau compliment qu'un cannibale puisse faire à une fille ? Vous êtes belle à croquer !",
        "Quel est le sport le plus fruité ?  La boxe :  tu prends des pêches plein la poire, tu tombes dans les pommes et tout ça pour des prunes.",
        "Quel est le sport le plus fruité ? La boxe, parce que quand on te met une pêche dans la poire, tu tombes dans les pommes, t'as pas intérêt à ramener ta fraise et tout ça pour des prunes.",
        "Quel fruit obtient-on en tirant sur la queue d'une vache ? Un meuhh-long",
        "Quelle différence y a-t-il entre un horloger et une girouette ? L'horloger vend des montres et la girouette montre le vent.",
        "Quelle est la ressemblance entre un facteur et un jongleur ? Il leur faut tous les deux beaucoup d'adresse.",
        "Quelle est la ressemblance entre un parachute et l'humour ? Quand on n'en a pas, on s'écrase !",
        "Sur le tournage d'un film de Tarzan, l'acteur principal se plaint :  - A chaque fois que je m'accroche à une liane, le metteur en scène crit : Coupez !",
        "Un casse-pieds demande à un peintre:  - Pourquoi ne peignez-vous que des paysages?  - Parce que jamais un arbre n'est venu me dire qu'il n'était pas ressemblant!",
        "Un client entre chez un marchand de tableaux. Il demande:  - Je voudrais quelque chose pour ma salle-à-manger. Il faut que ce soit de bon goût, pas trop cher, et de préférence, à l'huile.  - Je vois, répond le marchand. Vous voulez une boite de sardines.",
        "Un client revient chez le pharmacien :  - Votre dentifrice a un goût infect.  - Et alors ? De toute façon, vous le recrachez.",
        "Un clochard discute avec un autre :  - Grâce à ma trompette, je suis très riche.  - Les gens te donnent beaucoup d'argent pour que tu joues ?  - Non justement, pour que je ne joue pas.",
        "Un commerçant demande à un client:  - Qu'est-ce que je vous sers?  - Serrez-moi la main!",
        "Un copain dit à Julien :  - Tu m'avais donné ta parole, et tu ne l'as pas tenue.  - je ne pouvais pas la tenir puisque je te l'avais donnée.",
        "Un e parle avec un é. - Tu peux répéter, je ne comprends rien avec ton accent !",
        "Un gendarme arrête une automobile qui roulait à trop grande vitesse :   - A combien rouliez-vous ?   - A deux seulement ! Mais si vous voulez monter, il reste de la place !",
        "Un gendarme fait stopper une automobiliste :  - Vous n'avez pas vu le feu rouge ?  - Si si. C'est vous que je n'avais pas vu !",
        "Un homme dit à un autre:  - On joue aux dames?  - Je ne peux pas, je ne suis pas marié!",
        "Un homme raconte :  - Je suis parti en voyage. J'ai écrit tous les jours à ma fiancée et à mon retour, elle s'est mariée.  - Eh bien, bravo !  - Non, sniff, elle s'est mariée avec le facteur !",
        "Un homme se présente chez le médecin:  - Voi-voilà-doc-docteur, je bébé, je bégaie. Alors le médecin:  - Bien, nous zazaa, nous zalons a-a-arran, arranger ça!",
        "Un homme va acheter un lit et demande à ce qu'il soit très solide. Le vendeur s'étonne:  - Pourtant, vous n'êtes pas si gros.  - Non, mais j'ai le sommeil lourd!",
        "Un invité murmure à sa voisine:  - Le champagne vous rend jolie.  - Je n'en ai pas bu une seule coupe.  - Oui, mais moi j'en suis à ma dixième!",
        "Un monsieur demande au serveur :  - Est-ce que je pourrais avoir un verre de vin ?  - Du blanc ou du rouge ?  - Ça n'a pas d'importance, c'est pour un aveugle.",
        "Un touriste visite un château en Ecosse:  - On m'a dit que votre château est hanté, dit-il au châtelain.  - C'est faux! Je n'y ai jamais vu aucun fantôme et pourtant je vis ici depuis 300 ans.",
        "Une dame dit à un oculiste :  - Docteur, ma vue baisse.  - Ah ! fait l'oculiste, et que faites-vous dans la vies ?  - ben justement, je suis voyante !",
        "Une grand-mère demande à son petit fils : - Qu'est-ce que ça veut dire « zarbi » ? - La même chose que « chelou » mamie",
        "Une jeune femme demande à une autre :  - Alors, toujours amoureuse de ton parachutiste ?  - Non, je l'ai laissé tombé.",
        "Une jeune fille se plaint à son amie :  - A tous nos rendez-vous, il m'offre des fleurs fanées.  - Eh bien, essaye d'arriver à l'heure ...",
        "Une mandarine va rendre visite à une clémentine malade : - Alors, que t'arrive-t-il ? - Que des pépins !",
        "Une mère demande à son fils : - Tu as fais ta lettre au Père Noël ? - Non mais je lui ai envoyé un texto !",
        "Une mère dit à son garçon :  -N'oublie pas que nous sommes sur terre pour travailler.  - Bon, alors moi, plus tard je serai marin !",
        "Une toute petite fille sort de la salle de bain. Elle crie :  - Maman, maman, est-ce que tu savais que papa est un garçon ?",
        "Une vis à un tournevis : - Tu me fais tourner la tête",
        ]

    def setTwitchToken(self):
        url = 'https://id.twitch.tv/oauth2/token'
        params = {'client_id': self.TWITCH_CLIENT_ID, 'client_secret': self.TWITCH_CLIENT_SECRET, 'grant_type': 'client_credentials'}
        tokenData = requests.post(url, json=params)
        self.TWITCH_TOKEN = tokenData.json()['access_token']

    def getTwitchDrops(self, game):
        self.setTwitchToken()
        gameIds = {
            'Sea of Thieves': '490377'}
        url = 'https://api.twitch.tv/helix/search/channels'
        params={'live_only': 'true', 'first': '100', 'query': game}
        headers = {'Authorization': 'Bearer '+self.TWITCH_TOKEN, 'Client-Id': self.TWITCH_CLIENT_ID}
        channelList = requests.get(url, params=params, headers=headers)
        channelList = json.loads(channelList.text)
        liveChanWithDrops = []
        for channel in channelList['data']:
            if channel['game_id'] == gameIds[game] and any(x in channel['title'] for x in ['drop', 'Drop', 'DROP']):
                liveChanWithDrops.append('https://www.twitch.tv/'+channel['broadcaster_login'])
        return liveChanWithDrops

    # kiwiCommands
    def kiwiHelp(self):
        helpmsg = """Je suis Kiwibot, un bot d'une intelligence douteuse, mais aux fonctionnalités étonnantes (ou pas).
        $kiwihelp: Affiche cette aide (bon en même temps si elle s'affiche c'est que tu connais cette commande)
        $kiwiblague: Je te raconte mes meilleures blagues pour animer tes soirées
        $kiwidrops: J'affiche les streams live de Sea of Thieves avec les drops actifs"""
        return helpmsg

    def kiwiBlague(self):
        return random.choice(self.blagues)