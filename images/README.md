# Images Directory

This directory contains images for the Parasha website.

## Required Images (you need to add these):

- `logo.png` - Site logo (referenced in build script)
- `default.jpg` - Default fallback image for articles without specific images

## Current Images:

- `korach_2025.jpg` - Image for Parashat Korach 2025
- `shalach_2025.jpg` - Image for Parashat Shlach 2025
- `haazinu_2025.jpg` - Image for Parashat Haazinu 2025

## Processing Pipeline (FOLLOW THIS ORDER):

### **Step 1: Pre-Flight Checks (CRITICAL)**

**ALWAYS verify BEFORE copying files:**

1. **Verify the date is today's date** in the article frontmatter
   - Hebrew calendar is ~11 days shorter than Gregorian (354 vs 365 days)
   - Same Gregorian year can span TWO Hebrew years
   - Example: Vayigash from Jan 2025 (Hebrew year 5785) will appear again in Dec 2025 (Hebrew year 5786)

2. **Check for duplicate articles from earlier in the same Gregorian year**
   ```bash
   # Check for existing articles with same parasha name
   ls content/*[parasha_name]*.md

   # Example for Vayigash:
   ls content/*vayigash*.md
   # May show: parasha_vayigash_2025.md from January
   ```

3. **Before copying**: Verify there's no article with the same parasha name and year already in content/

### **Step 2: Image Generation Template (STANDARD)**

**Use this exact template for all new images:**
```bash
ffmpeg -i /data/git/parasha_of_the_week/images/[SOURCE_FILE].png -vf scale=1200:1204 -q:v 75 -f mjpeg /data/git/parasha_of_the_week/images/[parasha_name]_[year].jpg
```

**Example - Vayera 2025:**
```bash
ffmpeg -i /data/git/parasha_of_the_week/images/Gemini_Generated_Image_15aw3c15aw3c15aw.png -vf scale=1200:1204 -q:v 75 -f mjpeg /data/git/parasha_of_the_week/images/vayera_2025.jpg
```

**Parameters:**
- Input: Full absolute path to source PNG file
- Scale: 1200x1204 pixels (standard size)
- Quality: 75 (good balance between size and quality)
- Format: MJPEG (produces optimized JPG files)
- Output: Full absolute path with correct naming convention

### **Step 3: Post-Processing Checks**

After copying and converting:
1. Check for arrow directions (use ← not → for RTL Hebrew)
2. Verify biblical verses have ניקוד (vowel points)
3. Ensure key verses use blockquote format (>) not code blocks

## Naming Convention:

Images should match the article naming pattern:
- `[parasha_name]_[year].jpg/png` (e.g., `behar_2025.jpg`)
- `parasha_[parasha_name]_[year].jpg/png` (e.g., `parasha_behar_2025.jpg`)
- `parashat_[parasha_name]_[year].jpg/png` (e.g., `parashat_shalach_2025.jpg`)

The build script will automatically match images to articles based on these patterns.