| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `taskset -c 0 /nix/store/99730p255raxhz6zynn5ffi37py56gdl-rust_snix-cli-0.1.0-linked/bin/snix --no-warnings -E 'with import <nixpkgs>{}; toString hello'` | 1.716 ± 0.009 | 1.703 | 1.732 | 4.56 ± 0.03 |
| `taskset -c 0 /nix/store/5va0h71mkv6g75y6m4s75sh4xx4fj0ic-lix-2.94.0-devpre20250802_cad6118/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{}; toString hello'` | 0.409 ± 0.002 | 0.407 | 0.413 | 1.09 ± 0.01 |
| `taskset -c 0 /nix/store/qvid77asahwls5904hrvrsawbjmdd2s8-nix-2.31.0pre20250804_0889960/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{}; toString hello'` | 0.376 ± 0.001 | 0.374 | 0.377 | 1.00 |
