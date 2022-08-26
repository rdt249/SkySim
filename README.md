# SkySim
Cadence Spectre simulation director

## Installation

```git clone https://github.com/rdt249/SkySim```

## Run a trivial simulation

```scripts/test.sh SL_nand2```

Note: You may get an error about permissions. Give permission with `chmod +x scripts/test.sh`.

You may have to open the demo circuit `SL_nand2` in Virtuoso before calling `scripts/test.sh`.
This will automatically create the netlist used in the simulation.
You can simulate any cell you want, but currently `template/simulate.scs` is only set up for `SL_nand2`
