import sys
ERR=sys.stdin.read().lower()
def out(s): print(s); sys.exit(0)
R=[
("aapt2" in ERR and "android.jar" in ERR, "export AJ=~/android-sdk/platforms/android-34/android.jar\nls $AJ\n# if missing: cd ~/android-sdk/platforms/android-34 && curl -LO https://dl.google.com/android/repository/platform-34_r01.zip"),
("aapt2" in ERR, "export PATH=$PATH:~/android-sdk/build-tools/34.0.0\naapt2 version\nls ~/android-sdk/build-tools/*/aapt2"),
("javac" in ERR, "pkg install -y openjdk-17\njavac -version\njavac -cp $AJ -source 8 -target 8 -d out *.java"),
("d8" in ERR, "d8 --classpath $AJ --lib $AJ --output dex/ out/*.class\n# if inner class error: split MainActivity$Bridge to NinoBridge.java"),
("apksigner" in ERR, "apksigner sign --ks ~/myAI/nino2.keystore --ks-pass pass:123456 --out app-signed.apk app.apk\napksigner verify app-signed.apk"),
("zipalign" in ERR, "zipalign -f -v 4 app.apk app-aligned.apk"),
("app not installed" in ERR or "isn't compatible" in ERR, "# AndroidManifest.xml: versionCode=1 versionName=1.0 minSdk=21 targetSdk=33\n# rebuild with target 33 NOT 34"),
("permission denied" in ERR, "chmod +x *.sh\ntermux-setup-storage"),
("fetch" in ERR, "# WebView blocks fetch(file) -> embed: <script>window.NINO_DATA=[...]</script>"),
("e: " in ERR or "error:" in ERR, "# FULL ERROR - paste file name + line:\n# Example: javac -cp $AJ -source 8 -target 8 -d out MainActivity.java\n# Then paste new error back"),
]
for cond,fix in R:
    if cond: out(fix)
print("# NO MATCH - paste FULL error + file name")
print(ERR[:800])
