#!/bin/bash
# Test all lab validation scripts
# Runs validation scripts for all labs

set -e

echo "🔍 Testing all lab validation scripts..."

# Find all validate.py scripts in labs directory
VALIDATE_SCRIPTS=$(find labs -name "validate.py" 2>/dev/null)

if [ -z "$VALIDATE_SCRIPTS" ]; then
    echo "⚠️  No validation scripts found in labs/"
    exit 0
fi

TOTAL=0
PASSED=0
FAILED=0

for script in $VALIDATE_SCRIPTS; do
    TOTAL=$((TOTAL + 1))
    LAB_NAME=$(dirname "$script")

    echo ""
    echo "Testing: $LAB_NAME"
    echo "----------------------------------------"

    if python3 "$script"; then
        PASSED=$((PASSED + 1))
        echo "✅ $LAB_NAME passed"
    else
        FAILED=$((FAILED + 1))
        echo "❌ $LAB_NAME failed"
    fi
done

echo ""
echo "📊 Results:"
echo "   Total labs: $TOTAL"
echo "   Passed: $PASSED"
echo "   Failed: $FAILED"

if [ $FAILED -gt 0 ]; then
    echo ""
    echo "❌ Some lab validations failed!"
    exit 1
else
    echo ""
    echo "✅ All lab validations passed!"
    exit 0
fi
