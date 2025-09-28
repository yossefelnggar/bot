import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN ='8122507680:AAGWHsP23WaJ_PR_Z4CCJ1LT_d5TAf9Rr-4'

# 100 Template (50 عربي + 50 إنجليزي)
TEMPLATES = [
    # ---------- عربي ----------
    "📅 14 مارس 2038\n[الاسم] اخترع جهاز بيترجم الأحلام مباشرة للواقع 🎧💭.",
    "📅 27 سبتمبر 2045\n[الاسم] افتتح أول كافيه على سطح القمر ☕🌕.",
    "📅 1 يناير 2050\nالصحف كتبت: [الاسم] اكتشف طريقة لتخزين الذكريات في USB 🔌🧠.",
    "📅 12 أغسطس 2042\n[الاسم] بقى أول شخص يركب أرجوحة بين برجين في المريخ 🌌🏗.",
    "📅 22 فبراير 2048\n[الاسم] اخترع شاحن موبايل شغال بالصوت 🎤🔋.",
    "📅 30 يونيو 2055\n[الاسم] أسس أول مدرسة لتعليم الدلافين الرياضيات 🐬➗.",
    "📅 19 أكتوبر 2044\n[الاسم] فتح مطعم بيقدم أكل من المستقبل 🍔🚀.",
    "📅 7 أبريل 2047\n[الاسم] اخترع حذاء يخليك تمشي على الميه 👟🌊.",
    "📅 15 نوفمبر 2039\n[الاسم] بقى أول واحد يزرع ورود بتنور في الضلمة 🌹💡.",
    "📅 2 يناير 2052\n[الاسم] عمل تطبيق بيخلي صورك تحكي قصص عن نفسها 📱📖.",
    "📅 4 يوليو 2043\nالعالم كله احتفل بعد ما [الاسم] اخترع إزازة مية ما بتخلصش 🚰♾.",
    "📅 9 مايو 2054\n[الاسم] اخترع قلم بيكتب أفكارك قبل ما تنطقها ✍️🧠.",
    "📅 11 ديسمبر 2046\n[الاسم] افتتح أول مدينة عائمة في البحر 🌊🏙.",
    "📅 6 يونيو 2051\n[الاسم] اخترع نظارة بتوري المستقبل 🔮👓.",
    "📅 21 يناير 2049\n[الاسم] بقى أول إنسان يتكلم مع النباتات 🌱💬.",
    "📅 3 مارس 2057\n[الاسم] أسس أول سيرك آلي بالكامل 🤖🎪.",
    "📅 25 أكتوبر 2041\n[الاسم] اكتشف طريقة يوقف المطر 10 دقايق ☔⏱.",
    "📅 17 أغسطس 2053\n[الاسم] بقى وزير التكنولوجيا في الأمم المتحدة 🌍💻.",
    "📅 8 سبتمبر 2040\n[الاسم] اخترع مرجيحة توصلك للفضاء 🎢🚀.",
    "📅 14 فبراير 2058\n[الاسم] اخترع وردة بتعزف موسيقى 🎶🌹.",
    "📅 1 يونيو 2047\n[الاسم] بقى عنده مزرعة روبوتات بتحلب الأبقار 🤖🐄.",
    "📅 23 مارس 2049\n[الاسم] اخترع أسانسير يوصلك لأي مكان في العالم 🌍⬆️.",
    "📅 18 أبريل 2056\n[الاسم] عمل أول بطولة كرة قدم في الفضاء ⚽🚀.",
    "📅 10 نوفمبر 2048\n[الاسم] اخترع مخدة بتخليك تحلم اللي عايزه 🛏💭.",
    "📅 29 ديسمبر 2050\n[الاسم] أسس أول متحف للذكريات الشخصية 🖼🧠.",
    "📅 13 مايو 2052\n[الاسم] اخترع جهاز يخلّي الكلاب تتكلم 🐶🗣.",
    "📅 30 أغسطس 2045\n[الاسم] بقى أول إنسان يعيش تحت البحر 🐠🏠.",
    "📅 27 يناير 2055\n[الاسم] اخترع شنطة تختفي في ثواني 🎒✨.",
    "📅 16 أبريل 2044\n[الاسم] بقى مدير محطة فضاء تجارية 🛰💼.",
    "📅 19 سبتمبر 2057\n[الاسم] اخترع لبس يخليك تطير لفوق 🦅👕.",
    "📅 7 فبراير 2046\n[الاسم] اخترع كوباية قهوة ما تبردش ☕🔥.",
    "📅 15 أغسطس 2051\n[الاسم] أسس أول بنك للذكريات 💳🧠.",
    "📅 2 أكتوبر 2054\n[الاسم] اخترع مروحة تديك طقس مثالي 🌬☀️.",
    "📅 6 ديسمبر 2042\n[الاسم] عمل أول مدينة كاملة بالطاقة الشمسية ☀️🏙.",
    "📅 22 يوليو 2047\n[الاسم] اخترع أسانسير للمريخ 🚀⬆️.",
    "📅 11 أبريل 2053\n[الاسم] اخترع كتاب بيقرألك نفسه 📖🔊.",
    "📅 28 نوفمبر 2049\n[الاسم] اخترع سماعة توريك أحلام غيرك 🎧💭.",
    "📅 9 مارس 2056\n[الاسم] اخترع كيبورد يكتب بالهواء ⌨️🌬.",
    "📅 31 مايو 2048\n[الاسم] اخترع مدينة جوة جبل 🏔🏙.",
    "📅 12 يناير 2052\n[الاسم] اخترع ساعة توقف الزمن ⏱🌀.",
    "📅 24 أغسطس 2045\n[الاسم] بقى أول مغني يغني مع قروب روبوتات 🎤🤖.",
    "📅 17 فبراير 2050\n[الاسم] اخترع بورتال ينقلك لأي مكان 🔮🌀.",
    "📅 8 يونيو 2054\n[الاسم] اخترع بستان فواكه بيتكلم 🍎🗣.",
    "📅 3 أكتوبر 2046\n[الاسم] اخترع إزازة بيبسي حجمها مالانهاية 🥤♾.",
    "📅 25 نوفمبر 2058\n[الاسم] اخترع جواكت ضد الغباء 🧥🧠.",
    "📅 14 أبريل 2043\n[الاسم] عمل أول فيلم تمثيل بين بشر وروبوتات 🎬🤖.",
    "📅 2 سبتمبر 2057\n[الاسم] اخترع عربية بتمشي على الغيوم ☁️🚗.",
    "📅 6 ديسمبر 2041\n[الاسم] اخترع قلادة تحافظ على مشاعرك ❤️🔒.",
    "📅 20 مارس 2059\n[الاسم] اخترع كاميرا بتصوّر أفكارك 📸💭.",

    # ---------- English ----------
    "📅 March 14, 2038\n[الاسم] invented a device that translates dreams into reality 🎧💭.",
    "📅 September 27, 2045\n[الاسم] opened the first coffee shop on the moon ☕🌕.",
    "📅 January 1, 2050\nBreaking News: [الاسم] discovered how to store memories on a USB stick 🔌🧠.",
    "📅 August 12, 2042\n[الاسم] became the first human to swing between two towers on Mars 🌌🏗.",
    "📅 February 22, 2048\n[الاسم] created a phone charger powered by sound 🎤🔋.",
    "📅 June 30, 2055\n[الاسم] founded the first school teaching dolphins mathematics 🐬➗.",
    "📅 October 19, 2044\n[الاسم] opened a restaurant serving food from the future 🍔🚀.",
    "📅 April 7, 2047\n[الاسم] invented shoes that let you walk on water 👟🌊.",
    "📅 November 15, 2039\n[الاسم] grew glowing roses in the dark 🌹💡.",
    "📅 January 2, 2052\n[الاسم] created an app where photos tell their own stories 📱📖.",
    "📅 July 4, 2043\nThe world celebrated [الاسم] for inventing an endless water bottle 🚰♾.",
    "📅 May 9, 2054\n[الاسم] built a pen that writes your thoughts before you do ✍️🧠.",
    "📅 December 11, 2046\n[الاسم] launched the first floating city 🌊🏙.",
    "📅 June 6, 2051\n[الاسم] created glasses that show the future 🔮👓.",
    "📅 January 21, 2049\n[الاسم] became the first human to talk with plants 🌱💬.",
    "📅 March 3, 2057\n[الاسم] founded a circus run entirely by robots 🤖🎪.",
    "📅 October 25, 2041\n[الاسم] invented a way to pause the rain for 10 minutes ☔⏱.",
    "📅 August 17, 2053\n[الاسم] was elected Minister of Technology at the UN 🌍💻.",
    "📅 September 8, 2040\n[الاسم] built a swing that reaches space 🎢🚀.",
    "📅 February 14, 2058\n[الاسم] created a rose that plays music 🎶🌹.",
    "📅 June 1, 2047\n[الاسم] ran a farm where robots milk cows 🤖🐄.",
    "📅 March 23, 2049\n[الاسم] invented an elevator that can reach anywhere 🌍⬆️.",
    "📅 April 18, 2056\n[الاسم] organized the first football match in space ⚽🚀.",
    "📅 November 10, 2048\n[الاسم] made a pillow that lets you dream what you want 🛏💭.",
    "📅 December 29, 2050\n[الاسم] founded the first museum of personal memories 🖼🧠.",
    "📅 May 13, 2052\n[الاسم] invented a device that lets dogs talk 🐶🗣.",
    "📅 August 30, 2045\n[الاسم] became the first human to live underwater 🐠🏠.",
    "📅 January 27, 2055\n[الاسم] created a bag that disappears instantly 🎒✨.",
    "📅 April 16, 2044\n[الاسم] managed the first commercial space station 🛰💼.",
    "📅 September 19, 2057\n[الاسم] invented a suit that makes you fly 🦅👕.",
    "📅 February 7, 2046\n[الاسم] created a coffee cup that never cools down ☕🔥.",
    "📅 August 15, 2051\n[الاسم] founded the first bank of memories 💳🧠.",
    "📅 October 2, 2054\n[الاسم] built a fan that creates perfect weather 🌬☀️.",
    "📅 December 6, 2042\n[الاسم] created the first solar-powered city ☀️🏙.",
    "📅 July 22, 2047\n[الاسم] invented an elevator to Mars 🚀⬆️.",
    "📅 April 11, 2053\n[الاسم] made a book that reads itself 📖🔊.",
    "📅 November 28, 2049\n[الاسم] created headphones that let you hear others’ dreams 🎧💭.",
    "📅 March 9, 2056\n[الاسم] designed a keyboard that types in the air ⌨️🌬.",
    "📅 May 31, 2048\n[الاسم] built a city inside a mountain 🏔🏙.",
    "📅 January 12, 2052\n[الاسم] invented a watch that freezes time ⏱🌀.",
    "📅 August 24, 2045\n[الاسم] performed the first concert with robots 🎤🤖.",
    "📅 February 17, 2050\n[الاسم] created a portal to anywhere 🔮🌀.",
    "📅 June 8, 2054\n[الاسم] grew talking fruit trees 🍎🗣.",
    "📅 October 3, 2046\n[الاسم] made a Pepsi bottle of infinite size 🥤♾.",
    "📅 November 25, 2058\n[الاسم] invented jackets against stupidity 🧥🧠.",
    "📅 April 14, 2043\n[الاسم] directed the first movie with robots and humans 🎬🤖.",
    "📅 September 2, 2057\n[الاسم] created a car that drives on clouds ☁️🚗.",
    "📅 December 6, 2041\n[الاسم] invented a necklace that locks emotions ❤️🔒.",
    "📅 March 20, 2059\n[الاسم] built a camera that captures your thoughts 📸💭."
]

WAITING_FOR_NAME = set()

# /start = زر "اسمك إيه؟"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("اسمك إيه؟", callback_data="ask_name")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔥 اضغط الزر وشوف مستقبلك!", reply_markup=reply_markup)

# التعامل مع الزر
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "ask_name":
        WAITING_FOR_NAME.add(query.from_user.id)
        await query.edit_message_text("📝 اكتب اسمك دلوقتي:")

# استقبال الاسم
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id in WAITING_FOR_NAME:
        user_name = update.message.text
        template = random.choice(TEMPLATES)
        message = template.replace("[الاسم]", user_name)
        await update.message.reply_text(message)
        WAITING_FOR_NAME.remove(user_id)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🔥 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()