import os
import math
import sys
# import numpy
from PIL import Image
from collections import Counter

languages = {"Afar":"aar", "Abkhazian":"abk", "Afrikaans":"afr", "Akan":"aka", "Albanian":"alb", "Amharic":"amh", "Arabic":"ara", "Aragonese":"arg", "Armenian":"arm", "Assamese":"asm", "Avaric":"ava", "Avestan":"ave", "Aymara":"aym", "Azerbaijani":"aze", "Bashkir":"bak", "Bambara":"bam", "Basque":"baq", "Belarusian":"bel", "Bengali":"ben", "Bihari languages":"bih", "Bislama":"bis", "Bosnian":"bos", "Breton":"bre", "Bulgarian":"bul", "Burmese":"bur", "Catalan; Valencian":"cat", "Chamorro":"cha", "Chechen":"che", "Chinese":"chi", "Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic":"chu", "Chuvash":"chv", "Cornish":"cor", "Corsican":"cos", "Cree":"cre", "Czech":"cze", "Danish":"dan", "Divehi; Dhivehi; Maldivian":"div", "Dutch; Flemish":"dut", "Dzongkha":"dzo", "English":"eng", "Esperanto":"epo", "Estonian":"est", "Ewe":"ewe", "Faroese":"fao", "Fijian":"fij", "Finnish":"fin", "French":"fre", "Western Frisian":"fry", "Fulah":"ful", "Georgian":"geo", "German":"ger", "Gaelic; Scottish Gaelic":"gla", "Irish":"gle", "Galician":"glg", "Manx":"glv", "Greek,  Modern (1453-)":"gre", "Guarani":"grn", "Gujarati":"guj", "Haitian; Haitian Creole":"hat", "Hausa":"hau", "Hebrew":"heb", "Herero":"her", "Hindi":"hin", "Hiri Motu":"hmo", "Croatian":"hrv", "Hungarian":"hun", "Igbo":"ibo", "Icelandic":"ice", "Ido":"ido", "Sichuan Yi; Nuosu":"iii", "Inuktitut":"iku", "Interlingue; Occidental":"ile", "Interlingua (International Auxiliary Language Association)":"ina", "Indonesian":"ind", "Inupiaq":"ipk", "Italian":"ita", "Javanese":"jav", "Japanese":"jpn", "Kalaallisut; Greenlandic":"kal", "Kannada":"kan", "Kashmiri":"kas", "Kanuri":"kau", "Kazakh":"kaz", "Central Khmer":"khm", "Kikuyu; Gikuyu":"kik", "Kinyarwanda":"kin", "Kirghiz; Kyrgyz":"kir", "Komi":"kom", "Kongo":"kon", "Korean":"kor", "Kuanyama; Kwanyama":"kua", "Kurdish":"kur", "Lao":"lao", "Latin":"lat", "Latvian":"lav", "Limburgan; Limburger; Limburgish":"lim", "Lingala":"lin", "Lithuanian":"lit", "Luxembourgish; Letzeburgesch":"ltz", "Luba-Katanga":"lub", "Ganda":"lug", "Macedonian":"mac", "Marshallese":"mah", "Malayalam":"mal", "Maori":"mao", "Marathi":"mar", "Malay":"may", "Malagasy":"mlg", "Maltese":"mlt", "Mongolian":"mon", "Nauru":"nau", "Navajo; Navaho":"nav", "Ndebele,  South; South Ndebele":"nbl", "Ndebele,  North; North Ndebele":"nde", "Ndonga":"ndo", "Nepali":"nep", "Norwegian Nynorsk; Nynorsk,  Norwegian":"nno", "Bokmål,  Norwegian; Norwegian Bokmål":"nob", "Norwegian":"nor", "Chichewa; Chewa; Nyanja":"nya", "Occitan (post 1500)":"oci", "Ojibwa":"oji", "Oriya":"ori", "Oromo":"orm", "Ossetian; Ossetic":"oss", "Panjabi; Punjabi":"pan", "Persian":"per", "Pali":"pli", "Polish":"pol", "Portuguese":"por", "Pushto; Pashto":"pus", "Quechua":"que", "Romansh":"roh", "Romanian; Moldavian; Moldovan":"rum", "Rundi":"run", "Russian":"rus", "Sango":"sag", "Sanskrit":"san", "Sinhala; Sinhalese":"sin", "Slovak":"slo", "Slovenian":"slv", "Northern Sami":"sme", "Samoan":"smo", "Shona":"sna", "Sindhi":"snd", "Somali":"som", "Sotho,  Southern":"sot", "Spanish; Castilian":"spa", "Sardinian":"srd", "Serbian":"srp", "Swati":"ssw", "Sundanese":"sun", "Swahili":"swa", "Swedish":"swe", "Tahitian":"tah", "Tamil":"tam", "Tatar":"tat", "Telugu":"tel", "Tajik":"tgk", "Tagalog":"tgl", "Thai":"tha", "Tibetan":"tib", "Tigrinya":"tir", "Tonga (Tonga Islands)":"ton", "Tswana":"tsn", "Tsonga":"tso", "Turkmen":"tuk", "Turkish":"tur", "Twi":"twi", "Uighur; Uyghur":"uig", "Ukrainian":"ukr", "Urdu":"urd", "Uzbek":"uzb", "Venda":"ven", "Vietnamese":"vie", "Volapük":"vol", "Welsh":"wel", "Walloon":"wln", "Wolof":"wol", "Xhosa":"xho", "Yiddish":"yid", "Yoruba":"yor", "Zhuang; Chuang":"zha", "Zulu":"zul"}

def main(input_chapter, series_title, input_volume, input_language, groups, folder='.'):
    input_chapter = str(input_chapter)
    images_width = []
    images_height = []
    images = []

    for f in os.listdir(folder):
        if f.endswith(('.png', '.jpg')):
            image = Image.open(os.path.join(folder, f))
            w, h = image.size
            images.append(f)
            images_width.append(w)
            images_height.append(h)
            image.close()
            continue
        else:
            continue

    # print(images_width)
    # print(images_height)

    # width_mean = (sum(images_width))/(len(images_width))
    # height_mean = (sum(images_height))/(len(images_height))

    # distance_to_mean_width = [((w - width_mean) ** 2) for w in images_width]
    # distance_to_mean_height = [((h - height_mean) ** 2) for h in images_height]

    # sum_distance_width = sum(distance_to_mean_width)
    # sum_distance_height = sum(distance_to_mean_height)

    # sum_division_width = sum_distance_width/(len(images_width))
    # sum_division_height = sum_distance_height/(len(images_height))

    # std_width = math.sqrt(sum_division_width)
    # std_height = math.sqrt(sum_division_height)

    # print(std_width)
    # print(std_height)

    n = len(images_width) 
    
    width_data = Counter(images_width) 
    get_width_mode = dict(width_data) 
    width_mode = [k for k, v in get_width_mode.items() if v == max(list(width_data.values()))] 

    if len(width_mode) == n: 
        get_width_mode = "No mode found"
    else: 
        get_width_mode = int(width_mode[0])

    n = len(images_height) 

    height_data = Counter(images_height) 
    get_height_mode = dict(height_data) 
    height_mode = [k for k, v in get_height_mode.items() if v == max(list(height_data.values()))] 

    if len(height_mode) == n: 
        get_height_mode = "No mode found"
    else: 
        get_height_mode = int(height_mode[0])


    if input_chapter != '':
        parts = input_chapter.split('.', 1)
        c = int(parts[0])
        chap_no = str(c).zfill(3)
        chap_prefix = 'c' if c < 1000 else 'd'
        chap_no = chap_no + '.' + parts[1] if len(parts) > 1 else chap_no
        chapter_number = chap_prefix + chap_no
    else:
        chapter_number = str(0).zfill(3)

    if input_volume != '':
        volume_number = f' (v{input_volume.zfill(2)})'
    else:
        volume_number = ''

    if input_language.lower() != '':
        languages_match = [l for l in languages.keys() if input_language.title() in l]
        if len(languages_match) > 1:
            print("Found multiple matching languages, please choose one from the following options.")
            [print(x) for x in languages_match]
            lang = int(input(f'Choose a number matching the position of the language. '))
            if lang not in range(1, (len(languages_match) + 1)):
                sys.exit('Invalid input.')
            else:
                lang_to_use = languages_match[(lang - 1)]
                language = f' [{languages[lang_to_use]}]'
        else:
            language = f' [{languages[language.title()]}]'
    else:
        language = ''

    if groups != '':
        if input_chapter == '':
            suffix = f'[Oneshot] [{groups}]'
        else:
            suffix = f'[{groups}]'
    else:
        if input_chapter == '':
            suffix = '[Oneshot] [Unknown]'
        else:
            suffix = '[Unknown]'

    prefix = f'{series_title.title()}{language} - {chapter_number}{volume_number}'

    page_number = 1

    for i, w in zip(images, images_width):
        
        width_range = range((w - 50),(w + 51))
        mode_range = range(((get_width_mode * 2) - 50),((get_width_mode * 2) + 51))

        if width_range[0] in mode_range or width_range[-1] in mode_range:
            page_no = f'{page_number:0>3}-{(page_number+1):0>3}'
            page_number += 2
        else:
            page_no = f'{page_number:0>3}'
            page_number += 1

        ext = i.rsplit('.', 1)[-1]
        page_name = f'{prefix} - p{page_no} {suffix}.{ext}'
        os.rename(os.path.join(folder, i), os.path.join(folder, page_name))
        print(f'Renamed {folder}: {i} to {folder}: {page_name}')

bulk_mode = input('Bulk mode? y or n ').lower()

if bulk_mode == 'y':
    folder_number = 1
    series_title = input('The series title: ').title()
    input_volume = input('The volume number if applicable: ')
    input_language = input('The language, if english leave blank: ')
    # groups = [x for x in input('The groups that worked on the series, separate each one with a , : ').split()]
    groups = input('The groups that worked on the series, separate each one with a , : ')
    for folder in os.listdir('.'):
        if os.path.isdir(folder):
            main(folder_number, series_title, input_volume, input_language, groups, folder)
            folder_number += 1
            continue
        else:
            continue
else:
    folder = os.path.relpath(".","..")
    series_title = input('The series title: ').title()
    input_chapter = input("The chapter number, if the chapter is a oneshot, leave this field empty: ")
    input_volume = input('The volume number if applicable: ')
    input_language = input('The language, if english leave blank: ')
    # groups = [x for x in input('The groups that worked on the series, separate each one with a , : ').split()]
    groups = input('The groups that worked on the series, separate each one with a , : ')
    main(input_chapter, series_title, input_volume, input_language, groups)