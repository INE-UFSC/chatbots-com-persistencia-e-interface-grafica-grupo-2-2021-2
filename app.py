#encoding: utf-8
from Controller.SistemaController import SistemaChatBot as scb
from Bots.BotCansado import BotCansado

lista_bots = [BotCansado("Rafael"), BotCansado("Carlos"), BotCansado("Gabriel")]

sys = scb("CrazyBots", lista_bots)
sys.inicio()
