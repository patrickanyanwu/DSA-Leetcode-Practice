set -e  # Exit on error

git add . 
git commit -m "Solved: $1" 
git push