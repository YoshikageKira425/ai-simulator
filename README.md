# 🏎️ AI 2D Car Racing Simulation

An autonomous 2D car racing simulation where agents learn to navigate complex tracks entirely on their own. Instead of using traditional reinforcement learning or backpropagation, the agents' neural network "brains" are evolved over successive generations using a **Vectorized Genetic Algorithm**.

Built with **[Python Arcade](https://api.arcade.academy/)** for rendering and physics, **NumPy** for high-performance matrix operations, and **Pillow** for pixel-accurate RGBA track collision masks.

---

## 🌟 Key Features

* **Neuroevolution Engine:** Vectorized uniform crossover and additive Gaussian mutation utilizing NumPy matrix operations.
* **Deterministic Sub-Stepping Physics:** Multi-tick simulation updates per frame (`1x` to `10x` game speed) that eliminate high-speed wall tunneling and ensure 100% deterministic physics across execution speeds.
* **5-Point Raycast Sensing:** Casts angular distance vectors relative to the vehicle heading to feed precise wall proximity data into the network.
* **Anti-Stagnation & Anti-Exploit Fitness System:** Enforces a high-water mark progress timeout, steering twitchiness penalties, and proximity penalties to prevent donut-spinning, wall-hugging, and reversing exploits.
* **RGBA Alpha-Mask Collision Engine:** Uses PIL image alpha channels to evaluate dynamic track boundaries without demanding heavy physics engine geometry.
* **Checkpoint & Resume System:** Compressed `.npz` archive saving and loading for both top individual models and full population generations.

---

## 🧠 How It Works

1. **Sensing (`raycasting.py`):** Each car casts 5 sensor rays ($[-90^\circ, -45^\circ, 0^\circ, +45^\circ, +90^\circ]$) to measure normalized distances $[0.0, 1.0]$ to the nearest off-track boundary.
2. **Thinking (`neural_network.py`):** Inputs are fed into a 3-layer feedforward network ($5 \to 6 \to 6 \to 2$) using `tanh` activations, producing normalized outputs for throttle and steering.
3. **Acting (`car_controller.py`):** Translates neural decisions into vehicle physics (acceleration, deceleration, friction, and speed-dependent steering limits).
4. **Evaluating (`car_agent.py`):** Cars accumulate fitness based on net distance traveled along the track layout while penalizing wall-hugging or twitchy steering adjustments.
5. **Evolving (`breed.py`):** Once all cars crash or stall out, Tournament Selection ($k=3$) and Elitism (preserving the top 2 models) create the next generation via crossover and Gaussian mutation.
6. **Checkpointing (`checkpoint.py`):** Whenever a generation sets an all-time record score, its neural weights are serialized to disk inside the `checkpoints/` directory.

---

## 📂 Project Structure

```text
checkpoints/                         # Saved neural network weight archives (.npz)
src/
├── ai/
│   ├── breed.py                     # Genetic operators (crossover, mutation, tournament selection)
│   ├── checkpoint.py                # Compressed .npz model & population save/load handlers
│   ├── neural_network.py            # Forward-pass execution engine using NumPy matrix math
│   └── simulation_environment.py    # Population update loop and generational management
│   ├── assets/
│   ├── maps/                            # Transparent RGBA track PNG maps (800x600)
│   └── sprites/                         # Vehicle and track tile graphics
├── core/
│   ├── car_agent.py                 # Individual agent state, fitness tracking, and idle timeout logic
│   ├── car_controller.py            # Physical motion, velocity, and steering control logic
│   ├── map_manager.py               # RGBA alpha-channel pixel lookup and spawn point registry
│   └── raycasting.py                # Distance-sensor engine for wall proximity detection
├── entity/
│   └── car.py                       # Arcade sprite representation (position, heading, dimensions)
├── model/
│   └── neural_network_model.py      # Dataclass containing layer weights (W1, W2, W_out) and biases
├── ui/
│   └── simulation_information_ui.py # Telemetry HUD (generation #, alive count, best fitness)
├── views/
│   ├── ai_game_view.py              # Real-time AI training visualization & debug overlays
│   ├── game_view.py                 # Human-controlled manual driving mode
│   └── simulation_view.py           # Sub-stepping update manager and generation orchestrator
├── constant.py                      # Global parameters, map configurations, and spawn points
main.py                          # Application entry point

```

---

## ⚙️ Hyperparameters & Network Architecture

| Parameter | Value | Description |
| --- | --- | --- |
| **Input Layer** | 5 Nodes | Distance raycasts (Far Left, Mid Left, Center, Mid Right, Far Right) |
| **Hidden Layer 1** | 6 Nodes | `tanh` activation |
| **Hidden Layer 2** | 6 Nodes | `tanh` activation |
| **Output Layer** | 2 Nodes | `tanh` activation (`[Throttle, Steering]`) |
| **Population Size** | 20 | Agents per generation |
| **Elitism Count** | 2 | Top models preserved unchanged |
| **Tournament Size ($k$)** | 3 | Selection sample size |
| **Mutation Rate** | 30% | Chance per gene/weight matrix entry |
| **Mutation Strength ($\sigma$)** | 0.1 | Standard deviation of additive Gaussian noise |

---

## 🚀 Getting Started

### Prerequisites

This project uses **[`uv`](https://github.com/astral-sh/uv)** for fast Python dependency management.

### Installation & Execution

```bash
# Clone the repository
git clone https://github.com/YoshikageKira425/ai-simulator.git
cd ai-car-racing

# Sync dependencies using uv
uv sync

# Run the simulation entry point
uv run src/main.py

```

---

## 🎮 Controls & Hotkeys

### Manual Driving Mode (`GameView`)

| Key | Action |
| --- | --- |
| **W** / **Up Arrow** | Accelerate |
| **S** / **Down Arrow** | Reverse / Brake |
| **A** / **Left Arrow** | Turn Left |
| **D** / **Right Arrow** | Turn Right |

### AI Simulation & Training Mode (`AIGameView`)

| Key | Action |
| --- | --- |
| **1** / **2** / **3** | Set simulation speed (`1x`, `2x`, `5x`) |
| **SPACE** | Pause / Resume physics simulation |
| **D** | Toggle sensor raycast line rendering |
| **R** | Force-kill current generation and evolve immediately |
| **S** | Manually save active leader checkpoint to disk |
| **M** | Advance to the next track layout in sequence |
