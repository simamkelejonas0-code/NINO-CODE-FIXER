import sys, re
path=sys.argv[1] if len(sys.argv)>1 else ""
code=open(path).read() if path else sys.stdin.read()
is_xml=path.endswith(".xml") or "<manifest" in code or "<" in code[:200] and ">" in code[:200] and "package" not in code[:200]
if not is_xml:
    if "webview" in code.lower() and "import android.webkit.WebView" not in code:
        code=re.sub(r"(package [^;]+;\n)", r"\1import android.webkit.WebView;\n", code, count=1)
    if "javascriptinterface" in code.lower() and "import android.webkit.JavascriptInterface" not in code:
        code=re.sub(r"(package [^;]+;\n)", r"\1import android.webkit.JavascriptInterface;\n", code, count=1)
    lines=code.split("\n")
    for i,l in enumerate(lines):
        s=l.strip()
        if s and not s.endswith(("{","}",";",":","//","/*","*","@")) and ("=" in s or "return" in s or "System.out" in s) and not s.startswith(("package","import","public","private","protected","if","for","while","class")):
            lines[i]=l+";  // FIXED: added ;"
    code="\n".join(lines)
if "class MainActivity" in code and "class Bridge" in code:
    print("# FIXED: Split inner class - COPY BOTH FILES")
    # remove only Bridge class block, keep outer closing brace
    m=re.sub(r"\s*class Bridge\s*\{[^{]*\{[^}]*\}[^}]*\}", "\n", code, count=1)
    if m.count("{")>m.count("}"):
        m=m+"}\n"
    print("# === FILE 1: MainActivity.java ===")
    print(m)
    print("\n# === FILE 2: NinoBridge.java ===")
    print("package com.nino.codefixer;\nimport android.webkit.JavascriptInterface;\npublic class NinoBridge {\n @JavascriptInterface public String fix(String e){ return e; }\n}")
    sys.exit(0)
if "fetch(" in code and "nino" in code.lower():
    code=code.replace("fetch('nino_study.json')", "Promise.resolve(window.NINO_DATA)")
if "<manifest" in code and "versionCode" not in code:
    code=code.replace("<manifest ", '<manifest android:versionCode="1" android:versionName="1.0" ',1)
print("# === FIXED WHOLE FILE - COPY ALL ===")
print(code)
