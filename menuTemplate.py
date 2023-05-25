#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :Simple Python Menu
#description     :Template for a custom scripting menu
#author          :@cortesjorgea
#date            :10/2018
#updated         :04/2020
#version         :2.0
#usage           :simple_python_menu.py
#notes           :Update section USER CONFIG dicts and reimplement methods
#                 of menu1 and menu2 classes at BACKEND section.
#python_version  :3.8.0
#=======================================================================
import sys, os, signal, colorama
from operacoes import *
from terminalFuncs import limpar_terminal
colorama.init() # Color init for Windows

# =======================
#    DEFINES
# =======================

colors = {
  "info":     "35m",      #Orange for info messages
  "error":    "31m",      #Red for error messages
  "ok":       "32m",      #Green for success messages
  "menu2c":  "\033[46m",  #Light blue menu
  "menu1c":  "\033[44m",  #Blue menu
  "close":  "\033[0m"     #Color coding close
  }
cc = "\033[0m"
ct = "\033[101m"
cs = "\033[41m"
c1 = colors["menu1c"]
c2 = colors["menu2c"]


# =======================
#    USER CONFIG
# =======================
programtitle="Banco do Pará"

menu1_colors = {
  "ct":ct,
  "cs":cs,
  "opt":c1
}
menu1_options = {
  "title":  "Operações",
  "1":      "Depositar",
  "2":      "Sacar",
  "3":      "Mostrar extrato",
  "0":      "Sair (ou use CNTRL+C)",
}

# =======================
#      HELPERS
# =======================
def printWithColor(color,string):
  print("\033["+colors[color]+" "+string+cc)
def printError():
  printWithColor("error","Error!!")
  return 1
def printSuccess():
  printWithColor("ok","Success!!")
  return 0

# Exit program
def exit():
  sys.exit()
  
#Handles the CNTRL+C to leave properly the script
def sigint_handler(signum, frame):
  print("CNTRL+C exit")
  sys.exit(0)

# =======================
#      ACTIONS
# =======================

# Menu template
class menu_template():

  def __init__(self,options,colors):
    self.menu_width = 50  # Width in characters of the printed menu
    self.options = options
    self.colors = colors

# =======================
#      Menu prints
# =======================
  def createMenuLine(self,letter,color,length,text):
    menu = color+" ["+letter+"] "+text
    line = " "*(length-len(menu))
    return  menu+line+cc

  def createMenu(self,size):
    line = self.colors["ct"] + " "+programtitle
    line += " "*(size-len(programtitle)-6)
    line += cc
    print (line)  # Title
    line = self.colors["cs"] + " "+self.options["title"]
    line += " "*(size-len(self.options["title"])-6)
    line += cc
    print (line) # Subtitle
    for key in self.options:
      if(key != "title"):
        print (self.createMenuLine(key,self.colors["opt"],size,self.options[key]))

  def printMenu(self):
    self.createMenu(self.menu_width)
# =======================
#      Action calls
# =======================
  def action(self,ch):
    if  ch == '1':
      self.method_1()
    elif ch == '2':
      self.method_2()
    elif ch == '3':
      self.method_3()
    elif (ch==''):
      pass # Print menu again
    elif ch == '0':
      sys.exit()
    else:
      printError()
# =======================
#      Empty methods
# =======================
  def method_1(self):
    valor = get_valor("Insira um valor real para depósito: ")
    depositar(valor)

    limpar_terminal(True, "Tecle enter para continuar")

  def method_2(self):
    if not saqueBlock():
      valor = get_valor("Insira um valor real para saque: ")
      sacar(valor)

    limpar_terminal(True, "Tecle enter para continuar")
  
  def method_3(self):
    extrato()

    limpar_terminal(True, "Tecle enter para continuar")

# =======================
#      BACKEND
# =======================

# Create here custom actions.

# First menu actions. Implement each method.
class menu1(menu_template):
  pass

# Second menu actions. Implement each method.
class menu2(menu_template):
  pass

# =======================
#      MAIN PROGRAM
# =======================

class menu_handler:

  def __init__ (self):
    self.current_menu="main"
    self.m1=menu1(menu1_options, menu1_colors)

  def menuExecution(self):
    self.m1.printMenu()

    choice = input(" >> ")
    self.actuator(0,choice)
    print("\n")

  def actuator(self,type,ch):
    if type == 0:
      self.m1.action(ch)
    else:
      self.m2.action(ch)

# Main Program
if __name__ == "__main__":
  x = menu_handler()
  signal.signal(signal.SIGINT, sigint_handler)
  while True:
    x.menuExecution()