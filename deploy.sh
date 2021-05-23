hugo --minify
git commit -am "deploy to public"
cd public
git commit -am "latest updates"
git push origin master