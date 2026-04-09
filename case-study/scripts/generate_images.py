#!/usr/bin/env python3
"""
Case Study Image Generator — Generates supporting visuals for Case Study pages
using FLUX 2 Pro via OpenRouter API.

Usage:
    python generate_images.py \
        --company "Acme Corp" \
        --industry "SaaS / Project Management" \
        --accent-color "#FF6B35" \
        --bg-color "#1a1a1a" \
        --tone "modern, bold, tech" \
        --output-dir ./output/case-study-work/images

Each image is saved as a PNG file named by page purpose (e.g., cover_photo.png).
Outputs a JSON manifest (image_manifest.json) mapping page roles to file paths.
"""

import argparse
import base64
import json
import os
import sys
import time
import requests
from pathlib import Path


def load_api_key():
    """Load OpenRouter API key from environment or .env file."""
    key = os.environ.get("FLUX_API_KEY")
    if key:
        return key

    # Walk up from script location to find .env
    search_dir = Path(__file__).resolve().parent
    for _ in range(5):
        env_file = search_dir / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if line.startswith("FLUX_API_KEY="):
                    return line.split("=", 1)[1].strip()
        search_dir = search_dir.parent

    print("ERROR: FLUX_API_KEY not found in environment or .env file", file=sys.stderr)
    sys.exit(1)


def generate_image(api_key: str, prompt: str, retries: int = 2):
    """Call OpenRouter FLUX API and return base64 image data URL, or None on failure."""
    for attempt in range(retries + 1):
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": "black-forest-labs/flux.2-pro",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "modalities": ["image"]
                }),
                timeout=120,
            )
            response.raise_for_status()
            result = response.json()

            if result.get("choices"):
                message = result["choices"][0]["message"]
                if message.get("images"):
                    return message["images"][0]["image_url"]["url"]

            print(f"  Warning: No image in response (attempt {attempt + 1})", file=sys.stderr)

        except requests.exceptions.RequestException as e:
            print(f"  Request error (attempt {attempt + 1}): {e}", file=sys.stderr)

        if attempt < retries:
            time.sleep(3)

    return None


def save_image(data_url: str, filepath: Path) -> bool:
    """Save a base64 data URL to a file. Returns True on success."""
    try:
        if "," in data_url:
            b64_data = data_url.split(",", 1)[1]
        else:
            b64_data = data_url

        img_bytes = base64.b64decode(b64_data)
        filepath.write_bytes(img_bytes)
        return True
    except Exception as e:
        print(f"  Error saving {filepath}: {e}", file=sys.stderr)
        return False


def build_prompts(company: str, industry: str, accent_color: str, bg_color: str, tone: str) -> dict:
    """
    Build image generation prompts for each Case Study page that needs a visual.
    Returns dict mapping image_key -> prompt string.
    """
    tone_desc = tone if tone else "professional, modern, clean"
    base_style = (
        f"Professional corporate photography style, {tone_desc} aesthetic, "
        f"high quality, 3:4 portrait aspect ratio, suitable for an A4 business document. "
        f"Color palette hints: accent color {accent_color}, dark background {bg_color}. "
        f"No text, no logos, no watermarks."
    )

    return {
        # Page 1: Cover — professional workspace photo (bottom-right of cover)
        "cover_photo": (
            f"Modern professional office interior or workspace for a {industry} company called {company}. "
            f"Clean desk with monitor, plants, warm ambient lighting, contemporary furniture. "
            f"Shot from a slight angle showing depth. Aspirational corporate environment. "
            f"{base_style}"
        ),

        # Page 4: Preferred Solution — subtle dark geometric background
        "solution_bg": (
            f"Abstract minimal dark background with subtle geometric patterns and soft glowing lines. "
            f"Dark theme with hints of {accent_color}. Conveys strategy, structure, and innovation. "
            f"Very subtle, not distracting — meant to sit behind text content. "
            f"{base_style}"
        ),

        # Page 6: Performance Results — dark data visualization background
        "results_bg": (
            f"Abstract data visualization background, dark theme. Subtle glowing charts, graphs, "
            f"or data points floating in space with hints of {accent_color}. "
            f"Conveys measurement, analytics, and performance tracking. "
            f"Very muted — will have stat cards overlaid on top. "
            f"{base_style}"
        ),

        # Page 8: Client Testimonial — trust-evoking dark background
        "testimonial_bg": (
            f"Soft abstract background suggesting trust and credibility. "
            f"Gentle gradient with subtle bokeh or light particles, dark theme with {accent_color} hints. "
            f"Very muted and non-distracting — will have testimonial text overlaid. "
            f"{base_style}"
        ),

        # Page 10: Thank You / Closing — minimal dark closing background
        "closing_bg": (
            f"Clean minimal abstract background for a closing/thank-you page. "
            f"Dark theme with a subtle warm glow or gradient in {accent_color}. "
            f"Inviting, professional, open feeling. Mostly dark with accent lighting. "
            f"{base_style}"
        ),
    }


def main():
    parser = argparse.ArgumentParser(description="Generate Case Study supporting visuals via FLUX")
    parser.add_argument("--company", required=True, help="Company name")
    parser.add_argument("--industry", required=True, help="Industry or sector description")
    parser.add_argument("--accent-color", required=True, help="Brand accent color (hex)")
    parser.add_argument("--bg-color", default="#1a1a1a", help="Dark background color (hex)")
    parser.add_argument("--tone", default="modern, professional, clean", help="Visual tone descriptors")
    parser.add_argument("--output-dir", required=True, help="Directory to save images")
    parser.add_argument("--slides", default="all", help="Comma-separated image keys to generate, or 'all'")
    args = parser.parse_args()

    api_key = load_api_key()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    prompts = build_prompts(
        company=args.company,
        industry=args.industry,
        accent_color=args.accent_color,
        bg_color=args.bg_color,
        tone=args.tone,
    )

    # Filter to requested images
    if args.slides != "all":
        requested = [s.strip() for s in args.slides.split(",")]
        prompts = {k: v for k, v in prompts.items() if k in requested}

    manifest = {}
    total = len(prompts)

    print(f"Generating {total} images for {args.company} Case Study...")
    print(f"Output directory: {output_dir}")
    print()

    for i, (key, prompt) in enumerate(prompts.items(), 1):
        print(f"[{i}/{total}] Generating: {key}")
        data_url = generate_image(api_key, prompt)

        if data_url:
            ext = "png"
            if "image/jpeg" in data_url[:30]:
                ext = "jpeg"
            elif "image/webp" in data_url[:30]:
                ext = "webp"

            filepath = output_dir / f"{key}.{ext}"
            if save_image(data_url, filepath):
                manifest[key] = str(filepath)
                print(f"  Saved: {filepath}")
            else:
                manifest[key] = None
                print(f"  FAILED to save: {key}")
        else:
            manifest[key] = None
            print(f"  FAILED to generate: {key}")

        print()

    # Write manifest
    manifest_path = output_dir / "image_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"Manifest written to: {manifest_path}")

    # Summary
    success = sum(1 for v in manifest.values() if v is not None)
    print(f"\nDone: {success}/{total} images generated successfully.")

    if success < total:
        sys.exit(1)


if __name__ == "__main__":
    main()
