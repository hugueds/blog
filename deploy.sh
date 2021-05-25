hugo --minify
git commit -am "deploy to public"
git push origin master
cd public
git commit -am "latest updates"
git push origin master