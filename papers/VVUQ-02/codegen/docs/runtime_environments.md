# Runtime Environments (Five Cross-Platform Recipes)

The deterministic seed contract (root seed 20260525) yields bit-identical
JSON and CSV outputs across all five platforms. Heavy backends are optional and
guarded; the core sweep and the 10-gate harness run on the Python standard
library plus PyYAML.

## 1. MacOS Apple Silicon

```bash
brew install python@3.12 git rustup duckdb
rustup install stable && rustup default stable
git clone https://github.com/kevinkawchak/cancer-automated.git
cd cancer-automated/papers/VVUQ-02/codegen
python3.12 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,viz]
python -m src.simulation.iterate --seed 20260525 --iterations 32
python -m src.vvuq.gate_registry --iterations-dir data/iterations
```

## 2. Windows 11 (PowerShell)

```powershell
winget install Python.Python.3.12
winget install Git.Git
winget install Rustlang.Rustup
git clone https://github.com/kevinkawchak/cancer-automated.git
cd cancer-automated\papers\VVUQ-02\codegen
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,viz]
python -m src.simulation.iterate --seed 20260525 --iterations 32
```

For the Rust runner on Windows, install WSL2 with `wsl --install -d Ubuntu-24.04`
and run `cargo run --release` from inside the WSL2 shell.

## 3. Linux Ubuntu 22.04 LTS (Server, A100 or H100)

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3-pip git build-essential
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source $HOME/.cargo/env
git clone https://github.com/kevinkawchak/cancer-automated.git
cd cancer-automated/papers/VVUQ-02/codegen
python3.12 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev,llm-local,zenodo,viz]
python -m src.simulation.iterate --seed 20260525 --iterations 32
cd src/simulation && cargo run --release --bin runner -- --seed 20260525 --iterations 32
```

## 4. Claude Code (CLI, Web, IDE)

```bash
npm install -g @anthropic/claude-code
cd cancer-automated/papers/VVUQ-02/codegen
claude
```

Claude Code sets up the virtual environment and runs the sweep and the 10-gate
harness on demand.

## 5. Containerized (Docker Compose)

```bash
cd cancer-automated/papers/VVUQ-02/codegen
docker compose up python
```

## Determinism

Per-iteration seed = root_seed + iteration_index. The Latin hypercube design seed
equals the root seed. All committed outputs are plain text (JSON, JSONL, CSV) and
are byte-stable across the five platforms. The optional Rust runner reproduces
the Python outputs for the same seed.
