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

### License
This software is licenced under the [public domain](https://github.com/minif/iphoneos2-app-fixer/blob/main/LICENSE). 
You may use it in any way without restriction. 