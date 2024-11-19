# diffusion2D

## Project description

This package provides a solution for the 2D diffusion equation over a square domain using the Finite Difference Method. The domain starts at a uniform temperature, with a circular disc at the center at a higher temperature. Users can modify thermal diffusivity and initial conditions to simulate various scenarios. The output includes four plots showing the diffusion process at different timepoints.

## Installing the package

To install the package, use:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple mamoyn_diffusion2d

```

### Required dependencies

- Python (>=3.6)
- numpy
- matplotlib

## Running this package

To run the simulation with default parameters, execute:

```bash
solve
```

For custom parameters, import and call the `solve` function:

```python
from mamoyn_diffusion2d import diffusion2d
diffusion2d.solve(dx=0.05, dy=0.05, D=2.0)
```

## Citing

If using this package, please cite:

> Yonatan Mamo. *mamoyn_diffusion2d: A Python Package for Solving 2D Diffusion Equations.* Version 0.0.1, 2024. Available at [https://test.pypi.org/project/mamoyn_diffusion2d/](https://test.pypi.org/project/mamoyn_diffusion2d/).
