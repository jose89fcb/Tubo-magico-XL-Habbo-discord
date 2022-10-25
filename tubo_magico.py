import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
import random


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def tubo(ctx,   keko, hotel):
    await ctx.message.delete() #Borramos el comando para no dejar sucio el chat xD
    await ctx.send("Generando tubo Mágico XL...", delete_after=0)
    time.sleep(3) #Añadimos un tiempo para que sea borrado
   
    
    response = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={keko}") #Api habbo hotel
 
   
    try:

     habbo = response.json()['figureString']
    except KeyError:
        await ctx.send("El keko no existe!") 
  
   

   
    ##jose89fcb

    
    
   
    try:

     url = "https://www.habbo.com/habbo-imaging/avatarimage?size=m&figure="+ habbo +"&action=none&direction=2&head_direction=2&gesture=std&size=m"
     img1 = Image.open(io.BytesIO(requests.get(url).content))
     img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko 1

   
    
    
    


    
    


    

   

    

    
    
    



     img2 = img1.copy()
    
    
    ###

    


     tubo_maquina = Image.open(r"imagenes/cristal_tubo_maquina.png").convert("RGBA") #imagen
     img1 = tubo_maquina.resize((98,172), Image.ANTIALIAS)#tamaño del maquina_tubo


    ###
     cristal_tubo = Image.open(r"imagenes/cristal_tubo.png").convert("RGBA") #imagen
     img1 = cristal_tubo.resize((98,172), Image.ANTIALIAS)#tamaño del cristal tubo
  
    ###
     tubo = Image.open(r"imagenes/tubo.png").convert("RGBA") #imagen
     img1 = tubo.resize((98,172), Image.ANTIALIAS)#tamaño del tubo
    ###
    ###
     arriba_tubo = Image.open(r"imagenes/arriba_tubo.png").convert("RGBA") #imagen
     img1 = arriba_tubo.resize((98,172), Image.ANTIALIAS)#tamaño del tubo parte de arriba
    ###


 
   
    
    
    
     
    
    
     img1.paste(tubo,(0,0), mask = tubo) #Posicion del tubo maquina
   
  
     img1.paste(tubo_maquina,(0,0), mask = tubo_maquina) #Posicion del tubo maquina
   
    
    
  
    
    ### 
     img1.paste(img2,(18,40), mask = img2) #Posicion del keko
    
     img1.paste(cristal_tubo,(0,0), mask = cristal_tubo) #Posicion del tubo maquina
     img1.paste(arriba_tubo,(0,0), mask = arriba_tubo) #Parte de arriba tubo Posicion
    
    
   ###
   
   
   
    ###
    
   
 
    
    
  ####
   
  ###
    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
     with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
    except UnboundLocalError:
        habbo=":("    
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"]) #Token bot discord
