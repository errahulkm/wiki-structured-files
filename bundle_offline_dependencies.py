#!/usr/bin/env python3
"""
Offline Wheelhouse Packager for STM32 Structured Wiki Generator.
Downloads all required Python wheels into a local 'wheels/' directory
for 100% offline, air-gapped, zero-internet deployment.
"""

import os
import sys
import subprocess
import shutil

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    req_file = os.path.join(root_dir, "requirements.txt")
    if not os.path.exists(req_file):
        req_file = os.path.join(root_dir, "project", "requirements.txt")

    wheels_dir = os.path.join(root_dir, "wheels")
    os.makedirs(wheels_dir, exist_ok=True)

    print("=" * 70)
    print("📦 Bundling Offline Dependencies into ./wheels")
    print(f"• Requirements File: {req_file}")
    print(f"• Target Wheelhouse: {wheels_dir}")
    print(f"• Host Platform:     {sys.platform} ({sys.version.split()[0]})")
    print("=" * 70)

    cmd = [
        sys.executable, "-m", "pip", "download",
        "-r", req_file,
        "-d", wheels_dir,
        "--prefer-binary"
    ]

    try:
        subprocess.check_call(cmd)
        print("=" * 70)
        print("✅ SUCCESS: All dependency wheels downloaded.")
        print(f"• Total wheels: {len(os.listdir(wheels_dir))}")
        print("• The release can now be installed 100% offline with zero internet access.")
        print("=" * 70)
    except Exception as e:
        print(f"❌ ERROR: Failed to download wheels: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
