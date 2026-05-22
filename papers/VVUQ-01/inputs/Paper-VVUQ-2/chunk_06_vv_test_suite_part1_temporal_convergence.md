# Chunk 06 — V&V Test Suite Part 1 and Temporal Convergence (dt) Results

---

## Digital Twin PDAC Virtual Trial: V&V Test Suite (Part 1)

---

### Model Verification & Numerical Checks

| Test ID | Details |
|---|---|
| V-01 | **Purpose:** Numerical Stability of Integrator - Assess if the simulation results are sensitive to the timestep dt. A stable solution should not change significantly with a smaller timestep. Parameter: GLOBAL_CONFIG['dt']. Original Value: 1.0. Test Values: 0.5, 0.1. |
| V-02 | **Purpose:** Stochastic Reproducibility - Confirm that setting a specific random seed produces identical results, a cornerstone of computational experiment reproducibility. Parameter: SEED. Original Value: 20260115. Test Values: 12345, 98765 (run twice with each new seed). |
| V-03 | **Purpose:** Zero-Efficacy Test - Verify that a drug with no effect (Emax=0) behaves as if it's not administered. Parameter: DRUG_PARAMS['gemcitabine']['Emax']. Original Value: 0.030. Test Values: 0.0, 1e-9. |
| V-04 | **Purpose:** Zero-Growth Test - Verify that in the absence of intrinsic tumor growth, tumors only shrink or remain static. Parameter: ARCHETYPES['ARCH-01']['growth_rate']. Original Value: 0.007. Test Values: 0.0, -0.001 (to test boundary). |
| V-05 | **Purpose:** Mass Balance / Boundary Conditions - Ensure tumor volume doesn't become negative or unrealistically large. This is handled by max(1e-9, ...) in the code. Parameter: Code Inspection. Original Value: N/A. Test Values: N/A. |
| V-06 | **Purpose:** Toxicity Model Logic - Verify that if the probability of a G3+ event is 100%, every patient experiences one, and if 0%, no one does. Parameter: REGIMEN_TOXICITY['A']['g3_prob']. Original Value: 0.048. Test Values: 1.0, 0.0. |

---

### Model Validation & Sensitivity Analysis

| Test ID | Details |
|---|---|
| S-01 | **Purpose:** Drug Potency (Emax) - Assess sensitivity to the maximum kill rate of a key drug (gemcitabine). Parameter: DRUG_PARAMS['gemcitabine']['Emax']. Original Value: 0.030. Test Values: 0.024 (-20%), 0.036 (+20%). |
| S-02 | **Purpose:** Drug Sensitivity (EC50) - Assess sensitivity to the concentration required for half-maximal effect for a targeted therapy (olaparib). Parameter: DRUG_PARAMS['olaparib']['EC50']. Original Value: 0.5. Test Values: 0.6 (+20%), 0.4 (-20%). |
| S-03 | **Purpose:** Drug Clearance (Half-life) - Assess sensitivity to the persistence of an immunotherapy agent (pembrolizumab). Parameter: DRUG_PARAMS['pembrolizumab']['half_life']. Original Value: 14.0. Test Values: 7.0, 21.0. |
| S-04 | **Purpose:** Tumor Aggressiveness - Assess sensitivity to the intrinsic tumor growth rate for a major patient archetype. Parameter: ARCHETYPES['ARCH-01']['growth_rate']. Original Value: 0.007. Test Values: 0.0056 (-20%), 0.0084 (+20%). |
| S-05 | **Purpose:** Primary Resistance Rate - Evaluate the impact of the baseline proportion of resistant cells on overall treatment efficacy. Parameter: In PatientSimulator.__init__: vol_sensitive, vol_resistant from primary_resistance_flag check. Modify the probability. Original Value: 0.4. Test Values: 0.2, 0.6. |
| S-06 | **Purpose:** Global Efficacy Tuning - Test the impact of the global sensitivity_multiplier, which represents inter-patient variability in drug sensitivity. Parameter: In generate_virtual_patients: np.random.lognormal(mean=-0.2, ...). Original Value: mean=-0.2. Test Values: mean=-0.4, mean=0.0. |
| S-07 | **Purpose:** Toxicity Leading to Dropout - Assess how the probability of dropping out after a toxic event affects survival outcomes. Parameter: REGIMEN_TOXICITY['C']['dropout_prob_on_g3']. Original Value: 0.40. Test Values: 0.20, 0.60. |
| S-08 | **Purpose:** Survival Model (Post-Progression) - Test the sensitivity of the OS calculation to the hazard multiplier after progression. Parameter: In PatientSimulator.calculate_hazard: hazard *= 5.0. Original Value: 5.0. Test Values: 3.0, 8.0. |
| S-09 | **Purpose:** Survival Model (Biomarker Effect) - Test the impact of the gBRCA hazard reduction, a key assumption for Arms J/K. Parameter: In PatientSimulator.calculate_hazard: base_hazard_rate *= 0.25. Original Value: 0.25. Test Values: 0.5, 0.1. |

*Caption: Verification & Validation Tests. Supplementary: ASME_VV40_FDA_Experiments*

---

### 4.2 Temporal Convergence (dt)

*Figure 2B: Convergence of Trial Endpoints at Higher dt*

#### dt = 0.1 Results

| Arm | N | ORR% | DCR% | mPFS (HR) | PFS-6 | mOS (HR) | OS-12 | G3+/Drop% |
|---|---|---|---|---|---|---|---|---|
| A | 100 | 65.0% | 93.0% | 20.5 (1.00) | 78.0% | 24.7 (1.00) | 70.0% | 68.0% / 47.0% |
| B | 100 | 66.0% | 95.0% | 28.9 (0.79) | 81.0% | 35.7 (0.77) | 77.0% | 65.0% / 43.0% |
| C | 100 | 83.0% | 96.0% | 35.5 (0.67) | 87.0% | 36.0 (0.69) | 82.0% | 70.0% / 35.0% |
| D | 100 | 67.0% | 91.0% | 25.2 (0.89) | 80.0% | 31.7 (0.80) | 80.0% | 73.0% / 51.0% |
| E | 100 | 68.0% | 90.0% | 26.1 (0.79) | 85.0% | 36.0 (0.70) | 77.0% | 72.0% / 52.0% |
| G | 100 | 46.0% | 93.0% | 24.3 (1.00) | 82.0% | 24.7 (1.00) | 70.0% | 66.0% / 43.0% |
| H | 100 | 75.0% | 91.0% | 25.2 (0.85) | 81.0% | 36.0 (0.64) | 76.0% | 63.0% / 46.0% |
| I | 100 | 34.0% | 90.0% | 27.1 (0.84) | 80.0% | 29.9 (0.85) | 76.0% | 62.0% / 38.0% |
| J | 100 | 72.0% | 98.0% | 36.0 (0.04) | 95.0% | 36.0 (0.20) | 91.0% | 84.0% / 23.0% |
| K | 100 | 0.0% | 99.0% | 10.3 (1.00) | 97.0% | 28.9 (1.00) | 89.0% | 33.0% / 6.0% |

#### dt = 0.5 Results

| Arm | N | ORR% | DCR% | mPFS (HR) | PFS-6 | mOS (HR) | OS-12 | G3+/Drop% |
|---|---|---|---|---|---|---|---|---|
| A | 100 | 43.0% | 94.0% | 11.3 (1.00) | 79.0% | 18.2 (1.00) | 74.0% | 58.0% / 37.0% |
| B | 100 | 51.0% | 92.0% | 11.6 (1.02) | 76.0% | 17.7 (0.97) | 64.0% | 60.0% / 41.0% |
| C | 100 | 67.0% | 98.0% | 16.4 (0.87) | 89.0% | 23.3 (0.94) | 81.0% | 50.0% / 24.0% |
| D | 100 | 36.0% | 93.0% | 11.4 (1.38) | 77.0% | 17.7 (1.33) | 67.0% | 52.0% / 25.0% |
| E | 100 | 53.0% | 95.0% | 11.5 (1.08) | 80.0% | 15.9 (1.10) | 72.0% | 57.0% / 35.0% |
| G | 100 | 10.0% | 95.0% | 7.2 (1.00) | 58.0% | 14.0 (1.00) | 60.0% | 40.0% / 25.0% |
| H | 100 | 60.0% | 91.0% | 12.3 (0.60) | 81.0% | 23.3 (0.47) | 79.0% | 62.0% / 43.0% |
| I | 100 | 26.0% | 90.0% | 8.4 (1.03) | 64.0% | 13.1 (0.89) | 55.0% | 45.0% / 25.0% |
| J | 100 | 54.0% | 97.0% | 20.5 (0.01) | 91.0% | 36.0 (0.24) | 91.0% | 65.0% / 25.0% |
| K | 100 | 0.0% | 99.0% | 2.1 (1.00) | 0.0% | 18.7 (1.00) | 68.0% | 20.0% / 5.0% |

#### dt = 1.0 Results

| Arm | N | ORR% | DCR% | mPFS (HR) | PFS-6 | mOS (HR) | OS-12 | G3+/Drop% |
|---|---|---|---|---|---|---|---|---|
| A | 100 | 21.0% | 82.0% | 4.7 (1.00) | 42.0% | 9.3 (1.00) | 43.0% | 31.0% / 17.0% |
| B | 100 | 31.0% | 85.0% | 6.3 (0.80) | 51.0% | 10.7 (0.96) | 48.0% | 44.0% / 19.0% |
| C | 100 | 44.0% | 96.0% | 7.5 (0.63) | 57.0% | 13.1 (0.67) | 54.0% | 39.0% / 21.0% |
| D | 100 | 19.0% | 82.0% | 3.8 (1.15) | 33.0% | 9.8 (1.07) | 40.0% | 26.0% / 17.0% |
| E | 100 | 44.0% | 95.0% | 5.6 (0.83) | 45.0% | 11.2 (0.83) | 48.0% | 41.0% / 26.0% |
| G | 100 | 3.0% | 41.0% | 1.8 (1.00) | 9.0% | 5.6 (1.00) | 15.0% | 18.0% / 10.0% |
| H | 100 | 47.0% | 93.0% | 7.5 (0.31) | 55.0% | 12.1 (0.34) | 55.0% | 36.0% / 21.0% |
| I | 100 | 17.0% | 79.0% | 3.1 (0.49) | 29.0% | 8.4 (0.58) | 35.0% | 22.0% / 12.0% |
| J | 100 | 39.0% | 97.0% | 10.3 (0.00) | 67.0% | 21.5 (0.38) | 85.0% | 47.0% / 18.0% |
| K | 100 | 0.0% | 0.0% | 1.0 (1.00) | 0.0% | 14.0 (1.00) | 58.0% | 14.0% / 5.0% |

*Caption: Results Convergence Top to Bottom: dt=0.1, dt=0.5, dt=1.0*
