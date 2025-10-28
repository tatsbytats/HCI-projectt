#!/bin/sh
echo "=== Django Static Files Check ==="
echo "STATIC_ROOT contents:"
ls -R staticfiles/
echo "\nSTATIC_ROOT size:"
du -sh staticfiles/
echo "\nSTATICFILES_DIRS contents:"
ls -R static/
echo "\nChecking specific files:"
for img in staticfiles/boards/img/*.jpg; do
  echo "- $img: $([ -f "$img" ] && echo "EXISTS" || echo "MISSING")"
done