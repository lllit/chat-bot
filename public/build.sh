source venv/Scripts/activate

pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --backend-only
reflex export --frontend-only

rm -rf public
unzip backend.zip -d public
unzip frontend.zip -d public
rm -f frontend.zip

deactivate