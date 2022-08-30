# SkySim
Cadence Spectre simulation director

## Installation

Clone the repo and install required Python packages.

```
git clone https://github.com/rdt249/SkySim
cd SkySim
pip3 install -r requirements.txt
```

## Run a simple simulation

The following command simulates the cell `SL_inv_1x` using the instructions defined in `input/SL_inv_1x/test1.scs`:

```scripts/sim.sh SL_inv_1x test1```

Note: You may get an error about permissions. Give permission with `chmod +x scripts/sim.sh`.

If the Spectre netlist (`input.scs`) has not yet been created with Virtuoso, the easiest way to do it manually is through Command Interpreter Window (CIW), which is the first window that pops up when you start Virtuoso. The following example creates a netlist for cell `SL_inv_1x` in library `MAINLIB_TESTING`:

```simulator("spectre"), design("MAINLIB_TESTING","SL_inv_1x","schematic"), createNetlist()```