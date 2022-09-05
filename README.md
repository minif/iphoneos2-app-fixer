# iphoneos2-app-fixer
#### A simple tool that modifies .ipa files to eliminate the "The application cannot be opened" error. 

### Explanation 
On Jailbroken iPhone OS 3.0+, users can install and run decrypted applications by using Appsync. 
However, iPhone OS 2.0 works slightly differently. The current solution is to overwrite MobileInstallation, allowing the installation 
of any decrypted .ipa file, but nothing is done to modify if apps can be run.

Fortunately, there is a quirk with how iPhone OS 2.0 works; So long as `info.plist` contains the key 
`SignerIdentity` with a value `Apple iPhone OS Application Signing`, and an encrypted app (either from the App Store or iTunes) 
is downloaded, decrypted apps will work without problem.

Old app cracking tools of the era would add this entry to `info.plist`, such as Crackulous. However, newer tools do not add this entry.
As a result, iPhone OS 2.0 will display the "The application cannot be opened" error. This tool adds back these entries to avoid the error.

### Requires
- Python 3.9 (Probably, untested for older versions)

### Usage
- Download repository to computer
- Place .ipa files into the /input folder
- In terminal, run the following command: 
  - On mac, use python3 rather than python
```
cd /path/to/gpx-to-csv
python main.py
```
- Optionally, use the included .bat or .sh files
- Files should now be updated.

### Troubleshooting

##### "The application cannot be opened" 
Make sure an encrypted app from the App Store is installed. Try to find an iPhone OS 2 app on the App Store. Alternitavely, downgrade an app
in your purchased tab to an older version. Sync that encrypted .ipa the same way you install .ipa files on your device. Then, reinstall all cracked apps.

If you are still having issues, contact me with the .ipa in question and I will investigate.

##### App crashing on launch
This might be an issue relating to permissions of the app binary itself. This tool does not fix this issue. 
Install MobileTerminal and `chmod -x` on the app binary.
A crude but effective method would to run `chmod -R 777 ~/Applications/*` which will work for all Applications.

Some applications will not be solved by this method. It will most likely not run on iPhone OS 2.0.

##### Unable to install
Make sure `MobileInstallation` is patched. If it is, the app may not be properly cracked. You may need to obtain a device on iOS 6 to dump the app (using the lock bug)
and then run that dump through this tool.

##### "(!!!) Error converting (app)!"
The tool has somehow run into an error. Contact me or leave an issue with a link to the app in question. It could either be an invalid .ipa file or an issue with the tool.

(This tool is extremely basic and does not test .ipa files. This functionality may be incorporated in the future)
### License
This software is licenced under the [public domain](https://github.com/minif/iphoneos2-app-fixer/blob/master/LICENSE). 
You may use it in any way without restriction. 
