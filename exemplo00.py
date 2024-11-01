from loguru import logger

#Codigo gambiarra sem log
# def soma(x,y):
#     print(x)
#     print(y)
#     print(x+y)
#     return x+y

# soma(2,'3')

logger.add('meu_app.log') #arquivo de log criado para registrar todos os logs

#Codigo com log
def soma(x,y):
    try:
        soma= x + y
        logger.info(soma)
    except:
        logger.critical('Voce tem que digitar um número valido')
    return x+y

soma(2,3)