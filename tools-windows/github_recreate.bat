copy .git\config \tmp\config /y
rm -rf .git
git init
copy \tmp\config .git /y
git add .
git commit -m "Initial commit"
git push -f
