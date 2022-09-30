# SkySim
Cadence Spectre simulation director

## Installation

Clone the repo and install required Python packages.

```
git clone https://github.com/rdt249/SkySim
cd SkySim
pip3 install -r requirements.txt
```

## Inverter simulation example

First things first, we need a netlist for the cell you want to simulate. Normally, Virtuoso doesn't save netlists in a readable format. However it's possible to export them using Virtuoso's Command Interpreter Window (CIW), which is the first window that appears when you start Virtuoso. The following example creates a netlist for a simple inverter cell `SL_inv_1x` found in library `MAINLIB_TESTING`:

```simulator("spectre"), design("MAINLIB_TESTING","SL_inv_1x","schematic"), createNetlist()```

The exported netlist should now be located in your home directory under `~/simulation/{CELL_NAME}/spectre/schematic/netlist/input.scs`. You can check to make sure it's there, because we will need it for the next step.

Next, we'll use a Python script to generate Spectre simulation files. Many test cases are generated automatically. Right now, the number of test cases generated will be the number of input conditions times the number of target devices. For the inverter example, there are two input conditions (input = high and low) and two target devices (NMOS and PMOS) resulting in four test cases. Make sure you navigate to the SkySim directory `cd SkySim` and use the following example to generate simulation files for the `MAINLIB_TESTING/SL_inv_1x` inverter.

```python3 scripts/generate.py MAINLIB_TESTING/SL_inv_1x```

There should be a new folder located at `SkySim/MAINLIB_TESTING/SL_inv_1x` which holds all the simulation files for that cell, as well as the netlist and a bash script called `run_all.sh`. Run the following command from the SkySim directory to execute that bash script and run all the simulations generated by the previous step.

```MAINLIB_TESTING/SL_inv_1x/run_all.sh```

That's it! The results from the simulations should be found in `SkySim/MAINLIB_TESTING/SL_inv_1x/testX`, where `X` is the test number (0 through 3 in this case). The transient simulation has been conveniently interpreted as a CSV named `transient.csv` for each test case. If you want to view the plotted data from this file, we have a Python script just for that. The follow example plots the results of test0.

```python3 scripts/plot.py MAINLIB_TESTING/SL_inv_1x/test0```

## Next steps

These are a few features I think we should try to add soon. This list isn't exhaustive.

1. _Export cell netlists from command line._ If we could run SKILL code from the command line without opening Virtuoso, it would save a lot of time and make things a lot easier for the user. However, I've run into issues with doing this over an SSH connection because of the way Virtuoso is built. An alternative approach is to try to read the supposedly free "Open Access" format that Virtuoso uses to store its netlists, and convert them to Spectre or Spice ourselves.

2. _Tunable radiation fault injection circuit._ We need to work on our fault injection circuit. There's lots of literature on how to do this with Spice components (see `cite/kauppila2009.pdf`). We could build and test a fault injector subcircuit in Virtuoso, save that netlist somewhere in this repo, and just copy and edit the file as we add it to simulation test cases. Ideally, we want the ability to choose an Linear Energy Transfer (LET) and/or total charge deposition (Qt). This would enable heavy ion simulations.

3. _Tunable laser fault injection circuit._ Similar to the radiation fault injector, but designed for lasers. This might require input from someone with some laser testing experience, and a deep dive into the literature.

4. _Other types of fault injection._ There's a lot of interest in simulating RTS noise in this technology. It would be cool to adapt this project for RTS noise simulation. It might be complicated to figure out where and how we'd want to inject the noise.