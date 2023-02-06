import game
import loader
from loader import dp
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        keyboardb = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton('Новая игра')
        button2 = KeyboardButton('Изменить количество конфет')
        keyboardb.add(button1, button2)
        await message.answer(f'Привет, {message.from_user.first_name}! '
                        f'Сыграем в игру?\n\nПравила очень просты: на столе лежит 150 конфет.'
        ' Мы по очереди берем не больше 28 конфет. Выигрывает тот, кто возьмёт последнюю конфету.'
        ' Победителю достаются все конфеты.\n\nТы можешь изменить количество конфет или сразу начать игру.', reply_markup=keyboardb)

@dp.message_handler(text=['Новая игра'])        
async def mes_newgame(message: Message):
    await message.answer(f'{message.from_user.first_name}, на столе 150 конфет, возьми со стола не более 28 конфет.')
    my_game = [message.from_user.id, message.from_user.first_name, 150]
    game.total.append(my_game)

@dp.message_handler(text=['Изменить количество конфет'])        
async def mes_changecount(message: Message):
    await message.answer(f'{message.from_user.first_name}, чтобы изменить количество конфет, ввели /set и чепез пробел число?')
    await (mes_newtotal)

@dp.message_handler(commands=['set'])
async def mes_newtotal(message: Message):
    newtotal = message.text.split()[1]
    if newtotal.isdigit() and int(newtotal) >= 29:
        # game.max_total = int(newtotal)
        await message.answer(f'Теперь на столе {newtotal} конфет. Твой ход возьми со стола не более 28 конфет.')
        my_game = [message.from_user.id, message.from_user.first_name, int(newtotal)]
        game.total.append(my_game)                             
    else:
        await message.answer(f'Введите число больше 29. Формат ввода "/set 100"')
