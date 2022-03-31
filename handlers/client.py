from aiogram import types, Dispatcher
from coin_info import bitcoin_loader
# from keyboards import kb_client
# from aiogram.types import ReplyKeyboardRemove


# если бот в одном файле, то можно тупо декораторы юзать
# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    await message.answer('Саламус! Тупо бот для отслеживания стоимости монеток, ежжи\n'
                         'Шо по коммандам:\n'
                         '/start - начать работу\n'
                         '/help - вызвать список комманд\n(если ты не видишь списочек при вводе слэшика, моя радость)\n'
                         '/btc - стоимость битка\n'
                         '/eth - стоимость эфирчика\n'
                         '/usdc - стоимость пендосского рубля\n'
                         '/top_five - стоимость пяти топовых монет\n'
                         'Развлекайся, солнце :0\n')  # , reply_markup=kb_client)


# @dp.message_handler(commands=['btc'])
async def commands_btc_loader(message : types.Message):
    # reply_markup здесь удаляет клаву после нажатия на инструкцию wasup
    await message.answer(bitcoin_loader.bitcoin_price_loader(), parse_mode="Markdown")  # , reply_markup=kb_client)


# @dp.message_handler(commands=['eth'])
async def commands_eth_loader(message : types.Message):
    # reply_markup здесь удаляет клаву после нажатия на инструкцию wasup
    await message.answer(bitcoin_loader.ethereum_price_loader(), parse_mode="Markdown")  # , reply_markup=kb_client)


# @dp.message_handler(commands=['usdc'])
async def commands_usdc_loader(message : types.Message):
    # reply_markup здесь удаляет клаву после нажатия на инструкцию wasup
    await message.answer(bitcoin_loader.usd_coin_price_loader(), parse_mode="Markdown")  # , reply_markup=kb_client)


# @dp.message_handler(commands=['top_five'])
async def commands_top_five_loader(message : types.Message):
    # reply_markup здесь удаляет клаву после нажатия на инструкцию wasup
    await message.answer(bitcoin_loader.top_five_price_loader(), parse_mode="Markdown")  # , reply_markup=kb_client)


def register_handler_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_btc_loader, commands=['btc'])
    dp.register_message_handler(commands_eth_loader, commands=['eth'])
    dp.register_message_handler(commands_usdc_loader, commands=['usdc'])
    dp.register_message_handler(commands_top_five_loader, commands=['top_five'])
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_btc_loader, commands=['btc'])
    dp.register_message_handler(commands_eth_loader, commands=['eth'])
    dp.register_message_handler(commands_usdc_loader, commands=['usdc'])
    dp.register_message_handler(commands_top_five_loader, commands=['top_five'])