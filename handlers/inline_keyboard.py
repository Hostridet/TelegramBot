from main import dp, types, bot
import src


@dp.callback_query_handler(text='today')
@dp.callback_query_handler(text='tomorrow')
async def callback_inline(call: types.CallbackQuery):
    try:
        if call.message:
            if call.data == 'today':
                schedule = src.Schedule()
                day_code = schedule.get_number_of_day()
                photo = open(schedule.get_name_of_day(day_code), 'rb')
                await bot.send_message(call.from_user.id,
                                       f'{schedule.get_week(day_code)}, {schedule.get_day()} {schedule.get_month()}')
                await bot.send_photo(call.from_user.id, photo)
            elif call.data == 'tomorrow':
                schedule = src.Schedule()
                day_code = schedule.get_number_of_day() + 1
                if day_code == 8:
                    day_code = 1
                photo = open(schedule.get_name_of_day(day_code), 'rb')
                await bot.send_message(call.from_user.id,
                                       f'{schedule.get_week(day_code)}, {schedule.get_day_tomorrow()} {schedule.get_month()}')
                await bot.send_photo(call.from_user.id, photo)
            await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        text="Расписание:",
                                        reply_markup=None)
    except Exception as e:
        print(repr(e))
