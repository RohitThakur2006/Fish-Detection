SPECIES_DATA = {
    "Clownfish": {
        "common_name": "Ocellaris Clownfish",
        "scientific_name": "Amphiprion ocellaris",
        "family": "Pomacentridae",
        "habitat": "Coral reefs, anemones",
        "depth_range": "1 - 15 m",
        "diet": "Omnivore (plankton, algae)",
        "average_size": "8 - 11 cm",
        "conservation_status": "Least Concern (LC)",
        "fun_fact": "All clownfish are born male. The largest in a group becomes female.",
        "sonar_signature": "Small biological // 8-10cm"
    },
    "Blue Tang": {
        "common_name": "Regal Blue Tang",
        "scientific_name": "Paracanthurus hepatus",
        "family": "Acanthuridae",
        "habitat": "Coral reefs",
        "depth_range": "2 - 40 m",
        "diet": "Herbivore (plankton, algae)",
        "average_size": "25 - 30 cm",
        "conservation_status": "Least Concern (LC)",
        "fun_fact": "They have sharp, venomous spines at the base of their tail.",
        "sonar_signature": "Medium biological // 20-30cm"
    },
    "Lionfish": {
        "common_name": "Red Lionfish",
        "scientific_name": "Pterois volitans",
        "family": "Scorpaenidae",
        "habitat": "Coral reefs, rocky crevices",
        "depth_range": "2 - 50 m",
        "diet": "Carnivore (small fish, invertebrates)",
        "average_size": "30 - 38 cm",
        "conservation_status": "Least Concern (LC)",
        "fun_fact": "It is a highly invasive species in the Atlantic Ocean.",
        "sonar_signature": "Medium biological // 30-40cm // Anomalous spine returns"
    },
    "Angelfish": {
        "common_name": "Emperor Angelfish",
        "scientific_name": "Pomacanthus imperator",
        "family": "Pomacanthidae",
        "habitat": "Coral reefs",
        "depth_range": "1 - 100 m",
        "diet": "Omnivore (sponges, tunicates)",
        "average_size": "30 - 40 cm",
        "conservation_status": "Least Concern (LC)",
        "fun_fact": "Juveniles have completely different coloration from adults.",
        "sonar_signature": "Medium biological // 30-40cm"
    },
    "Pufferfish": {
        "common_name": "White-spotted Puffer",
        "scientific_name": "Arothron hispidus",
        "family": "Tetraodontidae",
        "habitat": "Coral reefs, seagrass beds",
        "depth_range": "3 - 50 m",
        "diet": "Carnivore (crustaceans, mollusks)",
        "average_size": "35 - 50 cm",
        "conservation_status": "Least Concern (LC)",
        "fun_fact": "They contain tetrodotoxin, making them highly poisonous to eat.",
        "sonar_signature": "Variable biological // Expands on threat"
    },
    "Swordfish": {
        "common_name": "Swordfish",
        "scientific_name": "Xiphias gladius",
        "family": "Xiphiidae",
        "habitat": "Open ocean",
        "depth_range": "0 - 800 m",
        "diet": "Carnivore (fish, squid)",
        "average_size": "3 - 4.5 m",
        "conservation_status": "Near Threatened (NT)",
        "fun_fact": "They can swim at speeds up to 97 km/h (60 mph).",
        "sonar_signature": "Large biological // High-speed vector // 3-4m"
    },
    "Seahorse": {
        "common_name": "Lined Seahorse",
        "scientific_name": "Hippocampus erectus",
        "family": "Syngnathidae",
        "habitat": "Seagrass beds, mangroves",
        "depth_range": "0 - 70 m",
        "diet": "Carnivore (small crustaceans)",
        "average_size": "10 - 15 cm",
        "conservation_status": "Vulnerable (VU)",
        "fun_fact": "Male seahorses carry the eggs in a brood pouch until they hatch.",
        "sonar_signature": "Micro biological // Stationary // 10-15cm"
    },
    "Manta Ray": {
        "common_name": "Giant Oceanic Manta Ray",
        "scientific_name": "Mobula birostris",
        "family": "Mobulidae",
        "habitat": "Open ocean, reefs",
        "depth_range": "0 - 120 m",
        "diet": "Filter feeder (plankton)",
        "average_size": "4 - 7 m (wingspan)",
        "conservation_status": "Endangered (EN)",
        "fun_fact": "They have the largest brain-to-body mass ratio of all fish.",
        "sonar_signature": "Massive biological // Broad wingspan // 5-7m"
    },
    "Barracuda": {
        "common_name": "Great Barracuda",
        "scientific_name": "Sphyraena barracuda",
        "family": "Sphyraenidae",
        "habitat": "Reefs, mangroves, open ocean",
        "depth_range": "0 - 100 m",
        "diet": "Carnivore (fish)",
        "average_size": "1 - 1.5 m",
        "conservation_status": "Least Concern (LC)",
        "fun_fact": "They are known for their lightning-fast ambush attacks.",
        "sonar_signature": "Medium-large biological // Slender // 1-2m"
    },
    "Clown Triggerfish": {
        "common_name": "Clown Triggerfish",
        "scientific_name": "Balistoides conspicillum",
        "family": "Balistidae",
        "habitat": "Coral reefs",
        "depth_range": "1 - 50 m",
        "diet": "Carnivore (crustaceans, mollusks)",
        "average_size": "25 - 50 cm",
        "conservation_status": "Least Concern (LC)",
        "fun_fact": "They have very strong jaws for crushing hard-shelled prey.",
        "sonar_signature": "Medium biological // Dense core // 30-50cm"
    }
}

def get_species_info(species_name: str) -> dict | None:
    """Returns species information by name."""
    return SPECIES_DATA.get(species_name)
