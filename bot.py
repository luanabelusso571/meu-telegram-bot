 from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "COLOQUE_SEU_TOKEN_AQUI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = """
🔮 Bem-vindo(a) ao Atendimento Espiritual de Luana Belusso

💰 Valor da consulta: R$ 10,00

Use /pix para receber a chave Pix.

Após o pagamento envie:
✅ Comprovante
✅ Nome completo
✅ Sua dúvida espiritual

Temas:
🌙 Espiritualidade
✨ Mediunidade
🔮 Sonhos
⭐ Autoconhecimento
🦋 Desenvolvimento pessoal
"""
    await update.message.reply_text(mensagem)

async def pix(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = """
💰 PAGAMENTO VIA PIX

Valor: R$ 10,00

Chave Pix:
SUA_CHAVE_PIX_AQUI

Após o pagamento envie:
✅ Comprovante
✅ Nome completo
✅ Sua dúvida espiritual
"""
    await update.message.reply_text(mensagem)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pix", pix))

    print("Bot online!")
    app.run_polling()

if __name__ == "__main__":
    main()