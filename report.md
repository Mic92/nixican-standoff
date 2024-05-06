| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `tvix/target/release/tvix --no-warnings -E 'with import <nixpkgs>{}; toString hello'` | 1.941 ± 0.011 | 1.928 | 1.966 | 5.45 ± 0.09 |
| `/nix/store/nrnr2ddbf7cm7yblsz7lfm1sb2sb8gxa-nix-2.90.0pre20240506_106b959/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{}; toString hello'` | 0.356 ± 0.005 | 0.352 | 0.369 | 1.00 |
| `/nix/store/pzic67rvj74y4im1kvyhrzxgxj05di7c-nix-2.23.0pre20240506_20445df/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{}; toString hello'` | 0.386 ± 0.005 | 0.380 | 0.394 | 1.08 ± 0.02 |
