# Images Directory

This directory contains images for the Parasha website.

## Required Images (you need to add these):

- `logo.png` - Site logo (referenced in build script)
- `default.jpg` - Default fallback image for articles without specific images

## Current Images:

- `korach_2025.jpg` - Image for Parashat Korach 2025
- `shalach_2025.jpg` - Image for Parashat Shlach 2025
- `haazinu_2025.jpg` - Image for Parashat Haazinu 2025

## Image Creation:

To convert and optimize images to the correct format:
```bash
ffmpeg -i "source_image.png" -vf scale=1200:1204 -q:v 75 -f mjpeg [parasha_name]_[year].jpg
```

Example:
```bash
ffmpeg -i "Gemini_Generated_Image_5hi3ji5hi3ji5hi3.png" -vf scale=1200:1204 -q:v 75 -f mjpeg haazinu_2025.jpg
```

## Naming Convention:

Images should match the article naming pattern:
- `[parasha_name]_[year].jpg/png` (e.g., `behar_2025.jpg`)
- `parasha_[parasha_name]_[year].jpg/png` (e.g., `parasha_behar_2025.jpg`)
- `parashat_[parasha_name]_[year].jpg/png` (e.g., `parashat_shalach_2025.jpg`)

The build script will automatically match images to articles based on these patterns.