# iphoneos2-app-fixer
#### A simple tool that modifies .ipa files to eliminate the "The application cannot be opened" error. 

### Explanation 
On Jailbroken iPhone OS 3.0+, users can install and run decrypted applications by using Appsync. 
However, iPhone OS 2.0 works slightly differently. The current solution is to overwrite MobileInstallation, allowing the installation 
of any decrypted .ipa file, but nothing is done to modify if apps can be run.

Fortunately, there is a quirk with how iPhone OS 2.0 works; So long as `info.plist` contains the key 
`SignerIdentity` with a value `Apple iPhone OS Application Signing`, and `/var/mobile/Library/Caches/com.apple.mobile.installation.composite_trust.plist` contains the  `Apple iPhone OS Application Signing` key set to true, decrypted apps will work without problem.

Old app cracking tools of the era would add this entry to `info.plist`, such as Crackulous. However, newer tools do not add this entry.
As a result, iPhone OS 2.0 will display the "The application cannot be opened" error. This tool adds back these entries to avoid the error.

Make sure [the modified com.apple.mobile.installation.composite_trust.plist](https://github.com/minif/iphoneos2-app-fixer/raw/master/com.apple.mobile.installation.composite_trust.plist) file is placed in `/var/mobile/Library/Caches/`.

### Requires
- Python 3.9 (Probably, untested for older versions)

### Usage
- Download repository (git clone or download zip)
- Place .ipa files into the /input folder
- Use the included .bat or .sh files to perform the conversion

##### CLI Usage
```
cd /path/to/iphoneos2-app-fixer
python main.py appname
```
OR
```
cd /path/to/iphoneos2-app-fixer
python main.py --batch inputfolder
```

### Troubleshooting

##### "The application cannot be opened" 
Make sure [the modified com.apple.mobile.installation.composite_trust.plist](https://github.com/minif/iphoneos2-app-fixer/raw/master/com.apple.mobile.installation.composite_trust.plist) file is placed in `/var/mobile/Library/Caches/`. Reboot may be required.
You may need to reinstall all cracked apps.

If you are still having issues, contact me with the .ipa in question and I will investigate.

##### App crashing on launch
This might be an issue relating to permissions of the app binary itself. This tool does not fix this issue. 
Install MobileTerminal and `chmod -x` on the app binary. To find the app binary, use Filza, look in `/var/mobile/Applications` with Application Names enabled in preferences (the gear icon).
A crude but effective method would to run `chmod -R -x ~/Applications/*` which will work for all Applications.

Some applications will not be solved by this method. It will most likely not run on iPhone OS 2.0.

##### Unable to install
Make sure `MobileInstallation` is patched. If it is, the app may not be properly cracked. ~You may need to obtain a device on iOS 6 to dump the app (using the lock bug)
and then run that dump through this tool.

##### "(!!!) Error converting (app)!"
Contact me or leave an issue with a link to the app in question. It could either be an invalid .ipa file or an issue with the tool.

##### "ValueError: seek of closed file"
Remember to `cd` to the iphoneos2-app-fixer directory. 

(This tool is extremely basic and does not test .ipa files. This functionality may be incorporated in the future)

### License
This software is licenced under the [public domain](https://github.com/minif/iphoneos2-app-fixer/blob/master/LICENSE). 
