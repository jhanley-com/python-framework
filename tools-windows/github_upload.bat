set MSG=%1

if "%MSG%" == "" (
	set MSG="Updated documentation"
)

git add .
git commit -m %MSG%
git push -u origin master
