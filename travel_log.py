#!/usr/bin/env python3

travel_log = {
    "France": {"Paris": 4,
                "Lille": 1,
                "Dijon": 3
    },
    "Germany": {
        "Berlin": 2,
        "Hamburg": 1,
        "Stuttgard": 1
    }
}

travel_log = [
    {"country": "France", "cities": ["Paris", "Lille", "Dijon"], "visits": 12},
    {"country": "Germany", "cities": ["Berlin", "Hamburg", "Stuttgard"], "visits": 7}
]

def add_new_country(country, visits, list_of_visits):
    travel_log.append({"country": country, "cities": list_of_visits[:], "visits": visits} )

add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")