import subprocess
import shlex
import os
from pathlib import Path


def run(
    args: list[str], cwd: Path | str | None = None
) -> subprocess.CompletedProcess[str]:
    print(f"$ {shlex.join(args)}")
    return subprocess.run(args, check=True, stdout=subprocess.PIPE, cwd=cwd, text=True)


def nix_build(package: str) -> str:
    proc = run(["nix", "build", "--print-out-paths", package])
    return proc.stdout.strip()


def main() -> None:
    lix_path = nix_build("git+https://git.lix.systems/lix-project/lix")
    nix_path = nix_build("github:NixOS/nix")
    snix_path = Path("nix")
    if not snix_path.exists():
        run(["git", "clone", "https://git.snix.dev/snix/snix"])
    run(["git", "-C", str(snix_path), "fetch", "origin", "canon"])
    run(["git", "-C", str(snix_path), "reset", "--hard", "origin/canon"])
    run(["nix-shell", "--run", "cargo build --release"], cwd=snix_path)
    inxi = run(
        [
            "nix-shell",
            "-p",
            "inxi.override { withRecommends = true; }",
            "--run",
            "sudo inxi -F -a -i --slots -xxx -c0 -Z -i -m",
        ]
    )
    Path("hardware.md").write_text(f"```\n{inxi.stdout.strip()}\n```")
    hyperfine_command = [
        "hyperfine",
        "--export-json",
        "report.json",
        f"{snix_path}/target/release/tvix --no-warnings -E 'with import <nixpkgs>{{}}; toString hello'",
        f"{lix_path}/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{{}}; toString hello'",
        f"{nix_path}/bin/nix-instantiate --eval --json --expr 'with import <nixpkgs>{{}}; toString hello'",
    ]
    run(["nix", "shell", "nixpkgs#hyperfine", "--command"] + hyperfine_command)


if __name__ == "__main__":
    main()
