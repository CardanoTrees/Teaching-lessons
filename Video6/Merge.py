# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:19:36 2022

@author: Damian @cardanotrees
"""
####################################
# Parameters
####################################
AssetName = 'MergeBonsai'
####################################

####################################################
# Do not modify from here
####################################################
import json
from bs4 import BeautifulSoup as bs

fout = open(AssetName+".html", "w")

with open(AssetName+'.json') as json_file:
    data = json.load(json_file)
Layers = data["Layers"]
NLayers = len(Layers)
Order = data["Order"]

text = "<html><style>*{margin:0; padding:0;}html, body {width:100%; height:100%;}myCanvas { display:block;}</style><body style='background-color:black;'><section><div id='canvasesdiv' style='position:relative; width:100%; height:100%'>"
print(text, file=fout)

for ii in range(NLayers):
    text="<canvas id='layer"+str(ii+1)+"' style='z-index: "+str(ii+1)+";position:absolute;left:0px;top:0px;'></canvas>"
    print(text, file=fout)

print('</div>', file=fout)

for ii in range(len(Order)):
    ff = open(Order[ii]+".html", "r")
    soup = bs(ff, "html.parser")
    aux = soup.find_all("script")[0]
    print(aux,file=fout)     

print("<script>", file=fout)

for ii in range(NLayers):
    text="    const canvas"+str(ii+1)+" = document.getElementById('layer"+str(ii+1)+"'); const "+Layers[ii][0]+"ctx"+Layers[ii][1]+" = canvas"+str(ii+1)+".getContext('2d');"
    print(text, file=fout)

text="    var WIDTH = window.innerWidth; var HEIGHT = window.innerHeight;"
print(text, file=fout)

for ii in range(NLayers):
    text="    canvas"+str(ii+1)+".width = WIDTH; canvas"+str(ii+1)+".height = HEIGHT;"
    print(text, file=fout)

text="    function resizeCanvas() {"
print(text, file=fout)
text="        WIDTH = window.innerWidth; HEIGHT = window.innerHeight;"
print(text, file=fout)

for ii in range(NLayers):
    text="        canvas"+str(ii+1)+".width = WIDTH; canvas"+str(ii+1)+".height = HEIGHT;"
    print(text, file=fout)
    
text="        location.reload();"
print(text, file=fout)
text="    }"
print(text, file=fout)

text="    function InitAll(){"
print(text, file=fout)
for ii in range(NLayers):
    text="        "+Layers[ii][0]+"I"+Layers[ii][1]+Layers[ii][2]+";"
    print(text, file=fout)
text="        DrawAll();"
print(text, file=fout)  
print("    }", file=fout)

text="    function DrawAll(){"
print(text, file=fout)
for ii in range(NLayers):
    text="        "+Layers[ii][0]+"D"+Layers[ii][1]+Layers[ii][3]+";"
    print(text, file=fout)
print("    }", file=fout)

text="    window.addEventListener('resize', resizeCanvas, false);"
print(text, file=fout)
text="    InitAll();"
print(text, file=fout)

print("</script>", file=fout)
print("</section>", file=fout)
print("</body>", file=fout)
print("</html>", file=fout)

fout.close()