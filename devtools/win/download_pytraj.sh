appveyor DownloadFile https://ci.appveyor.com/api/buildjobs/04uqpbsvigvc1ha7/artifacts/pytraj.zip -FileName build.zip
7z x build.zip
# I know, I am suck at naming
mv build/lib*/pytraj .
