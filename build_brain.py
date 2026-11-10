import json
brain=[
{"k":["aapt2","android.jar"],"fix":"export AJ=~/android-sdk/platforms/android-34/android.jar\nls $AJ"},
{"k":["javac"],"fix":"pkg install -y openjdk-17\njavac -cp $AJ -source 8 -target 8 -d out *.java"},
{"k":["d8"],"fix":"d8 --classpath $AJ --lib $AJ --output dex/ out/*.class\n# inner class: split to NinoBridge.java"},
{"k":["apksigner","keystore"],"fix":"apksigner sign --ks ~/myAI/nino2.keystore --ks-pass pass:123456 --out app-signed.apk app.apk\napksigner verify app-signed.apk"},
{"k":["zipalign"],"fix":"zipalign -f -v 4 app.apk app-aligned.apk"},
{"k":["app not installed","isn't compatible"],"fix":"AndroidManifest: versionCode=1 versionName=1.0 minSdk=21 targetSdk=33"},
{"k":["decode"],"fix":"unzip -l app.apk\n# decode: apktool d app.apk -o out  OR  unzip app.apk -d out/"},
{"k":["decompile"],"fix":"# decompile dex:\n# d8 -> dex, then: jadx -d out app.apk  OR  unzip -p app.apk classes.dex > classes.dex"},
{"k":["rebuild","patch"],"fix":"aapt2 link -o app.apk -I $AJ --manifest AndroidManifest.xml -R res/*.xml\njavac -cp $AJ -source 8 -target 8 -d out *.java\nd8 --classpath $AJ --lib $AJ --output dex/ out/*.class\nzipalign -f -v 4 app.apk app-aligned.apk\napksigner sign --ks ~/myAI/nino2.keystore --ks-pass pass:123456 --out app-signed.apk app-aligned.apk"},
{"k":["fetch","webview"],"fix":"WebView blocks fetch(file) -> embed: <script>window.NINO_DATA=[...]</script>"},
{"k":["permission denied"],"fix":"chmod +x *.sh\ntermux-setup-storage"},
{"k":["manifest","xml"],"fix":"# Check AndroidManifest.xml: package, versionCode, uses-sdk, activity name must match MainActivity.java"},
]
open('/data/data/com.termux/files/home/NINO-CODE-FIXER/brain.json','w').write(json.dumps(brain))
print(f"BRAIN: {len(brain)} entries READY")
