# Inventario de Assets — Octo RPG

> 👁️ **Para VER todas las imagenes:** abre **[GALLERY.md](GALLERY.md)** — una galeria
> visual con miniaturas de los 1500+ PNG (assets + packs + tus subidas), agrupados
> por categoria, para elegir cuales usar.

### 🆕 Packs que subiste (analizados y añadidos a la galeria)

Estan extraidos en `.inv/uploads/` y ya aparecen en GALLERY.md:

| Pack subido | Contenido | Sirve para |
|---|---|---|
| **GandalfHardcore** (Assets.zip) | Personaje modular + 58 pelos, 39 sombreros, 36 items de mano, ropa (masc/fem), orejas, mascaras, capas, **NPC, Guerrero, Slime (enemigo), Mascota/Pet**, efectos, emojis/iconos | **Equipamiento real** (sombreros/ropa/armas-mano), aldeanos, un **mob slime** y una **mascota** |
| **Drive (link)** | 180 sprite-sheets grandes (~900x576) en 15 partes — set de tiles/decoracion | Terreno/decoracion nueva |
| **paquete1** | **Tiny RPG: Soldado & Orco** (Demo + v1.02 + v1.03b), **Universal Animation Library**, cascada | Personajes/mobs con animaciones, cascada |
| **paquete2** | tileset_dungeon | Mazmorra |
| **Stone UI** | Stone_UI_Sprite_Sheet | UI (ya en uso) |
| **Terrenos** | light_forest_tileset, dark_forest | Tilesets de bosque |

> ⚠️ **Nota sobre los "descargas1/2/3":** los subiste **directamente a GitHub** como
> `Descargas1.zip`, `descargas2.zip`, `descargas3.zip`. Ya los **descargue, extraje y
> añadi a la galeria**. El **link de Drive** tambien se proceso. ✅

### 🆕🆕 Packs de descargas1/2/3 (analizados y añadidos)

| Pack | Contenido | Sirve para |
|---|---|---|
| **Raven Fantasy Icons** + **Shikashi Fantasy Icons** | Cientos de **iconos de items** (espadas, pociones, anillos, comida...) en spritesheets | **Iconos de equipo/inventario** (lo que faltaba) |
| **Lost Lamb** | Cordero/animal animado | **Animal real** para el bosque |
| **Fish Fellas** | Peces | Pesca / fauna acuatica |
| **FREE Samurai 2D** | Personaje samurai animado | Aldeano/heroe alternativo |
| **Enemy Animations Set** | Animaciones de enemigos | Mobs |
| **2D Pixel Dungeon v2.0** + **RF Catacombs** | Tilesets y props de mazmorra | Interiores de cueva/mazmorra |
| **Blue Stone UI** | UI azul de piedra | Interfaz alternativa |
| **Super Pixel Effects Gigapack** + **100 Fx** + **10 Fx** | Cientos de efectos (magia, fuego, golpes...) en **spritesheets** | FX de combate/habilidades |
| **Universal Animation Library 2** | Animaciones universales | Movimiento de personajes |

> Nota: de los packs de **efectos** e **iconos** conserve los **spritesheets combinados**
> (se ven en la galeria) y **descarte los miles de frames sueltos** para no inflar el repo.

---

## 1. RESUMEN RAPIDO (decisiones pendientes)

| Necesidad | ¿Hay sprite? | Recomendacion |
|---|---|---|
| **Jugador** | ✅ `world/adventurer` (4 direcciones, idle/run/attack) | Mantener |
| **Aldeanos / NPCs** | 🟡 hoy se reusa el *adventurer* tintado · 📦 hay NPCs reales en **Pixel Crawler** (Knight, Rogue, Wizzard) y **Tiny Swords** (Pawn, Warrior, Archer, Monk, Lancer) | **Elegir uno** (ver §6) |
| **Animales (lobo, conejo, venado, oso)** | ❌ **No existe ninguno** (hoy son siluetas dibujadas por codigo) | 📦 Solo hay **oveja (Sheep)** y **pato** en Tiny Swords. Para lobo/conejo/venado/oso hay que **conseguir un pack de animales** o seguir con siluetas |
| **Mobs / enemigos** | ✅ `monsters/` (goblin, skeleton, mushroom, flying_eye) · 📦 mas variantes en Pixel Crawler (Orc, Skeleton Mage/Rogue/Warrior) | Mantener + opcional ampliar |
| **Armas (hacha/espada/baculo)** | 🟡 hoy **iconos dibujados por codigo** · 📦 Pixel Crawler trae `Weapons/` (Wood, Bone, Hands) | Opcional reemplazar por sprites |
| **Interfaz / iconos** | ✅ `ui/stone` (paneles, barras, corazon) · 📦 **Tiny Swords UI** (botones, banners, 10 iconos, barras) muy completa | Considerar Tiny Swords UI para botones bonitos |

**Lo mas importante:** para los **animales del bosque NO hay sprites reales** en ningun pack. Hay que decidir: (A) conseguir un pack de fauna, (B) usar la **oveja** de Tiny Swords como base, o (C) seguir con las **siluetas por codigo** actuales.

---

## 2. PERSONAJE JUGABLE

| Carpeta | Estado | Detalle |
|---|---|---|
| `assets/world/adventurer/` | ✅ EN USO | Base del **jugador** y de los **NPCs/aldeanos** (tintados). 12 hojas 768x80 = 8 frames/fila. Animaciones: idle, run, attack1, en 4 direcciones (down/up/left/right). |
| `assets/world/hero/` | 🟡 DISPONIBLE | Heroe alternativo (256x64 idle, 384x64 run/walk; 3 vistas: Down/Side/Up). No usado. Candidato para diferenciar aldeanos del jugador. |

---

## 3. MOBS / ENEMIGOS

| Carpeta | Estado | Frames (hoja) | Notas |
|---|---|---|---|
| `assets/monsters/goblin/` | ✅ EN USO (combate) | Idle/Death/TakeHit 600x150 (4f), Attack/Run 1200x150 (8f) | |
| `assets/monsters/skeleton/` | ✅ EN USO | Idle/Attack/Hit/Death/Run 600–1200x150 | |
| `assets/monsters/mushroom/` | ✅ EN USO | idem | |
| `assets/monsters/flying_eye/` | ✅ EN USO | idem (volador) | |
| `assets/world/orc/` | ✅ EN USO | Idle 128x32 (4f), Run 384x64 | overworld |
| `assets/world/orc_td/` | ✅ EN USO | Idle/Run/Death | overworld (top-down) |
| 📦 Pixel Crawler `Entities/Mobs/` | 📦 EN `.inv` | Orc (base/rogue/shaman/warrior), Skeleton (base/mage/rogue/warrior) — hojas Idle/Run/Death | Ampliacion de variedad de mobs |
| 📦 Monster Creatures 1.3 | 📦 EN `.inv` | Attack3 + proyectiles para goblin/skeleton/mushroom/flying eye | Ataques extra de los mobs actuales |

---

## 4. ANIMALES (fauna del Bosque Oscuro)  ⚠️

| Animal | ¿Sprite real? | Estado actual en el juego |
|---|---|---|
| Lobo | ❌ No hay | Silueta dibujada por codigo |
| Conejo | ❌ No hay | Silueta dibujada por codigo |
| Venado | ❌ No hay | Silueta dibujada por codigo |
| Oso | ❌ No hay | Silueta dibujada por codigo |
| **Oveja** | 📦 SI (Tiny Swords) | `Resources/Sheep/HappySheep_*` (idle/bouncing) y Free Pack `Sheep_Idle/Move/Grass` |
| **Pato** | 📦 SI (Tiny Swords Free) | `Rubber duck.png` (decorativo) |

**Decision necesaria:** ningun pack actual trae lobo/conejo/venado/oso. Opciones:
- **(A)** Conseguir un pack de animales de bosque (pixel art) — yo lo integro.
- **(B)** Usar la **oveja** como animal base y derivar otros por tinte/escala (limitado).
- **(C)** Mantener las **siluetas por codigo** (lo que hay hoy) y mejorarlas.

---

## 5. MUNDO / ESCENARIO

| Asset | Estado | Notas |
|---|---|---|
| `world/village/house1.png` (128x192) | ✅ EN USO | Fachada de **todas las casas** (modelo 3D) |
| `world/village/house2.png` | 🟡 DISPONIBLE | Casa alternativa (ya no se usa tras unificar modelo) |
| `world/village/mayor.png` (320x256) | ✅ EN USO | Fachada del **Gremio** |
| `world/cute/grass.png`, `path.png` | ✅ EN USO | Suelo / textura base |
| `world/cute/tree.png` (64x80) | ✅ EN USO | **Arbol del bosque** (copa unica) |
| `world/cute/tree_small.png` | ✅ EN USO | arbol decorativo |
| `world/cute/cliff.png`, `decor.png`, `fences.png`, `house.png` | 🟡 DISPONIBLE | `fences.png` candidato para vallas reales; `house.png` casa cute alternativa |
| `world/trees/tree_big.png` (448x368), `tree_small.png` | 🟡 PARCIAL | copa de dos tonos; se dejo de usar en el bosque por verse "doble" |
| `world/dungeon/wall.png`, `door_double.png` | ✅ EN USO | bordes y puertas |
| `world/dungeon/` (cave, door, floor, montain, tileset) | 🟡 DISPONIBLE | interiores de cueva/mazmorra |
| `world/tiles/` (Floors, grass_ts, path_ts, Vegetation, Water_tiles) | 🟡 DISPONIBLE | tilesets sin usar |
| `world/waterfall/` (sheet + wf1..8) | 🟡 DISPONIBLE | cascada animada |
| `world/woods/woods.png` | 🟡 DISPONIBLE | bosque tile |
| 📦 Tiny Swords `Terrain/`, `Deco/`, `Resources/Trees` | 📦 EN `.inv` | tilesets, puentes, agua, arboles, rocas, decoraciones (alta calidad) |
| 📦 Pixel Crawler `Environment/` | 📦 EN `.inv` | props animados, estructuras (walls/roofs/floors) |

---

## 5.bis MAZMORRA / CUEVAS (Dungeon)  🆕

Recopilados **todos los packs de Dungeon** que tenemos (📦 **EXCEPTO** `Pixel Crawler
- Free Pack 2.0.4`, que **no se usa**). Mira el apartado **"Mazmorra / Cuevas
(Dungeon)"** en [GALLERY.md](GALLERY.md) para elegir paredes, puertas, suelos, props.

**Set curado listo para usar:** `assets/world/dungeon_src/` (importado en Godot).

| Archivo (en `assets/world/dungeon_src/`) | Origen | Tamaño | Para |
|---|---|---|---|
| `pixeldungeon_tileset.png` | 2D Pixel Dungeon v2.0 | 160x160 (10x10 de 16px) | **Tileset principal**: paredes, suelos, puertas |
| `pixeldungeon_tileset_autotile.png` | 2D Pixel Dungeon | 512x512 | Variante autotile (más combinaciones) |
| `pixeldungeon_demo_referencia.png` | 2D Pixel Dungeon | 256x256 | Referencia de sala montada |
| `catacombs_tileset_principal.png` | RF Catacombs v1.0 | 1024x640 | **Tileset principal** de catacumbas |
| `catacombs_decorativo.png` | RF Catacombs | 256x256 | Decoración de pared/suelo |
| `paquete2_tileset_dungeon.png` | paquete2 | 256x256 | Tileset de mazmorra extra |
| `cueva_fondo_01/02/03.png` | Lost Lamb (Hidden Cave) | 480x256 | Fondos de cueva |
| `pixeldungeon_antorcha*.png`, `_cofre*.png`, `_caja.png`, `_pinchos.png` | 2D Pixel Dungeon | 16–32px | Props: antorcha, cofre, caja, pinchos |
| `catacombs_antorcha.png`, `_vela.png`, `_pinchos.png` | RF Catacombs | — | Props de catacumbas |

> Los **packs completos** (con todas las animaciones de props y los monstruos de
> mazmorra) siguen en `.inv/uploads/` y también aparecen en el apartado Dungeon de
> la galería, por si quieres tirar de algo más.

**EN USO (mazmorra HD):** fondo = `cueva_fondo_02`, suelo = `cueva_fondo_03`, muros =
piedra gris de `catacombs_decorativo` (tile sólido gx1), antorchas animadas =
`catacombs_antorcha_1..4` (cada ~5 pasos, única fuente de luz junto a la antorcha
equipable del jugador), cofres = `pixeldungeon_cofre`/`_abierto`.
>
> **Siguiente paso:** dime qué **pared / puerta / suelo** quieres (por nombre de
> archivo o señalando en la galería) y lo integro en las cuevas/mazmorras.

---

## 6. ALDEANOS / NPCs (candidatos)

| Fuente | Estado | Contenido |
|---|---|---|
| `world/adventurer` tintado | ✅ EN USO | Hoy los NPCs son el jugador con tinte de color |
| 📦 Pixel Crawler `Entities/Npc's/` | 📦 EN `.inv` | **Knight, Rogue, Wizzard** (Idle/Run/Death) — estilo coherente con el jugador |
| 📦 Tiny Swords `Units/` | 📦 EN `.inv` | **Pawn, Warrior, Archer, Monk, Lancer** en 5 colores (Blue/Red/Purple/Yellow/Black) | 
| 📦 Pixel Crawler `Body_A` | 📦 EN `.inv` | Cuerpo base con MUCHAS animaciones (fishing, watering, collect, carry...) ideal para granjero/aldeano |

> Para que los aldeanos no sean "clones" del jugador, lo mejor es **Pixel Crawler NPCs** (mismo estilo) o **Tiny Swords Pawn** (mas caricaturesco).

---

## 7. ARMAS / ITEMS

| Item | Estado | Notas |
|---|---|---|
| Hacha / Espada / Baculo | 🟡 ICONO POR CODIGO | Dibujados en `ItemIcon` (ficha) y textura simple sobre el jugador |
| Agua / Comida / Madera / Carne / Pieles... | 🟡 ICONO POR CODIGO | idem |
| 📦 Pixel Crawler `Weapons/` | 📦 EN `.inv` | `Wood`, `Bone`, `Hands` (sprites de arma reales) |
| 📦 Tiny Swords Pawn variantes | 📦 EN `.inv` | Pawn con Axe/Hammer/Knife/Pickaxe (util para herramientas) |

---

## 8. INTERFAZ (UI)

| Asset | Estado | Notas |
|---|---|---|
| `ui/stone/Stone_UI_Sprite_Sheet.png` | ✅ EN USO | Corazones, barras, paneles de piedra (HUD) |
| `ui/stone/orb.png`, `pieces/x_C_top.png` | ✅ EN USO | Barra de XP y orbe |
| `ui/stone/stone_font.fnt` + page | ✅ EN USO | Fuente del menu principal |
| `ui/stone/pieces/*` (A_panel, B_strip, C_panel, D_piece, rows...) | 🟡 DISPONIBLE | Trozos de panel sin usar |
| 📦 Tiny Swords `UI/` | 📦 EN `.inv` | **Botones** (azul/rojo, 3/9-slices, hover/pressed/disable), **banners**, **ribbons**, **10 iconos**, **punteros**. Muy completo y bonito |

---

## 9. PACKS SIN EXTRAER (`assets/_packs/*.zip` y copia en `.inv/`)

| Pack | Util para |
|---|---|
| `FREE_Adventurer 2D Pixel Art` | ✅ Ya extraido = el jugador actual |
| `Monsters_Creatures_Fantasy` (1.2/1.3) | ✅ Mobs actuales + ataques extra (Attack3, proyectiles) |
| `Pixel Crawler - Free Pack 2.0.4` | **NPCs** (Knight/Rogue/Wizard), **Mobs** (Orc/Skeleton variantes), **Weapons**, props, cuerpo base con muchas animaciones |
| `Tiny Swords` / `Tiny Swords (Free Pack)` | **Unidades** (Pawn/Warrior/Archer/Monk/Lancer ×5 colores), **UI completa**, terreno, **oveja**, arboles, edificios, recursos (oro/madera/carne) |

> Nota: las carpetas `__MACOSX/` dentro de los zips son basura del SO y se ignoran.

---

## 10. LIMPIEZA SUGERIDA

- `assets/_packs/*.zip` (~varios MB) → ya estan extraidos en `.inv/`; se pueden **borrar del repo** para aligerar (o mover fuera).
- `.inv/**/__MACOSX/` → basura, **borrar**.
- `world/village/house2.png`, `world/trees/tree_big.png` → en desuso; mantener solo si se quieren como alternativa.
- `world/hero/`, `world/tiles/`, `world/woods/`, `world/waterfall/` → disponibles sin usar; decidir si entran al juego o se quitan.

---

## ✅ Lo que necesito que decidas

1. **Animales** (lobo/conejo/venado/oso): ¿(A) busco/integro un pack de fauna, (B) uso la oveja de Tiny Swords, o (C) sigo con siluetas por codigo?
2. **Aldeanos/NPCs**: ¿Pixel Crawler (Knight/Rogue/Wizard) o Tiny Swords (Pawn/Warrior/...)?
3. **Armas**: ¿iconos por codigo (actual) o sprites de Pixel Crawler `Weapons/`?
4. **UI/botones**: ¿mantengo el estilo "stone" actual o migro botones a **Tiny Swords UI**?
5. **Limpieza**: ¿borro los `.zip` de `_packs/` y los `__MACOSX/` para aligerar el repo?
