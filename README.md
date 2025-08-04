| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `taskset -c 0 /nix/store/99730p255raxhz6zynn5ffi37py56gdl-rust_snix-cli-0.1.0-linked/bin/snix --no-warnings -E 'with import <nixpkgs>{}; toString firefox'` | 13.674 ± 0.107 | 13.508 | 13.832 | 6.26 ± 0.14 |
| `taskset -c 0 /nix/store/5va0h71mkv6g75y6m4s75sh4xx4fj0ic-lix-2.94.0-devpre20250802_cad6118/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{}; toString firefox'` | 2.656 ± 0.014 | 2.629 | 2.678 | 1.22 ± 0.03 |
| `taskset -c 0 /nix/store/qvid77asahwls5904hrvrsawbjmdd2s8-nix-2.31.0pre20250804_0889960/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{}; toString firefox'` | 2.185 ± 0.044 | 2.160 | 2.309 | 1.00 |
