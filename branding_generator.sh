#!/bin/bash

# Parasha of the Week — Branding Assets Generator
# Uses Vertex AI Imagen to generate the source logo, then processes all sizes

set -e

# ── Configuration ──────────────────────────────────────────────────────────────
GCP_PROJECT="nice-mix-458213-q0"
GCP_REGION="us-central1"
IMAGEN_MODEL="imagen-3.0-generate-002"
OUTPUT_DIR="branding-assets"
GENERATED_DIR="$OUTPUT_DIR/00-generated"

# Brand colors (matching site CSS variables)
BG_COLOR="#ffffff"       # White (site background)
ACCENT_COLOR="#2563eb"   # Blue (theme-color)
GOLD_COLOR="#c8a84b"     # Warm gold for Hebrew feel

# ── Terminal colors ────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

log_info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
log_error()   { echo -e "${RED}[ERROR]${NC} $1"; }
log_step()    { echo -e "${CYAN}[STEP]${NC} $1"; }

# ── Vertex AI: Generate source image with Imagen ───────────────────────────────
generate_with_vertex_ai() {
    log_step "Calling Vertex AI Imagen to generate Parasha logo..."

    local token
    token=$(gcloud auth print-access-token 2>/dev/null) || {
        log_error "Failed to get GCP access token. Run: gcloud auth login"
        exit 1
    }

    local prompt="A minimalist logo mark for a Jewish Torah learning website called 'Parasha of the Week'. \
The design blends ancient Hebrew wisdom with modern technology. \
Central motif: an open Torah scroll or the Hebrew letter Shin (ש) or Alef (א), \
combined with a subtle mathematical symbol (infinity sign, fractal, or geometric pattern). \
Color palette: deep blue (#2563eb) and warm gold (#c8a84b) on a clean white background. \
Clean vector aesthetic, premium educational brand, timeless and modern, \
no text, perfectly centered, high contrast, professional icon design."

    local request_body
    request_body=$(cat <<EOF
{
  "instances": [
    {
      "prompt": "$prompt"
    }
  ],
  "parameters": {
    "sampleCount": 4,
    "aspectRatio": "1:1",
    "safetyFilterLevel": "block_few",
    "personGeneration": "dont_allow"
  }
}
EOF
)

    log_info "Sending request to Imagen ($IMAGEN_MODEL)..."
    local response
    response=$(curl -s -X POST \
        "https://${GCP_REGION}-aiplatform.googleapis.com/v1/projects/${GCP_PROJECT}/locations/${GCP_REGION}/publishers/google/models/${IMAGEN_MODEL}:predict" \
        -H "Authorization: Bearer $token" \
        -H "Content-Type: application/json" \
        -d "$request_body")

    if echo "$response" | grep -q '"error"'; then
        log_error "Vertex AI returned an error:"
        echo "$response" | python3 -c "import sys,json; e=json.load(sys.stdin).get('error',{}); print(e.get('message','unknown error'))"
        exit 1
    fi

    local count
    count=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('predictions',[])))" 2>/dev/null || echo "0")

    if [ "$count" -eq 0 ]; then
        log_error "No images returned from Vertex AI"
        echo "$response" | head -200
        exit 1
    fi

    log_success "Received $count generated image(s) from Vertex AI"
    mkdir -p "$GENERATED_DIR"

    for i in $(seq 0 $((count - 1))); do
        local out_file="$GENERATED_DIR/candidate-$((i+1)).png"
        echo "$response" | python3 -c "
import sys, json, base64
d = json.load(sys.stdin)
img = d['predictions'][$i]['bytesBase64Encoded']
with open('$out_file', 'wb') as f:
    f.write(base64.b64decode(img))
print('Saved: $out_file')
"
    done

    SOURCE_IMAGE="$GENERATED_DIR/candidate-1.png"
    log_success "Source image: $SOURCE_IMAGE"
    log_info "Other candidates saved in $GENERATED_DIR/ — swap candidate-1.png to use a different one, then re-run with --process-only"
}

# ── Directory structure ────────────────────────────────────────────────────────
create_directories() {
    log_info "Creating directory structure..."
    local dirs=(
        "$GENERATED_DIR"
        "$OUTPUT_DIR/01-master"
        "$OUTPUT_DIR/02-github"
        "$OUTPUT_DIR/03-social"
        "$OUTPUT_DIR/04-web"
        "$OUTPUT_DIR/05-favicon"
        "$OUTPUT_DIR/06-app"
    )
    for d in "${dirs[@]}"; do mkdir -p "$d"; done
    log_success "Directories ready"
}

# ── Image helpers ──────────────────────────────────────────────────────────────
get_rounded_filter() {
    local width=$1 height=$2 radius_percent=$3
    [ "$radius_percent" -eq 0 ] && echo "" && return
    local radius=$(( width * radius_percent / 100 ))
    echo ",format=rgba,geq=\
r='if(gt(abs(X-(W/2)),W/2-${radius})*gt(abs(Y-(H/2)),H/2-${radius})*gt(hypot(${radius}-(W/2-abs(X-(W/2))),${radius}-(H/2-abs(Y-(H/2)))),${radius}),0,r(X,Y))'\
:g='if(gt(abs(X-(W/2)),W/2-${radius})*gt(abs(Y-(H/2)),H/2-${radius})*gt(hypot(${radius}-(W/2-abs(X-(W/2))),${radius}-(H/2-abs(Y-(H/2)))),${radius}),0,g(X,Y))'\
:b='if(gt(abs(X-(W/2)),W/2-${radius})*gt(abs(Y-(H/2)),H/2-${radius})*gt(hypot(${radius}-(W/2-abs(X-(W/2))),${radius}-(H/2-abs(Y-(H/2)))),${radius}),0,b(X,Y))'\
:a='if(gt(abs(X-(W/2)),W/2-${radius})*gt(abs(Y-(H/2)),H/2-${radius})*gt(hypot(${radius}-(W/2-abs(X-(W/2))),${radius}-(H/2-abs(Y-(H/2)))),${radius}),0,255)'"
}

make_png() {
    local name=$1 w=$2 h=$3 bg=$4 radius=$5 out=$6
    log_info "  → $name (${w}×${h})"

    local filter="scale=${w}:${h}:force_original_aspect_ratio=decrease"

    case "$bg" in
        white)       filter="${filter},pad=${w}:${h}:(ow-iw)/2:(oh-ih)/2:white" ;;
        blue)        filter="${filter},pad=${w}:${h}:(ow-iw)/2:(oh-ih)/2:color=0x2563EB" ;;
        transparent) filter="${filter},pad=${w}:${h}:(ow-iw)/2:(oh-ih)/2:color=0x00000000" ;;
    esac

    local rounded
    rounded=$(get_rounded_filter "$w" "$h" "$radius")
    filter="${filter}${rounded}"

    if ffmpeg -i "$SOURCE_IMAGE" -vf "$filter" -y "$out" 2>/dev/null; then
        log_success "    ✓ $name"
    else
        log_error "    ✗ Failed: $name"
        return 1
    fi
}

make_ico() {
    log_info "  → favicon.ico (16+32+48)"
    if command -v magick >/dev/null 2>&1; then
        magick "$OUTPUT_DIR/05-favicon/favicon-16.png" \
               "$OUTPUT_DIR/05-favicon/favicon-32.png" \
               "$OUTPUT_DIR/05-favicon/favicon-48.png" \
               "$OUTPUT_DIR/05-favicon/favicon.ico" 2>/dev/null
    elif command -v convert >/dev/null 2>&1; then
        convert "$OUTPUT_DIR/05-favicon/favicon-16.png" \
                "$OUTPUT_DIR/05-favicon/favicon-32.png" \
                "$OUTPUT_DIR/05-favicon/favicon-48.png" \
                "$OUTPUT_DIR/05-favicon/favicon.ico" 2>/dev/null
    else
        log_warning "ImageMagick not found — skipping ICO"
        return
    fi
    log_success "    ✓ favicon.ico"
}

# ── Phase 1: Master + Favicon ──────────────────────────────────────────────────
phase1_master_and_favicon() {
    log_step "=== PHASE 1: MASTER & FAVICON ==="
    make_png "logo-master-2000px"  2000 2000 "white"       0  "$OUTPUT_DIR/01-master/logo-master-2000px.png"
    make_png "logo-master-1000px"  1000 1000 "white"       0  "$OUTPUT_DIR/01-master/logo-master-1000px.png"
    make_png "logo-transparent"    2000 2000 "transparent" 0  "$OUTPUT_DIR/01-master/logo-transparent.png"

    make_png "favicon-16"            16   16 "white"       0  "$OUTPUT_DIR/05-favicon/favicon-16.png"
    make_png "favicon-32"            32   32 "white"       0  "$OUTPUT_DIR/05-favicon/favicon-32.png"
    make_png "favicon-48"            48   48 "white"       0  "$OUTPUT_DIR/05-favicon/favicon-48.png"
    make_ico
    log_success "Phase 1 complete!"
}

# ── Phase 2: Web & PWA Icons ───────────────────────────────────────────────────
phase2_web_pwa() {
    log_step "=== PHASE 2: WEB & PWA ICONS ==="
    make_png "apple-touch-icon"     180  180 "white"       0  "$OUTPUT_DIR/04-web/apple-touch-icon.png"
    make_png "icon-192"             192  192 "white"       0  "$OUTPUT_DIR/04-web/icon-192.png"
    make_png "icon-512"             512  512 "white"       0  "$OUTPUT_DIR/04-web/icon-512.png"
    # OG/social logo — wide format
    make_png "logo-og"            1200  630 "white"        0  "$OUTPUT_DIR/04-web/logo.png"
    log_success "Phase 2 complete!"
}

# ── Phase 3: Social & GitHub ───────────────────────────────────────────────────
phase3_social() {
    log_step "=== PHASE 3: SOCIAL & GITHUB ==="
    make_png "github-avatar"        420  420 "white"       0  "$OUTPUT_DIR/02-github/github-avatar.png"
    make_png "social-profile"       400  400 "white"       0  "$OUTPUT_DIR/03-social/social-profile.png"
    make_png "social-card-wide"    1200  600 "white"       0  "$OUTPUT_DIR/03-social/social-card-wide.png"
    log_success "Phase 3 complete!"
}

# ── Phase 4: App Icons ─────────────────────────────────────────────────────────
phase4_app_icons() {
    log_step "=== PHASE 4: APP ICONS ==="
    make_png "app-icon-1024"       1024 1024 "white"      17  "$OUTPUT_DIR/06-app/app-icon-1024.png"
    make_png "app-icon-ios"        1024 1024 "white"      22  "$OUTPUT_DIR/06-app/app-icon-ios.png"
    make_png "app-icon-android"     512  512 "white"      12  "$OUTPUT_DIR/06-app/app-icon-android.png"
    log_success "Phase 4 complete!"
}

# ── Deploy to repo source dirs (build.py picks them up) ───────────────────────
deploy_to_repo() {
    log_step "=== DEPLOYING TO REPO SOURCE DIRS ==="
    local repo_dir
    repo_dir="$(cd "$(dirname "$0")" && pwd)"

    # images/ → PWA icons + OG logo (copied to docs/images/ by build.py)
    cp "$OUTPUT_DIR/04-web/icon-192.png"         "$repo_dir/images/icon-192.png"
    cp "$OUTPUT_DIR/04-web/icon-512.png"         "$repo_dir/images/icon-512.png"
    cp "$OUTPUT_DIR/04-web/logo.png"             "$repo_dir/images/logo.png"
    # favicon.ico + apple-touch-icon → promoted to docs/ root by build.py
    cp "$OUTPUT_DIR/04-web/apple-touch-icon.png" "$repo_dir/images/apple-touch-icon.png"
    cp "$OUTPUT_DIR/05-favicon/favicon.ico"      "$repo_dir/images/favicon.ico"
    # Note: favicon-16/32/48.png are build intermediates — NOT committed to the repo

    log_success "Files deployed to images/ — build.py will pick them up on next build"
    log_info "Review candidates in $GENERATED_DIR/ before committing."
    log_info "To commit: cd $repo_dir && git add images/ && git commit -m 'Update branding from Vertex AI Imagen'"
}

# ── Summary ────────────────────────────────────────────────────────────────────
report() {
    echo ""
    echo "📁 Generated files:"
    find "$OUTPUT_DIR" -type f | sort | while read -r f; do
        local size
        size=$(du -h "$f" | cut -f1)
        echo "   ✓ ${f#$OUTPUT_DIR/} ($size)"
    done
    echo ""
    echo "📊 Total: $(find "$OUTPUT_DIR" -type f | wc -l) files, $(du -sh "$OUTPUT_DIR" | cut -f1)"
    echo ""
    echo "🎨 Candidates: $GENERATED_DIR/"
    echo "   Swap candidate-1.png with another, then re-run: $0 --process-only"
    echo ""
}

# ── Entry point ────────────────────────────────────────────────────────────────
main() {
    echo ""
    echo "📖  Parasha of the Week — Branding Generator (Vertex AI Imagen)"
    echo "================================================================="
    echo ""

    create_directories

    if [ "${1:-}" = "--process-only" ]; then
        SOURCE_IMAGE="$GENERATED_DIR/candidate-1.png"
        if [ ! -f "$SOURCE_IMAGE" ]; then
            log_error "No generated image found at $SOURCE_IMAGE"
            log_info "Run without --process-only first to generate images"
            exit 1
        fi
        log_info "Using existing source: $SOURCE_IMAGE"
    else
        generate_with_vertex_ai
    fi

    phase1_master_and_favicon
    phase2_web_pwa
    phase3_social
    phase4_app_icons

    deploy_to_repo
    report

    log_success "All Parasha branding assets generated! 📖"
}

main "$@"
