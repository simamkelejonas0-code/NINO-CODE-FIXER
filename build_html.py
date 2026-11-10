parts=[]
parts.append("<!DOCTYPE html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>NINO CODE FIXER</title>")
parts.append("<style>body{background:#000;color:#0f0;font-family:monospace;padding:10px}textarea{width:100%;height:180px;background:#111;color:#0f0}button{padding:14px;margin:5px;background:#0f0;color:#000;border:0;font-weight:bold;font-size:16px}pre{white-space:pre-wrap;background:#111;padding:10px}</style></head><body>")
parts.append("<h2>NINO CODE FIXER - V9 HONEST</h2><p>NO FAKE AI. NO GUESSING. ME = GENIUS. APK = YOUR BASH BAG.<br>God sleeps. Son watches. For every child.</p>")
parts.append("<textarea id='e' placeholder='Paste WHOLE Termux block here - commands + results + errors, all of it'></textarea><br>")
parts.append("<button id='b1'>GET WORKING BUILD SCRIPT</button>")
parts.append("<button id='b2'>PREPARE BLOCK FOR NINO (ME)</button>")
parts.append("<pre id='o'>Tap a button. Copy ALL. Bash it or paste to me. No editing lines.</pre><script>")
parts.append("""
function show(t){document.getElementById('o').textContent=t;}
document.getElementById('b1').addEventListener('click',function(){
show(`#!/bin/bash
# NINO CODE FIXER - LAST WORKING BUILD - WRITTEN BY NINO, TESTED BY YOU
# Copy ALL, paste in Termux, bash it. No editing.
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
cp NINO-CODE-FIXER.apk ~/storage/downloads/
ls -lh NINO-CODE-FIXER.apk
echo DONE - NINO CODE FIXER BUILT`);
});
document.getElementById('b2').addEventListener('click',function(){
let t=document.getElementById('e').value;
if(!t){show('Paste WHOLE Termux block first, then tap this.');return;}
show(`NINO - FIX THIS, BASH TO BASH. I bash, I never type. Give me ONE whole ready-to-bash script, copy-paste to Termux, no editing lines, no check spelling, no open file. Accurate precise like everyday.\\n\\nMY WHOLE TERMUX BLOCK:\\n`+t+`\\n\\nGIVE ME WHOLE BASH NOW.`);
});
""")
parts.append("</script></body></html>")
open('/data/data/com.termux/files/home/NINO-CODE-FIXER/APK/index.html','w').write("".join(parts))
print("V9 HONEST READY")
