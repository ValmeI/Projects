from nltk.corpus import stopwords
import re
import string
from estnltk import Text


def clearup(s, chars):
    clean_strings = re.sub('[%s]' % chars, '', s).lower()
    return clean_strings


est_stops = set(stopwords.words('estonian-stopwords - PRIS'))
f_open = open(r'C:\Users\ignar.valme\Desktop\pöördumise sisu.txt', 'r', encoding='utf-8')

'# eemaldab laused või nimed mis pole olulised'
clean = f_open.read()\
    .replace('Käesolev e-kiri võib sisaldada asutusesiseseks kasutamiseks tunnistatud teavet', '')\
    .replace('This e-mail may contain information which is classified for official use', '')\
    .replace('Rasmus Varblane', '')\
    .replace('Rauno Pihel', '')\
    .replace('Kui te ei ole selle kirja adressaat, palun võtke ühendust saatjaga ning kustutage e-kiri arvutist', '')\
    .replace('See kiri on mõeldud adressaadireal mõeldud isikule', '')\
    .replace('Isik, kes ei ole märgitud kirja adressaadiks, ei tohi seda kirja mingil viisil kasutada', '')\
    .replace('Kui olete saanud kirja eksituse tõttu, palun teavitage sellest kohe kirja saatjat ja kustutage kiri koos kõikide lisadega', '')\
    .replace('E-kirjas sisalduvat teavet ei tohi ilma saatja selgelt väljendatud loata edasi saata ega mistahes viisil kõrvalistele isikutele avaldada', '')\
    .replace('Juhul, kui Te olete saanud käesoleva e-kirja eksituse tõttu, teavitage sellest koheselt saatjat ning kustutage e-kiri oma arvutist', '')\
    .replace('This e-mail and any attachments may contain confidential and privileged information', '')\
    .replace('If you are not the intended recipient, please notify the sender immediately by return e-mail, delete this e-mail and destroy any copies', '')\
    .replace('Any dissemination or use of this information by a person other than the intended recipient is unauthorized and may be illegal', '')\
    .replace('Selles e-kirjas sisalduv teave (kaasa arvatud manused) on mõeldud ametialaseks kasutamiseks ning seda võivad kasutada vaid e-kirja adressaadid', '')\
    .replace('This e-mail may contain information which is classified for internal use', '')\
    .replace('If you are not the intended recipient of this message, please notify the sender immediately and delete the message', '')\
    .replace('This e-mail and any attachments may contain sensitive and privileged information', '')\
    .replace('See kiri on mõeldud adressaadireal nimetatud isikule', '')\
    .replace('Vaata oma registreeritud pöördumist iseteeninduse portaalist', '')\
    .replace('kus saad seda vajadusel taasavada', '')\
    .replace('VAATA PÖÖRDUMIST', '')\
    .replace('Hea kasutaja!', '')\
    .replace('Sinu pöördumine', '')


'# split to list'
all_words = clean.split()

print(all_words)

'# TEMP tühja faili kirjutamine, et ei peaks käsitsi kustutama'
file_open = open(r'C:\Users\ignar.valme\Desktop\pöördumise sisu TEMP_WRITE.txt', 'w', encoding='utf-8')

'# write, so it would create a new empty file, to avoid manual deleting'
f_write = open(r'C:\Users\ignar.valme\Desktop\pöördumise sisu WRITE.txt', 'w', encoding='utf-8')

for word in all_words:
        '# appends new lines to file, without nextline'
        f_writeTEXT = open(r'C:\Users\ignar.valme\Desktop\pöördumise sisu TEMP_WRITE.txt', 'a', encoding='utf-8')
        f_writeTEXT.write(word + ' ')
        #print(word)
print('END TEMP WRITE')

'# TEMP failist'
temp_open = open(r'C:\Users\ignar.valme\Desktop\pöördumise sisu TEMP_WRITE.txt', 'r', encoding='utf-8')

'# estnltk text kujule'
text = Text(temp_open.read())
'#listi kujule ja ainult lemmas, kui tahta kõik siis text.get.word_texts.lemmas.postag_descriptions.as_dataframe'
vastus = text.get.lemmas.as_list
#vastus = text.get.lemmas.

#print(vastus)

print('START LEMMAS LOOP')
for x in vastus:
    for y in x:
        #print(y)
        '# eemaldab tähemärgid, neil oli vaja  kuna bugi on 1.4 üleval https://github.com/estnltk/estnltk/issues/99'
        word_after_estnltk = clearup(y, string.punctuation+string.digits)
        '# tühjade väljade eemaldus, mis tekkis kui tähemärgid cleaniti eelmise funksiooniga'
        if word_after_estnltk is '':
            continue
        'eemaldame tekstist stopword-id'
        if word_after_estnltk not in est_stops:
            print(word_after_estnltk)
            '# appends new lines to file with nextline'
            f_write = open(r'C:\Users\ignar.valme\Desktop\pöördumise sisu WRITE.txt', 'a', encoding='utf-8')
            f_write.write(word_after_estnltk)
            f_write.write('\n')

print("\n\n--------END\n\n--------")



