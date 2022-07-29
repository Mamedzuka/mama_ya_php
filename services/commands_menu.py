from aiogram import Dispatcher
from aiogram import types
from aiogram.types import BotCommandScopeDefault


async def set_commands_menu(dp: Dispatcher):
    return await dp.bot.set_my_commands(
        commands=[
            types.BotCommand('start', 'Start bot'),
            types.BotCommand('help', 'Call help'),
            types.BotCommand('btc', 'BTC price'),
            types.BotCommand('eth', 'ETH price'),
            types.BotCommand('usdc', 'USDC price'),
            types.BotCommand('top_five', 'top five coins prices'),
        ],
        scope=BotCommandScopeDefault()
    )