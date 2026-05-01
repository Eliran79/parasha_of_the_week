#!/usr/bin/env python3
"""Generate article image for Emor 2026 via Vertex AI Imagen 3."""

from google import genai
from google.genai import types

PROJECT = "arc-project-487920"
LOCATION = "us-central1"
OUTPUT_PNG = "/data/git/parasha_of_the_week/images/emor_2026_raw.png"

PROMPT = (
    "A richly detailed digital painting in Israeli illuminated-manuscript style. "
    "An ancient Jewish scholar sits at a candlelit stone desk in a Jerusalem archway, "
    "writing musical neume notation above Hebrew letters on aged parchment. "
    "Above the parchment, delicate golden lines form a musical staff — "
    "Hebrew cantillation marks (taamei hamikra) glow in amber, "
    "interweaving with medieval Western neumes in the same luminous light, "
    "showing they are the same symbols in two different scripts. "
    "Through the arched window behind him: the walled Old City of Jerusalem at golden hour, "
    "olive trees silhouetted against a warm amber sky. "
    "Mood: scholarly, timeless, sacred, the beauty of hidden connections revealed. "
    "Deep amber, ivory, and indigo tones. Cinematic lighting. No readable text in the image."
)

def main():
    client = genai.Client(vertexai=True, project=PROJECT, location=LOCATION)

    print(f"Generating image with Imagen 3 (project={PROJECT})...")
    response = client.models.generate_images(
        model="imagen-3.0-generate-001",
        prompt=PROMPT,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="1:1",
            output_mime_type="image/png",
        ),
    )

    if not response.generated_images:
        print("ERROR: No images returned (safety filter may have blocked the prompt).")
        return

    with open(OUTPUT_PNG, "wb") as f:
        f.write(response.generated_images[0].image.image_bytes)
    print(f"Saved: {OUTPUT_PNG}")

if __name__ == "__main__":
    main()
