#!/usr/bin/env python3
"""
Simple test script to verify the build process works locally
Run this before committing to GitHub to catch issues early
"""

import os
import sys
from pathlib import Path

def test_build():
    """Test the build process"""
    print("🧪 Testing Parasha website build...")
    
    # Check if we're in the right directory
    if not Path("scripts/build.py").exists():
        print("❌ Error: Please run this from the project root directory")
        return False
    
    # Check required files
    required_files = [
        "scripts/build.py",
        "assets/css/style.css", 
        "assets/js/main.js",
        "requirements.txt",
        ".github/workflows/deploy.yml"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    # Check if content directory has articles
    content_dir = Path("content")
    if not content_dir.exists():
        print("❌ Error: content/ directory not found")
        return False
    
    md_files = list(content_dir.glob("*.md"))
    if not md_files:
        print("❌ Error: No markdown files found in content/")
        return False
    
    print(f"✅ Found {len(md_files)} markdown files")
    
    # Try to import the build script
    try:
        sys.path.insert(0, 'scripts')
        from build import ParashaWebsiteBuilder
        print("✅ Build script imports successfully")
    except ImportError as e:
        print(f"❌ Error importing build script: {e}")
        return False
    
    # Try to create builder instance
    try:
        builder = ParashaWebsiteBuilder()
        print("✅ Builder instance created successfully")
    except Exception as e:
        print(f"❌ Error creating builder: {e}")
        return False
    
    # Try to process a markdown file
    try:
        test_file = md_files[0]
        article = builder.process_markdown_file(test_file)
        print(f"✅ Test article processed: {article['title']}")
    except Exception as e:
        print(f"❌ Error processing test file {test_file}: {e}")
        return False
    
    # Test build process (but don't actually build)
    print("✅ All tests passed! Ready to build.")
    
    # Run full build test automatically
    print("\n🚀 Running full build test...")
    if True:
        try:
            print("🏗️ Running full build...")
            builder.build()
            print("🎉 Full build test successful!")
            
            # Check output
            docs_dir = Path("docs")
            if docs_dir.exists():
                html_files = list(docs_dir.glob("**/*.html"))
                print(f"📊 Generated {len(html_files)} HTML files")
                return True
            else:
                print("❌ Build completed but docs/ directory not found")
                return False
                
        except Exception as e:
            print(f"❌ Build failed: {e}")
            return False
    
    return True

if __name__ == "__main__":
    success = test_build()
    sys.exit(0 if success else 1)