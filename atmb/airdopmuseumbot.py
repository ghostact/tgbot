from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
from telegram.error import BadRequest

# Define a start command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('🌟 If you love the airdrops 🪂 happening on Telegram Then your at the right spot')
    await menu(update, context)  # Call the menu function after displaying the welcome message

# Define a main menu command handler function
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("All The Airdops We Know Of 🪂", callback_data='1')],
        [InlineKeyboardButton("Gaming Airdrops 🎮🕹️", callback_data='2'), InlineKeyboardButton("Referral Airdrops 👨‍👨‍👧‍👦", callback_data='3')],
        [InlineKeyboardButton("Mining Airdrops ⛏️", callback_data='4'), InlineKeyboardButton("Tap2Earn/Swipe2Earn/Read2Earn Airdrops 👆📚", callback_data='5')],
        [InlineKeyboardButton("This is the Main Menu 🏠", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('👨‍🔧 Kindly select an option, while we do some things behind the scenes to add more options to your plate 𓌉◯𓇋:', reply_markup=reply_markup)

# Define a submenu handler function
async def submenu(update: Update, context: ContextTypes.DEFAULT_TYPE, option_number: str) -> None:
    elaborations = {
        '1': 'Check out all the airdrops🪂 we know of. We will keep adding 🆕new ones so check back often.',
        '2': 'I use to wish to play🎮 games and earn 💵, now we can with play2earn bots on telegram.',
        '3': 'Referrals are a buzzkill, but thats how companies and products grow 📈 their customer base. Complete referral quests to qualify for these airdrops🪂',
        '4': 'These ones are easy, all you need to do most times is check back every few hours⌚ and claim your mining earnings, plus upgrading your mining ⛏️ levels.',
        '5': 'Not coin set the tone for the era of tap2earn👆, now we have swipe2earn read2earn on telegram. Goode times. 😎',
    }

    if option_number == '1':
        keyboard = [
            [InlineKeyboardButton("🔢 Math Coin Pro Bot 🎮", url='https://t.me/MathCoinProBot?start=MM-HBBYSH'), InlineKeyboardButton("👆 TapSwap 🕹️", url='https://t.me/tapswap_mirror_bot?start=r_1790463763')], 
            [InlineKeyboardButton("🔥 BBQCoin Bot 🎮", url='https://t.me/BBQcoin_bot/BBQcoin?startapp=rp_9000013_1790463763'), InlineKeyboardButton("🌾 Blum Crypto Bot 🕹️", url='https://t.me/BlumCryptoBot/app?startapp=ref_R53kgL0SWo')],
            [InlineKeyboardButton("📚 UnitonAIBot 🎮", url='https://t.me/UnitonAIBot?start=refar8ab8'), InlineKeyboardButton("🐹 Hamster Kombat Bot 🕹️", url='https://t.me/hamster_kombat_bot?start=kentId1790463763')],
            [InlineKeyboardButton("🐛 Wormfare Slap Bot 🎮", url='https://t.me/wormfare_slap_bot?start=r_1790463763'), InlineKeyboardButton("🚀 Shuttle Ton Bot 🕹️", url='https://t.me/Shuttle_ton_bot?start=r_1790463763')],
            [InlineKeyboardButton("🐈 Play Catizen 🎮", url='https://t.me/catizenbot/gameapp?startapp=rp_1654012'), InlineKeyboardButton("Gleam AquaProtocol Bot 🕹️", url='https://t.me/Gleam_AquaProtocol_Bot/app?startapp=cmM9MGZkMTk1NjU')],
            [InlineKeyboardButton("● Dotcoin Bot🎮", url='https://t.me/dotcoin_bot?start=r_1790463763'), InlineKeyboardButton("🐵 ApeToken Airdrop 🕹️", url='https://t.me/ApeTokenAirdropbot?start=1790463763')],
            [InlineKeyboardButton("👖 PocketFi 🎮", url='https://t.me/pocketfi_bot/Mining?startapp=1790463763'), InlineKeyboardButton("🧈 Avagoldcoin Bot 🕹️", url='https://t.me/avagoldcoin_bot?start=41c50749479446fa3be0')],
            [InlineKeyboardButton("🐮Mine Bull 🎮", url='https://t.me/BullApp_bot?start=1790463763'), InlineKeyboardButton("👾 MomoAI Bot 🕹️", url='https://t.me/MomoAI_bot/app?startapp=F95DNU')],
            [InlineKeyboardButton("💲 Collect $Daily 🎮", url='https://t.me/DailyWalletBot?start=1790463763'), InlineKeyboardButton("🎮 Join Gamee 🕹️", url='https://t.me/gamee?start=ref_1790463763')],
            [InlineKeyboardButton("👑 Earn Kingy 🎮", url='https://t.me/kingyGMbot/gmgm?startapp=ref_813649'), InlineKeyboardButton("👨‍🎤 Punks Gamebot 🕹️", url='https://t.me/Punks_Gamebot?start=1XaBpN')],
            [InlineKeyboardButton("🌀 CyberFinanceBot 🎮", url='https://t.me/CyberFinanceBot?start=cj1GTm5YNnNJZXRRTEcmdT1yZWY='), InlineKeyboardButton("🌊 Wave on Sui 🕹️", url='t.me/waveonsuibot/walletapp?startapp=1559283')],
            [InlineKeyboardButton("Vertus App Bot 🕹️", url='t.me/vertus_app_bot/app?startapp=1790463763')],
            [InlineKeyboardButton("💎 Join Ton Promoters 🎮", url='https://t.me/tonpromoters_bot?start=1790463763'), InlineKeyboardButton("Wcoin Tapbot 🕹️", url='https://t.me/wcoin_tapbot?start=MTc5MDQ2Mzc2Mw==')],
            [InlineKeyboardButton("🐦 Big Ball Birds Bot 🎮", url='https://t.me/big_balls_birds_bot?start=1790463763'), InlineKeyboardButton("💎 STONFi Bot 🕹️", url='https://t.me/STONfi_bot?start=stonboarding_invswm8x4l9qeb6g6pl87ks_tkn_tiger')],
            [InlineKeyboardButton("🌕 MarsDAO Bot 🎮", url='https://t.me/Marswallet_bot?start=ref_1790463763'), InlineKeyboardButton("🐣 Chickcooppfficial Bot 🕹️", url='https://t.me/chickcoopofficial_bot/chickcoop?startapp=ref_1790463763')],
            [InlineKeyboardButton("🎰 True Coin 🎮", url='https://t.me/true_coin_bot?start=1790463763'), InlineKeyboardButton("💛 Topcoin Bot 🕹️", url='https://t.me/topcoin_me_bot?start=r_1790463763')],
            [InlineKeyboardButton("👹 ZARGates Bot 🎮", url='https://t.me/ZARGatesBot/?start=5959867414'), InlineKeyboardButton("Hamsterdam PlayBot 🕹️", url='https://t.me/HamsterdamPlayBot/game?startapp=54263')],
            [InlineKeyboardButton("🦸‍♂️ Hexacoin Bot 🎮", url='https://t.me/HexacoinBot/wallet?startapp=1790463763'), InlineKeyboardButton("🙂 Simple Tap Bot 🕹️", url='https://t.me/Simple_Tap_Bot?start=1715732496376')],
            [InlineKeyboardButton("🪐 Cyberbase Farm Bot 🎮", url='https://t.me/CyberbaseFarm_bot?start=1790463763'), InlineKeyboardButton("XplusIO Bot 🕹️", url='https://t.me/xplusio_bot/xplus?startapp=1777805973767987200')],
            [InlineKeyboardButton("💲 Grindery AI Bot 🎮", url='https://t.me/grinderyaibot?start=aE7CCEBcF7'), InlineKeyboardButton("🧊 Iceberg App Bot 🕹️", url='https://t.me/IcebergAppBot?start=referral_1790463763')],
            [InlineKeyboardButton("✊ Hold wallet Bot 🎮", url='https://t.me/holdwallet_bot/app?startapp=HWVV9MAFAAYY'), InlineKeyboardButton("🍀Seed Coin Bot 🕹️", url='https://t.me/seed_coin_bot/app?startapp=1790463763')],
            [InlineKeyboardButton("💲 ZEX Airdrop Robot 🎮", url='https://t.me/ZEXAirdropRobot?start=Bot27877381'), InlineKeyboardButton("🐲 Dragon Dot Bot 🕹️", url='https://t.me/DragonDotBot?start=rp_xmnfhoae70')],
            [InlineKeyboardButton("🪐 Xblast App 🎮", url='https://t.me/XBlastAppBot/App?startapp=2XGBCJ'), InlineKeyboardButton("Pixel wallet Bot 🕹️", url='https://t.me/pixel_wallet_bot?start=1790463763')],
            [InlineKeyboardButton("👬 ToON Nation Bot 🎮", url='https://t.me/toon_nation_bot/toon_nation?startapp=1790463763'), InlineKeyboardButton("🌌 Galaxy wallet Bot 🕹️", url='https://t.me/galaxywallet_bot/walletapp?startapp=1790463763')],
            [InlineKeyboardButton("💠 Gemz coin Bot 🎮", url='https://t.me/gemzcoin_Bot/tap?startapp=1xAbPn-UF0lH3k17iG9oE1dg'), InlineKeyboardButton("Matmo AI Airdrop Bot 🕹️", url='https://t.me/MatmoAirdropBot?start=1790463763')],
            [InlineKeyboardButton("🇨 ChainCrops  🎮", url='https://t.me/chaincrops_bot?start=1790463763'), InlineKeyboardButton("🪓 LumberJack Game Bot 🕹️", url='https://t.me/LumberJackGame_bot?start=61281716152804')],
            [InlineKeyboardButton("M Mineralz Bot 🎮", url='https://t.me/mineralzbot?start=1790463763'), InlineKeyboardButton("CEX IO Tap Bot 🕹️", url='https://t.me/cexio_tap_bot?start=1716323293036845')],
            [InlineKeyboardButton("⍩⃝ The Yescoin Bot 🎮", url='https://t.me/theYescoin_bot/Yescoin?startapp=XQzXqL')],
            [InlineKeyboardButton("Back ↩", callback_data='back')]
        ]
        message = 'You know what to do 👀.'
    elif option_number == '2':
        keyboard = [
            [InlineKeyboardButton("🌾 Blum Crypto Bot 🕹️", url='https://t.me/BlumCryptoBot/app?startapp=ref_R53kgL0SWo')],
            [InlineKeyboardButton("🐈 Play Catizen 🎮", url='https://t.me/catizenbot/gameapp?startapp=rp_1654012'), InlineKeyboardButton("👾 MomoAI Bot 🕹️", url='https://t.me/MomoAI_bot/app?startapp=F95DNU')],
            [InlineKeyboardButton("🎮 Join Gamee 🕹️", url='https://t.me/gamee?start=ref_1790463763')],
            [InlineKeyboardButton("🐣 Chickcooppfficial Bot 🕹️", url='https://t.me/chickcoopofficial_bot/chickcoop?startapp=ref_1790463763')],
            [InlineKeyboardButton("👹 ZARGates Bot 🎮", url='https://t.me/ZARGatesBot/?start=5959867414')],
            [InlineKeyboardButton("🦸‍♂️ Hexacoin Bot 🎮", url='https://t.me/HexacoinBot/wallet?startapp=1790463763'), InlineKeyboardButton("XplusIO Bot 🕹️", url='https://t.me/xplusio_bot/xplus?startapp=1777805973767987200')],
            [InlineKeyboardButton("Pixel wallet Bot 🕹️", url='https://t.me/pixel_wallet_bot?start=1790463763')],
            [InlineKeyboardButton("Back ↩", callback_data='back')]
        ]
        message = '🖱️ Click below to join any of these gaming airdrops🪂 on telegram with one 👆tap.'
    elif option_number == '3':
        keyboard = [
            [InlineKeyboardButton("👑 Earn Kingy 🎮", url='https://t.me/kingyGMbot/gmgm?startapp=ref_813649'), InlineKeyboardButton("💎 Join Ton Promoters 🎮", url='https://t.me/tonpromoters_bot?start=1790463763')],
            [InlineKeyboardButton("💲 ZEX Airdrop Robot 🎮", url='https://t.me/ZEXAirdropRobot?start=Bot27877381'), InlineKeyboardButton("Matmo AI Airdrop Bot 🕹️", url='https://t.me/MatmoAirdropBot?start=1790463763')],
            [InlineKeyboardButton("🐵 ApeToken Airdrop 🕹️", url='https://t.me/ApeTokenAirdropbot?start=1790463763')],
            [InlineKeyboardButton("Back ↩", callback_data='back')]
        ]
        message = 'Refer people to earn. Or 🥱'
    elif option_number == '4':
        keyboard = [
            [InlineKeyboardButton("🌾 Blum Crypto Bot 🕹️", url='https://t.me/BlumCryptoBot/app?startapp=ref_R53kgL0SWo')],
            [InlineKeyboardButton("🚀 Shuttle Ton Bot 🕹️", url='https://t.me/Shuttle_ton_bot?start=r_1790463763')],
            [InlineKeyboardButton("Gleam AquaProtocol Bot 🕹️", url='https://t.me/Gleam_AquaProtocol_Bot/app?startapp=cmM9MGZkMTk1NjU')],
            [InlineKeyboardButton("👖 PocketFi 🎮", url='https://t.me/pocketfi_bot/Mining?startapp=1790463763')],
            [InlineKeyboardButton("🐮Mine Bull 🎮", url='https://t.me/BullApp_bot?start=1790463763')],
            [InlineKeyboardButton("💲 Collect $Daily 🎮", url='https://t.me/DailyWalletBot?start=1790463763')],
            [InlineKeyboardButton("🌀 CyberFinanceBot 🎮", url='https://t.me/CyberFinanceBot?start=cj1GTm5YNnNJZXRRTEcmdT1yZWY='), InlineKeyboardButton("🌊 Wave on Sui 🕹️", url='t.me/waveonsuibot/walletapp?startapp=1559283')],
            [InlineKeyboardButton("Vertus App Bot 🕹️", url='t.me/vertus_app_bot/app?startapp=1790463763')],
            [InlineKeyboardButton("🌕 MarsDAO Bot 🎮", url='https://t.me/Marswallet_bot?start=ref_1790463763'), InlineKeyboardButton("🐣 Chickcooppfficial Bot 🕹️", url='https://t.me/chickcoopofficial_bot/chickcoop?startapp=ref_1790463763')],
            [InlineKeyboardButton("🦸‍♂️ Hexacoin Bot 🎮", url='https://t.me/HexacoinBot/wallet?startapp=1790463763'), InlineKeyboardButton("🙂 Simple Tap Bot 🕹️", url='https://t.me/Simple_Tap_Bot?start=1715732496376')],
            [InlineKeyboardButton("🪐 Cyberbase Farm Bot 🎮", url='https://t.me/CyberbaseFarm_bot?start=1790463763'), InlineKeyboardButton("XplusIO Bot 🕹️", url='https://t.me/xplusio_bot/xplus?startapp=1777805973767987200')],
            [InlineKeyboardButton("🧊 Iceberg App Bot 🕹️", url='https://t.me/IcebergAppBot?start=referral_1790463763')],
            [InlineKeyboardButton("✊ Hold wallet Bot 🎮", url='https://t.me/holdwallet_bot/app?startapp=HWVV9MAFAAYY'), InlineKeyboardButton("🍀Seed Coin Bot 🕹️", url='https://t.me/seed_coin_bot/app?startapp=1790463763')],
            [InlineKeyboardButton("🪐 Xblast App 🎮", url='https://t.me/XBlastAppBot/App?startapp=2XGBCJ')],
            [InlineKeyboardButton("👬 ToON Nation Bot 🎮", url='https://t.me/toon_nation_bot/toon_nation?startapp=1790463763')],
            [InlineKeyboardButton("M Mineralz Bot 🎮", url='https://t.me/mineralzbot?start=1790463763')],
            [InlineKeyboardButton("Back ↩", callback_data='back')]
        ]
        message = 'Yeah mine, bitcoin started it so these ones just like the mining thingy👍'
    elif option_number == '5':
        keyboard = [
            [InlineKeyboardButton("👆 TapSwap 🕹️", url='https://t.me/tapswap_mirror_bot?start=r_1790463763')], 
            [InlineKeyboardButton("🔥 BBQCoin Bot 🎮", url='https://t.me/BBQcoin_bot/BBQcoin?startapp=rp_9000013_1790463763'), InlineKeyboardButton("🌾 Blum Crypto Bot 🕹️", url='https://t.me/BlumCryptoBot/app?startapp=ref_R53kgL0SWo')],
            [InlineKeyboardButton("📚 UnitonAIBot 🎮", url='https://t.me/UnitonAIBot?start=refar8ab8'), InlineKeyboardButton("🐹 Hamster Kombat Bot 🕹️", url='https://t.me/hamster_kombat_bot?start=kentId1790463763')],
            [InlineKeyboardButton("🐛 Wormfare Slap Bot 🎮", url='https://t.me/wormfare_slap_bot?start=r_1790463763'), InlineKeyboardButton("🚀 Shuttle Ton Bot 🕹️", url='https://t.me/Shuttle_ton_bot?start=r_1790463763')],
            [InlineKeyboardButton("● Dotcoin Bot🎮", url='https://t.me/dotcoin_bot?start=r_1790463763')],
            [InlineKeyboardButton("Wcoin Tapbot 🕹️", url='https://t.me/wcoin_tapbot?start=MTc5MDQ2Mzc2Mw==')],
            [InlineKeyboardButton("💛 Topcoin Bot 🕹️", url='https://t.me/topcoin_me_bot?start=r_1790463763')],
            [InlineKeyboardButton("🦸‍♂️ Hexacoin Bot 🎮", url='https://t.me/HexacoinBot/wallet?startapp=1790463763'), InlineKeyboardButton("🙂 Simple Tap Bot 🕹️", url='https://t.me/Simple_Tap_Bot?start=1715732496376')],
            [InlineKeyboardButton("🐲 Dragon Dot Bot 🕹️", url='https://t.me/DragonDotBot?start=rp_xmnfhoae70')],
            [InlineKeyboardButton("💠 Gemz coin Bot 🎮", url='https://t.me/gemzcoin_Bot/tap?startapp=1xAbPn-UF0lH3k17iG9oE1dg')],
            [InlineKeyboardButton("🇨 ChainCrops  🎮", url='https://t.me/chaincrops_bot?start=1790463763'), InlineKeyboardButton("🪓 LumberJack Game Bot 🕹️", url='https://t.me/LumberJackGame_bot?start=61281716152804'), InlineKeyboardButton("CEX IO Tap Bot 🕹️", url='https://t.me/cexio_tap_bot?start=1716323293036845')],
            [InlineKeyboardButton("⍩⃝ The Yescoin Bot 🎮", url='https://t.me/theYescoin_bot/Yescoin?startapp=XQzXqL')],
            [InlineKeyboardButton("Back ↩", callback_data='back')]
        ]
        message = 'All my favourites are here, from Yescoin🥰, to TapSwap to Hamster Kombat. You gotta love it.💖💗💞'
    else:
        keyboard = [
            [InlineKeyboardButton("Back ↩", callback_data='back')]
        ]
        message = f'This door 🚪✨ leads to Option {option_number}: {elaborations[option_number]}.\nCheck back later for more options .'

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await update.callback_query.edit_message_text(
            message,
            reply_markup=reply_markup
        )
    except BadRequest as e:
        await update.callback_query.message.reply_text(
            message,
            reply_markup=reply_markup
        )

# Define a button click handler function
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    data = query.data

    try:
        if data == 'main_menu':
            await menu(query, context)
        elif data == 'back':
            await menu(query, context)
        elif data in ['1', '2', '3', '4', '5', '6']:
            await submenu(update, context, data)
        else:
            await query.edit_message_text(text=f"You selected {data.replace('_', ' ')}.")
    except BadRequest as e:
        print(f"Error: {e}")

# Define a function to handle text messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's API token
    application = Application.builder().token("7497323449:AAHejx2wZHMMtuG9M50aCD8KOeyORkHMTts").build()

    # Add handlers for different commands and interactions
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Add GIF shortcuts for easy navigation
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'/start'), start))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'/menu'), menu))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
