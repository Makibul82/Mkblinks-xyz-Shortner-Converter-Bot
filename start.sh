echo "Cloning Repo...."
git clone https://github.com/MkbLinks/Mkblinks-xyz-Shortner-Converter-Bot.git /Mkblinks-xyz-Shortner-Converter-Bot
cd /Mkblinks-xyz-Shortner-Converter-Bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
