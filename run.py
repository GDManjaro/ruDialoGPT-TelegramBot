import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import token
modelpath = 'tinkoff-ai/ruDialoGPT-medium'
tokenizer = AutoTokenizer.from_pretrained(modelpath)
model = AutoModelWithLMHead.from_pretrained(modelpath)
API_TOKEN = token


logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет, нейронка работает на https://hf.co/tinkoff-ai/ruDialoGPT-medium \nНачать общение можно сейчас.")


@dp.message_handler()
async def echo(message: types.Message):
    themsg = await message.answer("Ждите...")
    msize = len(message.text)
    inputs = tokenizer(f'{message.text} ', return_tensors='pt')
    generated_token_ids = model.generate( 
    **inputs,
    top_k=10,
    top_p=0.95,
    num_beams=3,
    num_return_sequences=3,
    do_sample=True,
    no_repeat_ngram_size=2,
    temperature=1.2,
    repetition_penalty=1.2,
    length_penalty=1.0,
    eos_token_id=50257,
    pad_token_id=50257,
    max_new_tokens=40
    ) # тут можно поиграться с настройками, чтобы бот по разному отвечал
    context_with_response = [tokenizer.decode(sample_token_ids) for sample_token_ids in generated_token_ids]
    toans = context_with_response[0][msize::]
    toans = toans.replace('@@ПЕРВЫЙ@@', '')
    toans = toans.replace('@@ВТОРОЙ@@', '')
    await themsg.edit_text(toans)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
