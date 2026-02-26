
# Conway's Game of Life

A beautiful, interactive desktop application implementing Conway's Game of Life using Python and Pygame.

## Overview

Conway's Game of Life is a cellular automaton devised by mathematician John Horton Conway. This implementation provides a modern, interactive simulation where users can create patterns, watch them evolve, and explore the fascinating behavior of simple rules generating complex dynamics.

## Features

✨ **Core Features:**
- **Grid-based Cellular Automaton**: 100×60 grid with scalable cell sizes
- **Conway's 4 Rules Implementation**:
  1. Any live cell with 2-3 neighbors survives
  2. Any dead cell with exactly 3 neighbors becomes alive
  3. All other cells die or stay dead
- **Interactive Controls**:
  - **SPACE**: Play/Pause simulation
  - **R**: Randomize grid with random pattern
  - **C**: Clear grid (reset to all dead cells)
  - **UP/DOWN**: Adjust simulation speed (1-10x)
  - **Mouse Click**: Draw/erase cells (only while paused)
  - **Q**: Quit application

🎨 **UI Features:**
- Real-time generation counter
- Live cell population display
- FPS and speed indicator
- Status indicator (PLAYING/PAUSED)
- Visual grid with clear cell boundaries

⚡ **Performance:**
- 60 FPS gameplay
- Efficient neighbor counting algorithm

## Project Structure

```
gol/
├── main.py                 # Entry point for the application
├── src/
│   ├── cell.py            # Cell class with Game of Life rules
│   ├── grid.py            # Grid management and simulation logic
│   ├── game.py            # Main game loop and event handling
│   └── renderer.py        # Pygame rendering and UI drawing
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone or navigate to the project directory:**
```bash
cd gol
```

2. **Create a virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python main.py
```

The application window will open with an empty 100×60 grid.

### Basic Workflow

1. **Create a Pattern** (while paused):
   - Click on cells to toggle them between alive (green) and dead (gray)
   - Or press 'R' to randomize the grid

2. **Run the Simulation**:
   - Press SPACE to start the simulation
   - Watch the pattern evolve according to Conway's rules

3. **Adjust Speed**:
   - Press UP arrow to increase simulation speed (faster evolution)
   - Press DOWN arrow to decrease simulation speed (slower evolution)

4. **Reset**:
   - Press 'C' to clear the grid and reset generation counter
   - Press 'R' to fill grid with random pattern

### Classic Patterns

Try creating these famous patterns:

**Blinker** (Period-2 Oscillator):
```
. X .
. X .
. X .
```

**Block** (Still Life):
```
X X
X X
```

**Glider** (Spaceship):
```
. X .
. . X
X X X
```

**Beacon** (Period-2 Oscillator):
```
X X . .
X X . .
. . X X
. . X X
```

## Code Architecture

### `src/cell.py` - Cell Class
Represents individual cells in the grid with:
- Position (x, y) coordinates
- Current alive/dead state
- Next generation state
- Methods to toggle state and apply Conway's rules

### `src/grid.py` - Grid Class
Manages the 2D grid with:
- Cell creation and management
- Neighbor counting algorithm
- Generation stepping (evolution)
- Grid operations (randomize, clear)
- Population counting

### `src/renderer.py` - Renderer Class
Handles all Pygame rendering:
- Grid drawing with cells and borders
- UI overlay with status information
- Mouse-to-grid coordinate conversion
- Color schemes and font rendering

### `src/game.py` - Game Class
Main application orchestrator:
- Game loop (handle events → update → render)
- Event handling (keyboard, mouse, quit)
- State management (playing/paused, generation count)
- Speed control logic

## Technical Details

### Grid Topology
The grid uses a **toroidal topology** - the edges wrap around. This means:
- A cell at the right edge has the left edge as a neighbor
- A cell at the bottom edge has the top edge as a neighbor
- Patterns can wrap around and interact with themselves

### Simulation Algorithm
Each generation follows this process:
1. For each cell, count its alive neighbors
2. Apply Conway's rules to determine next state
3. Simultaneously update all cells to their next state
4. Increment generation counter

This ensures deterministic behavior where all cells update simultaneously (not sequentially).


## Keyboard Shortcuts Reference

| Key | Action |
|-----|--------|
| SPACE | Play/Pause simulation |
| R | Randomize grid |
| C | Clear grid |
| ↑ (UP) | Increase speed |
| ↓ (DOWN) | Decrease speed |
| Q | Quit application |
| Mouse Click | Toggle cell (when paused) |

## Customization

### Grid Size
Edit `src/game.py`:
```python
GRID_WIDTH = 100    # Change number of columns
GRID_HEIGHT = 60    # Change number of rows
```

### Cell Size
Edit `src/game.py`:
```python
CELL_SIZE = 10      # Size in pixels
```

### Colors
Edit `src/renderer.py` in the `Renderer.__init__` method:
```python
self.COLOR_ALIVE_CELL = (0, 255, 100)    # Green
self.COLOR_DEAD_CELL = (40, 40, 40)      # Dark gray
```

### Window Size
Edit `src/game.py`:
```python
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
```

## Interesting Things to Explore

1. **Still Lifes**: Patterns that never change
   - Block, Beehive, Loaf, Boat

2. **Oscillators**: Patterns that cycle with a period
   - Blinker (period 2), Toad (period 2), Beacon (period 2)
   - Pulsar (period 3)

3. **Spaceships**: Patterns that move across the grid
   - Glider (moves 1,1 every 4 generations)
   - Lightweight spaceship (LWSS)

4. **Chaos and Order**: Random seeds can create complex dynamics
   - Watch how order emerges from chaos
   - Oscillating regions mixed with still lifes


## Dependencies

- **pygame**: For window management, rendering, and event handling
- **Python 3.8+**: Core language

See `requirements.txt` for exact versions.


## References

- [Conway's Game of Life - Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Life Lexicon - Comprehensive Pattern Guide](http://www.conwaylife.com/wiki/Main_Page)


**Enjoy exploring Conway's Game of Life! 🚀**
