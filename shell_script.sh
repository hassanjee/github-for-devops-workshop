FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E "\.py$")

# Check each file for API keys
for FILE in $FILES; do
    echo "$FILE"
done