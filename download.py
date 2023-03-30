import os,re,shutil
import fileinput

dir_path = 'data/poc_python/page'

# boucler sur toutes les pages
def create_TRE_from_Template(textToReplace):
    shutil.copy('data/poc_python/template.download.html',
                'data/poc_python/page_created/'+'CodeSystem-'+textToReplace+'.download.html')
    for line in fileinput.input('data/poc_python/page_created/'+'CodeSystem-'+textToReplace+'.download.html',
                                inplace=True):
        print(line.replace('to_replace', textToReplace), end='')

def create_JDV_from_Template(textToReplace):
    shutil.copy('data/poc_python/template.download.html',
                'data/poc_python/page_created/'+'ValueSet-'+textToReplace+'.download.html')
    for line in fileinput.input('data/poc_python/page_created/'+'ValueSet-'+textToReplace+'.download.html',
                                inplace=True):
        print(line.replace('to_replace', textToReplace), end='')


for filename in os.listdir(dir_path):
    # vérifier si c'est un fichier
    if os.path.isfile(os.path.join(dir_path, filename)):
        #print(filename)
        matchCS = re.match(r'CodeSystem-(.*)\.ttl\.html', filename)
        if matchCS:
            matchedValue = matchCS.group(1)
            create_TRE_from_Template(matchedValue)
            print(matchedValue)
        matchVS = re.match(r'ValueSet-(.*)\.ttl\.html', filename)
        if matchVS:
            matchedValue = matchVS.group(1)
            create_JDV_from_Template(matchedValue)
            print(matchedValue)
