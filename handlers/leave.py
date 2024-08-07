from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from lexicon.lexicon_ru import lexicon
import keyboards.layouts as keyboards


async def leave(message: Message, state: FSMContext):
    await message.answer(lexicon['leave'], reply_markup=keyboards.start_kb)
    await state.set_state(None)

