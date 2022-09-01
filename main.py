from xml.dom.minidom import parse
import os
import zipfile
import plistlib
import warnings

INPUT_DIR = "input/"
NEW_KEY = "SignerIdentity"
NEW_VALUE = "Apple iPhone OS Application Signing"

def convert_ipa(input_ipa):
    """
    Adds NEW_KEY with value NEW_VALUE to the .ipa file passed in. Immediately writes to this file.
    :param input_ipa: Absolute filepath of .ipa file to read.
    :return: none
    """
    if os.path.isdir(input_ipa):
        return
    with zipfile.ZipFile(input_ipa, 'a') as ipa_file:
        payload_path = zipfile.Path(ipa_file,'Payload/')
        for i in payload_path.iterdir():
            info_plist_data = ipa_file.read("Payload/%s/Info.plist"%i.name)
            info_plist = plistlib.loads(info_plist_data)
            info_plist[NEW_KEY]=NEW_VALUE
            info_plist_new_data =ipa_file.open("Payload/%s/Info.plist"%i.name,"w")
            plistlib.dump(info_plist,info_plist_new_data)
            info_plist_new_data.close()

def main():
    """
    Main program function. Finds and processes all ipa files
    :return: none
    """

    warnings.filterwarnings("ignore") # Do this so the zip library doesn't complain
    for ipa in os.listdir(INPUT_DIR):
        try:
            convert_ipa(INPUT_DIR+ipa)
        except:
            print("Error reading %s!"%INPUT_DIR+ipa)

main()
