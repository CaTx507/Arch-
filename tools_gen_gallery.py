#!/usr/bin/env python3
"""Genera GALLERY.md: una galeria visual (Markdown, se ve en GitHub) con TODOS
los PNG de assets/ y de los packs en .inv/, agrupados por categoria, con su
tamaño. Asi se pueden ver y elegir para el juego."""
import os, struct, urllib.parse, glob

ROOT = os.path.dirname(os.path.abspath(__file__))

def png_size(p):
    try:
        with open(p, 'rb') as f:
            f.read(16)
            w, h = struct.unpack('>II', f.read(8))
            return w, h
    except Exception:
        return None

def collect():
    pngs = []
    for base in ("assets", ".inv"):
        for p in glob.glob(os.path.join(ROOT, base, "**", "*.png"), recursive=True):
            rel = os.path.relpath(p, ROOT)
            if "__MACOSX" in rel:
                continue
            pngs.append(rel.replace("\\", "/"))
    return sorted(pngs)

def category(rel):
    r = rel.lower()
    # --- MAZMORRA / CUEVAS: todo lo de Dungeon en UN apartado (menos Pixel Crawler) ---
    # Reune los tilesets/props de: 2D Pixel Dungeon, RF Catacombs, paquete2
    # (tileset_dungeon), los fondos de cueva (Hidden Cave), la carpeta curada
    # assets/world/dungeon_src y el assets/world/dungeon ya existente.
    if "pixel_crawler" not in r and (
            "pixel_dungeon" in r or "catacombs" in r or "tileset_dungeon" in r
            or "dungeon_src" in r or "/dungeon/" in r
            or "hidden cave" in r or "hiddencave" in r or "cueva_fondo" in r):
        return "Mazmorra / Cuevas (Dungeon)"
    # --- Packs subidos por el usuario (.inv/uploads) ---
    if "gandalfhardcore" in r:
        if "slime" in r:
            return "Mobs / Enemigos"
        if "pet" in r or "companion" in r:
            return "Animales / Mascotas"
        if "effect" in r or "emoji" in r or "/icon" in r or "icons" in r:
            return "Efectos / Iconos (GandalfHardcore)"
        if "character_asset" in r or "special_skin" in r or "free_warrior" in r or "free_npc" in r or "hostage" in r:
            return "Personaje modular / NPC (GandalfHardcore)"
        return "Equipo / Ropa / Accesorios (GandalfHardcore)"
    if "tiny_rpg_character" in r or "soldier" in r:
        return "Personajes (Tiny RPG: Soldado/Orco)"
    if "universal_animation" in r:
        return "Libreria de animaciones (Universal)"
    # Packs subidos via descargasN.zip
    if "raven_fantasy_icons" in r or "shikashi" in r:
        return "Iconos de items (Raven / Shikashi)"
    if "super_pixel_effects" in r or "fx_effects" in r:
        return "Efectos FX (spritesheets)"
    if "lost_lamb" in r:
        return "Animales / Mascotas"
    if "fish_fellas" in r:
        return "Animales / Mascotas"
    if "free_samurai" in r or "sample_idle_walk" in r:
        return "Personajes (Samurai / extra)"
    if "enemy_animations_set" in r:
        return "Mobs / Enemigos"
    if "pixel_dungeon" in r or "catacombs" in r:
        return "Mazmorra / Props / Estructuras"
    if "blue_stone_ui" in r:
        return "Interfaz (UI / iconos / botones)"
    if "drive_pack" in r:
        return "Pack subido (Drive) — tiles/decoracion"
    if "/uploads/terrenos" in r or "forest_tileset" in r or "dark_forest" in r:
        return "Terreno / Tilesets / Decoracion"
    # Animales
    if "sheep" in r or "rubber duck" in r:
        return "Animales / Mascotas"
    # NPCs / unidades / personajes
    if "/npc" in r or "/units/" in r:
        return "Aldeanos / NPCs / Unidades"
    if "entities/characters" in r or "/adventurer/" in r or "/hero/" in r:
        return "Personaje jugable"
    # Mobs
    if "/mobs/" in r or "/monsters/" in r or "/orc" in r or "monster_creatures" in r:
        return "Mobs / Enemigos"
    # Armas
    if "/weapons/" in r or "swords" in r or ("/pawn/" in r and ("axe" in r or "hammer" in r or "knife" in r or "pickaxe" in r)):
        return "Armas / Herramientas"
    # UI
    if "/ui" in r or "avatars" in r or "icon" in r or "button" in r or "banner" in r or "ribbon" in r or "/stone/" in r or "papers" in r or "cursor" in r:
        return "Interfaz (UI / iconos / botones)"
    # Edificios
    if "building" in r or "house" in r or "castle" in r or "tower" in r or "archery" in r or "barrack" in r or "monastery" in r or "/village/" in r:
        return "Edificios"
    # Terreno / tiles / deco
    if "terrain" in r or "/tiles/" in r or "tilemap" in r or "/deco" in r or "decorations" in r or "/cute/" in r or "/woods/" in r or "water" in r or "rock" in r or "bush" in r or "cloud" in r:
        return "Terreno / Tilesets / Decoracion"
    # Arboles / recursos
    if "/trees/" in r or "tree" in r or "resource" in r or "gold" in r or "wood" in r or "meat" in r or "stump" in r:
        return "Arboles / Recursos"
    # Cascada / fx
    if "waterfall" in r or "/effects/" in r or "particle" in r or "fire" in r or "explosion" in r or "dust" in r:
        return "Efectos / Cascada"
    # Dungeon
    if "/dungeon/" in r or "structures" in r or "environment/props" in r:
        return "Mazmorra / Props / Estructuras"
    return "Otros"

ORDER = [
    "Personaje jugable",
    "Mazmorra / Cuevas (Dungeon)",
    "Personaje modular / NPC (GandalfHardcore)",
    "Personajes (Tiny RPG: Soldado/Orco)",
    "Aldeanos / NPCs / Unidades",
    "Personajes (Samurai / extra)",
    "Animales / Mascotas",
    "Mobs / Enemigos",
    "Equipo / Ropa / Accesorios (GandalfHardcore)",
    "Armas / Herramientas",
    "Iconos de items (Raven / Shikashi)",
    "Interfaz (UI / iconos / botones)",
    "Efectos / Iconos (GandalfHardcore)",
    "Efectos FX (spritesheets)",
    "Edificios",
    "Arboles / Recursos",
    "Terreno / Tilesets / Decoracion",
    "Pack subido (Drive) — tiles/decoracion",
    "Libreria de animaciones (Universal)",
    "Efectos / Cascada",
    "Mazmorra / Props / Estructuras",
    "Otros",
]

def pack_of(rel):
    if rel.startswith("assets/"):
        return "assets/ (ya en el juego)"
    parts = rel.split("/")
    if len(parts) >= 2 and parts[0] == ".inv":
        return ".inv/" + parts[1]
    return rel

def main():
    pngs = collect()
    cats = {}
    for rel in pngs:
        cats.setdefault(category(rel), []).append(rel)

    lines = []
    lines.append("# Galeria Visual de Assets\n")
    lines.append("Todas las imagenes PNG del proyecto (assets en uso + packs en `.inv/`), ")
    lines.append("agrupadas por categoria para **verlas y elegirlas**. Cada miniatura ")
    lines.append("muestra el nombre y el tamaño (ancho x alto). Las hojas (sheets) salen ")
    lines.append("como tira de frames.\n")
    lines.append("> Para elegir, dime la **categoria + nombre** (o pega el nombre del PNG) ")
    lines.append("y lo integro en el juego.\n")
    total = len(pngs)
    lines.append(f"**Total: {total} imagenes.**\n")
    # Indice
    lines.append("## Indice\n")
    for c in ORDER:
        if c in cats:
            lines.append(f"- [{c}](#{slug(c)}) ({len(cats[c])})")
    lines.append("")

    for c in ORDER:
        if c not in cats:
            continue
        items = sorted(cats[c])
        lines.append(f"\n## {c}\n")
        # Agrupar por pack para orientacion
        bypack = {}
        for rel in items:
            bypack.setdefault(pack_of(rel), []).append(rel)
        for pack in sorted(bypack.keys()):
            lines.append(f"\n### {pack}\n")
            lines.append("| | | | |")
            lines.append("|---|---|---|---|")
            row = []
            for rel in bypack[pack]:
                s = png_size(os.path.join(ROOT, rel))
                dim = f"{s[0]}x{s[1]}" if s else "?"
                name = os.path.basename(rel)
                url = urllib.parse.quote(rel)
                cell = f"<img src='{url}' height='64'><br><sub>{name}<br>{dim}</sub>"
                row.append(cell)
                if len(row) == 4:
                    lines.append("| " + " | ".join(row) + " |")
                    row = []
            if row:
                while len(row) < 4:
                    row.append("")
                lines.append("| " + " | ".join(row) + " |")
    with open(os.path.join(ROOT, "GALLERY.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("OK", total, "imagenes")

def slug(s):
    out = ""
    for ch in s.lower():
        if ch.isalnum():
            out += ch
        elif ch in " -/":
            out += "-"
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")

if __name__ == "__main__":
    main()
