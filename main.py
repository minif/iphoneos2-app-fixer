from xml.dom.minidom import parse
import os
import zipfile
import plistlib
import warnings
import sys

# Tool related constants (No need to change)
INPUT_DIR = "input/" #Input directory for batch file conversion
NEW_KEY = "SignerIdentity"
NEW_VALUE = "Apple iPhone OS Application Signing"

def convert_ipa(input_ipa):
    """
    Adds NEW_KEY with value NEW_VALUE to the .ipa file passed in. Immediately writes to this file.
    :param input_ipa: Absolute filepath of .ipa file to read.
    :return: none
    """

    # Quick error checking to see if file is an ipa.
    if os.path.isdir(input_ipa):
        return
    if os.path.splitext(input_ipa)[1] != '.ipa':
        return
    # Perform the modification to info.plist
    with zipfile.ZipFile(input_ipa, 'a') as ipa_file:
        # Getting the info.plist, There should only be one app in Payload so this tool
        # just parses everything in that folder. (If multiple apps exist then they will all have
        # their info.plist modified)
        payload_path = zipfile.Path(ipa_file,'Payload/')
        for i in payload_path.iterdir():
            # Read the existing info.plist
            info_plist_data = ipa_file.read("Payload/%s/Info.plist"%i.name)
            info_plist = plistlib.loads(info_plist_data)
            # Add the key to the data
            info_plist[NEW_KEY]=NEW_VALUE
            # Write a new info.plist file with the modified data
            info_plist_new_data =ipa_file.open("Payload/%s/Info.plist"%i.name,"w")
            plistlib.dump(info_plist,info_plist_new_data)
            info_plist_new_data.close()
    print("Success converting %s!"%input_ipa)

def main():
    """
    Main program function. Finds and processes all ipa files
    :return: none
    """
    warnings.filterwarnings("ignore") # Do this so the zip library doesn't complain

    # Check arguements to get .ipa (or look for --batch)
    # If there is no arguements, display command information
    if len(sys.argv)<=1:
        print("Usage: main.py appname.ipa")
        print("Usage: main.py --batch inputfolder")
        sys.exit(1)

    if sys.argv[1]=="--batch":
        input = INPUT_DIR
        if len(sys.argv)>2:
            input = sys.argv[2]
        for ipa in os.listdir(input):
            try:
                convert_ipa(input+ipa)
            except:
                # Basic error handling so that loop is not inturruped
                print("(!!!) Error converting %s!"%input+ipa)
    else:
        try:
            convert_ipa(sys.argv[1])
        except:
            # Basic error handling so that loop is not inturruped
            print("(!!!) Error converting %s!"%sys.argv[1]+ipa)


    # Loop through all .ipa files in the input folder.


main()
