# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47' 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24' 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "-16° 42' 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "-08° 12' 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15' 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def name_star(targets):
    for keys in targets.keys():
        print(f"{keys}")

name_star(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def spectral_type(targets):
    for name, info in targets.items():
        print(f"{name} — {info['Spectral Type']}")
        
spectral_type(targets)
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def dimmer_than_point1(targets):
    result = []
    for name, info in targets.items():
        if info["Magnitude"] > 0.1:
            result.append(name)
    return result

print(dimmer_than_point1(targets))

# 4) Look up another target, add all the necessary information to the targets list. 

def add_target(targets):
    targets["Altair"] = {
        "RA": "19h 50m 46.0s",
        "Dec": "+08° 52' 05″",
        "Magnitude": 0.77,
        "Spectral Type": "A7V"
    }
    return targets

print(add_target(targets))
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def deg(dec_str):  # i created this function to make sure all the negative and positive degrees are converted to float degrees and also removing the other
    s = dec_str.strip().replace('-', '-')   # normalize minus, since some minus signs are different
    sign = -1 if s[0] == '-' else 1
    if s[0] in '+-':
        s = s[1:]
    d = float(s.split('°')[0])   # just the degree part, not the other sections
    return sign * d

def brightest_closest_to_20deg(targets):
    best = None  # (distance_to_20, magnitude, name)
    for name, info in targets.items():
        diff = abs(deg(info["Dec"]) - 20.0)
        mag  = info["Magnitude"]
        if best is None or diff < best[0] or (diff == best[0] and mag < best[1]):
            best = (diff, mag, name)
    return best[2]

print(brightest_closest_to_20deg(targets))

# 6) What is your favorite constellation?

print("Vega!!!!")