#!/usr/bin/env python3
import argparse
from pathlib import Path


def generate_svg(path: Path, width: int = 100, height: int = 100) -> None:
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive integers")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff4d4f" />
      <stop offset="100%" stop-color="#4096ff" />
    </linearGradient>
  </defs>
  <rect width="{width}" height="{height}" fill="url(#bg)" />
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a simple SVG image.")
    parser.add_argument("--output", default="generated.svg", help="Output image path.")
    parser.add_argument("--width", type=int, default=100, help="Image width.")
    parser.add_argument("--height", type=int, default=100, help="Image height.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = Path(args.output)
    generate_svg(output, args.width, args.height)
    print(f"Image generated: {output.resolve()}")


if __name__ == "__main__":
    main()
