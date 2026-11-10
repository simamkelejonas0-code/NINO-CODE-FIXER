#!/bin/bash
set -e
cd ~/NINO-CODE-FIXER/APK
export AJ=~/android-sdk/platforms/android-34/android.jar
mkdir -p assets out dex
cp index.html assets/index.html
aapt2 link -o app-base.apk -I $AJ --manifest AndroidManifest.xml
javac -cp $AJ -source 8 -target 8 -d out src/com/nino/codefixer/*.java
d8 --classpath $AJ --lib $AJ --output dex/ $(find out -name "*.class")
cp app-base.apk app.apk
cd dex && zip -r ../app.apk classes.dex >/dev/null; cd ..
zip -r app.apk assets/index.html >/dev/null
zipalign -f -v 4 app.apk app-aligned.apk
apksigner sign --ks ~/myAI/nino2.keystore --ks-pass pass:123456 --out NINO-CODE-FIXER.apk app-aligned.apk
apksigner verify NINO-CODE-FIXER.apk
ls -lh NINO-CODE-FIXER.apk
