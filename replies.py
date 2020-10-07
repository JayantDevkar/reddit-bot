import random

wrng = ['no. ', 'negative. ', 'nope. ', 'false. ']
rght = ['Yes. ', 'Correct. ', "Yup. ", 'yes. ', 'Si. ', "Bingo! ",
        'How do you know tha...?  Wait.... who is the A.I me or you? ']


def get_greetings(e_lst):
    comment = ""
    reply = ['Helo.', 'Hi. ', "Hello! ", "Hey! ", "Hi. ", "Hi There! ", "Hello There! ", "Hi, I am here to help you "]

    wellbng = ["I'm fine, thanks.\n", "I'm good.\n", "I'm great.\n", "I'm doing good, thanks.\n",
               "Trying to stay alive "
               "for now.\n", "I'm holding up good.\n", "fine, i guess?.\n", "Trying my best to be  fine :).\n"]
    comment += reply[(random.randrange(0, len(reply)))]
    if "wellbeing" in e_lst:
        comment += wellbng[(random.randrange(0, len(wellbng)))]
    return comment


def get_age(e_list):
    date = ["19th June. ", "Born on 19th June 2000. ", "June 19 2000. ", "6/19/2000. ", "19/6/2000. ", "My birthday "
                                                                                                       "in on 19th "
                                                                                                       "June. ",
            "It's on 19th "
            "June. ",
            "19 June 2000", "Poped on Earth on 19th June 2000\nPs- sorry for cringe reply"]
    reply = ["I'm 19. ", "Gonna turn 20 next month. ", "19 years old. ", "Born in 2000. ",
             "This is my last teen year. ",
             "Last teen year", "Nineteen. "]
    value = extractor(e_list, 'birthday')
    if "birthdate" == value:
        return date[(random.randrange(0, len(date)))] + " "
    return reply[(random.randrange(0, len(reply)))] + " "


def get_gender(e_list, qns):
    comment = ''
    reply = ["I'm male. ", "Male. ", "I identify as a male."]
    statement = ["You are ", "No u ", "No, You are ", "You ", "u ", " U "]
    stm = extractor(e_list, 'statement')
    bhv = extractor(e_list, 'behaviour')

    if stm == 'true' and bhv == 'false':
        if 'gay' in qns.lower():
            comment += statement[(random.randrange(0, len(statement)))]
            comment += 'gay. '
            return comment
        if 'male' in qns.lower():
            return rght[(random.randrange(0, len(rght)))]
        return statement[(random.randrange(0, len(statement)))]
    elif bhv == 'false':
        if 'gay' in qns:
            return "Everybody a lil gay on the inside. "
        return wrng[(random.randrange(0, len(wrng)))]
    return reply[(random.randrange(0, len(reply)))]


def get_weight(e_list):
    comment = ''
    reply = ["Weird question to ask but ok. 175 lbs. ", "I don't check usually. ", "Like real time weight? How would "
                                                                                   "I know that? ", "FAT SHAME is a "
                                                                                                    "real world "
                                                                                                    "problem. "]
    statement = ["And you are ugly, did I complain? ", "And you are dumb, am i complaining? "]
    stm = extractor(e_list, 'statement')
    bhv = extractor(e_list, 'behaviour')

    if bhv == 'false' and stm == 'true':
        return statement[(random.randrange(0, len(statement)))]
    if bhv == 'false':
        return wrng[(random.randrange(0, len(wrng)))]
    return reply[(random.randrange(0, len(reply)))]


def get_location(e_list):
    reply = ["In your heart. ", "San Luis Obispo, CA. ", "Slo. ", "Stuck in Slo. ", "Latitude: 35.282753\nLongitude: "
                                                                                    "-120.659615 ", "35.2828° N, "
                                                                                                    "120.6596° W ",
             "That's a creepy question, but ok: San Luis Obispo ",
             "Oh so we are getting super personal I see, I'm in Slo ;) "]
    return reply[(random.randrange(0, len(reply)))]


def get_height(e_list):
    reply = ["I'm tall enough. ", "5'11 ", "Taller than you. ", "Girls need heels to kiss me. ", "Do you mean how big"
                                                                                                 "?\nReal big. "]
    statement = ["Wrong, I'm High", "And you are small. "]

    stm = extractor(e_list, 'statement')
    bhv = extractor(e_list, 'behaviour')

    if bhv == 'false' and stm == 'true':
        return statement[(random.randrange(0, len(statement)))]
    elif bhv == 'false':
        return wrng[(random.randrange(0, len(wrng)))]
    return reply[(random.randrange(0, len(reply)))]


def get_feelings(e_list, qns):
    reply = ['Yes like always. ', "yes. ", "si. ", 'yup. ', 'who is not?']

    horny = ["Eww ", "why are you?", "nah just bored. ", "twice a week. "]

    lonely = ['I have my roomates with me. ', "So lonely that my current jam is : Supalonely"]

    feelings = ["I'm booooored. ", "Quarantine sucks. ", "bored out of my mind. "]

    if 'lonely' in qns.lower():
        return lonely[(random.randrange(0, len(lonely)))]
    elif 'sad' in qns.lower() or 'depressed' in qns.lower():
        return reply[(random.randrange(0, len(reply)))]
    elif 'horny' in qns.lower():
        return horny[random.randrange(0, len(horny))]
    elif 'happy' in e_list:
        return wrng[(random.randrange(0, len(wrng)))]
    return feelings[(random.randrange(0, len(feelings)))]


def get_country(e_list, qns):
    reply = ["I'm from India. ", "I'm an Indian citizen. ", "I came from India. ", "I'm an international student from "
                                                                                   "India. ", "My family is in India."
                                                                                              " "]
    fav = ["India is my fav country. ", "Ofc it's India. "]
    bhv = extractor(e_list, 'behaviour')

    if 'favorite' in e_list:
        return fav[(random.randrange(0, len(fav)))]
    if bhv == 'false':
        if 'indian' or 'india' in qns.lower():
            return rght[(random.randrange(0, len(rght)))]
    return reply[(random.randrange(0, len(reply)))]


def get_hobby(e_list):
    reply = ['I run when I get bored. ', "I work on side projects like this. ", "I usually code when I get bored. ",
             "I like to go on hikes alone. ", "If I have free time, I sleep. ", "Eat. Sleep.Repeat. ", "Hobbies? LOL. ",
             "I hobby is to procrastinate. "]
    return reply[(random.randrange(0, len(reply)))]


def get_skills(qns):
    reply = ["1) Procrastination.\n2)Coding.\n3)Binge watching Netflix.\n4)fUnNY\nAsk for my 'technical' skills. "]
    skills = ['1)Seriously? you asked for my technical skills?\n I am too lazy to write sory. ']
    if 'technical' in qns.lower():
        return skills[0]
    return reply[0]


def get_dick(e_list, qns):
    reply = ['Mah dick is BIG. ', "All i'm going to say is 'I'm blessed'. ", "It's real big and thicc. "]
    smll = ["Your mom liked it so I don't know what you are talking about. ", "Is big enough to satisfy your mom. ",
            "It is the biggest I have ever seen. "]
    bg = ['You know it. ', "Is real big. ", "Big enough. ", "Once you go brown, other colors let you down. "]
    mom = ['Your mom sucked mine. ', "Sorry that's your mom's job. ", "I have gotten my dick sucked by your mom. "]
    stm = extractor(e_list, 'statement')
    if stm:
        if 'big' in qns.lower():
            return 'Thankyou.'
        if 'small' in qns.lower():
            return 'So do you. Fuck U.'
    if 'suck' in qns.lower() or 'sucked' in qns.lower():
        return mom[(random.randrange(0, len(mom)))]
    if 'big' in qns.lower():
        return bg[(random.randrange(0, len(bg)))]
    if 'small' in qns.lower():
        return smll[(random.randrange(0, len(smll)))]
    return reply[(random.randrange(0, len(reply)))]


def get_relation(e_list, qns):
    reply = ["I am single. ", ""]
    sng = ["Why are you interested in me? ", "Ooo Someone is curious about me. ", "Yes, Why? ", "Si", "Yup"]
    bhv = extractor(e_list, 'behaviour')
    crush = ["I don't have one. ", "You think I have a gf? Wow I'm like super proud of myself. ", " L .O .L "]
    if 'person' in e_list:
        if 'date' in qns.lower() or 'dated' in qns.lower():
            return sng[(random.randrange(0, len(sng)))]
    if 'single' in qns.lower():
        return sng[(random.randrange(0, len(sng)))]
    if 'girlfriend' in qns.lower() or 'gf' in qns.lower():
        return crush[(random.randrange(0, len(crush)))]
    if bhv == 'false' and 'relationship' in qns:
        return wrng[(random.randrange(0, len(wrng)))]
    return reply[(random.randrange(0, len(reply)))]


def get_virginity(e_list, qns):
    reply = ["You like to ask weird questions don't you. ", "Why are you asking these creepy questions? ",
             "You weird. "]
    stm = ["Nope, did your mom"]
    sex = ['I have done it more than you. ', "More than you. ", "mAnY tImEs. "]
    sttm = extractor(e_list, 'statement')
    bhv = extractor(e_list, 'behaviour')

    if sttm and 'virgin' in qns.lower():
        return stm[0]
    elif bhv == 'false':
        if 'virgin' in qns.lower():
            return wrng[(random.randrange(0, len(wrng)))]
    elif 'times' in e_list:
        return sex[(random.randrange(0, len(sex)))]
    elif 'had' in qns.lower():
        return rght[(random.randrange(0, len(rght)))]
    return reply[(random.randrange(0, len(reply)))]


def get_LoveLife(e_list, qns):
    reply = ["I love Jesus. ", "My love of life is Jesus. ", "I love trees :) "]
    crush = ['Only thing I have crush on is trees. ', "I have a crush on your mom. ", "wE aRe fRiEnDs now. "]
    wng = []
    if 'person' in e_list:
        return wng[(random.randrange(0, len(wrng)))]
    if 'love' in qns.lower():
        return reply[(random.randrange(0, len(reply)))]
    if 'crush' in qns.lower():
        return crush[(random.randrange(0, len(crush)))]


def get_weed(e_list, qns):
    reply = ["Weed is not a drug, it's a religion. ", "Weed every day keeps the mind on creative mode. ", "Weed can "
                                                                                                          "create "
                                                                                                          "sleep "
                                                                                                          "dependensies. ",
             "1/10 User of Weed gets addicted. ", "Weed might have withdrawal symptoms on daily users. ",
             "Weed can help you think straight. ", "Weed can make you see the WORLD AROUND YOU. ",
             "Weed was considered gateway drug in 60's. ", "Weed is the most used drug in the world. ",
             "Weed can be a CATALYST for many mental illnesses. "]

    return reply[(random.randrange(0, len(reply)))]


def get_favorite(e_list, qns):
    typ = 'specific' in e_list
    fov = 'favorite' in e_list
    if 'music' in e_list:
        reply = ["Currently listening to: https://open.spotify.com/track/5LmFXAPlf8vFDRHSM1VrTT?si=3foFH7SBSH"
                 "-SA5hpoMgo5A\n", "Here is a good playlist that I listen too : "
                                   "https://open.spotify.com/playlist/0YNrYTklGH97e8cZbhwPyK?si"
                                   "=t7F7SMYCR_KU44LNUCsKeQ\n", "I listen to Juice Wrld on repeat. "]
        fav = ["My fav genre is Hip-Hop. ", 'I like EDMs. ', "Rap is  one of my fav genre of music. ", "I think Bob "
                                                                                                       "Marley made "
                                                                                                       "the best "
                                                                                                       "music. "]
        msc = ['Good people by Jack Johnson. ', "Toosie Slide by Drake. ", "Redbone by Childish Gambino. ",
               "Chicago Freestyle by Drake. "]
        if typ:
            return fav[(random.randrange(0, len(fav)))]
        elif fov:
            return msc[(random.randrange(0, len(msc)))]
        return reply[(random.randrange(0, len(reply)))]


    elif 'eat' in e_list:
        reply = ["I ate pasta. ", "I eat when I get bored. ", "I eat sleep for dinner. ", "To broke to eat. ",
                 "Eating is a privilage I don't get in college. ", "Me after making toast: 'mom I cooked today'. "]

        fav = ["I like FOOD. ", "There is no favorite, I eat anything I can. ", "I like anything that I can buy under "
                                                                                "$10. ", "Cheap food = Favorite food."
                                                                                         " ", "I lovvvvvveeee spicy "
                                                                                              "food. ", "nugget. just "
                                                                                                        "one singular"
                                                                                                        " nugget. ",
               "Desi food is the best food. ", "Too broke to have a favorite kind of food. "]

        if typ or fov:
            return fav[(random.randrange(0, len(fav)))]
        return reply[(random.randrange(0, len(reply)))]

    elif 'movie' in e_list:
        fav = ["The invisible Man. ", "The Shutter Island. ", "Inception. ", "Seven. "]
        actor = ["Bradley Cooper. ", "Leonardo Dicaprio. ", "Brad Pitt. "]
        actress = ['Emma Stone. ', "Emma Watson. ", "Scarlett Johansson. "]
        tvp = ["Fav Genre: Crime Thriller. ", "Fav Genre: Crime. ", "Fav Genre: Thriller"]
        reply = ["I don't watch movies that often now a days. ", "I watch T.V series more. ",
                 "My life is no less than a movie so I watch that. "]

        if 'actor' in qns.lower() or 'movie star' in qns.lower():
            return actor[(random.randrange(0, len(actor)))]
        elif 'actress' in qns.lower():
            return actress[(random.randrange(0, len(actress)))]
        elif typ:
            return tvp[(random.randrange(0, len(tvp)))]
        elif fov:
            return fav[(random.randrange(0, len(fav)))]
        else:
            return reply[(random.randrange(0, len(reply)))]

    elif 'places' in e_list:
        reply = ["Haven't explored the world yet....", "Haven't been to a lot of places. "]
        vst = ['I wanna go to Europe. ', "I want to visit a carnival in Brazil. ", "I want to visit  Russia. "]
        tvp = ['I like quite places. ', "I like places were there are very few people. ", "I like to be in nature. "]

        if 'visit' in qns.lower():
            return vst[(random.randrange(0, len(vst)))]
        elif typ:
            return tvp[(random.randrange(0, len(tvp)))]
        return reply[(random.randrange(0, len(reply)))]

    elif 'person' in e_list:
        reply = ["Ofc it's you ", "Yes, u. ", "Listen to me. I like you. ", "Finally you asked, i LIKE YOU. "]
        return reply[(random.randrange(0, len(reply)))]

    elif 'shows' in e_list:

        reply = ["Space Force. ", "ASUR - Indian Show. ", "The Spy. "]
        fav = ["Breaking Bad. ", "My fav tv show has to be 'On Air with AIB S-1"]
        tvp = ["Fav Genre: Crime Thriller. ", "Fav Genre: Crime. ", "Fav Genre: Thriller"]

        if typ:
            return tvp[(random.randrange(0, len(tvp)))]
        if fov:
            return fav[(random.randrange(0, len(fav)))]
        return reply[(random.randrange(0, len(reply)))]

    elif 'sports' in e_list:
        reply = ["I don't watch sports. ", "I am not a sports person. ", "Sports don't interest me. "]
        return reply[(random.randrange(0, len(reply)))]












    # to extract value from the feedback


def extractor(obj, key):
    if key in obj:
        val = list(obj[key])[0]['value']
        if val:
            return val
    return None
