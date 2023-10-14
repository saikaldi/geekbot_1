from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import questionnaire_one_keyboard
async def start_questionnaire(call: types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="R u hungry?",
        reply_markup=await questionnaire_one_keyboard()
    )

async def yes_answer(call: types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Ok",

    )

async def no_answer(call: types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Glad you r not hungry",

    )

def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(yes_answer,
                                       lambda call: call.data == "hungry_yes")
    dp.register_callback_query_handler(no_answer,
                                       lambda call: call.data == "hungry_no")
