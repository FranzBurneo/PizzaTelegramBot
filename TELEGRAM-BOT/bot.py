import telegram
from telegram.ext import *
import logging
import connectionOWL as con
import TeleToken as keys
import connectionDBP as dbp
import requests

# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

# Message error


def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')



# COMMANDS



def start_command(update, context):
    update.message.reply_text(
        'Bienvenido a DC Pizza :')
    update.message.reply_text(
        "Lista de comandos :"
        "\n/listNamedPizza "
        "\n/ingredientsAmericanaHot"
        "\n/ingredientsAmericana"
        "\n/ingredientsDonCangrejo"
        "\n/ingredientsMargherita"
        "\n/ingredientsSoho")


def types_command_namedPizza(update, context):
    qres = con.get_response_pizzas()
    update.message.reply_text('Lista de pizzas : ')
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)

def types_command_ingredientsAmericana (update, context):    
    update.message.reply_text('Lista de ingredientes : ')
    qres = con.get_response_ingredients("AmericanaPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))

def types_command_ingredientsAmericanaHot (update, context):    
    update.message.reply_text('Lista de ingredientes : ')
    qres = con.get_response_ingredients("AmericanaHotPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))

def types_command_ingredientsDonCangrejo (update, context):    
    update.message.reply_text('Lista de ingredientes : ')
    qres = con.get_response_ingredients("DonCagrejoPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))

def types_command_ingredientsMargherita (update, context):    
    update.message.reply_text('Lista de ingredientes : ')
    qres = con.get_response_ingredients("MargheritaPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))

def types_command_ingredientsSoho (update, context):    
    update.message.reply_text('Lista de ingredientes : ')
    qres = con.get_response_ingredients("SohoPizza")
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        ingredients = result['ingredients']['value']        
        update.message.reply_text(ingredients)
        update.message.reply_text(dbp.obtener_ingredientes(ingredients))
        



if __name__ == '__main__':
    updater = Updater(token=keys.API_KEY, use_context=True)
    bot = telegram.Bot(token=keys.API_KEY)
    

    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('listNamedPizza', types_command_namedPizza))
    dp.add_handler(CommandHandler('ingredientsAmericana', types_command_ingredientsAmericana))
    dp.add_handler(CommandHandler('ingredientsAmericanaHot', types_command_ingredientsAmericanaHot))
    dp.add_handler(CommandHandler('ingredientsDonCangrejo', types_command_ingredientsDonCangrejo))
    dp.add_handler(CommandHandler('ingredientsMargherita', types_command_ingredientsMargherita))
    dp.add_handler(CommandHandler('ingredientsSoho', types_command_ingredientsSoho))
     

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
