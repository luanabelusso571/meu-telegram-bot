import urllib.request
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Cole aqui o Token que você pegou no BotFather
TELEGRAM_TOKEN = '8883829115:AAGPaCQ6S7xRwQsoghUMBDjlK6ybPmi7HMk'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Use o comando /projeto para ver os dados do GitHub.')

async def projeto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://github.com"
    req = urllib.request.Request(url, headers={'User-Agent': 'TelegramBot'})
    with urllib.request.urlopen(req) as response:
        dados = json.loads(response.read().decode())
    
    mensagem = (
        f"📂 **Nome:** {dados['name']}\n"
        f"📝 **Descrição:** {dados['description']}\n"
        f"⭐ **Estrelas:** {dados['stargazers_count']}\n"
        f"🍴 **Forks:** {dados['forks_count']}\n"
        f"🔗 **Link:** {dados['html_url']}"
    )
    await update.message.reply_text(mensagem, parse_mode='Markdown')

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("projeto", projeto))
    print("Bot online...")
    app.run_polling()

if __name__ == '__main__':
    main()
