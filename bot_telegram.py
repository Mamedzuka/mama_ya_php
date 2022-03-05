import asyncio
from aiogram.utils import executor
from create_bot import dp


from handlers import client  # , admin, other, admin_registration
from services.commands_menu import set_commands_menu
from coin_info.bitcoin_loader import coin_prices_updater


# def background_tasks_creator(dispatcher) -> None:
#     pass


async def on_startup(dispatcher) -> None:
    # delete comments if u want manually change updating time (after opening of .bat)
    # updating_time = int(input("Input price updating time: "))
    asyncio.create_task(coin_prices_updater(120))  # updating_time))
    await set_commands_menu(dispatcher)
    print('@suck_some_bot\'s online')


def main() -> None:
    # admin_registration.register_handler_admin_registration(dp)
    client.register_handler_client(dp)
    # admin.register_handler_admin(dp)
    # other.register_handler_other(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == "__main__":
    main()
