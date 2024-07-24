﻿# Оголошення персонажів
define i = Character("Я")
define angel = Character("Ангел")
define unknown = Character("???")

# Оголошення музичних доріжок
# define audio.idle_music = "audio/music/idle.wav"
# define audio.alarm_clock = "audio/sound/alarm_clock.mp3"

# Оголошення службових змінних
# Змінні виконаних завдань
define is_first_task_completed = False
define is_second_task_completed = False
define is_third_task_completed = False
# Змінні правильності виконання завдань
define is_first_task_right = False
define is_first_task_wrong = False
define is_second_task_right = False
define is_second_task_wrong = False
define is_third_task_right = False
define is_third_task_wrong = False
# Змінні кінцівок
default persistent.paradise_ending = False
default persistent.hell_ending = False

# Оголошення ефекту розплющування та заплющування очей
init python:
    eye_open = ImageDissolve("images/art/eye.png", 0.5, 100)
    eye_close = ImageDissolve("images/art/eye.png", 0.5, 100, reverse=True)

label start:
    # scene dark
    "Останнім що я бачив у своєму житті були фари маленького фургончика."
    "Досить іронічно - все життя дивитись аніме в жанрі іссекай та сміятись із неправдоподібності зав'язки, і тепер опинитись тут же..."
    "Я більше не відчуваю свого тіла."
    "Нічого не болить."
    "Чи може це бути..{w} Смерть?"
    "Так, напевно це вона..."
    "Мене окутує пітьма та холод."
    "Страх сковує всі двадцять із чимось грами..."
    "Мої, напівпрозорі повіки пробиває яскраве світло."
    "Схоже мозок вже не працює, і настає сліпота."
    "А може це світло в кінці тунелю?"
    "..."
    unknown "Агов, хлопче, ти взагалі то можеш відкрити очі."
    i "..."
    unknown "Я серйозно. Відкрий очі, це виглядає дуже ніяково."
    i "Хто це? Що це за голос?"
    unknown "Ангел. Хто ж це ще може бути?"
    i "Ангел?"
    angel "Та ангел, ангел. Відкрий уже очі"
    "Почувши цю фразу мої спазмовано заплющенні очі відкрились"
    # scene first with eye_open
    # show angel at center
    i "Перепрошую, а де богиня?"
    angel "Яка богиня? Я ж казав, що я ангел"
    i "Ну, так але зважаючи на умови моєї смерті, я думав, що можливо зможу переродитись у іншому світі, чи ще щось.."
    angel "Хто тобі таке сказав? І про який ти такий \"інший\" світ говориш?"
    "Я зрозумів, що це точно не іссекай і вирішив промовчати."
    angel "Добре, не важливо. Давай приступимо до стандартної процедури."
    angel "Ти прожив недовге, несильно насичене життя, середньостатистичної людини твого часу."
    i "Ви, пане ангел, прямо таки по на рану сіль кидаєте.."
    angel "Як прожив так, і кажу. А ти мене не перебивай, а то наговорю всякого, і тебе одразу в пекло запишуть.."
    i "То, рай і пекло таки існують?"
    angel "Та, існує, існує. Не перебивай."
    angel "Отже, продовжимо."
    angel "Баланс поганих та гарних вчинків не поганий.."
    angel "Якихось великих гріхів не було помічено.."
    angel "Словом, ти не зробив нічого щоб заслужити потрапляння в пекло, але й до раю ти не дотягуєш.."
    i "То, що ж робити?"
    angel "Чесно тобі сказати, в такому випадку я би мав доставити тебе на небеса, щоб тебе распределили на переродження, щоб ти пройшов ще одне життя і може тоді хоч буде зрозуміло куди тебе.."
    angel "Але знаєш, мені так лінь.."
    angel "Я буквально щоденно це роблю, по кілька разів на години. Чесно кажучи мені якось набридло, тож давай так.."
    angel "Я дам тобі пергамент кармічного шляху більшого грішника за тебе, і якщо ти пройдеш його за три дні, то тебе без черги приймуть в рай, а якщо не впораєшся, то в пекло."
    i "Тобто в пекло? Чому три дні?"
    angel "Це приблизний час, може менше, може більше. Тут все залежить від оперативності твоєї сім'ї, все ж таки коли твоє тіло поховають, то ти повністю втратиш зв'язок із цим світом, і тоді за тобтою влаштують полювання посмертний патруль, щоб закинути тебе вже хоч кудись."
    i "Ти що намагаєшся мені сказати, що через твої лінощі, я маю проходити якийсь дурний квест за кілька днів, або потрапити в пекло?"
    angel "Саме так.."
    angel "А взагалі вини себе, якби ти хоч щось робив цьому житті, то просто потрапив би в пекло, або в рай. Ну, а так прожив абсолютно прісну, от я тобі і підкидую веселощів під його кінець.."
    i "Ти іще скажи, що я змарнував подарунок Божий.."
    angel "Чий?"
    i "Ну божий. Типу ваш головний, Аллах, Ісус, чи хто там у вас.."
    angel "Щось я не розумію про що ти.. Те що на Землі виникло життя - це суцільна удача. Поки що жодна планета у цілому всесвіті не бачила стільки ж випадковостей які змогли привести до того щоб моголо заробитись життя."
    i "Тоді хто ти такий? Хіба ти людина?"
    angel "Ні, не людина. Я ж казав, що я ангел."
    angel "Ангелами споконі вічно ставали люди які жили задля інших."
    i "Тобто все ж такий є якась вища сутність яка всім керує?"
    angel "Ні. Єдиною вищою сутністю в цьому світі є Весвіт."
    angel "Він постійно розширяється створюючи нову матерію у суцільному вакуумі. Ми ж, ангели, просто обслуговуємо його перенаправяючи енергію."
    angel "Ми просто виконуємо свою роботу, підтримуючи циркуляцію енергії. Без цього все просто зупинилося б."
    i "Але чому ви це робите? І як ви розумієте, що вам потрібно робити саме це?"
    angel "Насправді ніхто не знає. Просто після смерті за нами не приходять інші ангели, замість цього нам лишається цілий Всесвіт, після чого ми, рано чи пізно, просто стаємо до роботи."
    angel "Ми просто виконуємо свою роботу, підтримуючи циркуляцію енергії. Без цього все просто зупинилося б."
    i "А до чого тут енергія?"
    angel "Ну, як до чого? Кожна жива істота під час життя поглинає та виділяє енергію, яка формує його душу."
    angel "Після смерті душа покидає тіло, а отже енергія просто гуляє, що порушує закони Всесвіту, тому ми і займаємось перенаправленням енергії."
    angel "По факту ми просто підтримуємо баланс енергій, перенаправляючи душі туди, де вони найкраще впишуться."
    i "Але, тоді для чого оці історії про рай та пекло?"
    angel "Чесно кажучи не знаю звідки ви дізнались наші терміни, але від того куди ти потрапляєш залежить просто які умови будуть у тебе під час очікування, приблизно сто років, а потім у яке тіло твою плату вставлятимуть."
    angel "Тобто якщо ти потрапляєш до пекла, то це буде якась собака, чи свиня, а якщо рай, то в людське тіло. Ось і вся різниця.."
    i "І для чого це? Нащо таке робити?"
    angel "Як для чого? Я ж казав, що життя на Землі це результат безлічі випадковостей, тому є цінним. Всесвіт великий та байдужий, але весь час прагне до балансу, тому життя на Землі є для нього досить важливим, з точки зору того щоб не втрачати енергію, тому ми намагаємось вибудувати баланс на Землі, щоб ви, люди, не перебили один одного, і не знищили баланс Всесвіту." 
    angel "Таким чином більш добрі люди перероджуються в людей, а грішники в тварин, рослини і таке інше. Це допомагає підтримувати рівновагу енергій і при цьому не дати домінуючому виду знищити усі інші."
    "Потік всієї цієї інформації збив мене з пантелику і я не міг перетравити всього почутого."
    angel "То що, тобі ще треба крила, чи одразу в пекло?"
    i "Та ж треба..."
    angel "Ну, то тримай."
    i "Чекай, а хіба ти можеш так зробити?"
    angel "Так, звісно. За нами по факту стежить тільки програма, що виловлює ключові слова, що записані у протаколі, все інше ігнорується.."
    i "То, що буде із тим грішником кармічний шлях якого я отримав?"
    angel "В пекло."
    i "Але ж якщо я би не взяв його кармічний шлях, .."
    angel "Все одно в пекло."
    angel "Люди дуже рідко вибирають проходити кармічний шлях, тому вони проходять його не за три дні, як ти, а уже в наступному житті, напротязі всього життя."
    angel "Ну, добре, удачі тобі, у мене вже наступний виклик. Я полетів.."
    i "Чекай, а як я отримаю крила?"
    angel "Коли ти закінчиш із останнім завданням до тебе прибуде посмертний патруль, перевірить, як ти пройшов те все після чого тобі або видадуть крила і ти полетиш в рай, або розкриють землю і ти потрапиш в пекло."
    "Після цієї фрази ангел скрився за обрієм."
    "..."
    "Твою ж мать..."
    "Це що, якийсь божевільний сон?"
    "Але ж ні..."
    "Ангели. Справжні, чорт забирай, ангели."
    "Хоча, мабуть, краще не згадувати чорта в такій ситуації."
    "..."
    "І цей недороблений ангел..."
    "Від самої згадки про цього лінивого покидька у мене кров закипає."
    "Намагаючись втримати емоції під контролем, кулаки стиснулись самі собою."
    "Стоп.{w} Що це?"
    "Щось у правій руці. Щось незвичне, шурхотливе."
    "Обережно розтискаю пальці."
    "Папір?"
    "Звідки він тут взявся?"
    "Серце починає битися швидше."
    "..."
    "Тремтячими руками розгортаю аркуш."
    "На папері якимось дивним, ніби світящимся шрифтом нашкрябано три написи."
    # scene paper
    # "Назва першого завдання"
    # "Назва другого завдання"
    # "Назва третього завдання"
    # Далі головний герой має трохи вагатись, але в результаті зрозуміти, що все ж варто почати виконувати якісь завдання
    jump task_list
    return

# Сцена вибору наступного завдання
label task_list:
    # scene task_list
    menu:
        "Назва першого завдання" if is_first_task_completed == False:
            jump first_task
        "Назва другого завдання" if is_second_task_completed == False:
            jump second_task
        "Назва третього завдання" if is_third_task_completed == False:
            jump third_task
    return

# Сцена першого завдання
label first_task:
    "Текст першого завдання"
    menu:
        "Перший варіант":
            "Текст першого варіанту"
            $ is_first_task_right = True
        "Другий варіант":
            "Текст другого варіанту"
            $ is_first_task_wrong = True
    "Завершення першого завдання"
    $ is_first_task_completed = True
    jump check_tasks
    return

# Сцена другого завдання
label second_task:
    "Текст другого завдання"
    menu:
        "Перший варіант":
            "Текст першого варіанту"
            $ is_second_task_right = True
        "Другий варіант":
            "Текст другого варіанту"
            $ is_second_task_wrong = True
    "Завершення другого завдання"
    $ is_second_task_completed = True
    jump check_tasks
    return

# Сцена третього завдання
label third_task:
    "Текст третього завдання"
    menu:
        "Перший варіант":
            "Текст першого варіанту"
            $ is_third_task_right = True
        "Другий варіант":
            "Текст другого варіанту"
            $ is_third_task_wrong = True
    "Завершення третього завдання"
    $ is_third_task_completed = True
    jump check_tasks
    return

# Мітка перевірки всіх завдань
label check_tasks:
    if is_first_task_completed and is_second_task_completed and is_third_task_completed:
        $ correct_tasks = 0

        if is_first_task_right:
            $ correct_tasks += 1
        if is_second_task_right:
            $ correct_tasks += 1
        if is_third_task_right:
            $ correct_tasks += 1

        if correct_tasks >= 2:
            jump paradise
        else:
            jump hell
    else:
        jump task_list
    return

# Хороша кінцівка "Рай"
label paradise:
    "Текст кінцікви Рай"
    if correct_tasks == 2:
        "Деякий текст про те що виконані завдання не всі вірні"
        # Якщо виконано 2 з 3 завдант то має бути невеликий текст про те що головний герой типу не повністю впорався, але цього має бути достатньо, а от якщо 3 з 3, то нічого не мають казати
    "Завершення кінцікви Рай"
    window hide
    pause
    if persistent.paradise_ending == False:
        $ renpy.notify("Кінцівку \"Рай\" здобуто")
        $ persistent.paradise_ending = True
    return

# Погана кінцівка "Пекло"
label hell:
    "Текст кінцівки Пекло"
    "Завершення кінцівки Пекло"
    window hide
    pause
    if persistent.hell_ending == False:
        $ renpy.notify("Кінцівку \"Пекло\" здобуто")
        $ persistent.hell_ending = True
    return