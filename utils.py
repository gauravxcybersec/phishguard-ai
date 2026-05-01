import re

def extract_features(url):
    features = []
    url = url.lower()

    features.append(len(url))                    # length
    features.append(url.count("."))              # dots
    features.append(1 if "@" in url else 0)      # @
    features.append(1 if url.startswith("https") else 0)

    keywords = ["login", "secure", "bank", "verify", "update"]
    features.append(sum(word in url for word in keywords))

    features.append(1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0)  # IP
    features.append(1 if "-" in url else 0)                              # hyphen
    features.append(url.count("/"))                                      # slash

    domain = url.split("//")[-1].split("/")[0]
    features.append(len(domain))                                         # domain len

    return features


# 🔥 RULE BASED DETECTION (REAL POWER 😈)
def rule_based_check(url):
    url = url.lower()

    suspicious = ["login", "secure", "bank", "verify", "update"]

    if any(word in url for word in suspicious):
        return 1

    if url.startswith("http://"):   # no HTTPS
        return 1

    if "@" in url:
        return 1

    return 0