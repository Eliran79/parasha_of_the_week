# Images Directory

This directory contains images for the Parasha website.

## Required Images (you need to add these):

- `logo.png` - Site logo (referenced in build script)
- `default.jpg` - Default fallback image for articles without specific images

## Current Images:

- `korach_2025.jpg` - Image for Parashat Korach 2025
- `shalach_2025.jpg` - Image for Parashat Shlach 2025

## Naming Convention:

Images should match the article naming pattern:
- `[parasha_name]_[year].jpg/png` (e.g., `behar_2025.jpg`)
- `parasha_[parasha_name]_[year].jpg/png` (e.g., `parasha_behar_2025.jpg`)
- `parashat_[parasha_name]_[year].jpg/png` (e.g., `parashat_shalach_2025.jpg`)

The build script will automatically match images to articles based on these patterns.