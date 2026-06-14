# Octo RPG 🗡️🟥

**aRPG 2D** con estética **HD-2D** (inspirado en *Octopath Traveler*) y combate
por turnos **dinámico** al estilo de *Darkest Dungeon*.
Hecho en **Godot 4.6**.

> Arte 100% original generado por código (sin assets de terceros), inspirado
> en el estilo visual de los JRPG modernos para evitar problemas de copyright.

---

## 🎮 Qué incluye esta versión

- **Mundo explorable (top-down)**: caminas por un bosque con hierba alta donde
  pueden aparecer combates *(esta mecánica la puliremos a fondo después)*.
- **Combate estilo Darkest Dungeon — NADA estático**:
  - Los personajes **respiran, se balancean y oscilan** de forma continua.
  - **Entrada dramática**: las unidades se deslizan a escena al empezar.
  - Cada acción tiene **anticipación → embestida → impacto → recuperación**.
  - Reacción de dolor con destello, retroceso elástico y temblor.
  - Sprites más grandes y detallados estilo Octopath (luz de borde, sombreado).
- **3 comandos por turno** (iconos pequeños e interactuables):
  - ⚔️ **Atacar** → submenú con 3 intensidades:
    - **Ligero** (x1.0), **Fuerte** (x1.5), **Pesado** (x2.0).
  - ✦ **Magia** → submenú con 3 escuelas:
    - **Ataque**: **Kamehameha** — carga de energía y haz azul devastador (8 MP).
    - **Sanar**: recupera el **30% del HP máximo** (6 MP).
    - **Protección**: aura giratoria que reduce el daño recibido (5 MP).
  - 🛡️ **Defensa** — reduce daño y recupera algo de MP.
- **Estética HD-2D**: bosque con profundidad, rayos de sol, niebla, polvo
  flotante, sombras, viñeta, sacudida de cámara y números de daño con rebote.

---

## ▶️ Cómo abrir y jugar (en tu PC)

1. Descarga **Godot 4.6** (o superior) — versión estándar, NO la de C#/.NET:
   https://godotengine.org/download
   - Es un único ejecutable, no necesita instalación.
2. Abre Godot → **Importar** → selecciona el archivo `project.godot` de este
   proyecto → **Importar y editar**.
3. Pulsa el botón **▶ (Play)** arriba a la derecha (o tecla **F5**).

### Controles
- **Moverse** (mundo): flechas o **WASD**.
- **Combate**: toca/clic en los botones **Atacar / Magia / Defensa**.
- **Avanzar avisos / reintentar**: toca la pantalla o **Espacio/Enter**.

---

## 📱 Cómo exportar a Android (APK para tu celular / Play Store)

1. En Godot: menú **Editor → Administrar plantillas de exportación** →
   **Descargar e instalar**.
2. Instala **Android Studio** una vez (para el SDK + JDK). En Godot:
   **Editor → Configuración del editor → Export → Android** y apunta las rutas
   del SDK y del `adb`/`keytool`.
3. Menú **Proyecto → Exportar → Añadir… → Android**.
4. Para pruebas, **Exportar proyecto** genera un `.apk` que puedes copiar al
   celular. Para Play Store, exporta un **.aab** firmado con tu clave.

> La orientación ya está fijada en **horizontal (landscape)** y el render usa
> **GL Compatibility**, ideal para móviles.

---

## 🗂️ Estructura del proyecto

```
project.godot          Configuración del proyecto (autoloads, input, display)
icon.svg               Ícono del juego
scenes/
  Overworld.tscn       Escena del mundo explorable
  Battle.tscn          Escena del combate
scripts/
  PixelArt.gd          (Autoload) genera TODO el arte pixelado por código
  GameState.gd         (Autoload) estado del héroe entre mundo y combate
  Overworld.gd         Lógica del mundo: mapa, movimiento, encuentros
  Battle.gd            Lógica del combate por turnos + efectos HD-2D
```

---

## 🛠️ Próximos pasos (ideas para seguir creciendo)

- Pulir a fondo el mundo explorable (mapas, pueblos, NPCs, transiciones).
- Más personajes jugables y enemigos con sprites detallados y animados.
- Sistema de niveles/experiencia, objetos y más habilidades.
- Música y efectos de sonido.
- Joystick/botones en pantalla más vistosos para móvil.

---

## 🎨 Créditos de arte

- Arte original generado por código: estilo HD-2D / Darkest Dungeon.
- Pack de pixel art **"Pixel Crawler"** por **Anokolisa** (itch.io) —
  usado según su licencia. ¡Gracias!
  https://anokolisa.itch.io/free-pixel-art-asset-pack-topdown-tileset-rpg-16x16-sprites

---

Hecho con cariño para empezar tu juego. ¡A seguir construyéndolo! 🎮
