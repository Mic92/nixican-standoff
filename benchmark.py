import subprocess
import shlex
import os
from pathlib import Path


def run(args: list[str], cwd: Path | str | None = None) -> subprocess.CompletedProcess[str]:
    print(f"$ {shlex.join(args)}")
    return subprocess.run(args, check=True, stdout=subprocess.PIPE, cwd=cwd, text=True)


def nix_build(package: str) -> subprocess.CompletedProcess[str]:
    proc = run(["nix", "build", "--print-out-paths", package])
    return proc.stdout.strip()


def main() -> None:
    lix_path = nix_build("git+https://git.lix.systems/lix-project/lix")
    nix_path = nix_build("github:NixOS/nix")
    tvix_path = Path("tvix")
    if not tvix_path.exists():
        run(["git", "clone", "https://github.com/tvlfyi/tvix"])
    run(["git", "-C", str(tvix_path), "fetch", "origin", "canon"])
    run(["git", "-C", str(tvix_path), "reset", "--hard", "origin/canon"])
    run(["nix-shell", "--run", "cargo build --release"], cwd=tvix_path)
    hyperfine_command = [
        "hyperfine", "--export-markdown", "report.md",
        f"{tvix_path}/target/release/tvix --no-warnings -E 'with import <nixpkgs>{{}}; toString hello'",
        f"{lix_path}/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{{}}; toString hello'",
        f"{nix_path}/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{{}}; toString hello'",
    ]
    run(["nix", "shell", "nixpkgs#hyperfine", "--command"] + hyperfine_command)


if __name__ == "__main__":
    main()
