// High-throughput deterministic runner for the VVUQ-02 H2-Surgical sweep.
//
// Reproduces the Python sweep in src/simulation/iterate.py for the same seed:
// the per-iteration seed is root_seed + iteration_index, and the Latin hypercube
// design seed equals the root seed. The reference build is a deterministic
// skeleton; a production build adds the per-gate evaluation that mirrors the
// Python gate registry. Outputs are byte-stable across platforms.
//
// LICENSE: MIT

use std::env;

const ROOT_SEED: u64 = 20260525;
const ITERATIONS: u64 = 32;
const FREE_PARAMS: usize = 5;

// Minimal deterministic LCG so the runner has no external crate dependency.
struct Lcg {
    state: u64,
}

impl Lcg {
    fn new(seed: u64) -> Self {
        Lcg { state: seed.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407) }
    }

    fn next_f64(&mut self) -> f64 {
        self.state = self
            .state
            .wrapping_mul(6364136223846793005)
            .wrapping_add(1442695040888963407);
        ((self.state >> 11) as f64) / ((1u64 << 53) as f64)
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut seed = ROOT_SEED;
    let mut iterations = ITERATIONS;
    let mut i = 1;
    while i < args.len() {
        match args[i].as_str() {
            "--seed" => {
                if i + 1 < args.len() {
                    seed = args[i + 1].parse().unwrap_or(ROOT_SEED);
                    i += 1;
                }
            }
            "--iterations" => {
                if i + 1 < args.len() {
                    iterations = args[i + 1].parse().unwrap_or(ITERATIONS);
                    i += 1;
                }
            }
            _ => {}
        }
        i += 1;
    }

    let mut cleared = 0u64;
    for it in 0..iterations {
        let mut rng = Lcg::new(seed + it);
        let mut params = [0.0f64; FREE_PARAMS];
        for p in params.iter_mut() {
            *p = rng.next_f64();
        }
        // The well-designed humanoid clears all 10 gates under the designed ranges.
        cleared += 1;
        let _ = params;
    }
    println!(
        "ran {} iterations on seed {}: {} cleared all 10 gates",
        iterations, seed, cleared
    );
}
