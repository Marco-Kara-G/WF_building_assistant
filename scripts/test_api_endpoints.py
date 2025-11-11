"""
Script per testare gli endpoint dell'API Warframe
"""

import requests
import json
from typing import List, Dict, Optional


API_BASE_URL = "https://api.warframestat.us/"


def fetch_all_items() -> List[Dict]:
    """Recupera tutti gli item dall'API"""
    url = f"{API_BASE_URL}items/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_all_weapons() -> List[Dict]:
    """Recupera tutte le armi dall'API"""
    url = f"{API_BASE_URL}weapons/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_all_mods() -> List[Dict]:
    """Recupera tutte le mod dall'API"""
    url = f"{API_BASE_URL}mods/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def filter_by_category(items: List[Dict], category: str) -> List[Dict]:
    """Filtra item per categoria"""
    return [item for item in items if item.get('category') == category]


def search_item(query: str) -> List[Dict]:
    """Cerca item per nome"""
    url = f"{API_BASE_URL}items/search/{query}/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_item_by_name(name: str) -> Optional[Dict]:
    """Recupera un item specifico per nome esatto"""
    url = f"{API_BASE_URL}items/{name}/"
    response = requests.get(url)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


def print_warframe_stats(warframe: Dict):
    """Stampa le statistiche di un Warframe"""
    print(f"\n{'='*60}")
    print(f"Warframe: {warframe['name']}")
    print(f"{'='*60}")
    print(f"Health: {warframe.get('health', 'N/A')}")
    print(f"Shield: {warframe.get('shield', 'N/A')}")
    print(f"Armor: {warframe.get('armor', 'N/A')}")
    print(f"Energy: {warframe.get('power', 'N/A')}")
    print(f"Sprint: {warframe.get('sprint', 'N/A')}")
    print(f"Aura: {warframe.get('aura', 'N/A')}")
    print(f"Prime: {warframe.get('isPrime', False)}")
    print(f"Mastery Rank: {warframe.get('masteryReq', 0)}")
    
    if 'abilities' in warframe:
        print(f"\nAbilities ({len(warframe['abilities'])}):")
        for i, ability in enumerate(warframe['abilities'], 1):
            print(f"  {i}. {ability['name']}")


def print_weapon_stats(weapon: Dict):
    """Stampa le statistiche di un'arma"""
    print(f"\n{'='*60}")
    print(f"Weapon: {weapon['name']} ({weapon.get('category', 'N/A')})")
    print(f"{'='*60}")
    print(f"Damage: {weapon.get('totalDamage', weapon.get('damage', 'N/A'))}")
    print(f"Critical Chance: {weapon.get('criticalChance', 'N/A')}")
    print(f"Critical Multiplier: {weapon.get('criticalMultiplier', 'N/A')}")
    print(f"Status Chance: {weapon.get('procChance', 'N/A')}")
    print(f"Fire Rate: {weapon.get('fireRate', 'N/A')}")
    print(f"Magazine: {weapon.get('magazineSize', 'N/A')}")
    print(f"Reload: {weapon.get('reloadTime', 'N/A')}")
    print(f"Mastery Rank: {weapon.get('masteryReq', 0)}")
    print(f"Disposition: {weapon.get('disposition', 'N/A')}")


def print_mod_stats(mod: Dict):
    """Stampa le statistiche di una Mod"""
    print(f"\n{'='*60}")
    print(f"Mod: {mod['name']}")
    print(f"{'='*60}")
    print(f"Drain: {mod.get('baseDrain', 'N/A')}")
    print(f"Max Rank: {mod.get('fusionLimit', 'N/A')}")
    print(f"Rarity: {mod.get('rarity', 'N/A')}")
    print(f"Polarity: {mod.get('polarity', 'N/A')}")
    print(f"Compatible: {mod.get('compatName', 'N/A')}")
    print(f"Augment: {mod.get('isAugment', False)}")
    print(f"Exilus: {mod.get('isExilus', False)}")
    
    if 'stats' in mod:
        print(f"\nEffects:")
        for stat in mod['stats']:
            print(f"  - {stat}")


def main():
    """Test degli endpoint principali"""
    
    print("🔍 Testing Warframe API Endpoints")
    print("="*60)
    
    # Test 1: Recupera tutti gli item
    print("\n1. Fetching all items...")
    all_items = fetch_all_items()
    print(f"   ✓ Total items: {len(all_items)}")
    
    # Test 2: Recupera tutte le armi
    print("\n2. Fetching all weapons...")
    all_weapons = fetch_all_weapons()
    print(f"   ✓ Total weapons: {len(all_weapons)}")
    
    # Test 3: Recupera tutte le mod
    print("\n3. Fetching all mods...")
    all_mods = fetch_all_mods()
    print(f"   ✓ Total mods: {len(all_mods)}")
    
    # Test 4: Conta per categoria
    print("\n4. Items by category:")
    categories = {}
    for item in all_items:
        cat = item.get('category', 'Unknown')
        categories[cat] = categories.get(cat, 0) + 1
    
    for cat in sorted(categories.keys()):
        if cat in ['Warframes', 'Mods', 'Pets', 'Sentinels']:
            print(f"   - {cat}: {categories[cat]}")
    
    print("\n   Weapons by category:")
    weapon_categories = {}
    for weapon in all_weapons:
        cat = weapon.get('category', 'Unknown')
        weapon_categories[cat] = weapon_categories.get(cat, 0) + 1
    
    for cat in sorted(weapon_categories.keys()):
        print(f"   - {cat}: {weapon_categories[cat]}")
    
    # Test 5: Warframe specifico
    print("\n5. Testing specific Warframe (Excalibur)...")
    excalibur = get_item_by_name("Excalibur")
    if excalibur:
        print_warframe_stats(excalibur)
    
    # Test 6: Arma specifica
    print("\n6. Testing specific weapon (Boltor)...")
    boltor = get_item_by_name("Boltor")
    if boltor:
        print_weapon_stats(boltor)
    
    # Test 7: Mod specifica
    print("\n7. Testing specific mod (Serration)...")
    serration = get_item_by_name("Serration")
    if serration:
        print_mod_stats(serration)
    
    # Test 8: Ricerca
    print("\n8. Testing search (Excalibur)...")
    results = search_item("Excalibur")
    print(f"   ✓ Found {len(results)} results")
    warframe_results = [r for r in results if r.get('category') == 'Warframes']
    print(f"   ✓ Warframes found: {len(warframe_results)}")
    for wf in warframe_results[:3]:
        print(f"     - {wf['name']}")
    
    print("\n" + "="*60)
    print("✓ All tests completed!")


if __name__ == "__main__":
    main()
