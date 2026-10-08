# Flight Trajectory Simulator 🚀

A Python project that simulates the motion of a projectile and gradually develops into a more advanced flight trajectory simulator.

## V1 — Basic Projectile Motion

V1 calculates projectile motion **without air resistance**.

### Features

* Initial velocity input
* Launch angle input
* Horizontal velocity
* Vertical velocity
* Maximum height
* Flight time
* Horizontal range
* Degrees-to-radians conversion

### Physics Used

The simulator uses standard projectile-motion equations with:

* Gravity = 9.81 m/s²
* No air resistance
* Same launch and landing height

### Example

For an initial velocity of **50 m/s** and launch angle of **45°**:

```text
HORIZONTAL VELOCITY = 35.36 m/s
VERTICAL VELOCITY = 35.36 m/s
MAXIMUM HEIGHT = 63.71 m
TIME = 7.21 s
HORIZONTAL RANGE = 254.84 m
```

## Project Roadmap

* [DONE] V1 — Basic projectile motion
* [ ] V2 — Air resistance
* [ ] V3 — Matplotlib trajectory graph
* [ ] V4 — Interactive inputs
* [ ] V5 — No-drag vs drag comparison

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

## Technologies

* Python
* Math module

## Future Goal

The final version will simulate projectile motion with air resistance and visualize the difference between ideal and realistic trajectories.
