import asyncio
import random
import time
from .species_info import SPECIES_DATA, get_species_info

SUPPORTED_SPECIES = list(SPECIES_DATA.keys())

async def predict(image_bytes: bytes) -> dict:
    """
    Mock prediction function simulating an image classification model.
    """
    start_time = time.time()
    
    # Simulate processing time
    await asyncio.sleep(random.uniform(0.5, 1.5))
    
    # Pick a random primary species
    primary_species = random.choice(SUPPORTED_SPECIES)
    primary_confidence = random.uniform(0.75, 0.98)
    
    # Pick top 3 predictions
    other_species = [s for s in SUPPORTED_SPECIES if s != primary_species]
    secondary_species = random.sample(other_species, 2)
    
    # Ensure probabilities sum nicely
    remaining_conf = 1.0 - primary_confidence
    conf2 = random.uniform(0.01, remaining_conf * 0.8)
    conf3 = remaining_conf - conf2
    
    top_3 = [
        {"species": primary_species, "confidence": round(primary_confidence, 4)},
        {"species": secondary_species[0], "confidence": round(conf2, 4)},
        {"species": secondary_species[1], "confidence": round(conf3, 4)}
    ]
    
    # Sort top 3 by confidence descending
    top_3.sort(key=lambda x: x["confidence"], reverse=True)
    
    analysis_time_ms = int((time.time() - start_time) * 1000)
    species_info = get_species_info(primary_species)
    
    return {
        "species": primary_species,
        "confidence": round(primary_confidence, 4),
        "top_3": top_3,
        "analysis_time_ms": analysis_time_ms,
        "species_info": species_info
    }
