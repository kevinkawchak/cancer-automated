# NASA-STD-7009A

- Designation: NASA-STD-7009A
- Issuing body: National Aeronautics and Space Administration (NASA)
- Title: Standard for Models and Simulations

## Scope

NASA-STD-7009A sets requirements for the development, documentation, and use of
models and simulations, and for reporting their credibility. It treats
uncertainty quantification as a first-class credibility factor and defines a
credibility assessment scale across factors such as verification, validation,
input pedigree, uncertainty, robustness, and use history.

## Constructs VVUQ-02 uses

- Uncertainty quantification as a reported credibility factor.
- Explicit reporting of the basis for results and their dispersion.

## How VVUQ-02 applies it

The uncertainty dimension of every gate computes, across at least three seeded
runs, the per-metric mean, population standard deviation, and coefficient of
variation (cv = stdev / mean). The maximum cv is compared against a per-gate
bound; divergence above the bound sets ESCALATE rather than silently accepting an
unstable result. This realizes the NASA-STD-7009A position that uncertainty must
be quantified and reported, not assumed away.
