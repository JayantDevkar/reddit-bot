from wit import Wit
from replies import *

Traits = 'traits'
Entities = 'entities'
Greeting = 'greetings'
Access_Token = 'EM4HWKVERLHRFOQGPSCGBM27BZYN3RO2'
Behaviour = 'behaviour'
Gender = 'gender'
Intent = 'intent'
Weight = 'weight'
Sports = 'sports'
Places = 'places'
Person = 'person'
Show = 'shows'
Music = 'music'
LoveLife = 'LoveLife'
Virgin = 'verginity'
Movie = 'movie'
Relationship = 'relationship'
Food = 'eat'
Weed = 'weed'
Country = 'country'
Skill = 'skills'
Height = 'height'
Favorite = 'favorite'
Value = 'value'
Hobby = 'hobby'
Location = 'location'
Age = 'age'


def get_reply(qns):
    final_reply = ""

    dora = Wit(Access_Token)
    dict = dora.message(qns)
    entity_list = dict[Entities]
    print(entity_list)

    # TESTING
    # entity_list = qns

    # Check for greetings
    Lonely = 'lonely' in entity_list
    Feelings = 'feelings' in entity_list
    Happy = 'happy' in entity_list
    if Greeting in entity_list:
        final_reply += get_greetings(entity_list)

    # if Age in dict:
    if Age in entity_list:
        # final_reply += " "
        final_reply += get_age(entity_list)

    # Roles go in here.
    if Gender in entity_list:
        final_reply += get_gender(entity_list, qns)

    if Weight in entity_list:
        final_reply += get_weight(entity_list)

    if Height in entity_list:
        final_reply += get_height(entity_list)

    if Location in entity_list:
        final_reply += get_location(entity_list)

    if Lonely or Happy or Feelings:
        final_reply += get_feelings(entity_list, qns)

    if Country in entity_list:
        final_reply += get_country(entity_list, qns)

    if Hobby in entity_list:
        final_reply += get_hobby(entity_list)

    if Skill in entity_list:
        final_reply += get_skills(qns)

    if Music in entity_list:
        final_reply += get_favorite(entity_list, qns)

    if Food in entity_list:
        final_reply += get_favorite(entity_list, qns)

    if Movie in entity_list:
        final_reply += get_favorite(entity_list, qns)

    if Places in entity_list:
        final_reply += get_favorite(entity_list, qns)

    if Weed in entity_list:
        final_reply += get_weed(entity_list, qns)

    if Relationship in entity_list:
        final_reply += get_relation(entity_list, qns)

    if Virgin in entity_list:
        final_reply += get_virginity(entity_list, qns)

    if LoveLife in entity_list:
        final_reply += get_LoveLife(entity_list, qns)

    if Show in entity_list:
        final_reply += get_favorite(entity_list, qns)

    if Sports in entity_list:
        final_reply += get_favorite(entity_list, qns)

    if Favorite in entity_list and Person in entity_list:
        final_reply += get_favorite(entity_list, qns)

    if final_reply == '':
        return "Sorry the A.I does not know how to answer that, yet."
    return final_reply


def main():
    print(get_reply("How tall are you?"))


if __name__ == '__main__':
    main()
