from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TELEGRAM_TOKEN = ("8883829115:AAGPaCQ6S7xRwQsoghUMBDjlK6ybPmi7HMk")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensagem = """
🔮 Bem-vindo(a) ao Atendimento Espiritual de Luana Belusso 🔮

✨ Sou Luana Belusso, bruxa universalista e espírita.

💰 Valor da consulta: R$ 10,00

📌 Como funciona:

1️⃣ Realize o pagamento via Pix

2️⃣ Envie o comprovante

3️⃣ Envie seu nome

4️⃣ Envie sua dúvida ou situação espiritual

Temas aceitos:

🌙 Espiritualidade
✨ Mediunidade
🔮 Experiências espirituais
⭐ Propósito de vida
🦋 Autoconhecimento
📖 Sonhos e símbolos

Após a confirmação do pagamento, sua mensagem será analisada.

⚠️ Este serviço oferece orientação espiritual e não substitui atendimento médico, psicológico ou jurídico.

💜 Gratidão pela confiança.
"""

    await update.message.reply_text(mensagem)

async def pix(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensagem = """
💰 PAGAMENTO VIA PIX

Valor: R$ 10,00

Chave Pix:

fd07b8d6-a3f3-4190-aa6d-02b00ad0753f

Após o pagamento envie:

✅ Comprovante
✅ Nome completo
✅ Sua dúvida espiritual

🔮 Gratidão!
"""

    await update.message.reply_text(mensagem)

def main():

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pix", pix))

    print("Bot online!")

    app.run_polling()

if __name__ == "__main__":
    main()
